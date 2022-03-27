import cv2
import math

image_path = None
#output_path = None

def dist(x1,y1,x2,y2):
    return math.sqrt((x2 - x1)  2 + (y2 - y1)  2)

def detect_coins():
    coins = cv2.imread(image_path, 1)
    gray = cv2.cvtColor(coins, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(gray, 7)
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT, 1, 50, param1=100, param2=50, minRadius=150, maxRadius=300)
    unique_circles = []

    for detected_circle in circles[0]:
        x, y, r = detected_circle
        is_unique = True
        for c in unique_circles:
            if dist(x,y,c[0],c[1]) > 100:
                pass
            elif c[2] < r:
                unique_circles.append([x,y,r])
                unique_circles.remove(c)
                is_unique = False
            else:
                is_unique = False
        if is_unique:
            unique_circles.append([x,y,r])

    for c in unique_circles:
        x,y,r = c
        #coins_detected = cv2.circle(coins_copy, (int(x), int(y)), int(r), (0, 255, 0), 4,)

    print("Coins: %s" % (len(unique_circles)))

    #cv2.imwrite(output_path, coins_detected)

    return circles
detect_coins()
