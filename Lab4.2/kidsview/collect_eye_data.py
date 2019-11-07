import cv2
from GazeTracking.gaze_tracking import *

class CollectEyeData(object):
	"""
	This class is for collecting eye data per frame.
	Collects the coordinates for N frames
	Use the offset to calculate the true coordinate and saves it in a form of a list
	"""
	def __init__(self, video, offset, tot_frames):
		self.offset = offset
		self.frame_data = []
		self.total_frame_count = tot_frames
		self.num_of_frames = 0 
		self.gaze = GazeTracking()
		self.video_feed = video
		self.start_test()

	def add_frame_data(self, coord_left, coord_right):
		hold_coord_left = [0,0]
		hold_coord_right = [0,0]
		hold_coord_left[0] = coord_left[0] - self.offset[0][0]
		hold_coord_left[1] = coord_left[1] - self.offset[0][1]
		hold_coord_right[0] = coord_right[0] - self.offset[1][0]
		hold_coord_right[1] = coord_right[1] - self.offset[1][1]
		self.frame_data.append((hold_coord_left, hold_coord_right))
		self.num_of_frames += 1

	def get_frame_data(self):
		return self.frame_data

	def start_test(self):
		while (self.num_of_frames < self.total_frame_count):
			ret, frame = self.video_feed.read()
			self.gaze.refresh(frame)
			frame = self.gaze.annotated_frame()

			if(self.gaze.pupils_located == True):
				self.add_frame_data(self.gaze.pupil_left_coords(), self.gaze.pupil_right_coords())
			cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
			cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
			cv2.imshow("window", frame)
			if cv2.waitKey(1) == 27:
				break