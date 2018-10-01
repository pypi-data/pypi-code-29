#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (c) 2016 MasterCard International Incorporated
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this list of
# conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice, this list of
# conditions and the following disclaimer in the documentation and/or other materials
# provided with the distribution.
# Neither the name of the MasterCard International Incorporated nor the names of its
# contributors may be used to endorse or promote products derived from this software
# without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
# SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
# TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#


from __future__ import absolute_import
from mastercardapicore import BaseObject
from mastercardapicore import RequestMap
from mastercardapicore import OperationConfig
from mastercardapicore import OperationMetadata
from mastercardmastercom import ResourceConfig

class Chargebacks(BaseObject):
    """
    
    """

    __config = {
        
        "4712c4f2-4f92-4a02-b637-0659fd4cadc0" : OperationConfig("/mastercom/v3/chargebacks/acknowledge", "update", [], []),
        
        "fe9a9b48-e17f-4e1b-b7b5-9ea013244c9d" : OperationConfig("/mastercom/v3/claims/{claim-id}/chargebacks", "create", [], []),
        
        "fb0bb790-fc84-4182-acd0-38f7ca07868f" : OperationConfig("/mastercom/v3/claims/{claim-id}/chargebacks/{chargeback-id}/reversal", "create", [], []),
        
        "86d7c6c4-0247-47ef-a439-028e1837d545" : OperationConfig("/mastercom/v3/claims/{claim-id}/chargebacks/{chargeback-id}/documents", "query", [], ["format"]),
        
        "5f40ff03-82cf-472d-9a35-3b0088ed646a" : OperationConfig("/mastercom/v3/claims/{claim-id}/chargebacks/loaddataforchargebacks", "create", [], []),
        
        "13477f1d-a909-4052-8135-c65561c6efd2" : OperationConfig("/mastercom/v3/chargebacks/status", "update", [], []),
        
        "f88070db-a836-4d0a-922f-9677bd893261" : OperationConfig("/mastercom/v3/claims/{claim-id}/chargebacks/{chargeback-id}", "update", [], []),
        
    }

    def getOperationConfig(self,operationUUID):
        if operationUUID not in self.__config:
            raise Exception("Invalid operationUUID: "+operationUUID)

        return self.__config[operationUUID]

    def getOperationMetadata(self):
        return OperationMetadata(ResourceConfig.getInstance().getVersion(), ResourceConfig.getInstance().getHost(), ResourceConfig.getInstance().getContext(), ResourceConfig.getInstance().getJsonNative(), ResourceConfig.getInstance().getContentTypeOverride())



    def acknowledgeReceivedChargebacks(self):
        """
        Updates an object of type Chargebacks

        @return Chargebacks object representing the response.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("4712c4f2-4f92-4a02-b637-0659fd4cadc0", self)





    @classmethod
    def create(cls,mapObj):
        """
        Creates object of type Chargebacks

        @param Dict mapObj, containing the required parameters to create a new object
        @return Chargebacks of the response of created instance.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("fe9a9b48-e17f-4e1b-b7b5-9ea013244c9d", Chargebacks(mapObj))






    @classmethod
    def createReversal(cls,mapObj):
        """
        Creates object of type Chargebacks

        @param Dict mapObj, containing the required parameters to create a new object
        @return Chargebacks of the response of created instance.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("fb0bb790-fc84-4182-acd0-38f7ca07868f", Chargebacks(mapObj))











    @classmethod
    def retrieveDocumentation(cls,criteria):
        """
        Query objects of type Chargebacks by id and optional criteria
        @param type criteria
        @return Chargebacks object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("86d7c6c4-0247-47ef-a439-028e1837d545", Chargebacks(criteria))

    @classmethod
    def getPossibleValueListsForCreate(cls,mapObj):
        """
        Creates object of type Chargebacks

        @param Dict mapObj, containing the required parameters to create a new object
        @return Chargebacks of the response of created instance.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("5f40ff03-82cf-472d-9a35-3b0088ed646a", Chargebacks(mapObj))







    def chargebacksStatus(self):
        """
        Updates an object of type Chargebacks

        @return Chargebacks object representing the response.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("13477f1d-a909-4052-8135-c65561c6efd2", self)






    def update(self):
        """
        Updates an object of type Chargebacks

        @return Chargebacks object representing the response.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("f88070db-a836-4d0a-922f-9677bd893261", self)






