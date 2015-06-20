# FractalisAR: an augmented reality experiment with fractals
# Copyright (C) 2015  Carlos Matías de la Torre

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import cv2
import numpy as np

from fractal_manager import FractalsDirectory, BlendModes
from sensors import TestSensor


# Camera ID, in case there are many cameras available.
CAMERA_ID = 1

# Size of the captured frame
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720

# If True, result will be output raw to the standard output.
# Useful for straming
STDOUT = False

# If True, the captured frames will be shown in an OpenCV window.
SHOW_IMAGE = True

# If True, the mask  computed to merge images will be shown in an OpenCV window
SHOW_MASK = False

# If True, the resulting image will be shown in an OpenCV window.
SHOW_RESULT = True

# If True, a window with controls wil be shown
SHOW_CONTROLS = False

# If True, the original image will be saved in a file.
SAVE_IMAGE = True

# If True and SAVE_IMAGE is also True, this is the filename where the original
# image will be saved.
SAVE_IMAGE_FILENAME = 'original.avi'

# If True, the resulting image will be saved in a file.
SAVE_RESULT = True

# If True and SAVE_IMAGE is also True, this is the filename where the original
# image will be saved.
SAVE_RESULT_FILENAME = 'fractalized.avi'

# The FractalManager (sub-class of GalleriesManager) selects a fractal based on
# a distance value. Each fractal activates at its configured distance (cm).

FILTER_CONFIGURATION = (cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
FRACTALS_CONFIG = [
    {'distance': 40,
     'fractal': FractalsDirectory(data_src='data/quarf/',
                                  mode=BlendModes.MASK,
                                  filter_conf=FILTER_CONFIGURATION,
                                  color_low=np.array([0, 0, 69]),
                                  color_high=np.array([129, 118, 255]))},
    {'distance': 70,
     'fractal': FractalsDirectory(data_src='data/green/',
                                  mode=BlendModes.OVERLAY)},
    {'distance': 100,
     'fractal': FractalsDirectory(data_src='data/blup/',
                                  mode=BlendModes.OVERLAY)},
    {'distance': 130,
     'fractal': FractalsDirectory(data_src='data/mandal/',
                                  mode=BlendModes.OVERLAY)},
    {'distance': 160,
     'fractal': FractalsDirectory(data_src='data/fungi/',
                                  mode=BlendModes.OVERLAY)},
]

# Parameters to connect with the Arduino board, using the serial port.
SENSOR_CONFIGURATION = {
    'device': '/dev/ttyACM0',
    'baud': 9600,
}
# SENSOR = DistanceSensor(device=SENSOR_CONFIGURATION['device'],
#                        baud=SENSOR_CONFIGURATION['baud'])
SENSOR = TestSensor(0, 200)
