gocoin-python
=============

BETA - Python Library for the GoCoin API - Only Basic calls supported

Assumes you have an API Key or access token with user_read and invoice_read_write scopes

The full API spec is [here](http://docs.gocoinapi.apiary.io)

```
client = gocoin.Client(access_token)
```
Client Methods
##### get_active_user(self):
```user = client.get_active_user()```
    

##### get_user(self, user_id):
user_id = '123'
```user = client.get_user(user_id)```


##### get_invoice(self, invoice_id):
```user = client.get_invoice(invoice_id)```


##### create_invoice(self, merchant_id, invoice_params):

```
invoice_params = {"price_currency": "BTC",
                  "base_price": "10",
                  "base_price_currency": "USD"}

# if you do not have your merchant_id stored, you can get it from the user object
merchant_id = user[u'merchant_id']
invoice = client.create_invoice(merchant_id, invoice_params)
```

##### search_invoices(self, search_params):

```
search_params = {"status": 'billed'} 
client = gocoin.Client(self.access_token)
invoices = client.search_invoices(search_params)
```
