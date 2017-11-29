import cv2
# 打开摄像头
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("cap open failed")
    exit(1)
#读取摄像头并且显示数据

while True :
    ret,img = cap.read()
    # 人脸识别模块载入
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    print(faces)
    for x,y,w,h in faces :
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.namedWindow("vedio")
    cv2.imshow("vedio",img)
    if cv2.waitKey(1) & 0xFF == 27: break


# 释放所有资源

cap.release()
cv2.destroyAllWindows()
