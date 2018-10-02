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
        
        "1cdce220-1fac-4a1e-8a1f-e4a9b9fac851" : OperationConfig("/mpqr-accept/v1/api/bank/configuration", "query", [], []),
        
        "40fa43ee-a2a7-4d5e-a7fa-06e196ca4042" : OperationConfig("/mpqr-accept/v1/api/bank/configuration/publish", "update", [], []),
        
        "49183566-1230-4236-983b-66ce1d69f2bc" : OperationConfig("/mpqr-accept/v1/api/bank/configuration", "update", [], []),
        
        "cec2e0d2-ed5f-4a36-bda3-58c496a70210" : OperationConfig("/mpqr-accept/v1/api/bank/configuration/terminate", "update", [], []),
        
        "593fd3cc-d29e-46b1-8ba2-4d640a480fd3" : OperationConfig("/mpqr-accept/v1/api/bank/configuration/unpublish", "update", [], []),
        
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

        return BaseObject.execute("1cdce220-1fac-4a1e-8a1f-e4a9b9fac851", InstitutionConfiguration(criteria))


    def publish(self):
        """
        Updates an object of type InstitutionConfiguration

        @return InstitutionConfiguration object representing the response.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("40fa43ee-a2a7-4d5e-a7fa-06e196ca4042", self)






    def update(self):
        """
        Updates an object of type InstitutionConfiguration

        @return InstitutionConfiguration object representing the response.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("49183566-1230-4236-983b-66ce1d69f2bc", self)






    def terminate(self):
        """
        Updates an object of type InstitutionConfiguration

        @return InstitutionConfiguration object representing the response.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("cec2e0d2-ed5f-4a36-bda3-58c496a70210", self)






    def unpublish(self):
        """
        Updates an object of type InstitutionConfiguration

        @return InstitutionConfiguration object representing the response.
        @raise ApiException: raised an exception from the response status
        """
        return BaseObject.execute("593fd3cc-d29e-46b1-8ba2-4d640a480fd3", self)






