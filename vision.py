import cv2 as cv
import numpy as np
from picamera2 import Picamera2
from libcamera import controls
import solve
def nothing(x):
   pass

# Cube Array
cubeList = ""
clorhue = []

# Drawing intializing
lineLenght = 450
intialPoint = ((640//2)-(lineLenght//2),480-30)
pieceLenght = lineLenght // 3
topPoint = (intialPoint[0]+(lineLenght//2),intialPoint[1] - int((lineLenght//2)*np.tan(np.pi/3))) 
sidePointLower = (intialPoint[0]+(pieceLenght//2),intialPoint[1] - int((pieceLenght//2)*np.tan(np.pi/3))) 
sidePointUpper = (intialPoint[0]+pieceLenght,intialPoint[1] - int((pieceLenght)*np.tan(np.pi/3))) 

points = {
    "A" : intialPoint,
    "B":(intialPoint[0]+pieceLenght,intialPoint[1]),
    "C":(intialPoint[0]+(pieceLenght*2),intialPoint[1]),
    "D":(intialPoint[0]+lineLenght,intialPoint[1]),
    "E":sidePointLower,
    "F":(sidePointLower[0]+pieceLenght,sidePointLower[1]),
    "G":(sidePointLower[0]+(pieceLenght*2),sidePointLower[1]),
    "H":sidePointUpper,
    "I":(sidePointUpper[0]+pieceLenght,sidePointUpper[1]),
    "J":topPoint
}

# Drawing rectangle intializing
recLength = pieceLenght//5
recOffsetHeight = pieceLenght//2
recPoints = {
    0:((points['J'][0]-(recLength//2),points['J'][1]+recOffsetHeight),(points['J'][0]+(recLength//2),points['J'][1]+recOffsetHeight+recLength)),
    1:((points['H'][0]-(recLength//2),points['H'][1]+recOffsetHeight),(points['H'][0]+(recLength//2),points['H'][1]+recOffsetHeight+recLength)),
    2:((points['F'][0]-(recLength//2),points['F'][1]-recOffsetHeight),(points['F'][0]+(recLength//2),points['F'][1]-recOffsetHeight-recLength)),
    3:((points['I'][0]-(recLength//2),points['I'][1]+recOffsetHeight),(points['I'][0]+(recLength//2),points['I'][1]+recOffsetHeight+recLength)),
    4:((points['E'][0]-(recLength//2),points['E'][1]+recOffsetHeight),(points['E'][0]+(recLength//2),points['E'][1]+recOffsetHeight+recLength)),
    5:((points['B'][0]-(recLength//2),points['B'][1]-recOffsetHeight),(points['B'][0]+(recLength//2),points['B'][1]-recOffsetHeight-recLength)),
    6:((points['F'][0]-(recLength//2),points['F'][1]+recOffsetHeight),(points['F'][0]+(recLength//2),points['F'][1]+recOffsetHeight+recLength)),
    7:((points['C'][0]-(recLength//2),points['C'][1]-recOffsetHeight),(points['C'][0]+(recLength//2),points['C'][1]-recOffsetHeight-recLength)),
    8:((points['G'][0]-(recLength//2),points['G'][1]+recOffsetHeight),(points['G'][0]+(recLength//2),points['G'][1]+recOffsetHeight+recLength))
}

# color ranges:
redLower = 160
redUpper = 15 

yellowLower = redUpper + 1
yellowUpper = 55

greenLower = yellowUpper + 1
greenUpper = 80

blueLower = greenUpper + 1
blueUpper = redLower

# PiCamera Initializing 
# cap = cv.VedioCapture(0)
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration({"size": (640, 480)})
picam2.configure(camera_config)
picam2.start()
  

cv.namedWindow('image')


cv.createTrackbar('sat','image',0,100,nothing)
cv.createTrackbar('val','image',0,100,nothing)

while 1:
    image = picam2.capture_array()
    
    frame = cv.cvtColor(image, cv.COLOR_RGB2BGR) 
#    frame,ret = cap.read()

    cv.drawContours(frame,[np.array( [points[point] for point in ["A","B","E"]] )],-1,(255,255,0),3)
    cv.drawContours(frame,[np.array( [points[point] for point in ["B","C","F"]] )],-1,(255,255,0),3)
    cv.drawContours(frame,[np.array( [points[point] for point in ["C","D","G"]] )],-1,(255,255,0),3)
    cv.drawContours(frame,[np.array( [points[point] for point in ["E","F","H"]] )],-1,(255,255,0),3)
    cv.drawContours(frame,[np.array( [points[point] for point in ["F","G","I"]] )],-1,(255,255,0),3)
    cv.drawContours(frame,[np.array( [points[point] for point in ["H","I","J"]] )],-1,(255,255,0),3)

    hsvFrame = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    for i in range(9):
        cv.rectangle(frame,recPoints[i][0],recPoints[i][1],(150,150,150),1)
    
    satOffset = cv.getTrackbarPos('sat','image')
    valOffset = cv.getTrackbarPos('val','image')
    minSaturation = 0
    minValue = 0
    for i in [1,3,6]:
        minSaturation += np.mean(hsvFrame[recPoints[i][0][1]:recPoints[i][1][1],recPoints[i][0][0]:recPoints[i][1][0],1])-satOffset
        minValue += np.mean(hsvFrame[recPoints[i][0][1]:recPoints[i][1][1],recPoints[i][0][0]:recPoints[i][1][0],2])-valOffset
    # print(minSaturation,minValue)
    lower = np.array([0, minSaturation // 3, minValue // 3],dtype=np.uint8)
    upper = np.array([180, 255, 255],dtype=np.uint8)

    mask = cv.inRange(hsvFrame, lower , upper)
    result = cv.bitwise_and(frame, frame, mask=mask)

    faceColor = ""
    if cv.waitKey(115) & 0xFF == ord("s"):
        print("Colors Hues:")
        for i in range(9):
            hueValue = (hsvFrame[recPoints[i][0][1]+(recLength//2)][recPoints[i][0][0]+(recLength//2)][0])
            clorhue.append(hueValue)
            if 0 <= hueValue <= redUpper or redLower <= hueValue <= 180:
                faceColor += "r"
            elif yellowLower <= hueValue <= yellowUpper:
                faceColor += "y"

            elif greenLower <= hueValue <= greenUpper:
                faceColor += "g"
            
            elif blueLower <= hueValue <= blueUpper:
                faceColor += "b"
    
        cubeList += faceColor
        print(cubeList)
        print(clorhue)
        if len(cubeList) == 36:
            cubeListlist = list(cubeList)
            cubeList1 = list("".join(reversed(cubeList[28:31])))
            cubeList2 = list("".join(reversed(cubeList[31:36])))
            for i in range(len(cubeList1)):
                cubeListlist[28+i] = cubeList1[i]
            for i in range(len(cubeList2)):
                cubeListlist[31+i] = cubeList2[i]
            cubeList = "".join(cubeListlist)
            print("Corrected CubeList : ",cubeList)
            break
    result = cv.flip(result,1)
    cv.imshow("res",result)
    # ~ cv.imshow("Main",frame)

    if cv.waitKey(32) & 0xFF == ord(" "):
        break

# cap.release()
cv.destroyAllWindows()

solve.solveIt(cubeList)
