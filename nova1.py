from keystoneauth1 import loading
from keystoneauth1 import session
from novaclient import client
import glanceclient.v2.client as glclient
from neutronclient.v2_0 import client as neuclient


def show_attr(obj):
	for item in dir(obj):
		print(item, type(getattr(obj,item)))

VERSION = "2.1"
USERNAME = 'admin'
PASSWORD = 'redhat'
AUTH_URL = 'http://10.70.71.1:5000/v2.0'
PROJECT_ID = '85b14409730241139975ff4d9f44bbc6'

loader = loading.get_plugin_loader('password')
auth = loader.load_from_options(auth_url=AUTH_URL,username=USERNAME,password=PASSWORD,project_id=PROJECT_ID)
sess = session.Session(auth=auth)

nova = client.Client(VERSION, session=sess)
glance = glclient.Client(session=sess)
neutron = neuclient.Client(session=sess)

network = {'name': 'mynetwork', 'admin_state_up': True}
neutron.create_network({'network':network})

image = list(glance.images.list())[0]
#print(image.id)

#nova = client.Client(VERSION, USERNAME, PASSWORD, PROJECT_ID,AUTH_URL)
instances = nova.servers.list()

#for item in dir(nova):
#	print(item, type(getattr(nova,item)))
#print("------------------------------------")
#for item in dir(nova.glance):
#	print(item, type(getattr(nova.glance,item)))
#print("------------------------------------")
#for item in dir(nova.neutron):
#	print(item, type(getattr(nova.neutron,item)))
show_attr(neutron.list())


#print("Network:\r\n")
#print(nova.neutron.find_network("privete2").id)
netid = nova.neutron.find_network("privete2").id
#print("--------------------------------------\r\n")
#print("Images:\r\n")
#print(dir(nova.glance))
#print("-------------------------------------------")


#print(nova.servers.list())

fl = nova.flavors.find(ram=512)
#print(nova.servers.create("apiTest", flavor=fl,image=image,nics=[{'net-id':netid}]))
