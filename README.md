# Fractalis-AR

## An augmented reality experiment with fractals.

This is the code for the Fractalis-AR project. Read about it [here](http://cmdelatorre.github.io/fractalisar/)

## Requirements

  * [OpenCV 3.0](http://opencv.org/)
  * [Numpy](http://www.numpy.org/)
  * A set of images. For example [these](https://mega.nz/#F!aAME2TgC!-yJrr7o-PNV7ljeSyIYoNg).

## Running

To run the script make sure you have a camera connected (It is easy to modify the `main.py` script to accept the video data from a file, but I didn't do it yet). Review and update the `settings.py` file (show images? save results? what images to use?, etc.) 

```
$ python2.7 main.py
```

If you don't have an Arduino sending data you may want to develop a custom Sensor (no big deal, see `sensors.py`).

## Where's the tutorial/blog post?

I hope I'll have enough time to generalize and parametrize this code further. Also, I hope I'll have time to write a nice and neat blog post about the inner workings and details of this code... Meanwhile, contact me in cmdelatorre at gmail dot com if you need help using this.
