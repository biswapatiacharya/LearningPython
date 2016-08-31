import requests
import json
r = requests.get('https://api.github.com/user', verify=False, auth=('ashokmoorthi', 'ashok@30'))
#r = requests.get("http://systadash.eng.idirect.net:8080/view/CI%20Test%20suite/job/Evo-develop-8350-DLC-CarrierSanity/api/json")
#"http://systadash.eng.idirect.net:8080/view/CI%20Test%20suite/job/Evo-develop-8350-DLC-CarrierSanity/346/api/json"

# with open('C://python_test//json_test1.json', 'w') as f:
#     json.dumps(r, f, ensure_ascii=False)




# print(r.status_code)
#print(r.headers['content-type'])
#print(r.encoding)
# print(r.text)
print(r.json())
c= r.json()
print(type(c))
print(c.keys())
print(c['disk_usage'])
c['disk_usage'] = 6
print(c['disk_usage'])
print(c)
# a = open("C://python_test//json_test1.json", 'r')
# print(a)
