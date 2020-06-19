
import sys
import argparse
import cv2
import numpy as np
from collections import OrderedDict
from datetime import datetime, timedelta
from attendance import *
from faces import FaceDetector
from data import FaceData
from gabor import GaborBank
from emotions import EmotionsDetector
import tkinter as tk
from tkinter import filedialog
import pymysql
import face_recognition as fr
import os
import face_recognition
from time import sleep

#---------------------------------------------
class VideoData:
    """
    Helper class to present the detected face region, landmarks and emotions.
    """
    
    #-----------------------------------------
    def __init__(self,imagepath=None):
        """
        Class constructor.
        """

        self._faceDet = FaceDetector()
        '''
        The instance of the face detector.
        '''

        self._bank = GaborBank()
        '''
        The instance of the bank of Gabor filters.
        '''

        self._emotionsDet = EmotionsDetector()
        '''
        The instance of the emotions detector.
        '''

        self._face = FaceData()
        '''
        Data of the last face detected.
        '''

        self._emotions = OrderedDict()
        '''
        Data of the last emotions detected.
        '''
        print(imagepath)
        
    #-----------------------------------------
    def detect(self, frame,face):
        """
        Detects a face and the prototypic emotions on the given frame image.

        Parameters
        ----------
        frame: numpy.ndarray
            Image where to perform the detections from.

        Returns
        -------
        ret: bool
            Indication of success or failure.
        """
        listofemotions=[]
##        ret, face = self._faceDet.detect(frame)
##        if ret:
##            self._face = face

            # Crop just the face region
        frame, face = face.crop(frame)

            # Filter it with the Gabor bank
        responses = self._bank.filter(frame)

            # Detect the prototypic emotions based on the filter responses
        self._emotions = self._emotionsDet.detect(face, responses)
        listofemotions.append(self._emotions)
        

        return True,listofemotions
        

    #-----------------------------------------
    def draw(self, frame,face):
        """
        Draws the detected data of the given frame image.

        Parameters
        ----------
        frame: numpy.ndarray
            Image where to draw the information to.
        """
        # Font settings
        font = cv2.FONT_HERSHEY_SIMPLEX
        scale = 0.5
        thick = 1
        glow = 3 * thick

        # Color settings
        black = (0, 0, 0)
        white = (255, 255, 255)
        yellow = (0, 255, 255)
        red = (0, 0, 255)

        empty = True

##        # Plot the face landmarks and face distance
       
        
        try:
            
            empty = face.isEmpty()
            face.draw(frame)
            x=face.region[0]
            y=face.region[1]
            w = int(frame.shape[1]* 0.2)
        except:
            pass

        # Plot the emotion probabilities
        try:
            emotions = self._emotions
            if empty:
                labels = []
                values = []
            else:
                labels = list(emotions.keys())
                values = list(emotions.values())
                bigger = labels[values.index(max(values))]
               

                # Draw the header
                text = 'emotions'
                size, _ = cv2.getTextSize(text, font, scale, thick)
                y += size[1] + 20

                cv2.putText(frame, text, (x, y), font, scale, black, glow)
                cv2.putText(frame, text, (x, y), font, scale, yellow, thick)

                y += 5
                cv2.line(frame, (x,y), (x+w,y), black, 1)

            size, _ = cv2.getTextSize('happiness', font, scale, thick)
            t = size[0] + 20
            w = 150
            h = size[1]
            for l, v in zip(labels, values):
                lab = '{}:'.format(l)
                val = '{:.2f}'.format(v)
                size, _ = cv2.getTextSize(l, font, scale, thick)

                # Set a red color for the emotion with bigger probability
                color = red if l == bigger else yellow

                y += size[1] + 15

                p1 = (x+t, y-size[1]-5)
                p2 = (x+t+w, y-size[1]+h+5)
                cv2.rectangle(frame, p1, p2, black, 1)

##                # Draw the filled rectangle proportional to the probability
##                p2 = (p1[0] + int((p2[0] - p1[0]) * v), p2[1])
##                cv2.rectangle(frame, p1, p2, color, -1)
##                cv2.rectangle(frame, p1, p2, black, 1)

                # Draw the emotion label
                cv2.putText(frame, lab, (x, y), font, scale, black, glow)
                cv2.putText(frame, lab, (x, y), font, scale, color, thick)

                # Draw the value of the emotion probability
                cv2.putText(frame, val, (x+t+5, y), font, scale, black, glow)
                cv2.putText(frame, val, (x+t+5, y), font, scale, white, thick)
        except Exception as e:
            print(e)
            pass
        return bigger


    def unknown_image_encoded(self,img):
        """
        encode a face given the file name
        """
        face = fr.load_image_file("faces/" + img)
        encoding = fr.face_encodings(face)[0]

        return encoding
    def classify_face(self,im,face):
        """
        will find all of the faces in a given image and label
        them if it knows what they are

        :param im: str of file path
        :return: list of face names
        """

        encoded = {}
        listofnames=[]
        for dirpath, dnames, fnames in os.walk("./faces"):
            for f in fnames:
                if f.endswith(".jpg") or f.endswith(".png"):
                    face = fr.load_image_file("faces/" + f)
                    encoding = fr.face_encodings(face)[0]
                    encoded[f.split(".")[0]] = encoding

        faces = encoded
        
        faces_encoded = list(faces.values())
        known_face_names = list(faces.keys())

