# load library
from Library.Spout import Spout
import numpy as np

def main() :
    # create spout object
    spout = Spout(silent = False)
    # create receiver
    spout.createReceiver('input')
    # create sender
    spout.createSender('output')

    while True :

        # check on close window
        spout.check()
        # receive data
        data = spout.receive()
        #data = np.zeros((512, 512, 3))
        # send data
        spout.send(data)
    
if __name__ == "__main__":
    main()