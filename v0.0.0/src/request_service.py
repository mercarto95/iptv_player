import requests


def request_data(account):
    server_url = account.server
    username = account.username
    password = account.password


    server_url = server_url + "/get.php?username=" + username + "&password=" + password + "&type=m3u_plus&output=ts"
    # Connect to the server and retrieve the list of channels
    response = requests.get(f"{server_url}", auth=(username, password))
    #channels = response.json()
    c = 0
    file_name = account.name + ".bi"
    x = open("../data/" + file_name , "wb")
    """
    for i in response.text:
        try:
            x.write(response.text[c])
            c += 1
        except:
            c += 1
            print("problem")
    """
    try:
        x.write(response._content)
    except:
        print("Error while saving the file to the disk __request service.py")
    x.close()

    return True