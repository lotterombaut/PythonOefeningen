#oef04

invoer = int(input("Geef de leeftijd van uw hond in: "))

if(invoer < 0):
    print("Dit is onmogelijk.")
elif(invoer == 1):
    print("UW hond is 14 mensenjaren.")
elif(invoer == 2):
    print("Uw hond is 22 mensenjaren. ")
else:
    result = "Uw hond is {0} mensenjaren.".format((22 + (invoer - 2) * 5))
    print(result)