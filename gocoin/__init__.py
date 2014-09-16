#!/usr/bin/env python
#
# Copyright 2014 GoCoin Pte. Ltd.
# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, 
# software distributed under the License is distributed on an 
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, 
# either express or implied. See the License for the specific 
# language governing permissions and limitations under the License.

import urllib
import requests
import json

# Find a query string parser
try:
    from urllib.parse import parse_qs
except ImportError:
    from urlparse import parse_qs

from . import version


__version__ = version.__version__


class Client(object):
    """
    """
    def __init__(self, access_token=None, host=None, timeout=None):
        self.access_token = access_token
        self.timeout = timeout
        self.version = "v1"
        self.host = host or "https://api.gocoin.com" 
        self.base_url = self.host + "/api/" + self.version

    def get_active_user(self):
        """Fetchs the given object from the graph."""
        return self.request("/user")

    def request(self, path, args=None, post_args=None, method="GET"):
        """
        """
        args = args or {}
        req_headers = {'Content-Type': 'application/json'}
        route = self.base_url + path

        if 'oauth' not in path: 
          req_headers["Authorization"] = 'Bearer ' + self.access_token

        try:
            response = requests.request(method,
                                        route,
                                        timeout=self.timeout,
                                        params=args,
                                        headers=req_headers,
                                        data=json.dumps(post_args))

        #I dont think this is not the correct error handling
        except requests.HTTPError as e:
            response = json.loads(e.read())
            raise GoCoinError(response)

        headers = response.headers
        if 'json' in headers['content-type']:
            result = response.json()
        
        return result or True

    def get_access_token_from_code(self, code, redirect_uri, client_id, client_secret):
        """Get an access token from the "code" returned from an OAuth dialog.

        Returns a dict containing the user-specific access token and its
        expiration date (if applicable).

        """
        args = {
            "code": code,
            "redirect_uri": redirect_uri,
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": 'authorization_code'}

        return self.request("/oauth/token", post_data=args, method="POST")


class GoCoinError(Exception):
    def __init__(self, result):
        self.result = result
        try:
            self.status = result["status"]
        except:
            self.status = "500"

        # OAuth 2.0 Draft 10
        try:
            self.message = result["message"]
        except:
            try:
                self.message = result["error_description"]
            except:
                self.message = ""


        try:
            self.errors = result["errors"]
        except:
          try:
            self.errors = result["error"]
          except:
            self.errors = None

        Exception.__init__(self, self.message)


def auth_url(client_id, redirect_uri, scope, state):
    url = "https://dashboard.gocoin.com/auth?"
    kvps = {'client_id': client_id, 'redirect_uri': redirect_uri, 'scope': scope, 'state': state}
    return url + urllib.urlencode(kvps)


def get_access_token_from_code(code, redirect_uri, client_id, client_secret):
    return GoCoin().get_access_token_from_code(
        code, redirect_uri, client_id, client_secret)


def get_app_access_token(client_id, client_secret):
    return GoCoin().get_app_access_token(client_id, client_secret)
