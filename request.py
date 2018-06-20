import requests
import json

USERNAME = "admin"
PASSWORD = "Moustafa11"
PROJECT_ID = "730ac87b1e03449c8546f22440b17ff6"
AUTH_URL = "http://192.168.20.131/identity/v3/auth/tokens"
DOMAIN = "Default"

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
	print("Response Code : "+r.status_code)
	if(r.status_code < 400):
		#print(json.dumps(r.json()))
		token_id = r.headers.get('X-Subject-Token')
		#token_data = r.json()
		return token_id
	else:
		print(r.text)

TOKEN = authorize(USERNAME, PASSWORD, DOMAIN, PROJECT_ID, AUTH_URL)

url = "http://192.168.20.131/compute/v2.1/servers"
headers = {'X-Auth-Token': TOKEN}
r = requests.get(url,headers=headers)
print(r.status_code)
if(r.status_code < 400):
	print(json.dumps(r.json()))
	#token_data = r.json()
else:
	print(r.text)