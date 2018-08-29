import os
import time

class arrayHandling:
    def __init__(self):
        self.array = []
        self.choice = ""
        self.total = 0

    def menu(self):
        while True:
            try:
                print("\n"*500)
                print("1. Load Numbers")
                print("2. Print the Array")
                print("3. Sum the Array")
                print("4. Maximum of Array")
                print("5. Minimum of Array")
                print("6. Quit")

                choice = int(input("\n ENTER OPTION HERE:>> "))
                if choice == 1:
                    self.Load()
                elif choice == 2:
                    self.Print()
                elif choice == 3:
                    self.Sum()
                elif choice == 4:
                    self.Maximum()
                elif choice == 5:
                    self.Minimum()
                elif choice == 6:
                    print("See you next time!")
                    os.system("pause")
                    quit()
            except ValueError:
                print("Please enter an integer")
                time.sleep(2)

    def Load(self):
        while True:
            try:
                print("\n"*500)
                print("Enter \"Menu\" below to return to the menu")
                print("or Enter an integer to be added to the Array")
                self.choice = input("ENTER AN INTEGER HERE:>>")
                if str(self.choice.lower()) == "menu":
                    break
                self.array.append(int(self.choice))
            except ValueError:
                print('\nPLEASE ENTER AN INTEGER')
                time.sleep(2)
    def Print(self):
        print("\n"*500)
        print(self.array)
        print("There are " + str(len(self.array)) + " values in the Array")
        os.system("pause")

    def Sum(self):
        print("\n"*500)
        for i in self.array:
            self.total += i
        print("The sum of numbers in the Array is " + str(self.total))
        self.total = 0
        print("There are " + str(len(self.array)) + " values in the Array")
        os.system("pause")

    def Maximum(self):
        print("\n"*500)
        print("Maximum value was called")
        os.system("pause")

    def Minimum(self):
        print("\n"*500)
        print("Minimum value was called")
        os.system("pause")

instance = arrayHandling()
instance.menu()
