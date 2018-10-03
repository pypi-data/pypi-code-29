# -*- coding: utf-8 -*-
'''
@author: KaueBonfim
'''
''' Este arquivo tem o intuito de promover conexão e funções com banco de dados'''
import pymysql
import cx_Oracle
import sqlite3
import sqlalchemy
from pandas.io import sql
from pymongo import MongoClient
from .Error import Banco_erro

class Relacional():
    ''' Esta classe tem o intuito prover conexão e funções de CRUD em banco Relacional'''
    
    def __init__(self,servidor,user=None,senha=None,banco=None,endereco=None,porta=None):
        '''No construtor temos seis parametros sendo um obrigatorio
        
        Servidor(obrigatorio):Tipo de Servidor de banco de dados que vai trabalhar.EXP.: 'Oracle', 'SQLite' e 'MySQL'
        user: Usuario de conexão com o servidor
        senha: Senha de conexão com o servidor
        banco: O banco de dados na qual iremos no conectar no servidor
        endereco: É o endereço na qual vamos usar para nos conectar ao servidor.Exemplo: URL OU localhost OU 127.0.0.1...
        porta: É a porta de conexão para o endereço. Exemplo: 8080, 3601 ...
        '''
        
        if (servidor=="MySQL"):
            if(servidor is not None and user is not None and senha is not None and banco is not None and endereco is not None\
               and  porta is not None):
                self.__bank=pymysql.connect(user=user,passwd=senha,db=banco,host=endereco,port=porta,autocommit=True)
                
            else:
                Erro="""Não é um servidor valor valido para MySQL!
                        Valores obrigatorios são:
                        user=usuario que vai ser usado no banco,
                        senha=senha do usuario,
                        banco=banco de dados que sera usado,
                        endereco=endereco host do banco,
                        porta=porta do endereço de saida do banco
                        """
                raise Banco_erro(Erro)
        elif (servidor=="Oracle"):
            if(servidor is not None and user is not None and senha is not None and endereco is not None\
               and  porta is not None):
                self.__bank=cx_Oracle.connect('{}/{}@{}{}'.format(user,senha,endereco,porta))
            else:
                Erro="""Não é um servidor valor valido para MySQL!
                        Valores obrigatorios são:
                        user=usuario que vai ser usado no banco,
                        senha=senha do usuario,
                        endereco=endereco host do banco,
                        porta=porta do endereço de saida do banco
                        
                        """
                raise Banco_erro(Erro)
            
            
        elif(servidor=="SQLite"):
            if(banco is not None):
                self.__bank=sqlite3.connect(banco)
            else:
                Erro="""Não é um servidor valor valido para SQLite!
                        Valores obrigatorios são:
                       banco=Url ou Arquivo
                        """
                raise Banco_erro(Erro)
        else:
            Erro="\n\nNão é um servidor valido!\nOs servidores validos são: 'Oracle','MySQL' ou 'SQLite'\nInsira um valor correto!"
            raise Banco_erro(Erro)
            
                
        self.cursor=self.__bank.cursor()
        
    def buscar_tudo(self,query:str):
        '''Este metodo busca todos os valores de uma tabela, baseado em uma Query. Exemplo: buscar_tudo("SELECT {} FROM {}".format("*","table_name"))
           O retorno é uma lista com  dicionarios como colunas da tabela como chave
           , na qual temos os parametros
           
           query(obrigatorio): Select do banco'''
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def buscar_um(self,query:str):
        '''Este metodo busca o primeiro valor de uma tabela, baseado em uma Query. Exemplo: buscar_um("SELECT {} FROM {}".format("*","table_name"))
           O retorno é um dicionarios como colunas da tabela como chave
           , na qual temos os parametros
           
           query(obrigatorio): Select do banco'''
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
        
    def inserir_lista(self,sql:str,valores:list):
        '''Este metodo inseri diversos valores em uma tabela, baseado em uma script sql. Exemplo: 
            inserir_lista("INSERT INTO {} VALUES ({}, '{}');",[("a","b","c"),("a","b","c")...])
            
            
           , na qual temos os parametros
           
           sql(obrigatorio): SQL para inserir valor
           valores(obrigatorio):lista com tuplas de valores para serem inseridos'''
        self.cursor.executemany(sql,valores)
        self.__bank.commit()
    
    def inserir(self,sql:str,valores:tuple):
        '''Este metodo inseri diversos valores em uma tabela, baseado em uma script. Exemplo: inserir("INSERT INTO {} VALUES ({}, '{}');",("a","b","c"))
           , na qual temos os parametros
           
           sql(obrigatorio): SQL para inserir valor
           valores(obrigatorio):uma tupla de valores para serem inseridos'''
        self.cursor.execute(sql,valores)
        self.__bank.commit()
    
    def deletar(self,sql:str,valores:tuple):
        '''Este metodo deleta valores em uma tabela, baseado em uma script. Exemplo: deletar("DELETE FROM {} WHERE id = {}",("TABELA","3"))
           , na qual temos os parametros
           
           sql(obrigatorio): SQL para deletar valores da tabela
           valores(obrigatorio):uma tupla de valores para serem deletados'''
        self.cursor.execute(sql,valores)
        self.__bank.commit()
    
    def atualizar(self,sql:str,valores:tuple):
        '''Este metodo atualiza valores em uma tabela, baseado em uma script. Exemplo: atualizar("UPDATE {} SET title = {} WHERE id = {}",("TABELA","x","3"))
           , na qual temos os parametros
           
           sql(obrigatorio): SQL para atualizar valores da tabela
           valores(obrigatorio):uma tupla de valores para serem atualizados'''
        self.cursor.execute(sql,valores)
        self.__bank.commit()
        
    def fechar_conexao(self):
        '''Este metodo fecha conexão com o driver. Exemplo: fechar()'''
        self.cursor.close()
        self.__bank.close()
        
    
    
