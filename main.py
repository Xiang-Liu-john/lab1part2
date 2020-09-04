temperature = input("Enter temperature: ")
unit = input("Enter unit in F/f or C/c: ")
if unit == "F" or unit == "f":
  C = (float(temperature)-32)/1.8
  print(f"{temperature}° in Fahrenheit is equivalent to {C}° Celsius.")

elif unit == "C" or unit == "c":
  F = (float(temperature)*1.8)+32
  print(f"{temperature}° in Celsius is equivalent to {F}° Fahrenheit.")

else:
  print(f"Invalid unit({unit}).")
 