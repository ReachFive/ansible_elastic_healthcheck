#!/usr/bin/env python3
import requests
import json
import subprocess
import time
from random import randint

def readnodes():
    http_response = requests.get('http://127.0.0.1:9200/_cluster/health')
    jsonresponse = json.loads(http_response.text)
    return jsonresponse['number_of_nodes']

healthurl='http://127.0.0.1:9200/_cluster/health'
loop=0
while True:
    subprocess.run(["systemctl","restart","elasticsearch"])
    loop += 1
    while True:
        try:
            http_response = requests.get(healthurl)
        except requests.exceptions.ConnectionError as e:
            time.sleep(1)
        else:
            break
    time.sleep(30)
    if loop > 10 or readnodes()!=1:
        break
time.sleep(randint(60, 120))
print (readnodes())