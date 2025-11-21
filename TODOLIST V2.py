# TODOLIST V2

from rich import print
import os
import time
import sys
import json
import datetime

#-------------------STARTING ANIMATION------------------

start = "Running Program..."
for i in range(3):

    time.sleep(0.5)
    print(" "*len(start), end="\r")

    for st in start:

        if i == 0:
            color = "[yellow]"
            print(f"{color}{st}", end="")
            time.sleep(0.15)

        elif i == 1:
            color = "[purple]"
            print(f"\r{color}{st}", end="")
            time.sleep(0.15)

        else:
            color = "[bold bright_blue]"
            print(f"\r{color}{st}", end="")
            time.sleep(0.15)
    print("", end="\r")

time.sleep(2)

#-------------------DATA RESTARTING------------------

ToDoList = []

if os.path.exists("data0.json"):
    print("[green]Accessing data completed!")
    
    time.sleep(2)
else:
    with open("data0.json", "w") as dataf:
        print("[red]Data not found! new data file maked.")
        time.sleep(2)

#--------------------FUNCTIONS---------------------

def help():
    print("[yellow]-----------------------\n<<MAIN MENU HELP>>\nADD NEW TASK : a\nCHANGE TASK INFO : c\nSEE ALL TASKS : v\nDELETE A TASK : d\nBACK FROM ENYWHERE TO MAIN MENU : b\nCLOSE PROGRAM : e\nMORE HELP : h\n-----------------------")

def showtask():
    i = 0

    print("[yellow]\n-----------==INITIAL OF TASKS==-----------")

    if valid == True:
        print("[red]EMPTY[/red]")
    else:
        for t in ToDoList:
            i += 1
            print(f"{i}[bold bright_cyan]. {t["task"]} [bold white]-->", "[bold green]Done" if t["status"] == True else f"[bold bright_red]*Not Done* - [white]{t["date"]}")
    print("[yellow]-------------==END OF TASKS==-------------")
    info()

def info():
    done = 0
    not_done = 0
    all_Tasks = 0

    for t in ToDoList:

        if t["status"] == True:
            done += 1
            all_Tasks += 1

        elif t["status"] == False:
            not_done += 1
            all_Tasks += 1
    try:
        print(f"ALL TASKS : {all_Tasks}\n[green]DONE TASKS : {done} -- {(done/all_Tasks)*100}%\n[red]NOT DONE TASKS : {not_done} -- {(not_done/all_Tasks)*100}%\n")
    except ZeroDivisionError:
        print(f"ALL TASKS : {all_Tasks}\n")

def addtask():
    date = datetime.datetime.now().strftime("%Y/%m/%d - %H:%M:%S")
    tasks = {"task":title, "status":False, "priority":priority, "date":date}
    ToDoList.append(tasks)
    print("[green]ADDED!\n")
    with open("data0.json","w") as dataf:
        json.dump(ToDoList, dataf,ensure_ascii=False,indent=2)

def savetask():
    with open("data0.json","w") as dataf:
        json.dump(ToDoList, dataf,ensure_ascii=False,indent=2)

def loadtask():
    with open("data0.json","r") as dataf:
        list_load = json.load(dataf)
        global ToDoList
        ToDoList = list_load

def back():
    print("\n\n[blue]BACK TO MAIN MENU\n\n")
    return "continue"

def showfor_prioroty():
    i = 0

    print("[yellow]\n-----------==INITIAL OF TASKS==-----------")

    if valid == True:
        print("[red]EMPTY[/red]")
    else:
        for t in ToDoList:#########################################################
            while t["status"] == False:

                i += 1
                if t["priority"] == "High":
                    print(f"{i}[bold bright_cyan]. {t["task"]} [bold white]-->", "[bold green]Done" if t["status"] == True else f"[bold bright_red]*Not Done* - [white]{t["date"]}")
                    break
                if t["priority"] == "Medium":
                    print(f"{i}[bold bright_cyan]. {t["task"]} [bold white]-->", "[bold green]Done" if t["status"] == True else f"[bold bright_red]*Not Done* - [white]{t["date"]}")
                    break
                if t["priority"] == "Low":
                    print(f"{i}[bold bright_cyan]. {t["task"]} [bold white]-->", "[bold green]Done" if t["status"] == True else f"[bold bright_red]*Not Done* - [white]{t["date"]}")
                    break

            else:
                continue

        for t in ToDoList:
            if t["status"] == True:
                i += 1
                print(f"{i}[bold bright_cyan]. {t["task"]} [bold white]-->", "[bold green]Done" if t["status"] == True else f"[bold bright_red]*Not Done* - [white]{t["date"]}")
                
            else:
                continue   

    print("[yellow]-------------==END OF TASKS==-------------")
    info()

