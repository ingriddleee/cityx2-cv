# load necessary libraries
from Library.Spout import Spout
import numpy as np
import cv2
from ultralytics import YOLO
import zmq

def setup_zmq():
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)  # Publisher socket
    publisher.bind("tcp://*:5555")  # Bind on all interfaces, port 5555
    return publisher

# Function to send data via ZeroMQ
def send_data(publisher, data):
    publisher.send(data)

# Function to extract masks using Ultralytics API
def extract_masks(results):
    # Extract masks as a numpy array if they are available in the results
    if results[0].masks:
        return results[0].masks.numpy()  # Converts mask tensor to numpy array
    else:
        return None  # Return None if no masks are available

def main():
    # Initialize Spout
    spout = Spout(silent=False)
    spout.createReceiver('input')
    spout.createSender('output')  # Create a sender to send processed frames

    # Initialize YOLO model
    model = YOLO('yolov8s-seg.pt')

    # Setup ZeroMQ for messaging
    publisher = setup_zmq()

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

            # Extract masks directly from results
            masks = extract_masks(results)
            if masks is not None:
                # Send the mask data
                mask_data = cv2.imencode('.png', masks)[1].tobytes()
                send_data(publisher, mask_data)
            else:
                print("No masks detected")

            # Display the processed frame -- redundant. I will have two windows, frame as well as the 
            #cv2.imshow("YOLOv8 Inference", annotated_frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Clean up
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
