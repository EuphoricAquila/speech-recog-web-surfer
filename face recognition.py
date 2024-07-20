
### I linked the speech recog web surfer to this below so be sure to uncomment it out later

import face_recognition as fr
import cv2
import pyttsx3 as tts
# i can always add in new enc to register new faces
img = cv2.imread(r"C:\Users\User\OneDrive\Desktop\Mr.B Programming Stuff\Bharaath Facial Recog\man3.jpg")
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
enc = fr.face_encodings(rgb)[0]

#img2 = cv2.imread(r"C:\Users\User\Downloads\vsauce michael2.jpg")
#rgb2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
#enc2 = fr.face_encodings(rgb2)[0]
engine = tts.init()
cap = cv2.VideoCapture(0)
if True:
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    loc = fr.face_locations(rgb)
    enc3 = fr.face_encodings(rgb, loc)[0]

    results = fr.compare_faces([enc3], enc)
    if results == [True]:
        print("Hello Master!")
        engine.say("Hello Master!")
        engine.runAndWait()
        #with open(r"C:\Users\User\OneDrive\Desktop\Mr.B Programming Stuff\speech recog web surfer.py") as file:
         #   exec(file.read())
    else:
        engine.say("Who are you?")
        engine.runAndWait()


cv2.waitKey(0)
