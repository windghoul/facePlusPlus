import requests
import testDraw
from  testDraw import photoDraw
from json import JSONDecoder
# 调用Face++的API识别图片中的人脸
http_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
key = "JPofXVcqsEro1KO7pseh9H2KFXLuTjns"
secret = "vL2SaCF41T78-S-iz0DI-v4rrGxn1cuP"
filepath = "F:\\testPh\\liudehua.jpg"

data = {"api_key": key, "api_secret": secret, "return_landmark": "0"}
files = {"image_file": open(filepath, "rb")}
response = requests.post(http_url, data=data, files=files)

req_con = response.content.decode('utf-8')
req_dict = JSONDecoder().decode(req_con)

print(req_dict)
if req_dict.__contains__("error_message"):
    print(req_dict.get("error_message"))
    exit(1)
# 创建画图实例
Draw = photoDraw()

# 提取json中关于脸部位置的数据,并且在图片上画出方框
face_rectangle = req_dict.get("faces")
for index in range(len(face_rectangle)):
    face_rectangle_point = face_rectangle[index].get("face_rectangle")
    Draw.Draw(face_rectangle_point.get("top"),face_rectangle_point.get("left"),face_rectangle_point.get("width"),face_rectangle_point.get("height"))


Draw.show()
# print(face_rectangle_point)
# print(face_rectangle_point.get("width"))
