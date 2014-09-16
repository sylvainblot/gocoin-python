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

import gocoin
import os
import json
import unittest


class GoCoinTestCase(unittest.TestCase):
    """Sets up application ID and secret from environment."""
    def setUp(self):
        try:
            self.access_token = os.environ["ACCESS_TOKEN"]
        except KeyError:
            raise Exception("ACCESS_TOKEN "
                            "must be set as environmental variable.")


class TestUser(GoCoinTestCase):
    """
    Test the Users class methods

    """
    def test_get_active_user(self):
        client = gocoin.Client(self.access_token)
        user = client.get_active_user()
        assert(u'id' in user)

class TestInvoice(GoCoinTestCase):
    """Test invoices methods"""
    
    def test_create_invoice(self):
      invoice_params = {"price_currency": "BTC",
                      "base_price": "10",
                      "base_price_currency": "USD"}
      client = gocoin.Client(self.access_token)
      user = client.get_active_user()
      merchant_id = user[u'merchant_id']
      invoice = client.create_invoice(merchant_id, invoice_params)
      assert(u'id' in invoice)

    # def test_invoice_get(self): #Replace invoice id with one that belong to your test merchant
    #   invoice_id = '91d6fc5b-ef39-458e-9cb0-796d33a1cec6'
    #   client = gocoin.Client(self.access_token)
    #   invoice = client.get_invoice(invoice_id)
    #   assert(u'id' in invoice)

    # def test_search_invoice(self):
    #   search_params = {"status": 'billed'}
    #   client = gocoin.Client(self.access_token)
    #   invoices = client.search_invoices(search_params)
    #   assert(u'status' in invoices)


if __name__ == '__main__':
    unittest.main()
