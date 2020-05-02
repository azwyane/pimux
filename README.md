# pimux

[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://github.com/azwyane/pymux.git)

> PIMUX is here, made with :heart:

## What is pimux?
> pimux is a python module created by me, to access the termux-api(hardware
> and software api). To ease the access of these beautiful api's which 
> can be really useful for IOT projects deploying using your own android phone.

## Why to use pimux?
> For every pythonist and enthusiast pimux can really ease hardware and software
> access through termux-api.

## Special thanks 
 I would like to thank every developer before me who made this beautiful
 language(python),termux-api, termux, os(linux), and all others, on whose
 contributions I have been able to make this.

> This project is originally located at [pimux](https://github.com/azwyane/pimux)

## Table of Contents
- [Requirements](#Requirements)
- [Installation](#Installation)
- [Features](#Features)
- [Contributing](#Contributing)

## Requirements

- Termux app
- Termux-api (both app and package)
- Python

## Installation

🚀&nbsp; To install in your local machine follow the steps below:

### Method-1

You can always get the latest version of pimux maintained here in the github.
> To get the latest feature:
- Clone this repo to your local machine(termux) using `https://github.com/azwyane/pimux.git`

Goto to your terminal and type:

```sh
git clone https://github.com/azwyane/pimux.git
```

Now add this to site packages by first building by being where the setup.py is:
```
$ python3 setup.py sdist bdist_wheel

$ python3 -m pip install -e <path to pimux main dir>
```

Finally, you have it installed.

### Method-2

**Install by pip**
> The stable version is available in the Pypi, which you can download by:

```
$ python3 -m pip install pimux
```

## Run the project

> Now to run the pimux type in your terminal:

```bash
$ python
>>> from pimux import function

>>>help(function)
CLASSES
    builtins.object
        camera
        clipboard
        misc
        tts
        volume
        wifi

    class camera(builtins.object)
     |  The class camera is for fetching
     |  camera info or taking picture with the
     |  camera on the android.
     |
     |  Methods defined here:
     |
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  camera(self)
     |      This method returns camera info
     |      of the android device.It takes no argument.
     |
     |  takephoto(self, cid=0, saveas='newimg.jpeg')
     |      This method is for taking picture from the
     |      available camera on the device.
     |      It takes two argument:
     |      cid : camera id in int default(0)
     |      saveas: output file name in str format default("newimg.jpeg")
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:

```

```bash
>>> v=function.misc()

>>>help(v)
class misc(builtins.object)
 |  The class misc has miscellaneous methods
 |  of termuxa-pi available.
 |  Available methods are :
 |  battery,
 |  brightness,
 |  vibrate,
 |  contactlist,
 |  torch,
 |  downloadFile
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  battery(self)
 |      This method return battery status info.
 |
 |  brightness(self, Brightness)
 |      Set the brightness of your device.

>>>v.vibrate()    This command vibrates your device if not in silent.
'Done'

>>>v.brightness(Brightness=100) This command sets the brightness to 100.
'Done'
```
**Also**

```bash
$ python
>>>from pimux import Sensors

 >>>help(Sensors)
 CLASSES
    builtins.object
        sensor

    class sensor(builtins.object)
     |  This is a class that lets to view
     |  sensor data directly from your android device.
     |
     |  Methods defined here:
     |
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  allsensors(self)
     |      Method to print sensor data all at once.
     |      WARNING: Can cause over load to the device.
     |
     |  cleanup(self)
      Performs cleanup releasing sensor resources.
     |
     |  delay(self, sensorname='', delayvalue=3000)
     |      Method to delay time in milliseconds
     |      on receiving every new sensor update.
     |      Arguments:
     |      sensorname=""
     |      delayvalue=3000(default)(delayed by 3 sec)
     |
     |  listSensor(self)
     |      lists available sensors on the device.
```

```bash
>>> s=Sensors.sensor()
>>>help(s)
class sensor(builtins.object)
 |  This is a class that lets to view
 |  sensor data directly from your android device.
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  allsensors(self)
 |      Method to print sensor data all at once.
 |      WARNING: Can cause over load to the device.
 |
 |  cleanup(self)
 |      Performs cleanup releasing sensor resources.
 |
 |  delay(self, sensorname='', delayvalue=3000)
 |      Method to delay time in milliseconds
 |      on receiving every new sensor update.
 |      Arguments:
 |      sensorname=""


>>>s.listSensor()
'{  "sensors": [ ........]}'
```

## Features

> It is a side project of making use of android sensors and IOT projects. 
> It has the feature of termux-api which can be easily used with
> python projects.

---

## Contributing

### Step 1

- Option 1
    - 🍴 Fork this repo!

- Option 2
    - 👯 Clone this repo to your local machine using `https://github.com/azwyane/pimux.git`

### Step 2

- HACK AWAY!

### Step 3

- 🔃 Create a new pull request using <a href="https://github.com/azwyane/pymux/compare" target="_blank">`https://github.com/azwyane/pimux/compare`</a>.


---

###  Found a bug? Missing a specific feature?

Feel free to **file a new issue** with a respective title and description on the the [azwyane/pimux](https://github.com/azwyane/pymux/issues) repository. If you already found a solution to your problem, **I would love to review your pull request**!

