#Oefening 07

days = int(input("Geef aantal dagen "))*60*60*24
uren = int(input("Geef aantal uren "))*60*60
minuten = int(input("Geef aantal minuten"))*60
seconds = int(input("Geef aantal seconden in:"))

time = days + uren + minuten + seconds

print("Aantal seconden: {0}".format(time))