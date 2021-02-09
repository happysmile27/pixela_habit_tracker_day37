import requests
from datetime import datetime

USERNAME = "olia27"
TOKEN = "sdbcyrikwjsndcs"
GRAPH_ID = "book1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    "thanksCode": "Merci!"
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

#graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
header = {
    "X-USER-TOKEN": TOKEN
}
#
#graph_config = {
#    "id": GRAPH_ID,
#    "name": "numbers-of-pages",
#    "unit": "numbers",
#    "type": "int",
#    "color": "ichou"
#}
#
#response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
#print(response.text)

graph_update = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

graph_config = {
    "name": "Books reader",
    "unit": "pages"
}

response = requests.put(url=graph_update, json=graph_config, headers=header)
print(response.text)

pixel_add = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"


today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today? ")
}

response1 = requests.post(url=pixel_add, json=pixel_config, headers=header)
print(response1.text)
