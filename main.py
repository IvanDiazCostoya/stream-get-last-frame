import cv2

import queue

import VC_no_buffer

import threading

cv2.namedWindow("test", cv2.WINDOW_NORMAL)
cv2.moveWindow("test", 20, 20)
cv2.resizeWindow('test', 480, 270)

cv2.namedWindow("test2", cv2.WINDOW_NORMAL)
cv2.moveWindow("test2", 1000, 20)
cv2.resizeWindow('test2', 480, 270)

URL = "udp://224.0.0.1:9999?pkt_size=1316"

cap = cv2.VideoCapture(URL)
cap2 = VC_no_buffer.VideoCaptureNoBuffer(URL)

q = queue.Queue()

while True:

    ret, frame = cap.read()
    frame2 = cap2.read2()

    cv2.imshow("test", frame)
    cv2.imshow("test2", frame2)

    if not ret:
        break

    cv2.waitKey(20)
