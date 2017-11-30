import cv2
# 打开摄像头
def cap():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("cap open failed")
        exit(1)
    #读取摄像头并且显示数据
    i= 0
    while i != 10 :
        ret,img = cap.read()
        fileName = "./photod/cap"+ str(i) + ".jpg"
        cv2.imwrite(fileName,img)
        cv2.namedWindow("cap")
        cv2.imshow("cap",img)
        cv2.waitKey(30)
        i+= 1
        # if cv2.waitKey(1) & 0xFF == 27:
        #     break
    # 释放所有资源
    cap.release()

# 人脸识别模块载入
def faceDetector():
    i =0
    for i in range(10) :
        fileName = "./photod/cap"+ str(i) + ".jpg"
        img = cv2.imread(fileName)
        imgPrint = img.copy()
        faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)

        print(faces)
        for x,y,w,h in faces :
            face_save = img[x:x+w+1,y:y+h+1]
            imgPrint = cv2.rectangle(imgPrint, (x, y), (x + w, y + h), (255, 0, 0), 2)
        print(face_save.shape)
        cv2.namedWindow("vedio")

        cv2.namedWindow("crop")
        cv2.imshow("crop",face_save)
        cv2.imshow("vedio",imgPrint)
        faceFileName = "./faced/face"+ str(i)+ ".jpg"
        cv2.imwrite(faceFileName,face_save)
        cv2.waitKey(30)
    # 释放资源
    cv2.destroyAllWindows()



if __name__ == "__main__":
    cap()
    faceDetector()
