#! /usr/bin/python
import requests
import json
import time

url = "https://api.telegram.org/bot758261552:AAE1zVA2sHNw_WxDtVZolbLivX3-W8Xhd6k/"
response = requests.get("https://api.ethermine.org/miner/:0x6ddd79c6e71d4bfca125f4ae38c578af8c103daa/history/")
data = response.json()["data"][len(response.json()["data"])-1]
mhz = (int(data.get(u'reportedHashrate')))/1000000
response2 = requests.get("https://api.ethermine.org/miner/:0x93665d08f3581c1fa4cb30eaadee0b18ddc7b6cb/history/")
data2 = response2.json()["data"][len(response2.json()["data"])-1]
mhz2 = (int(data2.get(u'reportedHashrate')))/1000000

print ("ReportedHashrate_bh: " + str(mhz) + " MH/s")
print ("ReportedHashrate_bg: " + str(mhz2) + " MH/s")

def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()

def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

chat_id = get_chat_id(last_update(get_updates_json(url)))
send_mess(chat_id, "Monitoring service has been started\n" "ReportedHashrate_bh: " + str(mhz) + " MH/s\n" "ReportedHashrate_bg: " + str(mhz2) + " MH/s")
send_mess(chat_id, u'\U0001F4B0' + u"\U0001F680" + u'\U0001F4B0' + u"\U0001F680" + u'\U0001F4B0' + u"\U0001F680")

def monitoring():
    if mhz > 100 and mhz2 > 100:
        time.sleep(600)
    else:
        send_mess(chat_id, "Mining has been down, needs maintenance" + u"\U0001F4A3" + u"\U0001F4A3" + u"\U0001F4A3")
        time.sleep(2000)
while True:
    monitoring()
