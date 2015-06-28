#-*- coding: utf-8 -*-

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

import configargparse
import cv2
import logging
import serial
import sys

from collections import defaultdict

from fractals_config import FRACTALS_CONFIG
from fractal_manager import FractalManager
from sensors import DistanceSensor, TestSensor


SENSORS = defaultdict(TestSensor)
try:
    SENSORS['arduino'] = DistanceSensor()
except serial.SerialException:
    logging.info('No Arduino board found in default location. '
                 'Default TestSensor will be used')


def main(settings):
    # Input setup
    source = settings.input
    if isinstance(source, int):
        use_camera = True
    elif isinstance(source, str):
        use_camera = False
    else:
        raise ValueError("Expected int or str for input")

    cap = cv2.VideoCapture(source)
    if use_camera:
        # Try to set the camera frame size with the existing settings but as it
        # doesn't work equally for all cameras, afterwards record the resulting
        # frame size parameters
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, settings.height)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, settings.width)

    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    manager = FractalManager(sensor=SENSORS[settings.sensor])
    for fractal_conf in FRACTALS_CONFIG:
        fractal_conf.update({'height': height, 'width': width})
        manager.register(**fractal_conf)

    original_out = None
    if settings.original_image_filename:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        original_out = cv2.VideoWriter(settings.original_image_filename, fourcc,
                                       20.0, (width, height))
    result_out = None
    if settings.result_filename:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        result_out = cv2.VideoWriter(settings.result_filename, fourcc,
                                     20.0, (width, height))

    if settings.show_image:
        cv2.namedWindow('image')

    time = 0
    while True:
        frame_loaded, frame = cap.read()
        if frame_loaded:
            time += 1
        else:
            continue

        fractal = manager.get_current()
        result = fractal.merge(frame)

        if settings.show_image:
            cv2.imshow('image', frame)
        if settings.show_result:
            cv2.imshow('fractalized', result)

        if settings.original_image_filename:
            original_out.write(frame)
        if settings.result_filename:
            result_out.write(result)
        if settings.stdout:
            sys.stdout.write(result.tostring())

        # Press 'q' to exit the loop
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    if settings.original_image_filename:
        original_out.release()
    if settings.result_filename:
        result_out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    args = configargparse.ArgParser(default_config_files=['settings.ini'])
    args.add('-c', '--config', required=False, is_config_file=True,
               help='Custom config file path')
    args.add('-i', '--input', default=0, metavar='SOURCE',
               help='Camera ID or path to video file')
    # Setup
    args.add('-w', '--width', '--frame_width', default=640,
             help='Width of the captured frame')
    args.add('-he', '--height', '--frame_height', default=480,
             help='Height of the captured frame')
    args.add('-n', '--sensor', default='test',
             help='Where to take distance data from')
    # Save
    args.add('-o', '--original_image_filename', metavar='PATH',
             help='If given, the original video will be saved in this file.')
    args.add('-r', '--result_filename', metavar='PATH',
             help='If given, the resulting video will be saved in this file.')
    # Show
    args.add('-no', '--dont_show_image', action='store_true', default=False,
             help="If given, the captured frames won't be shown")
    args.add('-nt', '--dont_show_result', action='store_true', default=False,
             help="If given, the transformed frames won't be shown")
    args.add('--stdout', action='store_true', default=False,
             help='If given, result will be output raw to the standard output. '
                  'Useful for straming')

    settings = args.parse_args()
    settings.show_image = not settings.dont_show_image
    settings.show_result = not settings.dont_show_result
    main(settings)
    sys.exit(0)
