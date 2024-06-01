import requests
TOKEN = "5783477063:AAEhSy-Nsg4hSAzj-vyTRwlTMCnd7hGzsmI"
chat_id = "1411548069"
#2066274258 - aditya
#1361249595 - sahil
message = "chutiye h kya"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json())  # this sends the message
