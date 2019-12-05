import cv2
from GazeTracking.gaze_tracking import *

class TestCalibration(object):
	"""
	This class is for setting up the center coordinates of the screen.
	Retrieve the webcam coordinate for N frames and average them out
	Use the webcam coordinates to calculate the offset using the center of the screen
	"""

	def __init__(self, video, num_of_camera_frames, num_of_center_frames):
		self.avg_camera_coords_left = [0,0]
		self.avg_camera_coords_right = [0,0]
		self.avg_center_coords_left = [0,0]
		self.avg_center_coords_right = [0,0]
		self.offset_left = 0
		self.offset_right = [0,0]
		self.cam_num_frame = num_of_camera_frames
		self.cen_num_frame = num_of_center_frames
		self.gaze = GazeTracking()
		self.video_feed = video
		self.calibrate()
		self.calculate_offset()


	def add_camera_coord(self, coords_left, coords_right):
		self.avg_camera_coords_left[0] += coords_left[0]
		self.avg_camera_coords_left[1] += coords_left[1]
		self.avg_camera_coords_right[0] += coords_right[0]
		self.avg_camera_coords_right[1] += coords_right[1]

	def average_camera_coord(self):
		self.avg_camera_coords_left[0] /= self.cam_num_frame
		self.avg_camera_coords_left[1] /= self.cam_num_frame
		self.avg_camera_coords_right[0] /= self.cam_num_frame
		self.avg_camera_coords_right[1] /= self.cam_num_frame

	def get_camera_coord(self):
		return self.avg_camera_coords_left, self.avg_camera_coords_right

	def add_center_coord(self, coords_left, coords_right):
		self.avg_center_coords_left[0] += coords_left[0]
		self.avg_center_coords_left[1] += coords_left[1]
		self.avg_center_coords_right[0] += coords_right[0]
		self.avg_center_coords_right[1] += coords_right[1]

	def average_center_coord(self):
		self.avg_center_coords_left[0] /= self.cen_num_frame
		self.avg_center_coords_left[1] /= self.cen_num_frame
		self.avg_center_coords_right[0] /= self.cen_num_frame
		self.avg_center_coords_right[1]/= self.cen_num_frame

	def get_center_coord(self):
		return self.avg_center_coords_left, self.avg_camera_coords_right

	def calculate_offset(self):
		self.offset_left = (self.avg_camera_coords_left[0] - self.avg_center_coords_left[0], self.avg_camera_coords_left[1] - self.avg_center_coords_left[1])
		self.offset_right = (self.avg_camera_coords_right[0] - self.avg_center_coords_right[0], self.avg_camera_coords_right[1] - self.avg_center_coords_right[1])

	def get_offset(self):
		return self.offset_left, self.offset_right

	def calibrate(self):
		print("Starting webcam calibration")
		i = self.cam_num_frame
		while (i >= 0):
			ret, frame = self.video_feed.read()
			self.gaze.refresh(frame)
			frame = self.gaze.annotated_frame()
			if(self.gaze.pupils_located == True):
				self.add_camera_coord(self.gaze.pupil_left_coords(), self.gaze.pupil_right_coords())
			cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
			cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
			cv2.imshow("window", frame)
			if cv2.waitKey(1) == 27:
				break			
			i-=1

		self.average_camera_coord()
		print("Webcam coordinates are ", self.get_camera_coord())	

		print("Starting screen center calibration")
		i = self.cen_num_frame
		while(i >= 0):
			ret, frame = self.video_feed.read()
			self.gaze.refresh(frame)
			frame = self.gaze.annotated_frame()
			if(self.gaze.pupils_located == True):
				self.add_center_coord(self.gaze.pupil_left_coords(), self.gaze.pupil_right_coords())
			cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
			cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
			cv2.imshow("window", frame)
			if cv2.waitKey(1) == 27:
				break			
			i-=1			

		self.average_center_coord()
		print("Screen center coordinates are ", self.get_center_coord())