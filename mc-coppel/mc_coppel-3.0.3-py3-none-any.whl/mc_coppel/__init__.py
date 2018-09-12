#coding: utf-8
import sys,os
import pprint
import threading
import time
import json
import datetime
from kafka import KafkaConsumer
from kafka import KafkaProducer
from pymongo import MongoClient
import inspect 
import base64
import json
from colorama import init, Fore, Back, Style
from aiokafka import AIOKafkaProducer,AIOKafkaConsumer
import asyncio


loop = asyncio.get_event_loop()

class DictConvert(object):
    """Object view of a dict, updating the passed in dict when values are set
    or deleted. "Dictate" the contents of a dict...: """

    def __init__(self, d):
        # since __setattr__ is overridden, self.__dict = d doesn't work
        object.__setattr__(self, '_DictConvert__dict', d)

    # Dictionary-like access / updates
    def __getitem__(self, name):
        value = self.__dict[name]
        if isinstance(value, dict):  # recursively view sub-dicts as objects
            value = DictConvert(value)
        return value

    def __setitem__(self, name, value):
        self.__dict[name] = value
    def __delitem__(self, name):
        del self.__dict[name]

    # Object-like access / updates
    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        self[name] = value
    def __delattr__(self, name):
        del self[name]

    def __repr__(self):
        return "%s(%r)" % (type(self).__name__, self.__dict)
    def __str__(self):
        return str(self.__dict)

    def toJson(self):
        return dict(
            (key, value)
            for (key, value) in self.__dict__.items()
        )["_DictConvert__dict"]
        
class db():
    __mongoUri = ""
    def __obtenerIpMongo(self):
        miSecreto = ""
        try:
            miSecreto = os.environ["MONGO_CONFIG"]
        except:
            try:
                with open("/run/secrets/MONGO_CONFIG", 'r') as secret_file:
                    miSecreto = secret_file.read()
                    miSecreto = miSecreto.rstrip('\n')
            except:
                print("No se encontro la URI de conexion a mongoDB en variable de entorno (MONGO_CONFIG) ó Secrets Docker (MONGO_CONFIG)")
                print("mongodb://{ip}:{puerto}/")
                sys.exit(0)

        return miSecreto
    
    def __init__(self,mongoUri = ""):
        if mongoUri != "":
            self.__mongoUri = mongoUri
        else:
            self.__mongoUri = self.__obtenerIpMongo()
        
        
    def conexion(self):
        __conexion = None
        try:        
            __conexion = MongoClient(self.__mongoUri)
            return __conexion
        except:
            return None

