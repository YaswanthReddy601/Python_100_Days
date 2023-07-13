import requests
import datetime
end_point = "https://pixe.la/v1/users"
user= "yaswanth601"
graph_id = "graph2ef3e"

create_user = {
    "token": "Yaswanthas65434qasdadf",
    "username": "yaswanth601",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

#Creating the user
response = requests.post(url = end_point, json= create_user)
print(response.text)

creating_graph = {
    "id": "graph2ef3e",
    "name": "my_graph",
    "unit": "hours",
    "type": "float",
    "color": "sora"
}

headers={
    "X-USER-TOKEN" : "Yaswanthas65434qasdadf"
}

#creating graph
res = requests.post(url = f"{end_point}/{user}/graphs" , json=creating_graph, headers=headers )
print(res.text)

today = datetime.datetime(year=2023, month=6, day=25)
add_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15.0"
}

#adding data to the graph
add_response = requests.post(url= f"{end_point}/{user}/graphs/{graph_id}", json= add_data, headers= headers)
print(add_response.text)

new_data = {
    "quantity":"8.0"
}

#updating the graph
update_response = requests.put(url= f"{end_point}/{user}/graphs/{graph_id}/{today.strftime('%Y%m%d')}", json=new_data, headers=headers)
print(update_response.text)

#Deleting the data from the graph
delete_response = requests.delete(url= f"{end_point}/{user}/graphs/{graph_id}/{today.strftime('%Y%m%d')}", headers=headers)
print(delete_response.text)
