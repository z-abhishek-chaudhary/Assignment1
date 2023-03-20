import os
import time

class Main:

    def __init__(self):
        self.math = 30
        self.reserveMath = int(self.math*0.1)
        self.math -= int(self.reserveMath)
        self.biology = 30
        self.reserveBiology = int(self.biology*0.1)
        self.biology -= int(self.reserveBiology)
        self.commerce = 0
        self.reserveCommerce = int(self.commerce*0.1)
        self.commerce -= int(self.reserveCommerce)

        self.studentData = []

    
    def register(self):
        os.system('clear')
        list = []
        print("------------------------------")
        print("-> Please Enter the Details: ")
        print("------------------------------\n")
        name = input("\n\nEnter your name: ")
        list.append(name)

        age = int(input("\nEnter your age: "))
        list.append(age)

        gender = input("\nEnter your gender: [M/F] ").upper()
        while gender not in ("M","F"):
            print("\n-----> Invalid response, Please try again <-----")
            time.sleep(2)
            gender = input("\nEnter your gender: [M/F] ").upper()

        if gender == 'M':
            gender = 'Male'
        else: gender = 'Female'
        list.append(gender)



        differentlyAbled = input("\nAre you Differently Abled: [T/F] ").upper()
        if differentlyAbled not in ("T","F"):
            print("\n-----> Invalid response, Please try again <-----")
            time.sleep(2)
            differentlyAbled = input("\nAre you Differently Abled: [T/F] ").upper()


        if differentlyAbled == 'T':
            differentlyAbled = True
            list.append("Differently Abled")
        else: 
            differentlyAbled = False
            list.append("Not Differently Abled")



        genralAvailable = True
        specialAvailable = True
        available = True
        print("\n\nPlease select your preferred stream from the following:-")
        course = int(input("\nMaths [Enter 1]\nBiology [Enter 2]\nCommerce [Enter 3]\n\nYour Response: " ))
        while course not in [1,2,3]:
            print("\n-----> Invalid response, Please try again <-----")
            time.sleep(2)
            course = int(input("\nMaths [Enter 1]\nBiology [Enter 2]\nCommerce [Enter 3]\n\nYour Response: " ))

        if course == 1:
            if self.math == 0:
                genralAvailable = False
            if self.reserveMath == 0:
                specialAvailable = False

            if differentlyAbled and specialAvailable:
                self.reserveMath -= 1
            elif differentlyAbled and specialAvailable == False and genralAvailable:
                self.math -= 1
            elif differentlyAbled and not genralAvailable and not specialAvailable:
                available = False
            elif not differentlyAbled and genralAvailable:
                self.math -= 1
            elif not differentlyAbled and not genralAvailable:
                available = False
            course = 'Maths'

            

        elif course == 2:
            if self.biology == 0:
                genralAvailable = False
            if self.reserveBiology == 0:
                specialAvailable = False

            if differentlyAbled and specialAvailable:
                self.reserveBiology -= 1
            elif differentlyAbled and specialAvailable == False and genralAvailable:
                self.biology -= 1
            elif differentlyAbled and not genralAvailable and not specialAvailable:
                available = False
            elif not differentlyAbled and genralAvailable:
                self.biology -= 1
            elif not differentlyAbled and not genralAvailable:
                available = False
            course = 'Biology'



        elif course == 3:
            if self.commerce == 0:
                genralAvailable = False
            if self.reserveCommerce == 0:
                specialAvailable = False

            if differentlyAbled and specialAvailable:
                self.reserveCommerce -= 1
            elif differentlyAbled and specialAvailable == False and genralAvailable:
                self.commerce -= 1
            elif differentlyAbled and not genralAvailable and not specialAvailable:
                available = False
            elif not differentlyAbled and genralAvailable:
                self.commerce -= 1
            elif not differentlyAbled and not genralAvailable:
                available = False
            course = 'Commerce'

        else:
            print("Invaild Entry, Please Try Again")
            time.sleep(2)
            self.register()
    
        list.append(course)
        

        if(available):
            print(f"\n\n********************* You are successfully registered. *********************\n")
        else:
            print(f"\n\n------ Seats are not available for your selected {course} course. ------")

        self.studentData.append(list)
        input("\nPress Enter to Exit ")
        self.mainMenu()


    def mainMenu(self):
        os.system('clear')
        print("------------------------------------------------------------------------------------")
        print("====================> WELCOME TO THE STUDENT ENROLLMENT SYSTEM <====================")
        print("------------------------------------------------------------------------------------\n\n")
        print ("Choose the operation to perform :- \n")
        print("-> New Registration [Enter 1]\n\n-> Student Information [Enter 2]\n\n-> Check Remaining Seats [Enter 3]\n")
        newEntry = int(input("Your Response: "))
        entry = (1,2,3)
        while (newEntry not in entry):
            os.system('clear')
            print("\n\n")
            print("----------> Please Enter the Valid Entry <---------- ")
            time.sleep(2)
            self.mainMenu()

        if newEntry == 1:
            self.register()
        if newEntry == 2:
            self.showData()
        if newEntry == 3:
            self.checkSeatCount()
    

    def showData(self):
        os.system('clear')
        if len(self.studentData)==0:
            input("Sorry, There is no registered student\n\nPress enter to exit\n")
            self.mainMenu()
        else:
            # fmt = '\t'.join('{{:{}}}'.format(x) for x in 20)
            # table = [fmt.format(*row) for row in self.studentData]
            # print ('\n'.join(table))

            for i in range (len(self.studentData)):
                print(self.studentData[i])

            # print(self.studentData)
            input("\nPress Enter to Exit: ")
            self.mainMenu()


    def checkSeatCount(self):
        os.system('clear')
        print("\n---------------------------")
        print(" The remaining seats are:")
        print("---------------------------\n\n")
        print(f"Maths              |   {self.math} seats")
        print(f"Reserved Maths     |   {self.reserveMath} seats")
        print(f"Biology            |   {self.biology} seats")
        print(f"Reserved Biology   |   {self.reserveBiology} seats")
        print(f"Commerce           |   {self.commerce} seats")
        print(f"Reserved Commerce: |   {self.reserveCommerce} seats\n\n")
        input("\nPress Enter to Exit: ")
        self.mainMenu()



