import ttkbootstrap as ttk
import cv2

global webcam

def startWebCam(videoLabel, width, height):
    global webcam 
    webcam = cv2.VideoCapture(0)

    webcam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    while True:
        ret, frame= webcam.read()
        
        #update the image to tkinter
        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img_update = ttk.ImageTk.PhotoImage(ttk.Image.fromarray(frame))
        videoLabel.configure(image=img_update)
        videoLabel.image=img_update
        videoLabel.update()
 
        if not ret:
            print("failed to grab frame")
            break

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")

            webcam.release()
            cv2.destroyAllWindows()
            break

def stopWebCam(videoLabel, img_update):
    global webcam
    webcam.release()
    cv2.destroyAllWindows()
    videoLabel.configure(image=img_update)
