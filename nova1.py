from keystoneauth1 import loading
from keystoneauth1 import session
from novaclient import client
import glanceclient.v2.client as glclient
from neutronclient.v2_0 import client as neuclient


def show_attr(obj):
	for item in dir(obj):
		print(item, type(getattr(obj,item)))


VERSION = "2.1"
DOMAIN = 'default'
USERNAME = 'admin'
PASSWORD = 'Moustafa11'
AUTH_URL = 'http://192.168.20.131/identity'
PROJECT_ID = '730ac87b1e03449c8546f22440b17ff6'

loader = loading.get_plugin_loader('password')
auth = loader.load_from_options(auth_url=AUTH_URL,user_domain_name=DOMAIN,username=USERNAME,password=PASSWORD,project_id=PROJECT_ID)
sess = session.Session(auth=auth)


#---------- Compute Client -----------------------#
nova = client.Client('2.1', session=sess)

#show_attr(nova)
#print("------------------------------------")
#print(nova.glance.list())
#print("------------------------------------")
#show_attr(nova.neutron.list())
#print("------------------------------------")
#print(nova.servers.list())
#print("------------------------------------")


# ---------- Creating Nova Instance -------------#
#print("Network:\r\n")
#print(nova.neutron.find_network("privete2").id)
#netid = nova.neutron.find_network("privete2").id
#print("--------------------------------------\r\n")

#print("Image:\r\n")
#print(nova.glance.list())
#image = nova.glance.list()[0]
#print("-------------------------------------------")

#fl = nova.flavors.find(ram=512)
#print(nova.servers.create("apiTest", flavor=fl,image=image,nics=[{'net-id':netid}]))


#--------------- Image Client ----------------------#
glance = glclient.Client(session=sess)


#---------------- Network Client -------------------#
neutron = neuclient.Client(session=sess)

#network = {'name': 'mynetwork', 'admin_state_up': True}
#print(neutron.create_network({'network':network}))
#show_attr(neutron)
print("-------------------------")
print(neutron.show_network("103e8e54-8846-44b6-a9bd-8736facdf6f2"))