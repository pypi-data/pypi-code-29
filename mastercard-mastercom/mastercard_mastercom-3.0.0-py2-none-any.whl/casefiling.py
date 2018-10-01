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

class CaseFiling(BaseObject):
    """
    
    """

    __config = {
        
        "a0aec154-3c9c-41c1-9ca5-7373504a97e8" : OperationConfig("/mastercom/v3/cases", "create", [], []),
        
        "5af5dd15-0ce8-45a0-83d6-bda92ecf80ef" : OperationConfig("/mastercom/v3/cases/{case-id}/documents", "query", [], ["format","memo"]),
        
        "9d834fce-20c5-4557-a3ab-2e36a282e38f" : OperationConfig("/mastercom/v3/cases/status", "update", [], []),
        
        "a727b8cf-7e80-4e86-a63c-0b2270f3ce4d" : OperationConfig("/mastercom/v3/cases/{case-id}", "update", [], []),
        
    }

    def getOperationConfig(self,operationUUID):
        if operationUUID not in self.__config:
            raise Exception("Invalid operationUUID: "+operationUUID)

        return self.__config[operationUUID]

    def getOperationMetadata(self):
        return OperationMetadata(ResourceConfig.getInstance().getVersion(), ResourceConfig.getInstance().getHost(), ResourceConfig.getInstance().getContext(), ResourceConfig.getInstance().getJsonNative(), ResourceConfig.getInstance().getContentTypeOverride())


    @classmethod
    def create(cls,mapObj):
        """
        Creates object of type CaseFiling

        @param Dict mapObj, containing the required parameters to create a new object
        @return CaseFiling of the response of created instance.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("a0aec154-3c9c-41c1-9ca5-7373504a97e8", CaseFiling(mapObj))











    @classmethod
    def retrieveDocumentation(cls,criteria):
        """
        Query objects of type CaseFiling by id and optional criteria
        @param type criteria
        @return CaseFiling object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("5af5dd15-0ce8-45a0-83d6-bda92ecf80ef", CaseFiling(criteria))


    def caseFilingStatus(self):
        """
        Updates an object of type CaseFiling

        @return CaseFiling object representing the response.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("9d834fce-20c5-4557-a3ab-2e36a282e38f", self)






    def update(self):
        """
        Updates an object of type CaseFiling

        @return CaseFiling object representing the response.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("a727b8cf-7e80-4e86-a63c-0b2270f3ce4d", self)






