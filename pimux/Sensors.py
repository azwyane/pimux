from . import scrip as t

class sensor:
    '''
    This is a class that lets to view
    sensor data directly from your android device.
    '''
    def __init__(self):
        pass

    def listSensor(self):
        '''
        lists available sensors on the device.
        '''
        self.value=t.compute("termux-sensor -l")
        return self.value["output"]

    def cleanup(self):
        '''
        Performs cleanup releasing sensor resources.
        '''
        self.clean=t.compute("termux-sensor -c")
        return self.clean["output"]

    def delay(self,sensorname="",delayvalue=3000):
        '''
        Method to delay time in milliseconds
        on receiving every new sensor update.
        Arguments:
        sensorname=""
        delayvalue=3000(default)(delayed by 3 sec)
        '''
        self.sensorname=sensorname
        self.delayvalue=delayvalue
        if self.sensorname=="":
            return "provide a list of sensor(s). Example:sensorname=[\"Gravity\",\"RMD\"]"
        elif len(self.sensorname) == 1:
            self.sensorname=self.sensorname[0]
            self.delayvalue=delayvalue
            self.delayv=t.liveSave(f"termux-sensor -s {self.sensorname} -d {self.delayvalue}")
        elif len(self.sensorname) > 1:
            self.delaycmd="termux-sensor -s "+str([x for x in self.sensorname]).replace("[","").replace("]","").replace(" ","")+f"-d {self.delayvalue}"
            self.disp=t.liveSave(self.delaycmd)


    def specificSensors(self,sname=""):
        '''
        This is a method to print specific 
        sensor(s) data.
        Argument is either a single sensor
        or multiple sensors but in a list.
        '''
        
        self.sname=sname
        if self.sname=="":
            return "provide a list of sensor(s). Example:sname=\"Gravity\""
            
        else:
            self.livecmd="termux-sensor -s "+str([x for x in self.sname]).replace("[","").replace("]","").replace(" ","")
            self.display=t.liveSave(self.livecmd)
            

    

    def allsensors(self):
        '''
        Method to print sensor data all at once.
        WARNING: Can cause over load to the device.
        '''
        self.show=t.liveSave("termux-sensor -a")


