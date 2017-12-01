import requests
from  testDraw import photoDraw
from json import JSONDecoder
face_tokens_name = {'fe0fd82b5994b6c250e61be986cea100':'lizhuo',
                    'e95b49d46ad27af184eb96c2f4b72330':'lizhuo',
                    '54052636b3a3b494d11e4c2c1c0879d9':'lizhuo',
                    '69b74a5bd20dd1517934a19970f41bee':'lizhuo',
                    '6b893d8502d25ac5791963e1554caf50':'lizhuo',
                    '4aac5aa8263aa2f008404a01a5f671c4':'lizhuo',
                    '5aaf052e72902713d2ea0f224078ae2c':'lizhuo',
                    '9ff274553375ad88bb5773103c2555ce':'lizhuo',
                    'a07a7d1d9cb503602ad60fd8adf51869':'lizhuo',
                    '046e73611848d78b7b451eeb1d7348a7':'lizhuo'
                    }
http_url = "https://api-cn.faceplusplus.com/facepp/v3/search"
key = "JPofXVcqsEro1KO7pseh9H2KFXLuTjns"
secret = "vL2SaCF41T78-S-iz0DI-v4rrGxn1cuP"
outer = "faceName"

filePath = "./photod/cap0.jpg"

data = {"api_key": key, "api_secret": secret,"outer_id":outer}

files = {"image_file": open(filePath, "rb")}

response = requests.post(http_url, data=data,files=files)

req_con = response.content.decode('utf-8')
req_dict = JSONDecoder().decode(req_con)

print(req_dict)
if req_dict.__contains__("error_message"):
    print(req_dict.get("error_message"))
    exit(1)

# 创建画图实例
Draw = photoDraw(filePath)

# 提取json中关于脸部位置的数据,并且在图片上画出方框
face_rectangle = req_dict.get("faces")
for index in range(len(face_rectangle)):
    face_rectangle_point = face_rectangle[index].get("face_rectangle")
    Draw.Draw(face_rectangle_point.get("top"), face_rectangle_point.get("left"), face_rectangle_point.get("width"),
              face_rectangle_point.get("height"))

face_token_result = req_dict.get('results')[0].get('face_token')
name = face_tokens_name.get(face_token_result)
Draw.puttext(name)
print(name)

Draw.show()