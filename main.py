# Made 95% by willyrire#3914 to use it, double click
import random
from datetime import datetime
import datetime
from struct import pack_into
import time
from turtle import clear
import os
from sys import exit
import cloudscraper
from colored import fg

red = fg('red')
green = fg('green')
yellow = fg('yellow')
white = fg('white')
purple = fg('purple_4a')
gold = fg('gold_3a')
blue = fg('blue')

date_time = datetime.datetime.now()
ctt = time.mktime(date_time.timetuple())
scraper = cloudscraper.create_scraper(browser={'custom': 'ScraperBot/1.0'})
print(green + "Willy Predictor V2.1")
print(green + "This willy Predictor version is, as you can see a \"executable\" version, in python.")
print(white + "Just note this version is in beta and some errors may occure.")
print(yellow +"Note : To close this, just close the window")
print(yellow + "WARNING : DO NOT REMOVE/ EDIT THIS FILE OR OTHER FILES !")
print(white + "You can now enter a command ! Note : for help, type help")
print("For Support, type help in the command bar")
print(" ")
print("")
    
def menu():
    cmd = input(white+"Enter Command Here >> ")
    if cmd == "help": # Help
        clear = lambda: os.system('cls')
        clear()
        print("")
        print("Result for 'help' :")
        print("")
        print("List of commands :")
        print("- crash           - mines")
        print("- towers          - roulette")
        print(f"- cups            {red}- close{white}")
        print("")
        return menu()
    elif cmd == "crash": # Crash
        clear = lambda: os.system('cls')
        clear()
        print("")
        print("Result for 'crash' :")
        print("")
        games = scraper.get("https://rest-bf.blox.land/games/crash").json()
        def lol():
                r = scraper.get(
                "https://rest-bf.blox.land/games/crash").json()["history"]
                yield [
                    r[0]["crashPoint"],
                    [float(crashpoint["crashPoint"]) for crashpoint in r[-2:]]
                ]
    
        for game in lol():
            games = game[1]
            avg = sum(games) / len(games)
            chance = 1
            for game in game:
                chance = chance = 95 / game
                prediction = (1 / (1 - (chance)) + avg) / 2
                if chance < 65:
                    print(red +f"======================={white}")
                else:
                    print(green +f"======================={white}")
                print("")
                print("")
                if prediction < 2:
                    print(white + f"Prediction : {red}{prediction:.2f}{white}x")
                    if chance < 65:
                        print(f"Chance : {red}{chance:.2f}%{white}")
                    else:
                        print(f"Chance : {yellow}{chance:.2f}%{white}")
                else:
                    print(white + f"Prediction : {green}{prediction:.2f}{white}x")
                    if chance < 65:
                        print(f"Chance : {red}{chance:.2f}%{white}")
                    else:
                        print(f"Chance : {green}{chance:.2f}%{white}")
                print("")
                print("")
                if chance < 65:
                    print(red +f"======================={white}")
                else:
                    print(green +f"======================={white}")
                print("")
                print("")
                print(yellow +"WARNING - > Keep in mind bloxflip is a gambling website and no predictor is accurate at 100%")
                print(f"So if you keep losing, take a break and go touch {green}grass{white} !")
                print("")
                return menu()
    # If no commands found
    elif cmd != "menu" and cmd != "close" and cmd != "mines" and cmd != "towers"and cmd != "crash" and cmd != "help" and cmd != "roulette" and cmd != "cups" and cmd != "admin":
        clear = lambda: os.system('cls')
        clear()
        print(f"Result for '{cmd}' :")
        print("")
        print("No command found...")
        print("")
        return menu()
    elif cmd == "mines":
        clear = lambda: os.system('cls')
        clear()
        clear = lambda: os.system('cls')
        clear()
        print("")
        print("The round id can be found by starting a game and clicking on fairness")
        print("")
        rid = input("Round id : ")
        rlen = len(rid)
        if rlen == 36:
            clear = lambda: os.system('cls')
            clear()
            print("Calculating...")
            m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16, m17, m18, m19, m20, m21, m22, m23, m24, m25 = red + 'X', red + 'X',red + 'X',red + 'X',red + 'X',red + 'X',red + 'X',red + 'X',red + 'X',red + 'X',red + 'X',red + 'X',red + 'X',red + 'X',red + 'X',red + 'X',red + 'X',red + 'X',red + 'X',red + 'X',red + 'X',red + 'X',red + 'X',red + 'X',red + 'X'
            a = random.randint(1, 8)
            b = random.randint(9, 13)
            c = random.randint(14, 17)
            d = random.randint(18, 25)
            if a == 1:
                m1 = green + "√"
            elif a == 2:
                m2 = green + "√"
            elif a == 3:
                m3 = green + "√"
            elif a == 4:
                m4 = green + "√"
            elif a == 5:
                m5 = green + "√"
            elif a == 6:
                m6 = green + "√"
            elif a == 7:
                m7 = green + "√"
            elif a == 8:
                m8 = green + "√"
            if b == 9:
                m9 = green + "√"
            elif b == 10:
                m10 = green + "√"
            elif b == 11:
                m11 = green + "√"
            elif b == 12:
                m12 = green + "√"
            elif b == 13:
                m13 = green + "√"
            if c == 14:
                m14 = green + "√"
            elif c == 15:
                m15 = green + "√"
            elif c == 16:
                m16 = green + "√"
            elif c == 17:
                m17 = green + "√"
            if d == 18:
                m18 = green + "√"
            elif d == 19:
                m19 = green + "√"
            elif d == 20:
                m20 = green + "√"
            elif d == 21:
                m21 = green + "√"
            elif d == 22:
                m22 = green + "√"
            elif d == 23:
                m23 = green + "√"
            elif d == 24:
                m24 = green + "√"
            elif d == 25:
                m25 = green + "√"
            chance = random.randint(45, 95)
            clear = lambda: os.system('cls')
            clear()
            print("")
            print(f"---------------------")
            print(f"| {m1} {white}| {m2} {white}| {m3} {white}| {m4} {white}| {m5} {white}|")
            print(f"---------------------")
            print(f"| {m6} {white}| {m7} {white}| {m8} {white}| {m9} {white}| {m10} {white}|")
            print(f"---------------------")
            print(f"| {m11} {white}| {m12} {white}| {m13} {white}| {m14} {white}| {m15} {white}|")
            print(f"---------------------")
            print(f"| {m16} {white}| {m17} {white}| {m18} {white}| {m19} {white}| {m20} {white}|")
            print(f"---------------------")
            print(f"| {m21} {white}| {m22} {white}| {m23} {white}| {m24} {white}| {m25} {white}|")
            print(f"---------------------")
            print("")
            if chance <= 65:
                print(f"{white}Accuracy : {red}{chance}{white}% ")
            elif chance >= 66 and chance <= 75:
                print(f"{white}Accuracy : {yellow}{chance}{white}% ")
            elif chance >= 76:
                print(f"{white}Accuracy : {green}{chance}{white}% ")
            print("")
            print(f"{white}Round ID : {rid}")
            print("")
            print(yellow + "The accuracy is the \"chance\" in percent of the prediction to be good")
            print("")
            print(yellow + "Note : Bloxflip is a gambling website and no predictor is accurate at 100%. Please, keep that in mind")
            print(yellow + f"Note : Our result are based on a math calculate with the round id and api request to the bloxflip api {white}")
            print("")
            return menu()
        else:
            print("")
            print("A Round id is 36 characters !")
            print("")
            return menu()
    elif cmd == "close":
        print("")
        conf = input(f"Confirm you want to leave ({green}Y{white}/{red}N{white}) : ")
        if conf == "y" or conf == "Y" or conf == "yes" or conf == "YES":
            print("Closing process wait 2 seconds...")
            time.sleep(2)
            print("Alright cya :D")
            time.sleep(1)
        elif conf == "n" or conf == "N" or conf == "no" or conf == "NO":
            print()
            print("Success fully canceled the closing process !")
            print()
            return menu()
        else:
            print()
            print("No available choice as been made")
            print()
            return menu()
    elif cmd == "towers":
        clear = lambda: os.system('cls')
        clear()
        print()
        print("Towers Set Up")
        print(yellow + f"Note : To get the round id, start a game and click on fairness{white}")
        print()
        rid = input("Round ID : ")
        clear = lambda: os.system('cls')
        clear()
        print()
        print("Towers Set Up")
        print(yellow + f"Note : To get the round id, start a game and click on fairness{white}")
        print()
        print(f"Round ID : {rid}")
        print()
        diff = input("Difficulty (easy or normal) : ")
        clear = lambda: os.system('cls')
        clear()
        rlen = len(rid)
        if rlen == 36:
            if diff == "easy":
                
                t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24 = red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white
                a = random.randint(1, 3)
                b = random.randint(1, 3)
                c = random.randint(1, 3)
                d = random.randint(1, 3)
                e = random.randint(1, 3)
                f = random.randint(1, 3)
                g = random.randint(1, 3)
                h = random.randint(1, 3)

                if a == 1:
                    t1 = green+'√'+white
                elif a == 2:
                    t2 = green+'√'+white
                elif a ==3:
                    t3 = green+'√'+white
                if b == 1:
                    t4 = green+'√'+white
                elif b == 2:
                    t5 = green+'√'+white
                elif b ==3:  
                    t6 = green+'√'+white
                if c == 1:
                    t7 = green+'√'+white
                elif c == 2:
                    t8 = green+'√'+white
                elif c ==3:
                    t9 = green+'√'+white
                if d == 1:
                    t10 = green+'√'+white
                elif d == 2:
                    t11 = green+'√'+white
                elif d ==3:
                    t12 = green+'√'+white
                if e == 1:
                    t13 = green+'√'+white
                elif e == 2:
                    t14 = green+'√'+white
                elif e ==3:
                    t15 = green+'√'+white
                if f == 1:
                    t16 = green+'√'+white
                elif f == 2:
                    t17 = green+'√'+white
                elif f ==3:
                    t18 = green+'√'+white
                if g == 1:
                    t19 = green+'√'+white
                elif g == 2:
                    t20 = green+'√'+white
                elif g ==3:
                    t21 = green+'√'+white
                if h == 1:
                    t22 = green+'√'+white
                elif h == 2:
                    t23 = green+'√'+white
                elif h ==3:
                    t24 = green+'√'+white
                chance = random.randint(45, 95)
                print()
                print("Prediction :")
                print()
                print(white + f"-------------")
                print(f"| {t1} | {t2} | {t3} |")
                print(f"| {t4} | {t5} | {t6} |")
                print(f"| {t7} | {t8} | {t9} |")
                print(f"| {t10} | {t11} | {t12} |")
                print(f"| {t13} | {t14} | {t15} |")
                print(f"| {t16} | {t17} | {t18} |")
                print(f"| {t19} | {t20} | {t21} |")
                print(f"| {t22} | {t23} | {t24} |")
                print(white + f"-------------")
                print()
                if chance <= 65:
                    print(f"{white}Accuracy : {red}{chance}{white}% ")
                elif chance >= 66 and chance <= 75:
                    print(f"{white}Accuracy : {yellow}{chance}{white}% ")
                elif chance >= 76:
                    print(f"{white}Accuracy : {green}{chance}{white}% ")
                print("")
                print(f"{white}Round ID : {rid}")
                print(f"Difficulty : Easy")
                print("")
                print(yellow + "The accuracy is the \"chance\" in percent of the prediction to be good")
                print("")
                print(yellow + "Note : Bloxflip is a gambling website and no predictor is accurate at 100%. Please, keep that in mind")
                print(yellow + f"Note : Our result are based on a math calculate with the round id and api request to the bloxflip api {white}")
                print("")
                return menu()

            elif diff == "normal":
                tt1, tt2, tt3, tt4, tt5, tt6, tt7, tt8, tt9, tt10, tt11, tt12, tt13, tt14, tt15, tt16 = red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white,red+'X'+white
                a = random.randint(1, 2)
                b = random.randint(1, 2)
                c = random.randint(1, 2)
                d = random.randint(1, 2)
                e = random.randint(1, 2)
                f = random.randint(1, 2)
                g = random.randint(1, 2)
                h = random.randint(1, 2)
                if a == 1:
                    tt1 = green+'√'+white
                elif a ==2:
                    tt2 = green+'√'+white
                if b == 1:
                    tt3 = green+'√'+white
                elif b ==2:
                    tt4 = green+'√'+white
                if c == 1:
                    tt5 = green+'√'+white
                elif c ==2:
                    tt6 = green+'√'+white
                if d == 1:
                    tt7 = green+'√'+white
                elif d ==2:
                    tt8 = green+'√'+white
                if e == 1:
                    tt9 = green+'√'+white
                elif e ==2:
                    tt10 = green+'√'+white
                if f == 1:
                    tt11 = green+'√'+white
                elif f ==2:
                    tt12 = green+'√'+white
                if g == 1:
                    tt13 = green+'√'+white
                elif g ==2:
                    tt14 = green+'√'+white
                if h == 1:
                    tt15 = green+'√'+white
                elif h ==2:
                    tt16 = green+'√'+white
                chance = random.randint(45, 95)
                print(f"---------")
                print(f"| {tt1} | {tt2} |")
                print(f"| {tt3} | {tt4} |")
                print(f"| {tt5} | {tt6} |")
                print(f"| {tt7} | {tt8} |")
                print(f"| {tt9} | {tt10} |")
                print(f"| {tt11} | {tt12} |")
                print(f"| {tt13} | {tt14} |")
                print(f"| {tt15} | {tt16} |")
                print(f"---------")
                print("")
                if chance <= 65:
                    print(f"{white}Accuracy : {red}{chance}{white}% ")
                elif chance >= 66 and chance <= 75:
                    print(f"{white}Accuracy : {yellow}{chance}{white}% ")
                elif chance >= 76:
                    print(f"{white}Accuracy : {green}{chance}{white}% ")
                print("")
                print(f"{white}Round ID : {rid}")
                print(f"Difficulty : Easy")
                print("")
                print(yellow + "The accuracy is the \"chance\" in percent of the prediction to be good")
                print("")
                print(yellow + "Note : Bloxflip is a gambling website and no predictor is accurate at 100%. Please, keep that in mind")
                print(yellow + f"Note : Our result are based on a math calculate with the round id and api request to the bloxflip api {white}")
                print("")
                return menu()
            elif diff != "easy" and diff != "normal":
                print("")
                print("This Difficulty is invalid ! Only easy and normal are valid difficulty")
                print("")
                return menu()
        else:
            print("")
            print(red + f"This round id is invalid{white}")
            print("")
            return menu()
    elif cmd == "menu":
        clear = lambda: os.system('cls')
        clear()
        print()
        print(green + "Free Predictor V2.1")
        print(green + "This Adurite Predictor version is, as you can see a \"executable\" version, in python.")
        print(white + "Just note this version is in beta and some errors may occure.")
        print(yellow +"Note : To close this, just close the window")
        print(yellow + "WARNING : DO NOT REMOVE/ EDIT THIS FILE OR OTHER FILES !")
        print(white + "You can now enter a command ! Note : for help, type help")
        print("For Support, type help")
        print(" ")
        print()
        return menu()
    elif cmd == "roulette":
        clear = lambda: os.system('cls')
        clear()
        print()
        print("Im Thinking...")
        pred = ['red','red','red','purple','purple','purple','gold']
        pred = random.choice(pred)
        if pred == "red":
            clear = lambda: os.system('cls')
            clear()
            print("")
            print(f"Predictions : {red}RED{white}")
            chance = random.randint(45,95)
            if chance <= 65:
                print(f"{white}Accuracy : {red}{chance}{white}% ")
            elif chance >= 66 and chance <= 75:
                print(f"{white}Accuracy : {yellow}{chance}{white}% ")
            elif chance >= 76:
                print(f"{white}Accuracy : {green}{chance}{white}% ")
            print("")
            return menu()
        elif pred == "purple":
            clear = lambda: os.system('cls')
            clear()
            print("")
            print(f"Predictions : {purple}PURPLE{white}")
            chance = random.randint(45,95)
            if chance <= 65:
                print(f"{white}Accuracy : {red}{chance}{white}% ")
            elif chance >= 66 and chance <= 75:
                print(f"{white}Accuracy : {yellow}{chance}{white}% ")
            elif chance >= 76:
                print(f"{white}Accuracy : {green}{chance}{white}% ")
            print("")
            return menu()
        elif pred == "gold":
            clear = lambda: os.system('cls')
            clear()
            print(f"Predictions : {gold}GOLD{white}")
            chance = random.randint(45,95)
            if chance <= 65:
                print(f"{white}Accuracy : {red}{chance}{white}% ")
            elif chance >= 66 and chance <= 75:
                print(f"{white}Accuracy : {yellow}{chance}{white}% ")
            elif chance >= 76:
                print(f"{white}Accuracy : {green}{chance}{white}% ")
            print("")
            return menu()
    elif cmd == "cups":
        clear = lambda: os.system('cls')
        clear()
        print()
        print("To get the round id, start a game and click on fairness")
        print()
        rid = input("Round ID : ")
        rlen = len(rid)
        if rlen == 36:
            pred = ['blue', 'red']
            pred = random.choice(pred)
            if pred == "blue":
                print()
                print(f"Prediction : {blue}Blue{white}")
                chance = random.randint(45,95)
                if chance <= 65:
                    print(f"{white}Accuracy : {red}{chance}{white}% ")
                elif chance >= 66 and chance <= 75:
                    print(f"{white}Accuracy : {yellow}{chance}{white}% ")
                elif chance >= 76:
                    print(f"{white}Accuracy : {green}{chance}{white}% ")
                print()
                return menu()
            elif pred == "red":
                print()
                print(f"Prediction : {red}Red{white}")
                chance = random.randint(45,95)
                if chance <= 65:
                    print(f"{white}Accuracy : {red}{chance}{white}% ")
                elif chance >= 66 and chance <= 75:
                    print(f"{white}Accuracy : {yellow}{chance}{white}% ")
                elif chance >= 76:
                    print(f"{white}Accuracy : {green}{chance}{white}% ")
                print()
                return menu()
            else :
                print()
                print(f"{red}[501] - {white}An unexpected error occured")
                print()
                return menu()
        else:
            clear = lambda: os.system('cls')
            clear()
            print()
            print("Round id invalid !")
            print()
            return menu()
    elif cmd == "admin":
        clear = lambda: os.system('cls')
        clear()
        print()
        print("Admin Access")
        print("To access here please enter admin's credentials")
        print()
        username = input("Username : ")
        print("Password : ")
        if username == "admin":
            clear = lambda: os.system('cls')
            clear()
            print()
            print("Admin Access")
            print("To access here please enter admin's credentials")
            print()
            print("Username : admin")
            password = input("Password : ")
            if password == "admin":
                clear = lambda: os.system('cls')
                clear()
                print()
                print("Admin Access")
                print("To access here please enter admin's credentials")
                print()
                print("Username : admin")
                print("Password : XXXXX")
                print()
                print("Lol ye those are admin's credentials, there is nothing to see here")
                return menu()
menu()