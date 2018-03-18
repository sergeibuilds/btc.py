import time
import string
from random import randint
import random
import fourletterphat as flp
import urllib2
import json

# String of numbers for display to cycle while loading. Can be any letters/numb$
numbers = "1234567890"

while True:

  # End time - number at end (5) is seconds for loading screen (random numbers)$
  t_end = time.time() + 5

  while time.time() < t_end:
    flp.clear()
    flp.set_digit(0, random.choice(numbers))
    flp.set_digit(1, random.choice(numbers))
    flp.set_digit(2, random.choice(numbers))
    flp.set_digit(3, random.choice(numbers))
    flp.show()
    # Sleep for 0.05 seconds before choosing more random numbers
    time.sleep(0.05)
 
 # A bit of fun text before displaying the price
  flp.clear()
  flp.print_str("WAIT")
  flp.show()
  time.sleep(0.5)

  flp.clear()
  flp.print_str("FOR ")
  flp.show()
  time.sleep(0.5)

  flp.clear()
  flp.print_str("IT  ")
  flp.show()
  time.sleep(0.5)


  flp.clear()
  data = urllib2.urlopen("https://www.bitstamp.net/api/ticker").read()
  dataJSON = json.loads(data)

  price = dataJSON["last"]
  # Convert full number to XX.Xk




  print(price)
 # Decides where to place decimal, or if to use at all
  if float(price) > 99 and float(price) < 1000:
    flp.set_digit(1, price[1])
    flp.set_digit(2, price[2])
    flp.set_digit(3, price[3])
    flp.set_decimal(2, True)
  elif float(price) > 999 and float(price) <10000:
    # If you prefer 9999 instead of 9,9K
    flp.set_digit(0, price[0])
    flp.set_digit(1, price[1])
    flp.set_digit(2, price[2])
    flp.set_digit(3, price[3])

    # If you prefer 9,9K instead of 9999
    #flp.set_digit(1, price[0])
    #flp.set_digit(2, price[1])
    #flp.set_decimal(1, True)
    #flp.set_digit(3, "K")

  elif float(price) > 9999 and float(price) < 100000:
    flp.set_digit(0, price[0])
    flp.set_digit(1, price[1])
    flp.set_digit(2, price[2])
    flp.set_digit(3, "K")
    flp.set_decimal(1, True)
  elif float(price) > 99999 and float(price) < 1000000:
    flp.set_digit(0, price[0])
    flp.set_digit(1, price[1])
    flp.set_digit(2, price[2])
    flp.set_digit(3, "K")
  flp.show()
  # Sleep for 5 seconds, then refresh it all
  time.sleep(5)
