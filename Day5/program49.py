try:
    print("I am try just started")
    print(10/2)
    print("I am try,I am done")
except ZeroDivisionError as zd:
    print(zd)
else:
    print("Hi I am else now alive because try is executed")
finally:
    print("Hello there I am finally,I am going to close")