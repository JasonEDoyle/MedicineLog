#!/usr/bin/python3

# medicine.py
#
# Jason Doyle
# Feb. 2015
#
# A program for keeping track of when medicine is taken and it should be taken

import time

def add_medication(medication):
    med = input("Enter medication: ")
    orders = input("Enter orders: ")
    required = input("Is the medication required? ")
    qty = input("Enter Perscription Qty: ")

    medication.append([med, orders, required, qty])
#    print(medication)
    string = "\n".join("\t".join(map(str,l)) for l in medication) # Convert list to string
    with open("Medication.txt", "wt") as out_file:
        out_file.write(string)

def take_medication(medication):
    for i in medication:
        print(str(medication.index(i)+1) + ": " + str(i[0]))
    med = int(input("Selection: "))

    print(str(medication[med-1][0]) + ' was taken at ' + str(time.ctime()))

    with open("Medication.log", "a") as out_file:
        out_file.write(str(medication[med-1][0]) + ' ' + str(time.time()) + '\n')

def check_medication():
    pass

def refill_medication():
    pass


if __name__ == '__main__':

    with open("Medication.txt", "a+") as in_file:
        in_file.seek(0)
        text = in_file.read()
        medication = [x.split('\t') for x in text.split('\n')]
    print(medication)
    
    choice = 0

    while choice != 5:
        print("1) Add medication")
        print("2) Take medication")
        print("3) Check medications")
        print("4) Refill medication")
        print("5) Exit")
        choice = int(input("Selection: "))

        if choice == 1:
            add_medication(medication)

        elif choice == 2:
            take_medication(medication)

        elif choice == 3:
            check_medication()

        elif choice == 4:
            refill_medication()

        elif choice == 5:
            print("Exiting.")

        else:
            print('\nInvaild selection. \n')
