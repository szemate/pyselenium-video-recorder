pyselenium-video-recorder
=========================

A solution for Selenium Python bindings to record video of a test run through
repeated screenshot captures. Tested with Firefox and PhantomJS.

Dependencies
------------

gstreamer 1, gst-python, gst-plugins-base, gst-plugins-good

Installation
------------
```
python setup.py install --user
```
or
```bash
sudo apt install libcairo2-dev python3-dev pkg-config libxt-dev libgirepository1.0-dev

pip install pycairo PyGObject
```

Usage
-----

See [example.py](example.py).

Limitations
-----------

I couldn't make it work with Chrome Driver. Seen a couple of segmentation
faults. Also note that video encoding is quite CPU-intensive.
