import requests


class SheetReader:

    def __init__(self, auth_token):
        self.url = "https://api.sheety.co/a6a6000ca587d793c69152d8948c7b9f/flightWatcher/sheet1"
        self.headers = {
            "Authorization": auth_token
        }
        self.destination_data = {}

    def get_data(self):
        response = requests.get(url=self.url, headers=self.headers)
        # response.raise_for_status()
        self.destination_data = response.json()["sheet1"]
        return self.destination_data

    # def fill_iata(self, row, iata):
    #     new_row_data = {
    #         "sheet1": {
    #             "code": iata
    #         }
    #     }
    #     requests.put(url=f"{self.url}/{row}", json=new_row_data, headers=self.headers)

    def update_destination_codes(self):
        for city in self.destination_data:
            new_row_data = {
                "sheet1": {
                    "code": city["code"]
                }
            }
            response = requests.put(url=f"{self.url}/{city['id']}", json=new_row_data, headers=self.headers)
            # print(response.text)

    def update_price(self, airport, new_price, new_date):
        id_num = 0
        for elem in self.destination_data:
            if elem['code'] == airport:
                id_num = elem['id']
        if id_num:
            new_data = {
                "sheet1": {
                    "price": new_price,
                    "date": new_date
                }
            }
            requests.put(url=f"{self.url}/{id_num}", json=new_data, headers=self.headers)
