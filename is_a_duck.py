import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys

from matplotlib.colors import hsv_to_rgb


arguments = len(sys.argv) - 1
if arguments < 1:
    print("Need to input image filename")
    exit()
elif arguments > 1:
    print("Only input one image")
    exit()
    

img_name = sys.argv[1]

duck = cv2.imread(img_name)

duck = cv2.cvtColor(duck, cv2.COLOR_BGR2RGB)

hsv_duck = cv2.cvtColor(duck, cv2.COLOR_RGB2HSV)

#Color mask definitions
light_yellow =  (15, 150, 150)
dark_yellow = (50, 255, 255)

light_orange2 = (100, 100, 100)
dark_orange2 = (200, 255, 255)

light_orange = (0, 100, 100)
dark_orange = (15, 255, 255)

mask = cv2.inRange(hsv_duck, light_yellow, dark_yellow)

result_body = cv2.bitwise_and(duck, duck, mask=mask)



mask_orange = cv2.inRange(hsv_duck, light_orange, dark_orange)


mask_orange2 = cv2.inRange(hsv_duck, light_orange2, dark_orange2)
#result_orange2 = cv2.bitwise_and(duck, duck, mask=mask_orange2)

mask_orange = mask_orange+mask_orange2

result_bill = cv2.bitwise_and(duck, duck, mask=mask_orange)

total_mask = mask_orange+mask

result = cv2.bitwise_and(duck, duck, mask=total_mask)

num_body = cv2.countNonZero(mask)
num_bill =  cv2.countNonZero(mask_orange)
total_pix = duck.size


#print(num_body)
#print(num_bill)
#print(total_pix)

if (num_body > 25 and num_bill > 25):
    if(num_body > 4*num_bill and  num_body < 20*num_bill):
        message = "That's a duck!"
    else:
        message = "Probably not a duck"
else:
    message = "Probably not a duck"


plt.subplot(1, 2, 1)
plt.title(message)
plt.imshow(duck)
plt.subplot(1, 2, 2)
plt.imshow(result)
plt.show()