class Alquimista():
    ''' Esta classe tem o intuito prover conexão e funções de CRUD em banco Relacional e fazer um link direto com DataFrame'''
    def __init__(self,url):   
        '''No construtor temos um parametro sendo um obrigatorio
        
        url= É a url de conexão do servidor de banco de dados. EXEMPLO.:'jdbc:sqlserver://localhost:1433' ou'postgresql://usr:pass@localhost:5432/sqlalchemy'
        
        USAR URL VALIDA
        '''
        try:
            self.__engine=sqlalchemy.create_engine(url)
        except:
            Erro='''
            Url Invalida!!
            Use o Exemplo:
            sqlserver://[serverName[\instanceName][:portNumber]][;property=value[;property=value]] 
            '''
            raise Banco_erro(Erro)
        
    def buscar(self,query,params=None):
        '''Este metodo busca valores em uma tabela, baseado em uma script/Query. Exemplo: 
            buscar("SELECT %(valor) FROM data_table group by dept",[(valor:valor)])
        
           , na qual temos os parametros
           
           query(obrigatorio): query no banco
           params(obrigatorio):uma tupla de valores para serem atualizados'''
        return sql.read_sql_query(sql=query.format(params), con=self.__engine)
    
    def DF_para_sql(self,DF,nome_tabela):
        '''Este metodo inseri um DataFrame em um banco. Exemplo: DF_para_sql(DF,"TabelaNova")
           , na qual temos os parametros
           
           DF(obrigatorio): DataFrame que sera inserido
           nome_tabela(obrigatorio):Nome da tabela'''
        DF.to_sql(nome_tabela,self.__engine)
    
    
        
