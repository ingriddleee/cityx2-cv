#integrate producer.py with test-ultra.py
# load necessary libraries
from Library.Spout import Spout
import numpy as np
import cv2
from ultralytics import YOLO
import zmq
import time
import zlib
import pickle
from complex_object import ComplexObject

def send_zipped_pickle(socket, obj, flags=0, protocol=-1):
    """pickle an object, and zip the pickle before sending it"""
    p = pickle.dumps(obj, protocol)
    z = zlib.compress(p)
    return socket.send(z, flags=flags)

def main():
    # Initialize Spout
    spout = Spout(silent=False)
    spout.createReceiver('input')
    spout.createSender('output')  # Create a sender to send processed frames

    # Initialize YOLO model
    model = YOLO('yolov8s-seg.pt')

    #init networking
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://127.0.0.1:5555")

    try:
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
                spout.send(annotated_frame) #TODO: once finish testing, remove this as I only want to send back results / mask data. 

                send_zipped_pickle(socket, results)
                print("Published:", results)
                time.sleep(1)

                # Break the loop if 'q' is pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    finally:
        socket.close()
        context.term()
    # Clean up
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

