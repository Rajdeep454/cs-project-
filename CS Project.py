books = {}
students = []
teachers = []
issued = {}

while True:
    print("1.ADD BOOK")
    print("2.REGISTER STUDENT")
    print("3.REGISTER TEACHER")
    print("4.ISSUE BOOK")
    print("5.RETURN BOOK")
    print("6.SHOW BOOK")
    print("7.EXIT")

    option = input("Enter the option (1-7) = ")

    if option == "1":
        book_id = input("ENTER THE BOOK ID = ")
        name = input("ENTER THE BOOK NAME = ")
        books[book_id] = name
        print("BOOK IS ADDED!")

    elif option == "2":
        student_name = input("ENTER THE STUDENT NAME = ")
        students.append(student_name)
        print("STUDENT IS REGISTERED!")

    elif option == "3":
        teacher_name = input("ENTER THE TEACHER NAME = ")
        teachers.append(teacher_name)
        print("TEACHER IS REGISTERED!")

    elif option == "4":
        book_id = input("ENTER THE BOOK ID = ")

        if book_id in books and book_id not in issued:
            name = input("ENTER STUDENT/TEACHER NAME = ")
            if name in students or name in teachers:
                issued[book_id] = name
                print("BOOK IS ISSUED!")
            else:
                print("NAME NOT REGISTERED!")
        else:
            print("BOOKS NOT AVAILABLE!")

    elif option == "5":
        book_id = input("BOOK ID = ")
        if book_id in issued:
            del issued[book_id]
            print("BOOK IS RETURNED!")
        else:
            print("THIS BOOK ID IS NOT EXIST")

    elif option == "6":
        print("BOOK LIST ARE:")
        for book_id in books:
            if book_id in issued:
                print(book_id, "-", books[book_id], "(ISSUED TO", issued[book_id] + ")")
            else:
                print(book_id, "-", books[book_id], "(AVAILABLE)")

    elif option == "7":
        print("THANK YOU!")
        break

    else:
        print("OPTION NOT EXIST!")
        
    
    
    
    
    


