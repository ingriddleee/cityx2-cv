# load necessary libraries
from Library.Spout import Spout
import numpy as np
import cv2
from ultralytics import YOLO

def main():
    # Initialize Spout
    spout = Spout(silent=False)
    spout.createReceiver('input')
    spout.createSender('output')  # Create a sender to send processed frames

    # Initialize YOLO model
    model = YOLO('yolov8s-seg.pt')

    # Main loop
    while True:
        # Check for window close events
        spout.check()

        # Receive frame data from Spout
        frame = spout.receive()
        if frame is not None:
            # Convert the received data to an appropriate format if necessary
            frame = np.array(frame)  # Assuming 'frame' needs conversion to NumPy array

            # Process frame with YOLO
            results = model(frame)
            annotated_frame = results[0].plot()

            # Send processed frame back or to another destination
            spout.send(annotated_frame)

            # Display the processed frame -- redundant. I will have two windows, frame as well as the 
            #cv2.imshow("YOLOv8 Inference", annotated_frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Clean up
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
