# For Yolov8 Segmentation

Here is how to run Touch and Spout integrated with Yolov8 Segmentation and Ultralytics. 


# Download Libraries
Make sure to have cv2, 0mq, ultralytics, zlib, and pickle downloaded.

## Setting up Spout 

Clone the `Spout-for-Python-master` folder and then with anaconda3, create a new anaconda venv with python version 3.7 (highest compatible version for Spout). 

## Setting up Touch Designer

Make sure to copy `complex_object.py` into a file called `_init_.py`and create a directory called `complex_object` in your local Python site packages. Import python and it's site packages into the Touch Designer Pyton 64-bit module path. 

# Running the FIles

1. Open the `cx2-0mq - intWSpout - customPlot - Composite.toe` file. 
2. Pulse `SetUp` Parameters for the ScriptTOP.
3. Open a command prompt and activate your anaconda venv with Python 3.7. 
4. Switch into where you have `Spout-for-Python-master` folder cloned. 
5. Run `python test-ultra-0mq-producer-customPlot.py` command in the COMMAND PROMPT where your anaconda venv is running. 
6. Click `X` on the Spout program or run `Ctrl C` to cleanly exit the program. 


#For yolov3 Work
Download YoloV3 in TouchDesigner-MVP.
Click 'script4'.
Press Tab to open the Parameters and click 'Setup' tab then the 'Setup' button next to 'Setup Parameters'. 
Then click into the 'Yolo COnfig' page.
Click 'Pulse' next to 'Load YOLO Model' after you input the paths to your files. 

Mine was: 
YOLO Config Path. ' C:\Users\Admin\Desktop\yoloScripting\yolov3.cfg '
YOLO Weights Path. ' C:\Users\Admin\Desktop\yoloScripting\yolov3.weights '
Classes File Path. ' C:\Users\Admin\Desktop\yoloScripting\coco.names '

Then you can run.

Right Click script4_callbacks and 'Edit in TextPort' if wanted.
In TextPort, run ```op('/project1/script4_callbacks').cook(force=True)``` to force Cook when testing.
