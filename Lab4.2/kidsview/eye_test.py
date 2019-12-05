import cv2
from GazeTracking.gaze_tracking import *
import operator
from test_calibration import TestCalibration
from collect_eye_data import CollectEyeData

#Eye Movment Test
video = cv2.VideoCapture(0) #use "" to save file
test_calibration = TestCalibration(video, 100, 100)
collect_eye_data = CollectEyeData(video, test_calibration.get_offset(), 150)
video.release()

eye_movment_data = collect_eye_data.get_frame_data()

for i in eye_movment_data:
    print(i)

#Visual Acuity Test