import requests
import testDraw
from  testDraw import photoDraw
from json import JSONDecoder
# 调用Face++的API识别图片中的人脸
http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/create"
key = "JPofXVcqsEro1KO7pseh9H2KFXLuTjns"
secret = "vL2SaCF41T78-S-iz0DI-v4rrGxn1cuP"
filepath = "F:\\testPh\\liudehua.jpg"
outer = "faceName"
data = {"api_key": key, "api_secret": secret,"outer_id":outer}

# files = {"image_file": open(filepath, "rb")}
response = requests.post(http_url, data=data)

req_con = response.content.decode('utf-8')
req_dict = JSONDecoder().decode(req_con)

print(req_dict)
if req_dict.__contains__("error_message"):
    print(req_dict.get("error_message"))
    exit(1)
