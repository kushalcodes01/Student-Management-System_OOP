from sms import StudentManagementSystem

sms = StudentManagementSystem()

while True:
    print("\n======= SMS V2 =======")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Search by name")
    print("7. Total Students")
    print("8. Statistics")
    print("9. Exit")

    choice = input("Enter Your Choice:")

    if choice == "1":
        sms.add_student()

    elif choice == "2":
        sms.view_student()

    elif choice == "3":
        sms.search_student()

    elif choice == "4":
        sms.delete_student()

    elif choice == "5":
        sms.update_student()

    elif choice == "6":
        sms.search_by_name()

    elif choice == "7":
        sms.count_students()

    elif choice == "8":
        sms.statistics()
        
    elif choice == "9":
        print("Tata Bye Bye")
        break
