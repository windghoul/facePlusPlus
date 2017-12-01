import requests
from json import JSONDecoder
http_url = " https://api-cn.faceplusplus.com/facepp/v3/faceset/addface"
key = "JPofXVcqsEro1KO7pseh9H2KFXLuTjns"
secret = "vL2SaCF41T78-S-iz0DI-v4rrGxn1cuP"
outer = "faceName"
# face_tokens = "046e73611848d78b7b451eeb1d7348a7,fe0fd82b5994b6c250e61be986cea100,e95b49d46ad27af184eb96c2f4b72330,54052636b3a3b494d11e4c2c1c0879d9,69b74a5bd20dd1517934a19970f41bee"
face_tokens = "6b893d8502d25ac5791963e1554caf50,4aac5aa8263aa2f008404a01a5f671c4,5aaf052e72902713d2ea0f224078ae2c,9ff274553375ad88bb5773103c2555ce,a07a7d1d9cb503602ad60fd8adf51869"
data = {"api_key": key, "api_secret": secret,"outer_id":outer,"face_tokens":face_tokens}

response = requests.post(http_url, data=data)

req_con = response.content.decode('utf-8')
req_dict = JSONDecoder().decode(req_con)

print(req_dict)
if req_dict.__contains__("error_message"):
    print(req_dict.get("error_message"))
    exit(1)