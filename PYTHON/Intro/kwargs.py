# key word arguemnts (kwargs are just a dictionary)

#testing kwargs

#list of kwargs
def myKwargs(**kwargs):
    print("Kwargs is ", type(kwargs))
    print(kwargs)
    #print("B is ", type(kwargs))

#Scenario a=23,b=30 =? {a:23,b:30}
myKwargs(a=23,b=30)

#scenario bno 3
# name="Samson" email="samson@gmail.com"
#myKwargs({"name":"Samson"})
myKwargs(name="Samson",email="sam@sam.com",dict={"a":"a"})


def area_rectangle(length,width):
    area=length*width
    print(f"For rectangle with length {length} and width {width} area is {area}")

#option 1 you calll it directly wiht args
area_rectangle(5,2) #with args the order matters
width=4
length=39
area_rectangle(width,length) #args
area_rectangle(width=width, length=length) #kwargs

#option 2 you call it with kwargs: <>
area_rectangle(width=10, length=55) #with kwargs, order doesnt matter
#you must match the parameter with arguements
area_rectangle(width=10, length=55)