class Nao_Relacional():
    ''' Esta classe tem o intuito prover conexão e funções de CRUD em banco Não Relacional'''
    def __init__(self,Servidor,banco=None,endereco=None,porta=None):       
        '''No construtor temos seis parametros sendo um obrigatorio
        
        Servidor(obrigatorio):Tipo de Servidor de banco de dados que vai trabalhar.EXP.: 'Mongo'
        banco: O banco de dados na qual iremos no conectar no servidor
        endereco: É o endereço na qual vamos usar para nos conectar ao servidor.Exemplo: URL OU localhost OU 127.0.0.1...
        porta: É a porta de conexão para o endereço. Exemplo: 8080, 3601 ...
        '''
        if(Servidor=='Mongo'):
            if(Servidor is not None and banco is not None and endereco is not None and porta is not None):
                self.__con=MongoClient(endereco,porta)
                self.__bank=self.__con[banco]
            else:
                
                Erro="""Não é um servidor valor valido para MongoDB!
                        Valores obrigatorios são:
                        banco=banco de dados que sera usado,
                        endereco=endereco host do banco,
                        porta=porta do endereço de saida do banco
                        """
                raise Banco_erro(Erro)
        else:
            Erro="\n\nNão é um servidor valido!\nOs servidores validos são: 'Mongo'\nInsira um valor correto!"
            raise Banco_erro(Erro)  
        
    def buscar(self,dicionario,colecao):
        '''Este metodo busca o primeiro valor de chaves no banco: 
            buscar({"nome": "Radioactive"})
            
           O retorno é um dicionario com as chave que foi procurada
           , na qual temos os parametros
           
           dicionario: dicionario com chave e valor que queremos procurar
           coleção: é como uma tabela de banco de dados que queremos procurar'''
        return self.__bank[colecao].find_one(dicionario)
    
    def buscar_tudo(self,dicionario,colecao):
        '''Este metodo busca o todos os  valores de chaves no banco: 
            buscar_tudo({"nome": "Radioactive"})
            
           O retorno é um dicionario com as chave que foi procurada
           , na qual temos os parametros
           
           dicionario: dicionario com chave e valor que queremos procurar
           coleção: é como uma tabela de banco de dados que queremos procurar'''
        return self.__bank[colecao].find(dicionario)
    
    def atualizar(self,anterior,atual):
        '''Este metodo atualiza o todos os  valores de chaves no banco: 
            atualizar({"_id": 2},{"%set",{"novo":"Novooooo"}})
            
           , na qual temos os parametros
           
           anterior: dicionario com chave e valor que queremos procurar para atualizar
           atual: e o valor que queremos atualizar'''
        self.__bank.update_many(anterior,atual)
        
    def inserir(self,dicionario,ids=True):
        '''Este metodo inseri o todos os  valores de chaves no banco: 
            inserir({\
              "nome": "Nothing left to say",\
              "banda": "Imagine Dragons",\
              "categorias": ["indie", "rock"],\
              "lancamento": datetime.datetime.now()\
             },True)
            
           , na qual temos os parametros
           
           dicionario: dicionario com chave e valor que queremos inserir 
           ids: True, se vamos inserir um id e False, se o Id vir no dicionario'''
        if(ids==True):
            self.__bank.insert_one(dicionario).inserted_id
        else:
            self.__bank.insert_one(dicionario)
        
        
    def inserir_lista(self,lista,ids=True):
        '''Este metodo inseri diversos valores chave no banco: 
            inserir_lista({\
              "nome": "Nothing left to say",\
              "banda": "Imagine Dragons",\
              "categorias": ["indie", "rock"],\
              "lancamento": datetime.datetime.now()\
             },True)
            
           , na qual temos os parametros
           
           lista: lista de dicionarios com chave e valor que queremos inserir 
           ids: True, se vamos inserir um id e False, se o Id vir no dicionario'''
        if(ids==True):
            self.__bank.insert_many(lista).inserted_id
        else:
            self.__bank.insert_many(lista)
        
    def deletar(self,dicionario):
        '''Este metodo deletar um valore chave no banco: 
            deletar({"_id": 1})
            
           , na qual temos os parametros
           
           dicionario: dicionario de valor que queremos deletar'''
        self.__bank.delet_one(dicionario)
        
    def deletar_tudo(self,params):
        '''Este metodo deletar diversos valores chave no banco: 
            deletar_tudo({"banda": "Imagine Dragons"})
            
           , na qual temos os vparametros
           
           dicionario: dicionario de valor que queremos deletar'''
        self.__bank.delete_many(params)