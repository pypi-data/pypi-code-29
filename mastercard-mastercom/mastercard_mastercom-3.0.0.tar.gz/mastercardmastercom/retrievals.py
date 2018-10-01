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

class Retrievals(BaseObject):
    """
    
    """

    __config = {
        
        "7ae68c48-6e20-43e3-aeb6-337fdbf6356b" : OperationConfig("/mastercom/v3/claims/{claim-id}/retrievalrequests/{request-id}/fulfillments", "create", [], []),
        
        "03f98d53-d792-44ef-95d2-5cdb234735a0" : OperationConfig("/mastercom/v3/claims/{claim-id}/retrievalrequests", "create", [], []),
        
        "b6486902-c5bb-4afa-9d59-c29e3f3171dc" : OperationConfig("/mastercom/v3/claims/{claim-id}/retrievalrequests/loaddataforretrievalrequests", "query", [], []),
        
        "f43271a7-3512-428f-9f0f-832ab7589d8b" : OperationConfig("/mastercom/v3/claims/{claim-id}/retrievalrequests/{request-id}/documents", "query", [], ["format"]),
        
        "c318a78f-6bf3-403d-b4dd-8ab84f6f8bbc" : OperationConfig("/mastercom/v3/claims/{claim-id}/retrievalrequests/{request-id}/fulfillments/response", "create", [], []),
        
        "b05b31e5-6ef1-497f-9491-216605c3c881" : OperationConfig("/mastercom/v3/retrievalrequests/status", "update", [], []),
        
    }

    def getOperationConfig(self,operationUUID):
        if operationUUID not in self.__config:
            raise Exception("Invalid operationUUID: "+operationUUID)

        return self.__config[operationUUID]

    def getOperationMetadata(self):
        return OperationMetadata(ResourceConfig.getInstance().getVersion(), ResourceConfig.getInstance().getHost(), ResourceConfig.getInstance().getContext(), ResourceConfig.getInstance().getJsonNative(), ResourceConfig.getInstance().getContentTypeOverride())


    @classmethod
    def acquirerFulfillARequest(cls,mapObj):
        """
        Creates object of type Retrievals

        @param Dict mapObj, containing the required parameters to create a new object
        @return Retrievals of the response of created instance.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("7ae68c48-6e20-43e3-aeb6-337fdbf6356b", Retrievals(mapObj))






    @classmethod
    def create(cls,mapObj):
        """
        Creates object of type Retrievals

        @param Dict mapObj, containing the required parameters to create a new object
        @return Retrievals of the response of created instance.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("03f98d53-d792-44ef-95d2-5cdb234735a0", Retrievals(mapObj))











    @classmethod
    def getPossibleValueListsForCreate(cls,criteria):
        """
        Query objects of type Retrievals by id and optional criteria
        @param type criteria
        @return Retrievals object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("b6486902-c5bb-4afa-9d59-c29e3f3171dc", Retrievals(criteria))






    @classmethod
    def getDocumentation(cls,criteria):
        """
        Query objects of type Retrievals by id and optional criteria
        @param type criteria
        @return Retrievals object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("f43271a7-3512-428f-9f0f-832ab7589d8b", Retrievals(criteria))

    @classmethod
    def issuerRespondToFulfillment(cls,mapObj):
        """
        Creates object of type Retrievals

        @param Dict mapObj, containing the required parameters to create a new object
        @return Retrievals of the response of created instance.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("c318a78f-6bf3-403d-b4dd-8ab84f6f8bbc", Retrievals(mapObj))







    def retrievalFullfilmentStatus(self):
        """
        Updates an object of type Retrievals

        @return Retrievals object representing the response.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("b05b31e5-6ef1-497f-9491-216605c3c881", self)






