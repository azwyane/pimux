from compute import scrip as t


def battery():
    value=t.compute("termux-battery-status")
    return value["output"]
        

def brightness(bvalue):
    value=t.compute(f"termux-brightness {bvalue}")
    return value["output"]

class camera:
    '''
    The class camera is for fetching
    camera info or taking picture with the
    camera on the android.
    '''
    def __init__(self):
        pass

    def camera(self):
        '''
        This method returns camera info
        of the android device.It takes no argument.
        '''
        self.value=t.compute("termux-camera-info")
        return self.value["output"]
    def takephoto(self,cid=0,saveas="newimg.jpeg"):
        '''
        This method is for taking picture from the 
        available camera on the device.
        It takes two argument:
        cid : camera id in int default(0)
        saveas: output file name in str format default("newimg.jpeg")
        '''
        self.value=t.compute(f"termux-camera-photo -c {cid} {saveas}")
        return self.value["output"]



class clipboard:
    '''
    Clipboard on android stores copied value
    for short time until next copy.
    This class has two methods for 
    setting or getting the value from 
    clipboard.
    '''
    def __init__(self):
        pass
    def clipboardGet(self):
        '''
        The clipboardGet method returns
        value stored in the clipboard.
        '''
        self.value=t.compute("termux-clipboard-get")
        return self.value["output"]
    def clipboardSet(self,readval=" "):
        '''
        The clipboardSet method is to be used 
        when required to store value in the
        clipboard.
        BY DEFAULT if no argument given
        it sets empty value in the 
        clipboard.
        This method takes an argument of readval variable
        which is a string.
        '''
        self.readval=readval
        self.value=t.compute(f"termux-clipboard-set {self.readval}")
        return self.value["output"]


def sensor(val):
    if val=="all":
        value=t.compute("termux-sensor -a")
        return value["output"]
   
    elif val=="list":
        value=t.compute("termux-sensor -l")
        return value["output"]

       
    #elif val=="sensor"

class wifi:
    '''
    The class wifi has two methods:
    - toggle method switches wifi on or off
    - connectInfo method gets wifi connection
    info to stdout.
    '''
    def __init__(self):
        pass
    def toggle(self,switch=False):
        '''
        This method has switch as one argument
        whose default boolean value is false.
        supply True for true(turn on)
        and False for false(turn off)
        '''
        self.switch=switch
        if self.switch == False:
            self.value=t.compute("termux-wifi-enable false")
            return self.value["output"]
        else:
            self.value=t.compute("termux-wifi-enable true")
            return self.value["output"]


    def connectInfo(self):
        '''
        This method returns wifi connection
        information in stringified format.
        '''
        self.value=t.compute(f"termux-wifi-connectioninfo")
        return self.value["output"]


def contactlist():
    value=t.compute("termux-contact-list")
    return value["output"]


def torch(val="off"):
    value=t.compute(f"termux-torch {val}")
    return value["output"]

def tts_speak(eng="",
        lang="",
        regn="",
        varient="",
        pitch="",
        rate="",
        stream="",
        text="Hello from termux"):

    value=t.compute(f"termux-tts-speak {text}")
    return value["output"]


class volume:
    '''
    The class volume has two methods:
    - volumeInfo
    - volumeControl
    '''
    def __init__(self):
        pass
    def volumeInfo(self):
        '''
        This method returns 
        all volume info and takes no argument.
        '''
        self.value=t.compute(f"termux-volume")
        return self.value["output"]


    def volumeControl(self,stream="ring",volume=5):
        '''
        This method sets the volume of the 
        stream.
        It takes two arguments:
        - stream : in str format
        - volume : in int format
        '''
        self.value=t.compute(f"termux-volume {stream} {volume}")
        return self.value["output"]

def vibrate(duration=1000):
    '''
    vibrates your phone.
    Default duration is 1000ms.
    '''
    value=t.compute(f"termux-vibrate -d {duration}")
    return value["output"]