class microservicio(db):

    db = db
    """
        Clase para conectar el microservicio
        Arguments:
             app (str) -  nombre de la app para la cual es el servicio
             servicio (str) -  nombre del microservicio
    """

    __metadataBifurcacion = []
    __metadataBorra = []
    __registrarErroresFlag = False
    __registrarErrores = False
    __registrarErroresParams = {}
    __registrarDependenciasFlag = False
    __registrarDependencias = False
    __registrarDependenciasParams = {}
    __registrarConfig = False
    __app = ""
    __bdConfig = ""
    __errores = {}
    __configServ = {}
    __producer = None
    __producer2 = None
    __consumer = None
    __consumer2 = None
    __objErroTmp = {}
    __esWorker = False
    __registrarService = False
    __inicializaciones = dict(
        mongoUri="", 
        topicName="", 
        configuraciones={}
    )
    __functionWorkerCambiarData = None
    
    def __registrarServicio(self,isBif):
        print(Fore.GREEN+"Registrar servicio : "+self.__inicializaciones["topicName"]+Fore.WHITE)

    def __init__(self,app = "",servicio = ""):
        print("\033[2J\033[1;1f") # Borrar pantalla y situar cursor
        print(Fore.WHITE+"*****************************************************************************"+Fore.WHITE)
        self.__app = app
        self.__inicializaciones["topicName"] = servicio

        if self.__app == "appcoppel":
            self.__bdConfig = "configuraciones_appcom"
        else:
            self.__bdConfig = "configuraciones_"+self.__app

        if self.__app == "":
            print("No existe esta app : ("+self.__app+")")
            sys.exit(0)
        
    def __json_to_b64(self,json_in):
        return base64.b64encode(str.encode(json.dumps(json_in)))

    def __b64_to_json(self,encoded):
        decoded = base64.b64decode(encoded)
        return json.loads(decoded.decode('utf-8'))
        
    def __modificarFlujo(self):
        flujoMod = []
        contador = 0

        auxFlujo = []
        auxFlujo.append(self.__inicializaciones["topicName"])
        for item in self.__inicializaciones["flujo"]:
            auxFlujo.append(item)
        
        objetos = len(auxFlujo)
        count = 0
        for element in auxFlujo:
            objeto = {}
            objeto["owner_conf"] = element
            if (count + 1) < objetos:
                objeto["worker_conf"] = auxFlujo[count+1]
            else:
                 objeto["worker_conf"] = ""
            contador = contador + 1
            if contador == 1:
                objeto["grabar_metadata"] = True

            if contador < objetos :
                objeto["end"] = False
            else:
                objeto["end"] = True

            flujoMod.append(objeto)

            count = count + 1
        
        self.__inicializaciones["flujo"] = flujoMod

    def __dependencias_f(self,obj = {}):
        objTemp = {}
        if obj != {} and "development" not in obj or "production" not in obj:
            print("No se recibieron las dependencias del servicio de ests forma {'development':{},'production':{}}")
            sys.exit(0)
        else:
            if "ENV" in os.environ and (os.environ["ENV"] == "Production" or os.environ["ENV"] == "Prod"):
                print("resgistrar en bd configuracion "+Fore.GREEN+"obj.production"+Fore.WHITE)
                objTemp = obj["production"]
            else:
                print("resgistrar en bd configuracion "+Fore.RED+"obj.development"+Fore.WHITE)
                objTemp = obj["development"]

        self.__configServ = objTemp

    def dependencias(self,obj = {}):
        self.__registrarDependenciasFlag = True
        self.__registrarDependencias,self.__registrarDependenciasParams = self.__dependencias_f,obj

    def __errores_f(self,obj):
        if obj == {}:
            obj["-99"] = "Ocurrio una excepcion,favor de intentar de nuevo."
            obj["-1"] = "Error de conexion COLA DE MENSAJERIA."
            obj["-2"] = "Parametros Incorrectos."
            obj["-6"] = "Token Invalido."
        else:
            if "-1" in obj or "-2" in obj or "-3" in obj or "-4" in obj or "-5" in obj or "-6" in obj or "-99" in obj:
                print("los siguientes codigos no se pueden usar ( -1, -2, -3, -4, -5, -6, -99 )")
                sys.exit(0)

        self.__errores = obj

    def errores(self,obj = {}):
        self.__registrarErroresFlag = True
        self.__registrarErrores,self.__registrarErroresParams = self.__errores_f,obj
        
    def __inicializa(self,tipo):
        if tipo == 1:
            self.__esWorker = True
            if self.__obtererConfiguraciones():
                self.__streamMessageQueue(self.__functionWorkerCambiarData)
        elif tipo == 2:
            self.__modificarFlujo()
            if self.__obtererConfiguraciones():
                self.__streamMessageQueue(self.__functionBifurcacion)

    def startWorker(self,function = object):

        self.__functionWorkerCambiarData = function
        
        if self.__registrarErroresFlag == True:
            self.__registrarErrores(self.__registrarErroresParams)
        else:
            self.__errores_f({})

        if self.__registrarDependenciasFlag == True:
            self.__registrarDependencias(self.__registrarDependenciasParams)

        if len(inspect.getargspec(self.__functionWorkerCambiarData).args) == 0:
            print("")
            print("")
            print("La funcion (startWorker) recibe un objeto funcion")# debera recibir 2 argumentos no : "+str(countArgs))
            print("*****************************************************************************")
        else:
            
            try:
                ret = inspect.getsource(self.__functionWorkerCambiarData).index("return")
                countArgs = len(inspect.getargspec(self.__functionWorkerCambiarData).args)
                if countArgs == 2 or countArgs == 3:
                    """Si se ejecuta este metodo es para que el microservicio funcione como un worker"""
                    self.__inicializa(1)
                else:
                    print("*****************************************************************************")
                    print("la funcion de entrada debera recibir 2 ó 3 argumentos no : "+str(countArgs))
                    print("Argumentos:")
                    print("    1 argumento  = para recibir los datos de configuracion del microservicio")
                    print("    2 argumento  = para recibir los datos de entrada al servicio")
                    print("    3 argumento  = para recibir funcion escribirTokenAsincrono")
                    print("La funcion  debe retornar una tupla ejemplo :  (0 =int,{} =json)")
                    print("*****************************************************************************")
                    
            except:
                print("la funcion debe retornar una tupla ejm.: return (0,{})")

    def startBifurcacion(self,arreglo = [],function = object):        
        """
            descripcion: flujo de la bifurcacion
            ejemplo: 
            [
                "llavesInicioSesion",
                "consultaPerfilEcommerce"
            ]
        """
        self.__functionWorkerCambiarData = function
        
        if self.__registrarService:
            self.__registrarServicio(True)
            self.errores(self.__objErroTmp)

        if len(inspect.getargspec(self.__functionWorkerCambiarData).args) == 0:
            print("")
            print("")
            print("La funcion (startBifurcacion) recibe un objeto funcion")# debera recibir 2 argumentos no : "+str(countArgs))
            print("*****************************************************************************")
        else:
            countArgs = len(inspect.getargspec(self.__functionWorkerCambiarData).args)
            if countArgs != 5:
                print("*****************************************************************************")
                print("la funcion de entrada debera recibir 5 argumentos no : "+str(countArgs))
                print("funcionalidad de la funcion : modificar la data de entrada del siguiente worker")
                print("Argumentos:")
                print("    1 argumento  = para recibir Nombre del worker que respondio")
                print("    2 argumento  = para recibir Id_transaction")
                print("    3 argumento  = para recibir Configuracion general del Microservicio")
                print("    4 argumento  = para recibir Data inicial de la transaccion")
                print("    5 argumento  = para recibir Respuesta del Worker anterior")
                print("*****************************************************************************")
            else:
                if len(arreglo) == 0:
                    print("****************************************")
                    print("No se recibio el flujo del a bifurcacion")
                    print("****************************************")
                else:
                    self.__inicializaciones["flujo"] = arreglo
                    self.__inicializa(2)
    
    def __obtererConfiguraciones(self):
        bRetorno = True

        cg,cs,err = self.__configuracionGeneralServicios()
        cg["configService"] = cs
        x = cg
        self.__errores = err    
        self.__inicializaciones["configuraciones"] = x

        return bRetorno

    def __buscar(self,microservicio):
        ret = {}
        for item in self.__inicializaciones["flujo"]:
            if item["owner_conf"] == microservicio:
                ret = item
                break
        return ret

    def __guardarMetadata(self,col,obj):
        #print("Guardar metadata en BD")
        try:
            
            obj["fecha_alta"] = datetime.datetime.now()
            self.__metadataBifurcacion.append(obj)
        except Exception as e:
            print("error :"+str(e))

    def __grabarRespuestaMicroservicio(self,respuesta):
        #print("Grabar respuesta_microservicio_granular")
        try:
            print("anule grabar respuesta microservicio granukar")
        except Exception as e:
            print("error :"+str(e))
    
    def __obtenerMetadataInicial(self,id):
        #print("Obtener Metadata Inicial")
        meta = {}
        data = {}
        try:
            index = 0
            for item in self.__metadataBifurcacion:
                if id == item["_id"]:
                    data = item["data"]
                    meta = item["metadata"]
                    meta["mtype"] = "output"
                    break
                index += 1
        except Exception as e:
            print("error :"+str(e))

        return data,meta
    
    async def borrarMetadata(self,id):
        try:
            index = 0
            for item in self.__metadataBifurcacion:
                if id == item["_id"]:
                    self.__metadataBifurcacion.pop(index)
                    break
                index += 1
        except:
            print("")

    def __configuracionGeneralServicios(self):
        try:
            cnxMongo = self.db().conexion()
            db = cnxMongo[self.__bdConfig]
            collection = db["configuraciones"]
            info_gen = collection.find({"_id":"general"})
            #info_ser = collection.find({"_id":self.__inicializaciones["topicName"]})
            count = info_gen.count()
            if(count > 0):
                conf_gen = info_gen[0]["configuracion"]
                conf_serv = self.__configServ
                errores = self.__errores

                if "flask_server" in conf_serv :
                    conf_gen["flask_server"] = conf_serv["flask_server"]
                    conf_gen["flask_port"] = conf_serv["flask_port"]

                if "kafka_server" in conf_serv :
                    conf_gen["kafka_server"] = conf_serv["kafka_server"]
                    conf_gen["kafka_port"] = conf_serv["kafka_port"]

                if "mongo_server" in conf_serv :
                    conf_gen["mongo_server"] = conf_serv["mongo_server"]
                    conf_gen["mongo_port"] = conf_serv["mongo_port"]

                if "redis_server" in conf_serv :
                    conf_gen["redis_server"] = conf_serv["redis_server"]
                    conf_gen["redis_port"] = conf_serv["redis_port"]
                    conf_gen["redis_db_id"] = conf_serv["redis_db_id"]

                if "timeout" in conf_serv :
                    conf_gen["timeout"] = conf_serv["timeout"]

                if "reconexion" in conf_serv :
                    conf_gen["reconexion"] = conf_serv["reconexion"]

                if "timeout_internos" in conf_serv :
                    conf_gen["timeout_internos"] = conf_serv["timeout_internos"]

                if "tiempo_revision" in conf_serv:
                    conf_gen["tiempo_revision"] = conf_serv["tiempo_revision"]
                
                cnxMongo.close()
                return conf_gen,conf_serv,errores
            else:
                cnxMongo.close()
                print("No se ha Registrado la configuracion del la app")
                sys.exit(0)
            
        except Exception as e:
            print("error :"+str(e))
            print("No se ha Registrado la configuracion del la app")
            sys.exit(0)

    def __functionBifurcacion(self,configService,jsonArguments):
        log = print
        """Retorna topico a responder y json a escribir"""
        metadata = jsonArguments["metadata"]
        data = jsonArguments["data"]
        headers = jsonArguments["headers"]
        response = {}
        if "response" in jsonArguments:
            response = jsonArguments["response"]
        OWNER = metadata["owner"]
        ID_TRANSACCION = metadata["id_transaction"]
        try:
            log("[ "+ID_TRANSACCION + " ] - input - ["+metadata["owner"]+"] \nHeaders : " + str(headers) +"\nData : "+ str(data) +"\nResponse : "+ str(response)+ "\n" )
            metadata["mtype"] = "input"
            metadata["time"] = str(datetime.datetime.now())
            metadata["bifurcacion"] = True
            
            cursor_conf = self.__buscar(metadata["owner"])
            if "grabar_metadata" in cursor_conf:
                self.__guardarMetadata("metadata_"+metadata["owner"],{"_id":jsonArguments["metadata"]["id_transaction"],"metadata":jsonArguments["metadata"],"data":jsonArguments["data"]})
                uWorker_async = metadata["uworker"]
                string = str(time.time()).replace('.', '')
                jsonArguments["metadata"]["id_operacion"] = int(string)
                jsonArguments["metadata"]["uowner"] = uWorker_async
                jsonArguments["metadata"]["worker"] = cursor_conf["worker_conf"]
                jsonArguments["metadata"]["uworker"] = metadata["worker"]+"_"+str(metadata["id_operacion"])
                jsonArguments["metadata"]["owner"] = self.__inicializaciones["topicName"]
                data_mod = self.__functionWorkerCambiarData(OWNER,ID_TRANSACCION,self.__inicializaciones["configuraciones"],jsonArguments["data"],jsonArguments["data"])
                if data_mod != {}:
                    jsonArguments["data"] = data_mod
                jsonArguments["response"] = {}
                return jsonArguments["metadata"]["worker"],jsonArguments
            else:
                
                self.__grabarRespuestaMicroservicio({"servicio":metadata["owner"],"id_transaccion":jsonArguments["metadata"]["id_transaction"],"response":jsonArguments["response"]})
                data_inicial,metadata_inicial = self.__obtenerMetadataInicial(metadata["id_transaction"])
                success =True
                #Reviso la respuesta del servicio entrante
                if "response" in jsonArguments and jsonArguments["response"]["meta"]["status"] == "ERROR":
                    success = False
                
                # si success y  servicio es fin y  envio al servicio que sigue
                if success == True:
                    log("[ "+ID_TRANSACCION + " ] - "+metadata["owner"] +" SUCCESS"+ "\n")
                    if cursor_conf["end"] == False:
                        log("[ "+ID_TRANSACCION + " ] - "+metadata["owner"] +" NO ES SERVICIO FINAL"+ "\n")
                        uWorker_async = metadata["uworker"]
                        string = str(time.time()).replace('.', '')
                        jsonArguments["metadata"]["id_operacion"] = int(string)
                        jsonArguments["metadata"]["uowner"] = uWorker_async
                        jsonArguments["metadata"]["worker"] = cursor_conf["worker_conf"]
                        jsonArguments["metadata"]["uworker"] = metadata["worker"]+"_"+str(metadata["id_operacion"])
                        jsonArguments["metadata"]["owner"] = self.__inicializaciones["topicName"]
                        responseAnterior = {}
                        if "data" in jsonArguments["response"]:
                            responseAnterior = jsonArguments["response"]["data"]["response"]
                        else:
                            responseAnterior = jsonArguments["data"]
                        data_mod = self.__functionWorkerCambiarData(OWNER,ID_TRANSACCION,self.__inicializaciones["configuraciones"],data_inicial,responseAnterior)
                        if data_mod != {}:
                            jsonArguments["data"] = data_mod
                        jsonArguments["response"] = {}
                        return jsonArguments["metadata"]["worker"],jsonArguments
                    else:
                        log("[ "+ID_TRANSACCION + " ] - "+metadata["owner"] +" ES SERVICIO FINAL"+ "\n")
                        JSON_RESPUESTA_FIN = {}
                        if JSON_RESPUESTA_FIN == {}:
                            JSON_RESPUESTA_FIN = jsonArguments["response"]

                        loop.create_task(self.borrarMetadata(metadata["id_transaction"]))
                        msj = {"_id":metadata["id_transaction"],"response":JSON_RESPUESTA_FIN,"metadata":metadata_inicial}
                        return "respuesta_"+metadata["callback"],msj
                else:
                    log("[ "+ID_TRANSACCION + " ] - "+metadata["owner"] +" ERROR"+ "\n")
                    msj = {"_id":metadata["id_transaction"],"response":jsonArguments["response"],"metadata":metadata_inicial}
                    loop.create_task(self.borrarMetadata(metadata["id_transaction"]))
                    return "respuesta_"+metadata["callback"],msj
        except Exception as e:            
            error = {"_id":jsonArguments["metadata"]["id_transaction"],"servicio":self.__inicializaciones["topicName"],"error":str(e)}
            loop.create_task(self.borrarMetadata(jsonArguments["metadata"]["id_transaction"]))
            self.__escribirColaMensajeria("Errores_criticos",error,jsonArguments["metadata"]["id_transaction"])

        return self.__inicializaciones["topicName"],{}
    
    def __buscarMensaje(self,id):
        res = ""
        if str(id) in self.__errores:
            res = self.__errores[str(id)]
        else:
            res = "Error No Definido"
        return res

    def __response(self,code,data = None,metadata = None):
        response = {}
        response["meta"] = {}
        response["data"] = {}

        response["meta"]["id_transaction"] = metadata["id_transaction"]
        
        if code == 0:
            response["meta"]["status"] = "SUCCESS"    
            response["data"]["response"] = data
        else:
            response["meta"]["status"] = "ERROR"
            response["data"]["response"] = {
                "errorCode":str(code),
                "userMessage":self.__buscarMensaje(str(code))
            }
        return response
        
    async def escribir(self,topico,respuesta,idTransaction):
        msj = self.__json_to_b64(respuesta)
        self.__producer.send(topico,key=str.encode(str(idTransaction)),value=msj)
        self.__producer.flush()
        print("[ "+idTransaction+" ] -  output - ["+topico+"]\n"+str(respuesta) + "\n")

    def __escribirColaMensajeria(self,topico,respuesta,idTransaction = ""):
        loop.create_task(self.escribir(topico,respuesta,idTransaction))
    
    def llamarWorkerAsincrono(self,topico,respuesta,idTransaction = ""):
        loop.create_task(self.escribir(topico,respuesta,idTransaction))
        
    async def __functionBridge(self,function,*args):


        if "data" in args[1] and ("smoketest" in args[1]["data"] or ("configuraciones" in args[1]["data"] and args[1]["data"]["configuraciones"] == True)):
            metadata = args[1]["metadata"]
            data = args[1]["data"]
            headers = args[1]["headers"]
            respuesta = {}
            respuesta["meta"] = {}
            respuesta["data"] = {}
            respuesta["meta"]["id_transaction"] = ""
            respuesta["meta"]["status"] = "SUCCESS"
            if "smoketest" in args[1]["data"]:
                respuesta["data"]["response"] = {
                    "errorCode":"0",
                    "userMessage":"smoketest ok"
                }
            else:
                respuesta["data"]["response"] = self.__configServ

            respuestax = {}                                                                                                                                                                                                                                                  																																																														
            respuestax["metadata"] = metadata                                                                                                                                                                                                                                            
            respuestax["headers"] = headers                                                                                                                                                                                                                                              
            respuestax["data"] = data     
            respuestax["response"] = respuesta
            respuestax["metadata"]["time"] = str(datetime.datetime.now())                                                                                                                                                                                                                
            respuestax["metadata"]["worker"]  = respuestax["metadata"]["owner"]                                                                                                                                                                                                           
            respuestax["metadata"]["owner"]  = self.__inicializaciones["topicName"]
            respuestax["metadata"]["mtype"] = "output"                                                                                                                                                                                                                                   
            if("uowner" in respuestax["metadata"]):                                                                                                                                                                                                                                      
                uowner = respuestax["metadata"]["uowner"]                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                        
            if("uworker" in respuestax["metadata"]):                                                                                                                                                                                                                                     
                uworker = respuestax["metadata"]["uworker"]                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                        
            respuestax["metadata"]["uworker"] = uowner                                                                                                                                                                                                                                   
            respuestax["metadata"]["uowner"] = uworker 


            if(metadata["bifurcacion"] == True):                                                                                                                                                                                                                                        
                metadata["bifurcacion"] = False                                                                                                                                                                                                                                     
                TOPICO = respuestax["metadata"]["callback"]
                self.__escribirColaMensajeria(TOPICO,respuestax,metadata["id_transaction"])
            else:
                TOPICO = "respuesta_"+metadata["owner"]
                respuesta2 = {"_id":respuestax["metadata"]["id_transaction"],"response":respuestax["response"],"metadata":respuestax["metadata"]}
                self.__escribirColaMensajeria(TOPICO,respuesta2,metadata["id_transaction"])
        else:                
            if self.__esWorker == True:
                #guarda metadata
                msj2 = {}
                msj2["data"] =  args[1]["data"]
                msj2["headers"] =  args[1]["headers"]
                msj2["metadata"] =  args[1]["metadata"]
                #self.__guardarMetadata("metadata_"+self.__inicializaciones["topicName"],{"_id":args[1]["metadata"]["id_transaction"],"metadata":args[1]["metadata"]})
                code = 0
                datax = {}
                try:
                    entrada = DictConvert(msj2)
                    conf = DictConvert(args[0])
                    code,dataxx = function(conf,entrada,args[2])
                    try:
                        datax = dataxx.toJson()
                    except:
                        datax = dataxx
                except Exception as e:
                    code,datax  = -99,{}
                    error = {"_id":args[1]["metadata"]["id_transaction"],"servicio":self.__inicializaciones["topicName"],"error":str(e)}
                    self.__escribirColaMensajeria("Errores_criticos",error,args[1]["metadata"]["id_transaction"])
                
                metadata = args[1]["metadata"]
                data = args[1]["data"]
                headers = args[1]["headers"]

                if "metadata" not in args[1] or "data" not in args[1] or "headers" not in args[1]:
                    print("No contiene datos correctos")
                else:
                    respuesta = self.__response(code,datax,metadata)
                    respuestax = {}                                                                                                                                                                                                                                                              																																																														
                    respuestax["metadata"] = metadata                                                                                                                                                                                                                                            
                    respuestax["headers"] = headers                                                                                                                                                                                                                                              
                    respuestax["data"] = data                                                                                                                                                                                                                                              
                    respuestax["response"] = respuesta                                                                                                                                                                                                                                      
                    respuestax["metadata"]["time"] = str(datetime.datetime.now())                                                                                                                                                                                                                
                    respuestax["metadata"]["worker"]  = respuestax["metadata"]["owner"]                                                                                                                                                                                                           
                    respuestax["metadata"]["owner"]  = self.__inicializaciones["topicName"]
                    respuestax["metadata"]["mtype"] = "output"                                                                                                                                                                                                                                   
                    if("uowner" in respuestax["metadata"]):                                                                                                                                                                                                                                      
                        uowner = respuestax["metadata"]["uowner"]                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                
                    if("uworker" in respuestax["metadata"]):                                                                                                                                                                                                                                     
                        uworker = respuestax["metadata"]["uworker"]                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                
                    respuestax["metadata"]["uworker"] = uowner                                                                                                                                                                                                                                   
                    respuestax["metadata"]["uowner"] = uworker    

                    if(metadata["bifurcacion"] == True):                                                                                                                                                                                                                                        
                        metadata["bifurcacion"] = False                                                                                                                                                                                                                                     
                        TOPICO = respuestax["metadata"]["callback"]
                        self.__escribirColaMensajeria(TOPICO,respuestax,respuestax["metadata"]["id_transaction"])
                    else:
                        TOPICO = "respuesta_"+metadata["owner"]                                                                                                                                                                                                                             
                        respuesta2 = {"_id":respuestax["metadata"]["id_transaction"],"response":respuestax["response"],"metadata":respuestax["metadata"]}                                                                                                                                                                                                                                                                                                                             
                        self.__escribirColaMensajeria(TOPICO,respuesta2,respuestax["metadata"]["id_transaction"])
            else:
                TOPICO,respuesta = function(args[0],args[1])
                self.__escribirColaMensajeria(TOPICO,respuesta,args[1]["metadata"]["id_transaction"])

    def __conecctMQ(self):
        ret = False
        try:
            self.__producer = KafkaProducer(bootstrap_servers=self.__inicializaciones["configuraciones"]["kafka_servers"])
            #self.__consumer = KafkaConsumer(self.__inicializaciones["topicName"],bootstrap_servers=self.__inicializaciones["configuraciones"]["kafka_servers"],group_id=str(self.__inicializaciones["topicName"]))
            #self.__producer2 = AIOKafkaProducer(loop=loop, bootstrap_servers=self.__inicializaciones["configuraciones"]["kafka_servers"])
            self.__consumer2 = AIOKafkaConsumer(self.__inicializaciones["topicName"],loop=loop, bootstrap_servers=self.__inicializaciones["configuraciones"]["kafka_servers"],group_id=str(self.__inicializaciones["topicName"]))
            ret = True
        except:
            ret = False
        return ret

    async def __consume(self,function,configService):
        print(Fore.CYAN+" * Running Daemon on : " + str(self.__inicializaciones["configuraciones"]["kafka_servers"]) + " topic: " + self.__inicializaciones["topicName"]+Fore.WHITE)
        #await self.__producer2.start()
        await self.__consumer2.start()
        try:
            async for msg in self.__consumer2:
                try:
                    msj = self.__b64_to_json(msg.value)
                    loop.create_task(self.__functionBridge(function,configService,msj,self.llamarWorkerAsincrono))   
                except:
                    pass
        finally:
            await self.__consumer2.stop()
            #await self.__producer2.stop()
            print("se desconecto la cola de mensajeria (reconectar)")
            self.__conecctMQ()
            if self.__esWorker == True:
                self.__streamMessageQueue(self.__functionWorkerCambiarData)
            else:
                self.__streamMessageQueue(self.__functionBifurcacion)
            
    def __streamMessageQueue(self,function):

        proxy = {}
        if "proxy" in self.__inicializaciones["configuraciones"]:
            proxy = self.__inicializaciones["configuraciones"]["proxy"]
        
        configService = {
            "configGral":{
                "proxy":proxy,
                "timeoutInternos":self.__inicializaciones["configuraciones"]["timeout_internos"],
                "mongoUri" : self.__inicializaciones["configuraciones"]["mongo_uri"]},
            "configService":self.__inicializaciones["configuraciones"]["configService"]
        }
        self.__inicializaciones["mongoUri"] = configService["configGral"]["mongoUri"]

        if self.__conecctMQ() ==True:
            loop.run_until_complete(self.__consume(function,configService))
        else:
	        print("Error:\n############################\nNo esta activo el Message Queue\n############################\n")

