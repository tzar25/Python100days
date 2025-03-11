import requests
from datetime import datetime, date
from os import getenv
from dotenv import load_dotenv

load_dotenv(override=True)

TOKEN = getenv("TOKEN")
USER_NAME = getenv("USER_NAME")
PYTHON_GRAPH_ID = "graph01"

# ======= One-time user creation =======
pixela_parameters = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

pixela_endpoint = "https://pixe.la/v1/users"

# response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(response.text)

# ============ Graph creation ==============
graphs_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
pixela_headers = {
    "X-USER-TOKEN": TOKEN
}
graphs_parameters = {
    "id": PYTHON_GRAPH_ID,
    "name": "Python commitment",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu"
}

# response = requests.post(url=graphs_endpoint, json=graphs_parameters, headers=pixela_headers)
# print(response.text)

# ============= Post a pixel ================
today = datetime.now().strftime("%Y%m%d")
last_day = date(2025, 2, 27).strftime("%Y%m%d")
pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{PYTHON_GRAPH_ID}"
pixel_parameters = {
    "date": last_day,
    "quantity": "180"
}

# response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=pixela_headers)
# print(response.text)

# ================ modifying with requests.put() =============
modify_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{PYTHON_GRAPH_ID}/{today}"
modify_parameters = {
    "quantity": "90"
}

# response = requests.put(url=modify_endpoint, json=modify_parameters, headers=pixela_headers)
# print(response.text)

# ================ Deleting existing data ==================
delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{PYTHON_GRAPH_ID}/{last_day}"

response = requests.delete(url=delete_endpoint, headers=pixela_headers)
print(response.text)