#-----------------------LOAD&HELP-----------------------

try:
    loadtask()
except:
    pass

help()
  
#---------------------PROGRAM START---------------------

while True:
#-----------EMPTY CHECK-------------
    if ToDoList == []:
        valid = True
    else:
        valid = False
#-----------------------------------
    print("[bright_blue]>>>>>>>>>>(*)(**)($$$$$$)(**)(*)<<<<<<<<<<")
    func = input("CHOOSE FUNCTION : ").lower().strip()

    if func == "a": # add a task <=====================
        title = input("ENTER YOUR TASK TITLE : ").lower().strip()

        if title == "b":
            back()

        ent_pri = input("ENTER YOUR TASK PRIORITY(1.Low, 2.Medium, 3.High) : ").lower().strip()

        if ent_pri == "1":
                priority = "Low"
                addtask()

        elif ent_pri == "2":
                priority = "Medium"
                addtask()

        elif ent_pri == "3":
                priority = "High"
                addtask()

        elif ent_pri == "b":
            back()
        
        else:
            print("[red]invalid input!\n")

    elif func == "c": #change task title or status <=====================
        
        if valid == True:
            print("\n[red]TASK LIST IS EMPTY!\n")

        else:
            showtask()

            try:
                n = input("WHICH TASK DO YOU WANT TO CHANGE?  : ").lower().strip()

                if n == "b":
                    back()

                elif ToDoList[int(n)-1] in ToDoList:
                    f = input("do you want to change 1.title? or 2.status? : ").lower().strip()

                    if f == "1":

                        ToDoList[int(n)-1]["task"] = input("ENTER NEW TITLE OF TASK : ").lower().strip()
                        savetask()
                        print("[green]CHANGED!")

                    elif f == "2":

                        if ToDoList[int(n)-1]["status"] == True:
                            print("[yellow]ALREADY DONE!\n")

                        else:
                            ToDoList[int(n)-1]["status"] = True
                            savetask()
                            print("[green]CHANGED TO DONE!\n")

                    elif f == "b":
                        back()

                    else:
                        print("[red]invalid input!\n")

            except:
                print("[red]invalid input!\n")

    elif func == "v": #task vision <=====================

        if valid == True:
            print("\n[red]TASK LIST IS EMPTY!\n")
        
        else:
            f = input("DO YOU WANT TO SEE ALL TASKS BY DATE (sd) OR BY PRIORITY(sp)? : ").lower().strip()

            if f == "sd":
                showtask()

            elif f == "sp":
                showfor_prioroty()

            elif f == "b":
                back()

            else:
                print("[red]invalid input!\n")

    elif func == "h": #help list <=====================
        help()

    elif func == "d": #delete tasks <=====================

        if valid == True:
            print("\n[red]TASK LIST IS EMPTY!\n")
        
        else:
            showtask()

            n = input("DO YOU WANT TO DELETE A TASK(enter number of task) OR ALL TASKS(da)? : ").lower().strip()

            if n == "b":
                back()

            elif n == "da":
                ToDoList.clear()
                savetask()
                print("[green]ALL TASKS DELETED!\n")

            else:

                try:
                    if ToDoList[int(n)-1] in ToDoList:
                        ToDoList.remove(ToDoList[int(n)-1])
                        savetask()
                        print("[green]DELETED!")
                except:
                    print("[bright_red]Task number not found!")

    elif func == "e": #program exit <=====================
        exit = "PROGRAM WILL CLOSE SOON. GOOD LUCK."
        print()

        for ex in exit:
            print(f"\r{ex}", end="")
            time.sleep(0.1)
        time.sleep(2)
        sys.exit()

    else:
        print("\n[bright_red]!!!!!!!!!!!!!!!!!!!!!!!!!!!\nINVALID FUNCTION!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!\n") 