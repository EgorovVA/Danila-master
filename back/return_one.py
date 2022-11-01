import eel
import cv2

@eel.expose
def apdate():
     image_file = r'C:/Users/vlade/Desktop/test_eel-master/Danila-master/front/images/photo.jpg' 
     image_file_new = r'C:/Users/vlade/Desktop/test_eel-master/Danila-master/front/images/photo_one.jpg' 
     with open("C:/Users/vlade/Desktop/test_eel-master/Danila-master/front/comand/gcode.txt", 'r+') as f:
          f.truncate(0)
     img = cv2.imread(image_file_new)
     cv2.imwrite(image_file, img)
     cv2.imwrite("C:/Users/vlade/Desktop/test_eel-master/Danila-master/front/images/lupe_1.jpg", img)
     cv2.imwrite("C:/Users/vlade/Desktop/test_eel-master/Danila-master/front/images/lupe_0.jpg", img)