import cv2
from ultralytics import YOLO
import time

model = YOLO('yolov8s-seg.pt')

video_path = 'cars.MOV'
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    
    if success:
        #start = time.perf_counter()
        results = model(frame) #run yolov8 inference on the frame
        #end = time.perf_counter()
        #total_time = end - start
        #fps = 1 / total_time

        annotated_frame = results[0].plot()

        #cv2.putText(annotated_frame, f"FPS: {int(fps)}")
        cv2.imshow("yolo8 Inference", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()