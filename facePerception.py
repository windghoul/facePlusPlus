import cv2
# 打开摄像头
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("cap open failed")
    exit(1)
#读取摄像头并且显示数据

ret,img = cap.read()
cv2.namedWindow("vedio")
cv2.imshow("vedio",img)


# 释放所有资源
