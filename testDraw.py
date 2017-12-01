import cv2
class photoDraw():
    def __init__(self,fileName):
        self.image1 = cv2.imread(fileName)
        cv2.namedWindow("Image")
    def Draw(self,top,left,width,height):
        self.top = top
        self.left = left
        cv2.rectangle(self.image1,(left,top),(left+width,top+height),(255,0,0),3)
    def puttext(self,name):
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(self.image1,name,(self.left,self.top - 10),font,0.8,(0,255,0),1)
    def show(self):
        cv2.imshow("Image",self.image1)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()

