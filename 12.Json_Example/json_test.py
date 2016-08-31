import json


f = open("C://python_test//json_test.json","r")
b=f.read()
#print (b)
c={}
c= json.loads(b)
print(c.keys())
#  print(c['Satellite_Constellation'].keys())

# print(c['Satellite_Constellation'][0].keys()

# print(c['Satellite_Constellation']['Satellites'][0]['AllSatellites'][0]['SatLong'])

print(type(c['Satellite_Constellation']['Satellites'][0]['AllSatellites']))
# print(type(c['Satellite_Constellation']))


#print(c['data'][0]['obj_id'])
