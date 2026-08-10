from sms import StudentManagementSystem

sms = StudentManagementSystem()

while True:

    print("\n===== SMS V4 =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Students")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        sms.add_student()

    elif choice == "2":
        sms.view_students()

    elif choice == "3":
        sms.search_student()

    elif choice == "4":
        print("Goodbye")
        break

    else:
        print("Invalid Choice")