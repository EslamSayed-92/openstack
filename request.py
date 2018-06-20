import requests
import json

USERNAME = "admin"
PASSWORD = "Moustafa11"
PROJECT_ID = "730ac87b1e03449c8546f22440b17ff6"
AUTH_URL = "http://192.168.20.131/identity/v3/auth/tokens"
DOMAIN = "Default"

def handle_response(response):
	print(response.status_code)
	if(r.status_code < 400):
		print(json.dumps(response.json(), sort_keys=True,indent=4, separators=(',', ': ')))
		#token_data = r.json()
	else:
		print(response.text)
	

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
	url = "http://192.168.20.131/compute/v2.1/servers"
	r = requests.get(url,headers=HEADERS)
	handle_response(r)

def list_flavors():
	url = "http://192.168.20.131/compute/v2.1/flavors"
	r = requests.get(url,headers=HEADERS)
	handle_response(r)


def create_nova(server_name,image_id,flavor_id,network_id):
	url = "http://192.168.20.131/compute/v2.1/servers"
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

create_nova("new-server","6eff6563-714d-4423-921c-59c9961dce51","1","4f60cbed-e98c-49b1-b5a6-97923d684418")


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

