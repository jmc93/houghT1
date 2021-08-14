import cv2
import numpy as np

font = cv2.FONT_HERSHEY_COMPLEX

img = cv2.imread("25.jpg")
img2 = cv2.imread("25.jpg")

szarosc = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
can = cv2.Canny(szarosc, 50, 200)

linie = cv2.HoughLinesP(can, 5, np.pi/180,20,3,0)
wszkolka = np.uint16(np.around(linie))
print(wszkolka)
print(wszkolka.shape)
print('kropek ' + str(wszkolka.shape[1]))

#print(len(linie))
konturVec = []
x5=0
y5=0
for line in linie:
    x1, y1, x2, y2 = line[0]
    x = x2 - x1
    y = y2 - y1
    if (x-x5)>4 or (x-x5)<-4 or (y-y5)>4 or(y-y5)<-4 :
        konturVec.append(1)
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)
    x5=x
    y5=y

#test githuba
cv2.imshow("Krawedzie", can)
cv2.imshow("WykrKrawedzie", img)
cv2.imshow("Oryginal", img2)
cv2.imwrite("CanKrawedzie.jpg",can)
cv2.imwrite('WykrKrawedzie.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()


