import requests as rq, json as js

def airlyrq (url):
    headers = {
    'Accept' : 'application/json',
    'Accept-Language':'en',
    'apikey': 'IU1E4Ryh7zyMt4glv7LeV72JHkOMoiQ0'
    }
    response = rq.get(url, headers=headers)
    return response

installations = airlyrq ('https://airapi.airly.eu/v2/installations/nearest?lat=54.383789&lng=18.62799&maxDistanceKM=30&maxResults=20')

def jprint(obj):
    text = js.dumps(obj, sort_keys=True, indent=4)
    print(text)

#all_instas = installations.json()
#jprint(all_instas)

all_inst = installations.json()
print (type(all_inst))
#print (all_inst)

#dispAddress2_list = []
#for ins in address:
#    dispA2 = ins['address']
#    for x in dispA2:
#        disp = x['displayAddress2']
#        dispAddress2_list.append(disp)
#
#print (dispAddress2_list)
        
all_addresses_list = []

for a in all_inst:
    address = a['address']
    all_addresses_list.append(address)

all_disp_Address2_list = []
#print (all_addresses_list) 

for dispA in all_addresses_list:
    dispAddress2 = dispA['displayAddress2']
    all_disp_Address2_list.append(dispAddress2)

print(all_disp_Address2_list)

outputs['addresy'] = all_disp_Address2_list
