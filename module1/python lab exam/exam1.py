members = {}

while True:
    print("\n--- COLLEGE CLUB MANAGEMENT ---")
    print("1. Add Member")
    print("2. Search Member")
    print("3. Update Phone Number")
    print("4. Delete Member")
    print("5. Display Members")
    print("6. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        name = input("Enter name: ")

        if name in members:
            print("Member already exists!")
        else:
            phone = input("Enter phone number: ")
            members[name] = phone
            print("Member added successfully!")

    elif ch == "2":
        name = input("Enter name to search: ")

        if name in members:
            print("Name:", name)
            print("Phone:", members[name])
        else:
            print("Member not found!")

    elif ch == "3":
        name = input("Enter name to update: ")

        if name in members:
            phone = input("Enter new phone number: ")
            members[name] = phone
            print("Phone number updated!")
        else:
            print("Member not found!")

    elif ch == "4":
        name = input("Enter name to delete: ")

        if name in members:
            del members[name]
            print("Member deleted successfully!")
        else:
            print("Member not found!")

    elif ch == "5":
        if len(members) == 0:
            print("No members available!")
        else:
            for name, phone in members.items():
                print("Name:", name, "| Phone:", phone)

    elif ch == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")