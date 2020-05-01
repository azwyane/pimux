from compute import scrip as t

class sensor:
    '''
    This is a class that lets to view
    sensor data directly from your android device.
    '''
    def __init__(self):
        pass

    def listSensor(self):
        self.value=t.compute("termux-sensor -l")
        return self.value["output"]

    def cleanup(self):
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
        self.delayv=t.compute(f"termux-sensor -s {self.sensorname} -d {self.delayvalue}")
 
        return self.delayv["output"]

    def specificSensors(self,sname=""):
        '''
        This is a method to print specific 
        sensor(s) data.
        Argument is either a single sensor
        of list of sensors.
        '''
        
        self.sname=sname
        if self.sname=="":
            self.display=t.compute(f"termux-sensor -s")
            return self.display["output"]
        else:
            command="termux-sensor -s "+str([x for x in self.sname]).replace("[","").replace("]","").strip()
            self.display=t.compute(command)
            return self.display["output"]

    

    def allsensors(self):
        '''
        Method to print sensor data all at once.
        WARNING: Can cause over load to the device.
        '''
        pass
