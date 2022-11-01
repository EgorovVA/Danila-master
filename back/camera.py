import cv2
import eel

@eel.expose
def click(com_port:int):    
    cap = cv2.VideoCapture(com_port, cv2.CAP_DSHOW)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")


    ret, frame = cap.read()
    if ret:
        cv2.imwrite("C:/Users/vlade/Desktop/test_eel-master/Danila-master/front/images/photo.jpg", frame)
        cv2.imwrite("C:/Users/vlade/Desktop/test_eel-master/Danila-master/front/images/lupe_1.jpg", frame)
        cv2.imwrite("C:/Users/vlade/Desktop/test_eel-master/Danila-master/front/images/lupe_0.jpg", frame)
        print("Successfully saved")
    else:
        print("err")

    cap.release()
    cv2.destroyAllWindows()
    cv2.waitKey(0)
