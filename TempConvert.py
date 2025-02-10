#TempConvert.py
#Name: Alex Hernandez Lopez
#Date: 2/8/25
#Assignment: Lab 3


def main():
  #Prompt the user for a Fahrenheit temperature
  tempF = input("Enter a Temperature in Farenheit: ")
  tempF = float(tempF)
  #Convert that temperature to celsius, rounding to 1 decimal percision
  tempC = 5/9 * (tempF - 32)
  tempC = round(tempC, 1)
  #Output converted temperature.
  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
