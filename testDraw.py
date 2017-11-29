import cv2
class photoDraw():
    def __init__(self):
        self.image1 = cv2.imread("F:\\testPh\\liudehua.jpg")
        cv2.namedWindow("Image")
    def Draw(self,top,left,width,height):
        cv2.rectangle(self.image1,(left,top),(left+width,top+height),(255,0,0),3)
    def show(self):
        cv2.imshow("Image",self.image1)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()

