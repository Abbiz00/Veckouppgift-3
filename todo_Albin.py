import numpy as np
array_1 = np.array ([])
array_2 = np.array ([])

# funktion skriv ut lista
def print_list(array):
    if len(array) == 0:
        print("listan är tom")
        return
    for i, task in enumerate(array, start=1):
        print(f"{i}. {task}")

def add_item(input_array, task):
    array_add = np.append(input_array, task)
    print(f"Ok, lade till {task} i listan")
    return array_add

def delete(array):
    if len(array) == 0:
        print("listan är tom")
        return array

    print_list(array)
    delete_items =input("Vilken uppgift är du klar med? Ange nummer:")

    try:
        index =int(delete_items) -1
        if 0 <= index < len(array):
            print(f"{array[index]} är klar")
            array = np.delete(array, index)
            return array
        else:
            print("fel")
    except ValueError:
        print("error")
    return array


def move_ready(array_1, array_2):
    if len(array_1) == 0:
        print("listan är tom")
        return array_1, array_2

    print_list(array_1)
    move_items =input("Vilken uppgift vill du flytta? Ange nummer:")

    try:
        index = int(move_items) -1
        if 0 <= index < len(array_1):
            task = array_1[index]
            array_2 = np.append(array_2, task)
            array_1 = np.delete(array_1, index)
            print(f"{task} flyttad till klar")

        else:
            print(" Ogiltigt nummer")
    except ValueError:
        print(" Ange ett tal")
    return array_1, array_2

def move_not_ready(array_1, array_2):
    if len(array_2) == 0:
        print("Klarlistan är tom")
        return array_1, array_2

    print("\nKlara uppgifter:")
    print_list(array_2)
    move_items = input("Vilken uppgift vill du flytta tillbaka? Ange nummer: ")

    try:
        index = int(move_items) - 1
        if 0 <= index < len(array_2):
            task = array_2[index]
            array_1 = np.append(array_1, task)
            array_2 = np.delete(array_2, index)
            print(f"  '{task}' flyttad tillbaka till arbetslistan!")
        else:
            print("Ogiltigt nummer")
    except ValueError:
        print(" Ange ett tal")
    return array_1, array_2




while True:
    print("\n1. Lista arbetsuppgifter")
    print("2. Lägg till arbetsuppgifter")
    print("3. Ta bort")
    print("4  Flytta till klarlista")
    print("5  Flytta tillbaka från klarlista")
    print("6. Avsluta")
    print("\n")
    menu=input("välj ett alternativ")


    if menu  == "6":
        break

    elif  menu == "1":
        print_list(array_1)

    elif menu == "2":
        task_input = input("Skriv in en arbetsuppgift: ")
        array_1 = add_item(array_1, task_input)

    elif menu == "3":
        array_1 = delete(array_1)

    elif menu == "4":
        print("meny 4")
        array_1, array_2 = move_ready(array_1, array_2)

    elif menu == "5":
        print("meny5")
        array_1, array_2 = move_not_ready(array_1, array_2)

    else:
        print("Försök igen")