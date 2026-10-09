import os
import json

note = []


def add():
    while True:
        task = input("Enter Task (q to quit): ")

        if task.lower() == "q":
            os.system("cls" if os.name == "nt" else "clear")
            return
        note.append({"Task": task, "Status": "Pending"})
        save()


def view():
    while True:
        if len(note) == 0:
            print("The List is Empty")
            return

        print("\n" + "=" * 40)
        print("           📋 TASK LIST")
        print("=" * 40)

        for i, task in enumerate(note, start=1):
            print(f"{i}: {task['Task']} - {task['Status']}")

        choice = input("Select for Marking Done (q to exit) ")
        if choice == "q":
            break

        else:
            try:

                index = int(choice) - 1

                if 0 <= index < len(note):
                    if note[index]["Status"] == "Done":
                        note[index]["Status"] = "Pending"
                    else:
                        note[index]["Status"] = "Done"
                    save()
                    os.system("cls" if os.name == "nt" else "clear")
                else:
                    print("Invlaid Choicr")
            except ValueError:
                print("Enter Correct Value")


def remove():
    while True:
        for i, task in enumerate(note, start=1):
            print(f"{i}: {task['Task']} - {task['Status']}")

        if len(note) == 0:
            os.system("cls" if os.name == "nt" else "clear")
            print("\nThe List is Empty")
            return

        search_index = input("Enter number to remove (q to quit):")
        if search_index.lower() == "q":
            os.system("cls" if os.name == "nt" else "clear")
            return

        else:
            try:
                index = int(search_index) - 1
                if 0 <= index < len(note):
                    remove_task = note.pop(index)
                    save()
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f"The Task {remove_task['Task']} Removed")
                else:
                    print("Invalid Choice:")
            except ValueError:
                print("Please Enter a valid number")


def save():
    with open("task.json", "w") as file:
        json.dump(note, file)


def load():
    global note
    try:
        with open("task.json", "r") as file:
            note = json.load(file)
    except:
        note = []


def view_pending():
    os.system("cls" if os.name == "nt" else "clear")
    if len(note) == 0:
        print("List is Empty")
        return

    found = False

    for i, task in enumerate(note, start=1):
        if task["Status"] == "Pending":
            print(f"{i}. {task['Task']} - {task['Status']}")
            found = True

    if not found:
        print("No Pending Task in List")
        return

    input("\nPress any Key")
    os.system("cls" if os.name == "nt" else "clear")


def view_done():
    os.system("cls" if os.name == "nt" else "clear")
    if len(note) == 0:
        print("List is Empty")
        return

    found = False
    for i, task in enumerate(note, start=1):
        if task["Status"] == "Done":
            print(f"{i} {task['Task']}")
            found = True

    if not found:
        print("No Task Done Yet")
        return

    input("\nPress any Key")
    os.system("cls" if os.name == "nt" else "clear")


def ui():
    while True:

        print("=" * 40)
        print("        🚀 TODO APP")
        print("=" * 40)

        print("1. Add List")
        print("2. View List")
        print("3. Remove List")
        print("4. Exit")

        print("=" * 40)

        try:
            choice = int(input("Enter Your Choice 1/2/3/4?: "))
        except ValueError:
            print("Enter Correct Numbers:")
            continue

        if choice == 1:
            os.system("cls" if os.name == "nt" else "clear")
            add()
        elif choice == 2:
            os.system("cls" if os.name == "nt" else "clear")

            print("1.View All")
            print("2.View Pending Task")
            print("3.View Done Task")

            try:
                sub_choice = int(input("Enter Choice 1/2/3?"))
            except ValueError:
                print("Inalid Choice")

            if sub_choice == 1:
                view()
            elif sub_choice == 2:
                view_pending()
            elif sub_choice == 3:
                view_done()

        elif choice == 3:
            os.system("cls" if os.name == "nt" else "clear")
            remove()
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Exiting")
            exit(0)


load()
ui() 