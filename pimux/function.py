from . import scrip as t

class misc():
    '''
    The class misc has miscellaneous methods 
    of termuxa-pi available.
    Available methods are :
    battery,
    brightness,
    vibrate,
    contactlist,
    torch,
    downloadFile
    '''
    def __init__(self):
        pass
      
    def battery(self):
        '''
        This method return battery status info.
        '''
        self.batteryvalue=t.compute("termux-battery-status")
        return self.batteryvalue["output"]
        

    def brightness(self,Brightness):
        '''
        Set the brightness of your device.
        It takes argument Brightness (int)
        from 0 to 100.
        '''
        self.Brightness=Brightness
        self.brightvalue=t.compute(f"termux-brightness {self.Brightness}")
        return self.brightvalue["output"]

    def vibrate(self,duration=1000):
        '''
        vibrates your phone.
        Default duration is 1000ms.
        '''
        self.duration=duration
        self.vibratevalue=t.compute(f"termux-vibrate -d {self.duration}")
        return self.vibratevalue["output"]


    def contactlist(self):
        '''
        Dumps all contact avalable on the phone.
        '''
        self.cvalue=t.compute("termux-contact-list")
        return self.cvalue["output"]


    def torch(self,switch=False):
        '''
        Toggles the torch on/off
        Takes argument as:
        True: turn on
        False: turn off
        '''
        self.switch=switch
        if self.switch == False:
            self.torchvalue=t.compute("termux-torch off")
            return self.torchvalue["output"]
        else:
            self.torchvalue=t.compute("termux-torch on")
            return self.torchvalue["output"]


    def downloadFile(self,description="From termux",title="Download",url=" "):
        '''
        This is the method for downloading anything 
        from the internet.
        The arguments to be supplied are:
        - description
        - title
        - url
        '''
        self.description=description
        self.title=title
        self.url=url
        self.downloadF=t.compute(f"termux-download -t {self.title} {self.url}")
        return self.downloadF["output"]




class tts():
    '''
    This class is for getting tts-engine
    info and for tts support.
    There are two methods available:
    ttsinfo
    and
    tts_speak
    '''

    def __init__(self):

        pass

    def ttsinfo(self):
        '''
        Gets tts-engines info as an output.
        '''
        self.ttsvalue=t.compute("termux-tts-engines")
        return self.ttsvalue["output"]


    def tts_speak(self,
            eng="com.google.android.tts",
            lang="eng",
            regn="",
            varient="",
            pitch=1.0,
            rate=1.0,
            stream="",
            text="Hello from termux"):
        '''
        This is a tts-engine api for conversion of text into speech.
        It has arguments:
            eng: engine
            lang: language
            pitch: pitch
            rate: ratei
            text: text to speak
            #for now this feature isn't set
            regn: region            
            varient: varient 
            stream: stream 
        for more info visit [termux wiki](https://wiki.termux.com/wiki/Termux-tts-speak)
        '''
        
        self.eng=eng
        self.lang=lang
        self.regn=regn
        self.varient=varient
        self.pitch=pitch
        self.rate=rate
        self.stream=stream
        self.text=text
        
        self.tvalue=t.compute(f"termux-tts-speak -e {self.eng} -l {self.lang} -p {self.pitch} -r {self.rate} {self.text}")
        return self.tvalue["output"]

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





