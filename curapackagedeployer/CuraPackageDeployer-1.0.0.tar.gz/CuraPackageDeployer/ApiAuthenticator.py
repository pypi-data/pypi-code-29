# Copyright (c) 2018 Ultimaker B.V.
# !/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Dict
from requests import Request


class ApiAuthenticator:
    """
    HTTP authenticator that uses bearer tokens for any number of base URLs.
    """

    def __init__(self):
        self.bearer_tokens: Dict[str, str] = {}  # mapping in format {path: token}

    def matches(self, url) -> bool:
        """
        Returns true if this authenticator applies to the given url.
        :param url: URL to check.
        :return: True if URL starts with the base URL, False otherwise.
        """
        return any(url.startswith(path) for path in self.bearer_tokens)

    def apply(self, request: Request) -> Request:
        """
        Applies the authentication to the request.
        :param request: The request to apply.
        :return: The request with authentication applied.
        """
        for path, bearer_token in self.bearer_tokens.items():
            if request.url.startswith(path):
                request.headers['Authorization'] = "Bearer {}".format(bearer_token)
                break
        return request
