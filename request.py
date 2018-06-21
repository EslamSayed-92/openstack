import requests
import json
import urllib.parse

BASE_URL = "http://192.168.20.131"

USERNAME = "admin"
PASSWORD = "Moustafa11"
PROJECT_ID = "730ac87b1e03449c8546f22440b17ff6"
AUTH_URL = BASE_URL+"/identity/v3/auth/tokens"
DOMAIN = "Default"

def handle_response(response):
	print(response.status_code)
	if(response.status_code < 400):
		print(json.dumps(response.json(), sort_keys=True,indent=4, separators=(',', ': ')))
		return response.json()
	else:
		print(response.text)
		return None
	

def authorize(username, password, domain, project_id, auth_url):
	auth_data = {
	    "auth": {
	        "identity": {
	            "methods": [
	                "password"
	            ],
	            "password": {
	                "user": {
	                    "name": username,
	                    "domain": {
	                        "name": domain
	                    },
	                    "password": password
	                }
	            }
	        },
	        "scope": {
	            "project": {
	                "id": project_id
	            }
	        }
	    }
	}
	r = requests.post(auth_url, json=auth_data)
	#print(r.status_code)
	if(r.status_code < 400):
		#print(json.dumps(r.json()))
		token_id = r.headers.get('X-Subject-Token')
		#token_data = r.json()
		return token_id
	else:
		print(r.text)
		return None
	

HEADERS = {'X-Auth-Token': authorize(USERNAME, PASSWORD, DOMAIN, PROJECT_ID, AUTH_URL) }

def list_servers():
	url = BASE_URL+"/compute/v2.1/servers"
	r = requests.get(url,headers=HEADERS)
	handle_response(r)

def list_flavors():
	url = BASE_URL+"/compute/v2.1/flavors"
	r = requests.get(url,headers=HEADERS)
	handle_response(r)

def filter_flavor(conds):
	url = BASE_URL+"/compute/v2.1/flavors?"
	data = urllib.parse.urlencode(conds)
	r = requests.get(url+data,headers=HEADERS)
	return handle_response(r)["flavors"]

def get_network(name):
	url = BASE_URL+":9696/v2.0/networks?name="+name
	r = requests.post(url,json=data,headers=HEADERS)
	handle_response(r)

def create_nova(server_name,image_id,flavor_id,network_id):
	url = BASE_URL+"/compute/v2.1/servers"
	data = {
	    "server": {
	        "name": server_name,
	        "imageRef": image_id,
	        "flavorRef": flavor_id,
	        "networks": [
	        	{"uuid":network_id}
	        ]
	    }
	}
	r = requests.post(url,json=data,headers=HEADERS)
	handle_response(r)


get_network("mynetwork")

# 1- Get Flavor
#flavor = filter_flavor({"minRam":"512","limit":"1"})[0]["id"]

#create_nova("new-server","6eff6563-714d-4423-921c-59c9961dce51","1","4f60cbed-e98c-49b1-b5a6-97923d684418")


# url = " http://192.168.20.131/image/v2/images"
# headers = {'X-Auth-Token': TOKEN}
# data={
# 	"container_format": "bare",
#     "disk_format": "raw",
#     "name": "Ubuntu",
# }
# r = requests.get(url,headers=headers)
# print(r.status_code)
# if(r.status_code < 400):
# 	#print(json.dumps(r.json(), sort_keys=True,indent=4, separators=(',', ': ')))
# 	print(r.headers)
# 	print(r.json())
# 	#token_data = r.json()
# else:
# 	print(r.text)

