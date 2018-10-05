import time

from connection import QISConnection, PYConnection, QPSConnection

class quarchDevice:
    
    def __init__(self, ConString, ConType = "PY", timeout = "5"):
        self.ConString = ConString
        self.ConType = ConType
        self.timeout = int(timeout)

        # Initializes the object as a python or QIS connection
        ## Python
        if self.ConType == "PY":
            self.connectionObj = PYConnection(self.ConString)    # Creates the connection object. 
            
            # Exposes the connection type and module for later use.
            self.connectionName = self.connectionObj.ConnTarget
            self.connectionTypeName = self.connectionObj.ConnTypeStr
        
        ## QIS
        # ConType may be QIS only or QIS:ip:port [:3] checks if the first 3 letters are QIS.
        elif self.ConType[:3] == "QIS":
            # If host and port are specified.
            try:
                # Extract QIS, host and port.
                QIS, host, port = self.ConType.split(':')
                # QIS port should be an int.
                port = int(port)
            # If host and port are not specified. 
            except:
                host='127.0.0.1'
                port=9722

            numb_colons = self.ConString.count(":")
            if numb_colons == 1:
                self.ConString = self.ConString.replace(':', '::')

            # Creates the connection object.
            self.connectionObj = QISConnection(self.ConString, host, port)  

            ##FROM HERE. MATT CREATED - 28-09-18##

            list = self.connectionObj.qis.getDeviceList()
            list_str = "".join(list)

            #check for device in list, has a timeout
            while 1:
                if (self.timeout == 0):
                    raise ValueError("Search timeout - no Quarch module found.")
                
                elif (self.ConString in list_str):
                    break
                
                else:
                    time.sleep(1)
                    self.timeout-=1
                    list = self.connectionObj.qis.getDeviceList()

            self.connectionObj.qis.sendAndReceiveCmd(cmd="$default " + self.ConString)
            
         ## QPS
        elif self.ConType[:3] == "QPS":
            try:
                # Extract QIS, host and port.
                QIS, host, port = self.ConType.split(':')
                # QIS port should be an int.
                port = int(port)
            # If host and port are not specified. 
            except:
                host='127.0.0.1'
                port=9822

            numb_colons = self.ConString.count(":")
            if numb_colons == 1:
                self.ConString = self.ConString.replace(':', '::')


            # Creates the connection object.
            self.connectionObj = QPSConnection(host, port) 
                                    
        ## Neither PY or QIS, connection cannot be created.
        else:
            raise ValueError("Invalid connection type. Please select PY or QIS")
  
    def sendCommand(self, CommandString):
        if self.ConType[:3] == "QIS":
        
            numb_colons = self.ConString.count(":")
            if numb_colons == 1:
                self.ConString = self.ConString.replace(':', '::')
                
            return self.connectionObj.qis.sendCmd(self.ConString, CommandString)
        
        elif self.ConType == "PY":
            return self.connectionObj.connection.sendCommand(CommandString)
        
        elif self.ConType[:3] == "QPS":
            #checking if the command string passed has a $ as first char
            if CommandString[0] != '$':
                CommandString = self.ConString + " " + CommandString

            return self.connectionObj.qps.sendCmdVerbose(CommandString)

    def openConnection(self):
        if self.ConType[:3] == "QIS":
            self.connectionObj.qis.connect()

        elif  self.ConType == "PY":
            del self.connectionObj
            self.connectionObj = PYConnection(self.ConString)
            return self.connectionObj
        
        elif self.ConType[:3] == "QPS":
            self.connectionObj.qps.connect(self.ConString)
 
    def closeConnection(self):
        if self.ConType[:3] == "QIS":
            self.connectionObj.qis.disconnect()
        elif self.ConType == "PY":
            self.connectionObj.connection.close()

        elif self.ConType[:3] == "QPS":
            self.connectionObj.qps.disconnect(self.ConString)

