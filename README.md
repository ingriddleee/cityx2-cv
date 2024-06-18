### For Yolov8 Segmentation
1. IN COMMAND PROMPT: Activate (pt37) `C:\Users\Admin\Desktop\sklar-repo\cityx2-cv\Spout-for-Python-master` make sure in this directory. This environment also uses pt37.
    1. conda env list
    2. conda activate pt37
2. In VSCode, open Spout-For-Python-Master and use `cx2-0mq - intWSpout.toe` and `test-ultra-0mq-producer.py` (Successfully receive frame from TD and run Yolo/Ultralytics locally on it to detect), currently in progress is `test-ultra-0mq.py`. (extracting frames and sending it back). 
3. Run `python test-ultra-0mq-producer.py` command in the COMMAND PROMPT (where I activated my conda env). Click X on Spout window to cleanly close program.

Make sure to pulse SetUp Parameters for Script1 and Import a Folder having complex_object. [If using Pickling]


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
