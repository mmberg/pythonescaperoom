import cv2
import numpy as np


def run(data):
    koord = [data[5], data[6]]
    numbers = [data[0], data[1], data[2], data[3], data[4]]

    solution = [0,0]

    for i in range(len(koord)):
        img_rgb = cv2.imread(koord[i])
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        for j in range(len(numbers)):
            count = 0
            template = cv2.imread(numbers[j], 0)
            w, h = template.shape[::-1]
            res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
            if j == 0:
                threshold = .99
            else:
                threshold = .84
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):  
                count += 1
                solution[i] += int(numbers[j].split("/")[-1].split(".")[0])
    return solution
