# Fractalis-AR

## An augmented reality experiment with fractals.

This is the code for the Fractalis-AR project. Read about it [here](http://cmdelatorre.github.io/fractalisar/)

## Requirements

  * [OpenCV 3.0](http://opencv.org/)
  * [Numpy](http://www.numpy.org/)
  * What's listed in the requirements.txt file
  * A camera or a video file
  * A set of images. For example [these](https://mega.nz/#F!aAME2TgC!-yJrr7o-PNV7ljeSyIYoNg).

## Running

The program reads the input data either from a camera (default) or from an input video file. 

For a the full set of options, run:

```
$ python2.7 main.py -h
```

## Configuration

The configuration parameters are

  * provided `settings.ini` file, or
  * a different settings file can be given with the `-c` argument, or
  * they can be overwritten with command line arguments

## Sensors data

In the original project, we had an Arduino board sending distance data through the serial port.
But don't worry, in the highly probable case that you don't have such a working infrastructure, 
there's a very simple `TestSensor` class (that's used as default) and works just fine (see `sensors.py`).

## Where's the tutorial/blog post?

I hope I'll have enough time to generalize and parametrize this code further. Also, I hope I'll have time to write a nice and neat blog post about the inner workings and details of this code... Meanwhile, contact me in cmdelatorre at gmail dot com if you need help using this.
