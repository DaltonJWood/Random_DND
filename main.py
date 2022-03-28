# Main Script for "DNDAdv" by DW

import random
import tkinter
from tkinter import *


m = tkinter.Tk()

# Picking randomly from predetermined list.
fname = [line.strip() for line in open('lists/fname.txt')]
lname = [line.strip() for line in open('lists/lname.txt')]
cl = [line.strip() for line in open('lists/Classes.txt')]
races = [line.strip() for line in open('lists/races.txt')]
rancl = [line.strip() for line in open('lists/num.txt')]
rancl2 = [line.strip() for line in open('lists/num.txt')]

m.title('Test Two')

# Defining class and race for bonus generation
Clss = random.choice(cl)
Race = random.choice(races)
rnum1 = random.choice(rancl)
rnum2 = random.choice(rancl2)


# Generating stats
num1 = random.randint(1, 20)
num2 = random.randint(1, 20)
num3 = random.randint(1, 20)
num4 = random.randint(1, 20)
num5 = random.randint(1, 20)
num6 = random.randint(1, 20)

# Sanity Check
print(Race)
print(Clss)
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print(num6)
print(rnum1)
print(rnum2)


# Adding Race Bonuses
# num1 = Strength
# num2 = Dexterity
# num3 = Constitution
# num4 = Intelligence
# num5 = Wisdom
# num6 = Charisma

if Race == 'Dragonborn':
    num1 = num1 + 2
    num6 = num6 + 1
if Race == 'Dwarf':
    num3 = num3 + 2
if Race == 'Elf':
    num2 = num2 + 2
if Race == 'Gnome':
    num4 = num4 + 2
if Race == 'Half-Elf':
    num6 = num6 + 2
if Race == 'Halfling':
    num2 = num2 + 2
if Race == 'Half-Orc':
    num1 = num1 + 2
    num3 = num3 + 1
if Race == 'Human':
    num1 = num1 + 1
    num2 = num2 + 1
    num3 = num3 + 1
    num4 = num4 + 1
    num5 = num5 + 1
    num6 = num6 + 1
if Race == 'Tiefling':
    num6 = num6 + 2
    num4 = num4 + 1

# Generating bonuses
if num1 == 1:
    bnum1 = '-5'
if num1 == 2 or num1 == 3:
    bnum1 = '-4'
if num1 == 4 or num1 == 5:
    bnum1 = '-3'
if num1 == 6 or num1 == 7:
    bnum1 = '-2'
if num1 == 8 or num1 == 9:
    bnum1 = '-1'
if num1 == 10 or num1 == 11:
    bnum1 = '+0'
if num1 == 12 or num1 == 13:
    bnum1 = '+1'
if num1 == 14 or num1 == 15:
    bnum1 = '+2'
if num1 == 16 or num1 == 17:
    bnum1 = '+3'
if num1 == 18 or num1 == 19:
    bnum1 = '+4'
if num1 == 20:
    bnum1 = '+5'

if num2 == 1:
    bnum2 = '-5'
if num2 == 2 or num2 == 3:
    bnum2 = '-4'
if num2 == 4 or num2 == 5:
    bnum2 = '-3'
if num2 == 6 or num2 == 7:
    bnum2 = '-2'
if num2 == 8 or num2 == 9:
    bnum2 = '-1'
if num2 == 10 or num2 == 11:
    bnum2 = '+0'
if num2 == 12 or num2 == 13:
    bnum2 = '+1'
if num2 == 14 or num2 == 15:
    bnum2 = '+2'
if num2 == 16 or num2 == 17:
    bnum2 = '+3'
if num2 == 18 or num2 == 19:
    bnum2 = '+4'
if num2 == 20:
    bnum2 = '+5'

if num3 == 1:
    bonus3 = '-5'
if num3 == 2 or num3 == 3:
    bonus3 = '-4'
if num3 == 4 or num3 == 5:
    bonus3 = '-3'
if num3 == 6 or num3 == 7:
    bonus3 = '-2'
if num3 == 8 or num3 == 9:
    bonus3 = '-1'
if num3 == 10 or num3 == 11:
    bonus3 = '+0'
