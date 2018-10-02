#oefening 08

time = int(input("Geef het aantal seconden in: "))

days = time/ (60*60*24)
time = time % (60*60*24)

hours = time/3600
time = time%(60*60)

minutes = time/60
seconds = time % 60

print("d:h:m:s ==> {0}:{1}:{2}:{3}".format(int(days),int(hours),int(minutes),int(seconds)))


