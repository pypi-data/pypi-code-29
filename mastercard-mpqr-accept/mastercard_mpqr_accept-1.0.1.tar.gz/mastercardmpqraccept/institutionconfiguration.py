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
from mastercardmpqraccept import ResourceConfig

class InstitutionConfiguration(BaseObject):
    """
    
    """

    __config = {
        
        "69579603-119b-4a58-9e72-543609d9bd4f" : OperationConfig("/labs/proxy/mpqr-accept/v1/api/bank/configuration", "query", [], []),
        
        "1d5b0f4d-fe38-4cb9-9476-68736beffa93" : OperationConfig("/labs/proxy/mpqr-accept/v1/api/bank/configuration/publish", "update", [], []),
        
        "c96c791c-4301-4cff-b2ac-87e6d0807263" : OperationConfig("/labs/proxy/mpqr-accept/v1/api/bank/configuration", "update", [], []),
        
        "7761cebd-21e2-4242-9e24-5ac5bd57f461" : OperationConfig("/labs/proxy/mpqr-accept/v1/api/bank/configuration/terminate", "update", [], []),
        
        "aa49eddc-e266-41a7-80f7-26e7158037b7" : OperationConfig("/labs/proxy/mpqr-accept/v1/api/bank/configuration/unpublish", "update", [], []),
        
    }

    def getOperationConfig(self,operationUUID):
        if operationUUID not in self.__config:
            raise Exception("Invalid operationUUID: "+operationUUID)

        return self.__config[operationUUID]

    def getOperationMetadata(self):
        return OperationMetadata(ResourceConfig.getInstance().getVersion(), ResourceConfig.getInstance().getHost(), ResourceConfig.getInstance().getContext(), ResourceConfig.getInstance().getJsonNative(), ResourceConfig.getInstance().getContentTypeOverride())







    @classmethod
    def read(cls,criteria):
        """
        Query objects of type InstitutionConfiguration by id and optional criteria
        @param type criteria
        @return InstitutionConfiguration object representing the response.
        @raise ApiException: raised an exception from the response status
        """

        return BaseObject.execute("69579603-119b-4a58-9e72-543609d9bd4f", InstitutionConfiguration(criteria))


    def publish(self):
        """
        Updates an object of type InstitutionConfiguration

        @return InstitutionConfiguration object representing the response.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("1d5b0f4d-fe38-4cb9-9476-68736beffa93", self)






    def update(self):
        """
        Updates an object of type InstitutionConfiguration

        @return InstitutionConfiguration object representing the response.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("c96c791c-4301-4cff-b2ac-87e6d0807263", self)






    def terminate(self):
        """
        Updates an object of type InstitutionConfiguration

        @return InstitutionConfiguration object representing the response.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("7761cebd-21e2-4242-9e24-5ac5bd57f461", self)






    def unpublish(self):
        """
        Updates an object of type InstitutionConfiguration

        @return InstitutionConfiguration object representing the response.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("aa49eddc-e266-41a7-80f7-26e7158037b7", self)






