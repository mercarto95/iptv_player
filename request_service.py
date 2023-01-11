import requests


def request_data(account):
    server_url = "XXXX"
    username = "XXXX"
    password = "XXXXX"

  # Connect to the server and retrieve the list of channels
    response = requests.get(f"{server_url}", auth=(username, password))
    #channels = response.json()
    c = 0
    x = open("try3.txt", "w")
    for i in response.text:
        try:
            x.write(response.text[c])
            c += 1
        except:
            c += 1
            print("problem")