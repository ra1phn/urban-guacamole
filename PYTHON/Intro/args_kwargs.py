#args are passed first the kwargs
#otherwise there will be an error

def args_kwargs(*args,**kwargs):  
    print("__________________")
    print("All args", args)
    print("All kwargs",  kwargs)
    print("__________________")

#Error
#args_kwargs (a=2, b=30, 45, 39)
args_kwargs(45, 39, a=2, b=30)