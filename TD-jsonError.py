#///////////////////
# me - this DAT
# scriptOp - the OP which is cooking
#
# press 'Setup Parameters' in the OP to call this function to re-create the parameters.
import cv2
from ultralytics import YOLO
import torch
import numpy as np

def onSetupParameters(scriptOp):
	##page = scriptOp.appendCustomPage('Ultralytics Model Path')
	#page.appendStr('Ultralyticsmodel', label='Ultralytics Model Path') 
	#page.appendPulse('Loadmodel', label='Load YOLO Model')
	model = YOLO(r'C:\Users\Admin\Desktop\sklar-repo\yolov8s-seg.pt')  # Load the model
	baseOp = op('script1')
	# Store the loaded model in 'script1'
	baseOp.store('model', model)
	print('model loaded and stored')
	return

# called whenever custom pulse parameter is pushed
def onPulse(par):
	'''if par.name == 'Loadmodel':  # Check if the pulse parameter 'Loadmodel' is triggered
		print('Loading YOLO Model')
		baseOp = op('script1')  # Assuming 'script1' is where you want to store the model
		# Load the model using the path specified in the 'Ultralyticsmodel' parameter
		modelPath = baseOp.par.Ultralyticsmodel.eval()
		model = YOLO(modelPath)  # Load the model

		# Store the loaded model in 'script1'
		baseOp.store('model', model)

		print('Model loaded and stored')'''
	return


def onCook(scriptOp):
	model = op('script1').fetch('model', None)
	if model is not None:
		print('model is loaded:' )
	else: 
		print('model is NOT loaded ')
		return
	
	img = op('null1').numpyArray(delayed=True)
	frameRGB = img[:, :, :3] 
	frame = np.flip(frameRGB, 2)
	results = model(frame)
	annotated_frameRGB = results[0].plot()
	outputFrameRGB = np.flip(annotated_frameRGB, 2)  # Flip color channels back if necessary
	h, w, _ = outputFrameRGB.shape
	alphaChannel = np.ones((h, w, 1), dtype=outputFrameRGB.dtype) * 255  # Create an opaque alpha channel
	outputFrameRGBA = np.concatenate((outputFrameRGB, alphaChannel), axis=-1)
	
	# Update the Script TOP's output with the processed frame, now in RGBA format
	scriptOp.copyNumpyArray(outputFrameRGBA) 
	return