##        image = cv2.imread(im, 1)
    ##    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    ##    img = img[:,:,::-1]
##        scale_percent=0.30
##        width=int(im.shape[1]*scale_percent)
##        height=int(im.shape[0]*scale_percent)
##        dimension=(width,height)
##        img=cv2.resize(im,dimension,interpolation=cv2.INTER_AREA)
        face_locations = face_recognition.face_locations(im)
        unknown_face_encodings = face_recognition.face_encodings(im, face_locations)

        face_names = []
        for face_encoding in unknown_face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(faces_encoded, face_encoding)
            name = "Unknown"

            # use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)
            listofnames.append(name)
            

            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Draw a box around the face
                cv2.rectangle(im, (left-20, top-20), (right+20, bottom+20), (255, 0, 0), 2)

                # Draw a label with a name below the face
                cv2.rectangle(im, (left-20, bottom -15), (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(im, name, (left -20, bottom + 15), font, 1.0, (255, 255, 255), 2)

        return(listofnames)
        # Display the resulting image
##        while True:
##
##            cv2.imshow('Video', img)
####            if cv2.waitKey(1) & 0xFF == ord('q'):
##            return face_names 

#---------------------------------------------
def main(argv):
    """
    Main entry of this script.

    Parameters
    ------
    argv: list of str
        Arguments received from the command line.
    """
    
    
    # Parse the command line
    args = parseCommandLine(argv)
    
    # Loads the video or starts the webcam
    if args.source == 'cam':
       ## args.source=filedialog.askopenfilename(filetypes = (("video files","*.mp4")))
        video = cv2.VideoCapture("IMG_1328.mp4")
        
##        video = cv2.VideoCapture(args.id)
        if not video.isOpened():
            print('Error opening webcam of id {}'.format(args.id))
            sys.exit(-1)

        fps = 0
        frameCount = 0
        sourceName = 'Webcam #{}'.format(args.id)
   ##     
    else:
        video = cv2.VideoCapture('IPCAM_IPCAM_2019-10-06_21-34-17.mp4')
##        video = cv2.VideoCapture(args.file)
        if not video.isOpened():
            print('Error opening video file {}'.format(args.file))
            sys.exit(-1)

        fps = int(video.get(cv2.CAP_PROP_FPS))
        frameCount = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        sourceName = args.file

    # Force HD resolution (if the video was not recorded in this resolution or
    # if the camera does not support it, the frames will be stretched to fit it)
    # The intention is just to standardize the input (and make the help window
    # work as intended)
  ##  video.set(cv2.CAP_PROP_FRAME_WIDTH, 0.55*fps);
  ##  video.set(cv2.CAP_PROP_FRAME_HEIGHT, 0.55*fps);
   ## video.set(cv2.CAP_PROP_FPS, fps*0.01);
   ## video.set(cv2.CAP_PROP_POS_MSEC,1000)

    # Create the helper class
    data = VideoData()
##    image = cv2.imread('face1.png')
##    frame=image
    # Text settings
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 1
    thick = 1
    glow = 3 * thick

    # Color settings
    color = (255, 255, 255)

    paused = False
    frameNum = 0
    print("Frame rate : {0}".format(video.get(cv2.CAP_PROP_FPS)))
    count=0
    nameslist=[]
    biggernames=[]
    listofnames=[]
    name=[]
    finalnamelist = []
##    # Process the video input
    while True:

        if not paused:
            start = datetime.now()

        ret, img = video.read()
        
        if ret:
            
            frame = img.copy()
            FACES= FaceDetector()
            ret, face = FACES.detect(frame)
            print (len(face))
            for obj in face:
                listofnames=data.classify_face(frame,obj)
                listofemotions=data.detect(frame,obj)  
                bigger=data.draw(frame,obj)

                if(len(listofnames) != 0):
                    nameslist.append(listofnames[0])
                    name.append(listofnames[0])
                   
                   
                    nameslist.append(bigger)
                   
           ## resize = cv2.resize(sourceName, (680, 680)) 
            cv2.imshow(sourceName, frame)
            count+=30
            video.set(1,count)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
            
    cv2.destroyAllWindows()
    for i in name:
        if i not in finalnamelist:
            finalnamelist.append(i)
    print(finalnamelist)
    video.release()
    
   



    finalresult=[]
    count=0
    expressions=[]
    for i in finalnamelist:
        while(count !=len(nameslist)):
            if (i==nameslist[count]):
                expressions.append(nameslist[count+1])
                count+=2
            else:
                count+=2
        neutral=expressions.count("neutral")
            
        happiness=expressions.count("happiness")
        sadness=expressions.count("sadness")
        anger=expressions.count("anger")
        fear=expressions.count("fear")
        surprise=expressions.count("surprise")
        disgust=expressions.count("disgust")
        activeorinactive=max(neutral,happiness,sadness,anger,fear,surprise,disgust)
        if(activeorinactive == neutral):
            finalresult.append(i)
            finalresult.append("InActive")
        elif(activeorinactive == happiness):
            finalresult.append(i)
            finalresult.append("Active")
        elif(activeorinactive == sadness):
            finalresult.append(i)
            finalresult.append("InActive")
        elif(activeorinactive == anger):
            finalresult.append(i)
            finalresult.append("Active")
        elif(activeorinactive == fear):
            finalresult.append(i)
            finalresult.append("Active")
        elif(activeorinactive == surprise):
            finalresult.append(i)
            finalresult.append("Active")
        elif(activeorinactive == disgust):
            finalresult.append(i)
            finalresult.append("InActive")

    print(finalresult)   

##    conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
####        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
##    cur=conn.cursor()
##    query=("insert into tbl_registration(reg_firstname,reg_lastname, reg_email ,reg_registration, reg_department,reg_session,reg_section) values (%s, %s,%s,%s,%s,(select ses_ID from tbl_session where ses_name=%s),(select sec_ID from tbl_section where sec_name=%s))")
##    data= cur.execute(query,(st_firstname, st_lastname,st_email,st_department,st_registration,self.combosession.currentText(),st_section))
##    conn.commit()

    conn = pymysql.connect(host="localhost" , user='root', password="fatima1234" , db="db_attendance")
##        conn = mysql.connector.connect(host="localhost" , user='root', password="aroojanum242" , database="db_attendance")
    cur=conn.cursor()
    query2=("select CURDATE()")
    cur.execute(query2)
    data2=cur.fetchall()
    print(data2)
    dblist=[]
    print(finalnamelist[0])
    for i in finalnamelist:
       
        query4=("select reg_ID from tbl_registration where reg_registration=%s")
        cur.execute(query4,(i))
        data4=cur.fetchall()
        print(data4)

    for i in finalnamelist:
        dblist.append(i)
        finalnamelist.remove(i)
        
    for i in dblist:
        query=("update tbl_attendance set att_attendance= %s,att_date=(select curdate()),reg_ID=(select reg_ID from tbl_registration where reg_registration=%s),att_productivity=%s order by att_ID desc limit 1")
        data= cur.execute(query,(True,i,finalresult[1]))



    query3=("select sub_ID from tbl_attendance order by att_ID desc limit 1")
    cur.execute(query3)    
    data3=cur.fetchall()
    print(data3)



    query4=("select ses_ID from tbl_attendance order by att_ID desc limit 1")
    cur.execute(query4)    
    data4=cur.fetchall()
    print(data4)

    query5=("select sec_ID from tbl_attendance order by att_ID desc limit 1")
    cur.execute(query5)    
    data5=cur.fetchall()
    print(data5)
    

    s=0

    for i in finalnamelist:
        s+=1
        query=("insert into tbl_attendance(ses_ID,sec_ID,sub_ID,reg_ID,att_date,att_attendance,att_productivity) values(%s,%s,%s,(select reg_ID from tbl_registration where reg_registration=%s),(select curdate()), %s,%s)")
        data= cur.execute(query,(data4,data5,data3,i,True,finalresult[s]))

        
    print(finalnamelist)
    conn.commit()

    
    
            
                
                
            
            

###---------------------------------------------
def parseCommandLine(argv):
    """
    Parse the command line of this utility application.

    This function uses the argparse package to handle the command line
    arguments. In case of command line errors, the application will be
    automatically terminated.

    Parameters
    ------
    argv: list of str
        Arguments received from the command line.

    Returns
    ------
    object
        Object with the parsed arguments as attributes (refer to the
        documentation of the argparse package for details)

    """
    parser = argparse.ArgumentParser(description='Tests the face and emotion '
                                        'detector on a video file input.')

    parser.add_argument('source', nargs='?', const='Yes',
                        choices=['video', 'cam'], default='cam',
                        help='Indicate the source of the input images for '
                        'the detectors: "video" for a video file or '
                        '"cam" for a webcam. The default is "cam".')

    parser.add_argument('-f', '--file', metavar='<name>',
                        help='Name of the video file to use, if the source is '
                        '"video". The supported formats depend on the codecs '
                        'installed in the operating system.')

    parser.add_argument('-i', '--id', metavar='<number>', default=0, type=int,
                        help='Numerical id of the webcam to use, if the source '
                        'is "cam". The default is 0.')


    args = parser.parse_args()

    if args.source == 'video' and args.file is None:
        parser.error('-f is required when source is "video"')

    return args

#---------------------------------------------
# namespace verification for invoking main
#---------------------------------------------
if __name__ == '__main__':
    
    main(sys.argv[1:])
    
