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
import sys

import settings

from fractal_manager import FractalManager


def main(*args):
    # Input setup
    source = settings.CAMERA_ID
    if len(args) > 1:
        source = args[1]
    cap = cv2.VideoCapture(source)
    # Try to set the camera frame size with the existing settings but as it
    # doesn't work equally for all cameras, record the resulting frame size
    # parameters
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, settings.FRAME_HEIGHT)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, settings.FRAME_WIDTH)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    manager = FractalManager(sensor=settings.SENSOR)
    for fractal_conf in settings.FRACTALS_CONFIG:
        fractal_conf.update({'height': height, 'width': width})
        manager.register(**fractal_conf)

    original_out = None
    if settings.SAVE_IMAGE:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        original_out = cv2.VideoWriter(settings.SAVE_IMAGE_FILENAME, fourcc,
                                       20.0, (width, height))
    result_out = None
    if settings.SAVE_RESULT:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        result_out = cv2.VideoWriter(settings.SAVE_RESULT_FILENAME, fourcc,
                                     20.0, (width, height))

    if settings.SHOW_IMAGE:
        cv2.namedWindow('image')

    time = 0
    while True:
        frame_loaded, frame = cap.read()
        if frame_loaded:
            time += 1

        fractal = manager.get_current()
        result = fractal.merge(frame)

        if settings.SHOW_IMAGE:
            cv2.imshow('image', frame)
        if settings.SHOW_RESULT:
            cv2.imshow('fractalized', result)

        if settings.SAVE_IMAGE:
            original_out.write(frame)
        if settings.SAVE_RESULT:
            result_out.write(result)
        if settings.STDOUT:
            sys.stdout.write(result.tostring())

        # Press 'q' to exit the loop
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    if settings.SAVE_IMAGE:
        original_out.release()
    if settings.SAVE_RESULT:
        result_out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)
    sys.exit(0)
