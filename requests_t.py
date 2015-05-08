#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

# r = requests.get('http://127.0.0.1:5000/login', auth=('magigo', '123456'))
# print r.text
#
# token ='bWFnaWdvOjAuMzE4MTUxNTA1MjQ4OjE0MjU4MzkzMjMuODk='
# r = requests.get('http://127.0.0.1:5000/test1', params={'token': token})
# print r.text
#

r = requests.get('http://localhost:5000/client/login')
print r.text
print '======='
print r.history
print '======='
print r.url
print '======='
uri_login = r.url.split('?')[0] + '?user=magigo&pw=123456'
r2 = requests.get(uri_login)
print r2.text
print '======='
r = requests.get('http://127.0.0.1:5000/test1', params={'token': r2.text})
print r.text