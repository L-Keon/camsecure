import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pyautogui
import camera as cam
import numpy as np

class CamSecureGUI():
    width, height = pyautogui.size() #Get the screen resolution
    menuSize = 250
    cameraSize = 60
    
    
    def __init__(self, title, theme="darkly" ) -> None:
        #
        self.root = ttk.Window(title= title, themename=theme)
        self.root.geometry('{}x{}'.format(self.width-100, self.height-100))
        self.root.resizable(True, True)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        
        self.recognitionVal = ttk.IntVar()
        self.classificationVal = ttk.IntVar()
        self.detectionVal = ttk.IntVar()

        #
        self.app = ttk.PanedWindow(self.root, orient=VERTICAL, bootstyle=DARK)
        self.app.grid(row=0, column=0, sticky=N+S+W+E)

        #create webcams selector zone
        self.cameras = ttk.PanedWindow(self.root, orient=HORIZONTAL, bootstyle=SECONDARY, height=self.cameraSize)
        self.app.add(self.cameras)

        self.title=ttk.Label(self.cameras, text="CamSecure", bootstyle=DANGER, font=("Century Gothic", 25))
        self.title.grid(row=0, column=0, sticky=N+S+W+E)
        self.title.place(relx=0.5, rely=0.5, anchor=CENTER) #Centrer un élément

        #Create container region
        self.container = ttk.PanedWindow(self.root, orient=HORIZONTAL, bootstyle=DARK)
        self.app.grid(row=0, column=0, sticky=N+S+W+E)
        self.app.add(self.container)

        #create menu region
        self.menu = ttk.PanedWindow(self.container, orient=VERTICAL, width=self.menuSize, bootstyle=SECONDARY)
        self.container.add(self.menu)

                
        #create current camera zone
        self.selectedCamera = ttk.PanedWindow(self.container, orient=HORIZONTAL, bootstyle=DARK, height=self.cameraSize)
        self.container.add(self.selectedCamera)

        #Start detection
        self.btnStartCam = ttk.Button(self.menu, text="Start Camera", bootstyle=SUCCESS,command=self.startCam)
        self.btnStartCam.grid(row=0, column=0, padx=5, pady=5)

        #Stop detection
        self.btnStopCam = ttk.Button(self.menu, text="Stop Camera", bootstyle=DANGER, command=self.stopCam)
        self.btnStopCam.grid(row=1, column=0, padx=5, pady=5)

        #alarm setting
        self.alarmSetting = ttk.LabelFrame(self.menu, text="Alarm Setting", bootstyle=INFO)
        self.alarmSetting.grid(row=2, column=0, padx=5, pady=15)

        #Activate Alarm
        self.btnActivateAlarm = ttk.Button(self.alarmSetting, text="Activate Alarm", bootstyle=SUCCESS, command=self.activateAlarm)
        self.btnActivateAlarm.grid(row=0, column=0, padx=5, pady=5)

        #Activate Alarm
        self.btnDesactivateAlarm = ttk.Button(self.alarmSetting, text="Desactivate Alarm", bootstyle=DANGER, command=self.desactivateAlarm)
        self.btnDesactivateAlarm.grid(row=1, column=0, padx=5, pady=5)

        #Volume Setting
        self.btnVolumeSetting = ttk.Scale(self.alarmSetting, from_=100, to=0, orient=VERTICAL, bootstyle=INFO, command=self.getVolume)
        self.btnVolumeSetting.grid(row=2, column=0, padx=5, pady=5)

        #Preferencies setting
        self.preferencies = ttk.LabelFrame(self.menu, text="Options", bootstyle=INFO)
        self.preferencies.grid(row=3, column=0, padx=5, pady=15)

        self.classification = ttk.Checkbutton(self.preferencies, text="Objets Classification",  bootstyle=INFO, command=self.getClassification, variable=self.classificationVal, onvalue=1, offvalue=0)
        self.classification.grid(row=2, column=0, padx=5, pady=5)

        self.recognition = ttk.Checkbutton(self.preferencies, text="Face Recognition", bootstyle=INFO, command=self.getRecognition, variable=self.recognitionVal, onvalue=1, offvalue=0)
        self.recognition.grid(row=1, column=0, padx=5, pady=5)

        self.detection = ttk.Checkbutton(self.preferencies, text="Objets Detection", bootstyle=INFO, command=self.getDetection, variable=self.detectionVal, onvalue=1, offvalue=0)
        self.detection.grid(row=0, column=0, padx=5, pady=5)

        self.videoFrame =np.random.randint(0,255,[100,100,3],dtype='uint8')

        self.img = ttk.ImageTk.PhotoImage(file="assets/cam.png")
        self.logoCams = ttk.Label(self.selectedCamera, image=self.img)
        self.logoCams.place(relx=0.5, rely=0.5, anchor=CENTER) #Centrer un élément
        
    def activateAlarm(self):
        print("Alarm Activated")

    def desactivateAlarm(self):
        print("Alarm Desactivated")

    def getRecognition(self):
        print(self.recognitionVal.get())

    def getClassification(self):
        print(self.classificationVal.get())

    def getDetection(self):
        print(self.detectionVal.get())


    def startGUI(self):
        self.root.mainloop()

    def stopCam(self):
        cam.stopWebCam(self.logoCams, self.img)
        print("Camera stoped")

    def startCam(self):
        self.img = ttk.ImageTk.PhotoImage(ttk.Image.fromarray(self.videoFrame))
        cam.startWebCam(self.logoCams, width=self.width, height= self.height)
        print("Camera start")
    
    def getVolume(self, value):
        print(value)
    
    def setVolume(self, value):
        self.btnVolumeSetting.set(value=value)




cmara = CamSecureGUI(title="CamSecure" )
cmara.startGUI()