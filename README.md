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
