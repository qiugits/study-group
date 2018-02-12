from imutils.video.pivideostream import PiVideoStream
import time
import datetime
import numpy as np
import cv2


class SimpleStreamer(object):
    def __init__(self, flip = False):
        self.vs = PiVideoStream(resolution=(800, 608)).start()
        self.flip = flip
        time.sleep(2.0)

    def __del__(self):
        self.vs.stop()

    def flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 0)
        return frame

    def get_frame(self):
        frame = self.flip_if_needed(self.vs.read())
        # gray_vid = cv2.cvtColor(frame, cv2.IMREAD_GRAYSCALE)
        edge_frm = cv2.Canny(frame, 50, 110)
        ret, jpeg = cv2.imencode('.jpg', edge_frm)
        return jpeg.tobytes()
