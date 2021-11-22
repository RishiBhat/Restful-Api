import json
import requests


URL = "http://127.0.0.1:8000"


def get_data(id=None):             
    data={}                         
    
    if id is not None:         
        data={'id':id}         
    headers={'content-Type':'application/json'}                               
    json_data = json.dumps(data)   
    r=requests.get(url=URL, data=json_data,headers=headers)
    data=r.json()                 
    print(data) 

#get_data()


def post_data():
    data = {
        'username':'r@r.com',
        'email':'r@r.com',
    }
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data,headers=headers)
    data = r.json()
    print(data)
post_data()


def update_data():
    data = {
        'id':4,
        'name':'Ravan',
        'roll':99, 
        'city':'Sri Lanka'
    }
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data, headers=headers)    
    data = r.json()
    print(data)

#update_data()

 

def delete_data():
    data ={ 'id': 4}     
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r = requests.delete(url=URL, data=json_data, headers=headers)    
    data = r.json()
    print(data)
#delete_data()