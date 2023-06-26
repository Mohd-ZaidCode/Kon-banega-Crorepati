#import satatments
import random
import time
import click
import sys

#List of all the Questions, options and the right answer
Questions = [
  [
    "1.MS Dhoni ", "2.Baichng Butia", "3.Sunil Shetri ", "4.Milkha Singh",
    "Who is the top scorer in Indian National Football Team", 3, "Sunil Shetri"
  ],
  [
    "1.Methane ", "2.Carbon monoxide", "3.Nitrous oxide ",
    "4.Hydrogen Sulphide",
    "Which among the following gas usually causes explosions in coal mines", 1,
    "Methane"
  ],
  [
    "1.CPU ", "2.Memory", "3.Storage ", "4.Graphic Card",
    "Which of the following is the processing unit of the computer", 1, "CPU"
  ],
  [
    "1.Extra power ", "2.Exciting xamp", "3.Extended Platform ",
    "4.Experience", "In the Windows XP, what does XP stands for", 4,
    "Experience"
  ],
  [
    "1.India Gate ", "2.Laal kila", "3.Taj Mahal ", "4.Imaambaada",
    "Taj Hotel is front of which Indian historic place", 1, "India Gate"
  ],
  [
    "1.Narendra Modi ", "2.Indira Gandhi", "3.Pandit Nehru ",
    "4.manmohan Singh", "Who is the first Prime minister of India", 3,
    "Pandit Nehru"
  ],
  [
    "1.Maharastra ", "2.Delhi", "3.UP ", "4.Bihar",
    "What is the capital of India?", 2, "Delhi"
  ]
]

#defined non-local variables
bool = True
priceMoney = 0


#function for typing effect in output
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)


#Question methods
def checking_method(inpu):
  #defines variables
  global priceMoney, bool
  #Printing Question and all the options
  print(inpu[4])
  print(inpu[0], inpu[1])
  print(inpu[2], inpu[3])

  #Taking input from the user
  a = input("Enter your answer:")
  b = int(a)

  #Comparing answer and showing output
  if ((b == inpu[5]) or (a == inpu[6])):
    typingPrint(f"Computer ji {a}...... per tala lagaiye\n\n")
    time.sleep(2)
    typingPrint("AUR YHE SAHI UTTER... ADBHUTTT ADBHUUUTTT...\n\n")

    time.sleep(2)
    priceMoney += 20000

    typingPrint(f"Aur ab apka price money {priceMoney} ho gaya hai")
    time.sleep(3)
    click.clear()
    typingPrint("Aiye agle padhav pr badte hai\n\n\n")
#if answer is wrong
  else:
    typingPrint("Afsoos...yhe galat uttar hai...\n")
    time.sleep(2)
    typingPrint(
      f"Apka saafr yahi khatam hota hai...aur apne jeeta hai {priceMoney} ka Price Money\n\nKIYA KAREGI/KAREGE AP ITNI DHAN RASHI KA ??...\n"
    )
    bool = False
    time.sleep(3)
    click.clear()


#Staring of show
typingPrint(
  "Abhar abhinandn deviyo aur sjjano.. mai Amitab bachan aur suwagat hai apka is adbhut khel me jo hai....PUNCHKOTI MAHANANI KON BANEGA CROREPATI yani KBC\n\n"
)
typingPrint("\nTho chaliye suru karte hai yhe adbhut khel\n")

#Shuffle Question sequence
random.shuffle(Questions)


#calling function for Question answering
i = 0
while (bool):
  if (i <= 5):
    checking_method(Questions[i])

  elif (i == 6):
    checking_method(Questions[i])
    bool = False
    typingPrint("\nCongratulations!!!.... apne jeet liya hai 7 Crore..")
  i += 1

typingPrint(
  "\n Isi ke sath apse vida lete hai fir milege dubara is adbhut khel ke sath PUNCHKOTI MAHANANI KON BANEGA CROREPATI yani KBC "
)