if num3 == 12 or num3 == 13:
    bonus3 = '+1'
if num3 == 14 or num3 == 15:
    bonus3 = '+2'
if num3 == 16 or num3 == 17:
    bonus3 = '+3'
if num3 == 18 or num3 == 19:
    bonus3 = '+4'
if num3 == 20:
    bonus3 = '+5'

if num4 == 1:
    bonus4 = '-5'
if num4 == 2 or num4 == 3:
    bonus4 = '-4'
if num4 == 4 or num4 == 5:
    bonus4 = '-3'
if num4 == 6 or num4 == 7:
    bonus4 = '-2'
if num4 == 8 or num4 == 9:
    bonus4 = '-1'
if num4 == 10 or num4 == 11:
    bonus4 = '+0'
if num4 == 12 or num4 == 13:
    bonus4 = '+1'
if num4 == 14 or num4 == 15:
    bonus4 = '+2'
if num4 == 16 or num4 == 17:
    bonus4 = '+3'
if num4 == 18 or num4 == 19:
    bonus4 = '+4'
if num4 == 20:
    bonus4 = '+5'

if num5 == 1:
    bonus5 = '-5'
if num5 == 2 or num5 == 3:
    bonus5 = '-4'
if num5 == 4 or num5 == 5:
    bonus5 = '-3'
if num5 == 6 or num5 == 7:
    bonus5 = '-2'
if num5 == 8 or num5 == 9:
    bonus5 = '-1'
if num5 == 10 or num5 == 11:
    bonus5 = '+0'
if num5 == 12 or num5 == 13:
    bonus5 = '+1'
if num5 == 14 or num5 == 15:
    bonus5 = '+2'
if num5 == 16 or num5 == 17:
    bonus5 = '+3'
if num5 == 18 or num5 == 19:
    bonus5 = '+4'
if num5 == 20:
    bonus5 = '+5'

if num6 == 1:
    bonus6 = '-5'
if num6 == 2 or num6 == 3:
    bonus6 = '-4'
if num6 == 4 or num6 == 5:
    bonus6 = '-3'
if num6 == 6 or num6 == 7:
    bonus6 = '-2'
if num6 == 8 or num6 == 9:
    bonus6 = '-1'
if num6 == 10 or num6 == 11:
    bonus6 = '+0'
if num6 == 12 or num6 == 13:
    bonus6 = '+1'
if num6 == 14 or num6 == 15:
    bonus6 = '+2'
if num6 == 16 or num6 == 17:
    bonus6 = '+3'
if num6 == 18 or num6 == 19:
    bonus6 = '+4'
if num6 == 20:
    bonus6 = '+5'

# Gui elements

Label(m, text='Now Showing Random DND Stats!').grid(row=0, column=1)

Label(m, text=random.choice(fname)).grid(row=1, column=0)
Label(m, text=random.choice(lname)).grid(row=1, column=1)

Label(m, text='Strength').grid(row=2,column=0)
Label(m, text=num1).grid(row=2, column=1)
Label(m, text=bnum1).grid(row=2, column=2)

Label(m, text='Dexterity').grid(row=3,column=0)
Label(m, text=num2).grid(row=3, column=1)
Label(m, text=bnum2).grid(row=3, column=2)

Label(m, text='Constitution').grid(row=4,column=0)
Label(m, text=num3).grid(row=4, column=1)
Label(m, text=bonus3).grid(row=4, column=2)

Label(m, text='Intelligence').grid(row=5,column=0)
Label(m, text=num4).grid(row=5, column=1)
Label(m, text=bonus4).grid(row=5, column=2)

Label(m, text='Wisdom').grid(row=6,column=0)
Label(m, text=num5).grid(row=6, column=1)
Label(m, text=bonus5).grid(row=6, column=2)


Label(m, text='Charisma').grid(row=7,column=0)
Label(m, text=num6).grid(row=7, column=1)
Label(m, text=bonus6).grid(row=7, column=2)

Label(m, text='Race').grid(row=8, column=0)
Label(m, text=Race).grid(row=8, column=1)

Label(m, text='Class').grid(row=9, column=0)
Label(m, text=Clss).grid(row=9, column=1)

mainloop()