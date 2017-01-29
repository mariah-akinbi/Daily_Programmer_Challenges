days_of_Xmas = ["first", "second", "third", "fourth", "fifth", "sixth",\
"seventh", "eight", "ninth", "tenth", "eleventh", "twelfth"]

gift_list = ["Partridge in a Pear Tree", "Turtle Doves", "French Hens",\
"Calling Birds", "GOLDENNNN RIIIIINGS", "Geese a Laying", "Swans a Swimming",\
"Maids a Milking", "Ladies Dancing" ,"Lords a Leaping", "Pipers Piping", \
"Drummers Drumming"]

alphabet_numbers = ["a", "two", "three", "four", "five", "six", "seven", \
"eight", "nine", "ten", "eleven", "twelve"]

def twelve_days_of_Christmas():
  day_count = 0

  for day in days_of_Xmas:
    print ("\n" + "On the " + day +  " of Christmas" + "\n" + "my true love sent to me: ")
    gift_counter = day_count #resets gift_counter to day_count after the while loop

    while gift_counter > 0: #decrements through the list
        print (alphabet_numbers[gift_counter], gift_list[gift_counter])
        gift_counter -= 1
    if gift_counter == 0 and day_count == 0:
        print (alphabet_numbers[gift_counter], gift_list[gift_counter])
    elif gift_counter == 0:
        print ("and", alphabet_numbers[gift_counter], gift_list[gift_counter])
        day_count += 1
        continue
    day_count += 1

convo = input("Hiyah! Would you like to sing a song? Y/N:")
if convo == 'N' or convo == 'n':
  print ("Boo you! Maybe next time...")
elif convo == 'Y' or convo == 'y':
  convo = input("Ok, would you like to sing The 12 Days of Christmas? Y/N: ")
  if convo=='Y' or convo == 'y':
    print ("Sweet! Here we go...")
    twelve_days_of_Christmas()
  else:
    print ("Boo! That's all I got! Maybe next time..")
else:
  print ("hmmmm.. I didn't quite catch that.. let's sing The 12 Days of Christmas! Here are the lyrics!")
  twelve_days_of_Christmas()
