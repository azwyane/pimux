import subprocess


def compute(func):
    outvalue_tuple = subprocess.Popen(
            func,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,shell=True)
    output,err=outvalue_tuple.communicate()
    output=output.decode("utf-8").replace("\n","")
    err=err.decode("utf-8")
    if err !="":
        return {"output":err}
    elif output=="":
        return {"output":"Done"} 
    else:
        return {"output":output} 


