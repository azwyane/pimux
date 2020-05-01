from compute import scrip as t

class sensor:
    '''
    This is a class that lets to view
    sensor data directly from your android device.
    '''
    def __init__(self):
        pass

    def sensor(val):
    if val=="all":
        value=t.compute("termux-sensor -a")
        return value["output"]
   
    elif val=="list":
        value=t.compute("termux-sensor -l")
        return value["output"]

       
    #elif val=="sensor00"
