import requests
import json
import os
from datetime import datetime

with open(os.path.dirname(os.path.realpath(__file__)) + "/settings.json") as json_settings_file:
    json_settings = json.load(json_settings_file)

os2iot_url = json_settings['os2iot']['base_url'] + "chirpstack/gateway?organizationId=2"
sms2go_url = "https://pushapi.ecmr.biz/v1.0/Sms/batches/" + json_settings['sms2go']['gatewayid']
textmessage = ""

response = requests.request("GET", os2iot_url, headers={"x-api-key": json_settings['os2iot']['api-key']})

responsejson = json.loads(response.text)

for item in responsejson['result']:
  
  if not "offline" in item['name'].casefold():
    timenotseen = datetime.now().astimezone() - datetime.fromisoformat(item['lastSeenAt'].replace('Z', '+00:00'))
    if timenotseen.seconds > 3600:
      textmessage += item['name'] + ": Last seen on " + item['lastSeenAt'][0:16] + "\r\n"

if textmessage != "":
   sms2go_response = requests.request("POST", sms2go_url, headers={"Content-Type": "application/json", "Authorization": "Bearer " + json_settings['sms2go']['bearer']}, allow_redirects=True, data="{\"body\":\"" + textmessage + "\",\"to\":["+json_settings['sms2go']['recipient']+"]}")