Install dependencies; kidsview/GazeTracking/requirements.txt

Run eye_test.py

eye_test.py:
    Starts video stream
    Passes video stream to calibration object
    Passes video stream to eye movement data collection object
    Saves eye movement data into array 

test_calibration.py
	TestCalibration():
		Intilaize object with video stream, number of frames looking at the camera, and number of frames looking at the center. 
		Intilizes all variables 
		Start GazeTracking object
		calls calibrate function 
		Calculate camera offset to center

	Calibrate():
		Starts by recording and averaging all the coordinates looking at the camera for the # of frames intialized 
		Then records and averages the coordinates looking at the center for the # of frames intialized 

collect_eye_data.py
	CollectEyeData():
		Intilize object with video stream, offset of camera and screen center, frame count
		Intilizes all variables and starts GazeTracking Object 
		Starts eye movement test

	StartTest()
		Records all coordniates for the seet frame count 

GazeTracking
	Library used to get coordinates of pupil
	GazeTracking object gets fram of video stream and analyzes frame by frame.