class_instance = Main()
class_instance.mainMenu()

class Register:
    def register():
        os.system('clear')
        list = []
        print("------------------------------")
        print("-> Please Enter the Details: ")
        print("------------------------------\n")
        name = input("\n\nEnter your name: ")
        list.append(name)

        age = int(input("\nEnter your age: "))
        list.append(age)

        gender = input("\nEnter your gender: [M/F] ").upper()
        while gender not in ("M","F"):
            print("\n-----> Invalid response, Please try again <-----")
            time.sleep(2)
            gender = input("\nEnter your gender: [M/F] ").upper()

        if gender == 'M':
            gender = 'Male'
        else: gender = 'Female'
        list.append(gender)



        differentlyAbled = input("\nAre you Differently Abled: [T/F] ").upper()
        if differentlyAbled not in ("T","F"):
            print("\n-----> Invalid response, Please try again <-----")
            time.sleep(2)
            differentlyAbled = input("\nAre you Differently Abled: [T/F] ").upper()


        if differentlyAbled == 'T':
            differentlyAbled = True
            list.append("Differently Abled")
        else: 
            differentlyAbled = False
            list.append("Not Differently Abled")



        genralAvailable = True
        specialAvailable = True
        available = True
        print("\n\nPlease select your preferred stream from the following:-")
        course = int(input("\nMaths [Enter 1]\nBiology [Enter 2]\nCommerce [Enter 3]\n\nYour Response: " ))
        while course not in [1,2,3]:
            print("\n-----> Invalid response, Please try again <-----")
            time.sleep(2)
            course = int(input("\nMaths [Enter 1]\nBiology [Enter 2]\nCommerce [Enter 3]\n\nYour Response: " ))

        if course == 1:
            if Main.math == 0:
                genralAvailable = False
            if Main.reserveMath == 0:
                specialAvailable = False

            if differentlyAbled and specialAvailable:
                Main.reserveMath -= 1
            elif differentlyAbled and specialAvailable == False and genralAvailable:
                Main.math -= 1
            elif differentlyAbled and not genralAvailable and not specialAvailable:
                available = False
            elif not differentlyAbled and genralAvailable:
                Main.math -= 1
            elif not differentlyAbled and not genralAvailable:
                available = False
            course = 'Maths'

            

        elif course == 2:
            if Main.biology == 0:
                genralAvailable = False
            if Main.reserveBiology == 0:
                specialAvailable = False

            if differentlyAbled and specialAvailable:
                Main.reserveBiology -= 1
            elif differentlyAbled and specialAvailable == False and genralAvailable:
                Main.biology -= 1
            elif differentlyAbled and not genralAvailable and not specialAvailable:
                available = False
            elif not differentlyAbled and genralAvailable:
                Main.biology -= 1
            elif not differentlyAbled and not genralAvailable:
                available = False
            course = 'Biology'



        elif course == 3:
            if Main.commerce == 0:
                genralAvailable = False
            if Main.reserveCommerce == 0:
                specialAvailable = False

            if differentlyAbled and specialAvailable:
                Main.reserveCommerce -= 1
            elif differentlyAbled and specialAvailable == False and genralAvailable:
                Main.commerce -= 1
            elif differentlyAbled and not genralAvailable and not specialAvailable:
                available = False
            elif not differentlyAbled and genralAvailable:
                Main.commerce -= 1
            elif not differentlyAbled and not genralAvailable:
                available = False
            course = 'Commerce'

        else:
            print("Invaild Entry, Please Try Again")
            time.sleep(2)
            Main.register()
    
        list.append(course)
        

        if(available):
            print(f"\n\n********************* You are successfully registered. *********************\n")
        else:
            print(f"\n\n------ Seats are not available for your selected {course} course. ------")

        Main.studentData.append(list)
        input("\nPress Enter to Exit ")
        Main.mainMenu()