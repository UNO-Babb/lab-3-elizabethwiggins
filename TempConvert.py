#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.

  tempF=(input("Temperature Fahrenheit:"))

  tempC1 = (tempF-36)*5/9

  print(tempF, "is ", tempC1, "degrees celsius.")
if __name__ == '__main__':
  main()

