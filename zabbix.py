# -*- coding : utf-8 -*-

import urllib2,json
from urllib2 import URLError

class ZabbixAPI(object):
	def __init__(self):
		self.url = 'http://192.168.45.237/zabbix/api_jsonrpc.php'
		self.user = 'Admin' //default
		self.password = 'zabbix'
		self.header = {"Content-Type":"application/json"} 

	def __getattr__(self,name):
		def handlerFun(kwargs):
			return self._request_api(name,kwargs)
		return handlerFun

	def _request_api(self,name,kwargs):
		self._get_auth()
		data = json.dumps({"jsonrpc" : "2.0","method" : name,"params" : kwargs,"auth" : self.authID,"id" : 1})
		return data

	def _get_auth(self):
		data = json.dumps({ 
	                       "jsonrpc": "2.0", 
	                       "method": "user.login", 
	                       "params": { 
	                                  "user": "Admin", 
	                                  "password": "zabbix" 
	                                  }, 
	                       "id": 0 
	                       }) 

		request = urllib2.Request(self.url, data) 
		response = ''
		for key in self.header: 
			request.add_header(key, self.header[key]) 
		try: 
			result = urllib2.urlopen(request) 
		except URLError as e: 
			print "fail login", e 
		else: 
			response = json.loads(result.read())['result']
			result.close() 
	        #print response['result'] 
	        self.authID = response

api = ZabbixAPI()
request = {'k':'v'}
print api.abc(request)
