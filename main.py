import cv2
from cvzone.HandTrackingModule import HandDetector

class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (50, 50, 50), 3)
        cv2.putText(img, self.value, (self.pos[0] + 40, self.pos[1] + 60),
                    cv2.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)

    def checkClick(self, x, y):

        if self.pos[0] < x < self.pos[0] + self.width and self.pos[1] < y < self.pos[1] + self.height:
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                          (255, 255, 255), cv2.FILLED)
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                          (50, 50, 50), 3)
            cv2.putText(img, self.value, (self.pos[0] + 20, self.pos[1] + 70),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 5)
            return True
        else:
            return False


# webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280) # width of the image displayed
cap.set(4, 720) # height of the image displayed
detector = HandDetector(detectionCon=0.8, maxHands=1)

# creating the buttons
buttonListValues = [['7', '8', '9', '*'],
                    ['4', '5', '6', '-'],
                    ['1', '2', '3', '+'],
                    ['0', '/', '.', '=']]

# variables
myEquation = ''
delayCount = 0

buttonList = []
for x in range(4):
    for y in range(4):
        xpos = x*100 + 800
        ypos = y*100 + 150
        buttonList.append(Button((xpos,ypos), 100, 100, buttonListValues[y][x]))

# loop
while True:
    # get image from webcam
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # hand detection
    hands, img = detector.findHands(img, flipType=False)

    # draw top box displaying input
    cv2.rectangle(img, (800, 70), (1200, 170), (225, 225, 225), cv2.FILLED)
    cv2.rectangle(img, (800, 70), (1200, 170), (50, 50, 50), 3)

    # draw each buttons
    for button in buttonList:
        button.draw(img)

    # check for hands
    if hands:
        lmList = hands[0]['lmList']
        length, info, img = detector.findDistance(lmList[4][0:2], lmList[8][0:2], img,
                                                  color=(255, 0, 255), scale=10)
        x, y = lmList[4][0:2]
        if length < 40:
            for i, button in enumerate(buttonList):
                if button.checkClick(x, y) and delayCount == 0:
                    currentValue = buttonListValues[int(i%4)][int(i/4)]
                    if currentValue == '=':
                        myEquation = str(eval(myEquation))
                    else:
                        myEquation += currentValue
                    delayCount = 1

    # avoid duplicates
    if delayCount > 0:
        delayCount += 1
        if delayCount > 10:
            delayCount = 0


    # display equation/result
    cv2.putText(img, myEquation, (810, 120), cv2.FONT_HERSHEY_PLAIN, 3, (50, 50, 50), 3)


    # display the image that is resulted
    cv2.imshow('Image', img)
    key = cv2.waitKey(1)

    if key == ord('c'):
        myEquation = ''