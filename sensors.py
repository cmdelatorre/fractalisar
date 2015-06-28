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

import serial


class Sensor(object):
    """Base class to represent the Sensor interface."""

    def get_data(self):
        raise NotImplementedError()


# The Sensor class abstracts a data-input mechanism. Currently, the
# DistanceSensor reads data from the Serial port where an Arduino board sends
# distance data.
class DistanceSensor(Sensor):
    def __init__(self, device='/dev/ttyACM0', baud=9600):
        self.arduino = serial.Serial(device, baud)

    def get_data(self):
        data = None
        try:
            # TODO: Improve this: read the last measure sent.
            data = int(self.arduino.readline())
        except:
            pass
        return data


class TestSensor(Sensor):
    """
    Returns the sequence of values from min to max, until max is reached. Then
    the inverse sequence is returned. Finally, it starts again.

    """
    def __init__(self, min_val=0, max_val=200):
        self.min_val = min_val
        self.max_val = max_val
        self.current = min_val
        self.step = 1

    def get_data(self):
        if self.current == self.min_val:
            self.step = 1
        elif self.current == self.max_val:
            self.step = -1

        self.current += self.step

        return self.current
