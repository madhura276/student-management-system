import student_management as SM

def main():
    system = SM.StudentManagement()
    filename = "students.txt"
    system.load_from_file(filename)

    while True:
        print("\n==== Student Management System ====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Roll Number")
        print("4. Update Marks")
        print("5. Calculate Average Marks")
        print("6. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            roll = int(input("Enter roll number: "))
            name = input("Enter name: ")
            course = input("Enter course: ")
            marks = int(input("Enter marks: "))
            system.add_student(roll, name, course, marks)
        elif choice == "2":
            system.view_students()
        elif choice == "3":
            roll = int(input("Enter roll number to search: "))
            student = system.search_student(roll)
            if student:
                print(student)
            else:
                print("❌ Student not found.")
        elif choice == "4":
            roll = int(input("Enter roll number: "))
            new_marks = int(input("Enter new marks: "))
            system.update_marks(roll, new_marks)
        elif choice == "5":
            avg = system.calculate_average()
            print(f"📊 Average marks: {avg}")
        elif choice == "6":
            system.save_to_file(filename)
            print("💾 Data saved. Exiting...")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
