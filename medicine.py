#!/usr/bin/python3

# medicine.py
#
# Jason Doyle
# Feb. 2015
#
# A program for keeping track of when medicine is taken and it should be taken

import time

def add_medication():
    input("Enter medication: ")
    input("Enter orders: ")
    input("Is the medication required? ")
    input("Enter Perscription Qty: ")

def take_medication():
    pass

def check_medication():
    pass

x = 0

while x != 4: 
    print("1) Add medication")
    print("2) Take medication")
    print("3) Check medications")
    print("4) Exit")
    x = int(input("Selection: "))

    if x == 1:
        add_medication()

    elif x == 2:
        take_medication()

    elif x == 3:
        check_medication()

    elif x== 4:
        break

    else:
        print('\nInvaild selection. \n')
