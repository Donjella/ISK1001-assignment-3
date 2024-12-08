from prettytable import PrettyTable  # External library used to display tabular data. E.g. list students by classrooms in individual tables
from colored import Style, stylize, attr, fg  # External library for colored text styling.

from classes.person import Person  # Import the Person class for shared methods like age formatting.
from constants import color3, color4, color5  # Imported constants for consistent colored output.

def assign_student(classrooms, student, silent=False):
    """
    Assign a student to a valid classroom based on their age.

    Purpose:
        This function iterates through a list of classrooms to find one that matches the student's age range.
        If a match is found, the student is assigned to that classroom.
        If no match is found, the student's details (e.g., name, birthday) are cleared to ensure consistency.

    Arguments:
        classrooms (list): A list of Classroom instances to check against the student's age.
        student (Student): The student instance to be assigned to an appropriate classroom.
        silent (bool, optional): Suppresses output messages if set to True. This is particularly useful 
            during operations like loading data from a file (e.g., `load_students` in `file_functions.py`) 
            to prevent re-generating student IDs or displaying assignment messages. Default is False.

    Example Usage:
        # Sample Data
        classrooms = [
            Classroom("Babies Room (0-2 years)", 0, 2),
            Classroom("Toddlers Room (2-3 years)", 2, 3)
        ]
        student = Student("Lamine", "Yamal", "2020-01-01", student_id=1)

        # Assign the student to a classroom
        assign_student(classrooms, student)

        # Expected Output (if silent=False):
        # Lamine Yamal (Student ID: 1) is 2 years, 0 months old and is assigned to Toddlers Room (2-3 years).

        # Result:
        # student.classroom -> "Toddlers Room (2-3 years)"
        # classrooms[1].students -> [Student("Lamine", "Yamal", "2020-01-01", student_id=1)]
    """


    age = student.calculate_age() # Calculate the student's age in years, including fractional months, using the `calculate_age` method from the Person class.

    
    # Initialize to track if the student is assigned
    assigned = False

    # Try to assign the student to a valid classroom
    for classroom in classrooms:
        if classroom.is_valid_for_age(age):
            classroom.students.append(student)  # Add the student to the classroom's student list
            student.assign_classroom(classroom)  # Assign the classroom to the student
            assigned = True
            # If silent mode is not enabled, provide user feedback with output below
            if not silent:
                # Format the student's age as a user-friendly string (e.g., "3 years and 2 months old")
                formatted_age = Person.age_in_years_and_months(age)
                print(f"\n{color3}{student.full_name} (Student ID: {student.get_formatted_id()}) is {formatted_age} and is assigned to {classroom.name}.{Style.reset}")
            
            break  # Exit the loop once the student is assigned

    if not assigned:
        # Clear student details if no classroom is suitable
        student.fname = None
        student.lname = None
        student.birthday = None
        student.allergies = []
        student.guardian = None

        if not silent:
            formatted_age = Person.age_in_years_and_months(age)
            if student.fname and student.lname:
                print(f"{student.full_name}, {formatted_age} cannot be added to any classroom due to age restriction. Therefore, they are not enrolled.")
            else:
                print(f"Student of age: {formatted_age} cannot be added to any classroom due to age restriction. Therefore, they are not enrolled.")


def list_students_by_classroom(classrooms):
    """
    Display a list of students for each classroom in a tabular format.

    Purpose:
        Iterates through the provided list of Classroom instances and displays enrolled students in a table format.
        The table includes each student's full name, student ID, and age in a readable format, grouped by classroom.

    Arguments:
        classrooms (list): A list of Classroom instances, each containing a list of assigned students.

    Example Usage:
        # Sample Data
        classrooms = [
            Classroom("Babies Room (0-2 years)", 0, 2),
            Classroom("Toddlers Room (2-3 years)", 2, 3)
        ]
        student1 = Student("Dani", "Olmo", "2020-01-01", student_id=1)
        student2 = Student("Harry", "Kane", "2019-06-15", student_id=2)
        classrooms[0].students.append(student1)  # Assign Dani to Babies Room
        classrooms[1].students.append(student2)  # Assign Harry to Toddlers Room

        Call the function
        list_students_by_classroom(classrooms)

        Expected Output:
        Babies Room (0-2 years)
        -------------------------
        Student Name (Student ID)     Age
        Dani Olmo (1)                  2 years, 0 months
        
        Toddlers Room (2-3 years)
        --------------------------
        Student Name (Student ID)     Age
        Harry Kane (2)                3 years, 0 months
    """

    for classroom in classrooms:
        if classroom.students:  # Check if the classroom has any students
            # Initialize the table for the specific classroom
            table = PrettyTable()

            # Bold and style headers for table
            header_color = fg("blue") + attr("bold")
            header_student_name_id = stylize("Student Name (Student ID)", header_color)
            header_age = stylize("Age", header_color)

            # Apply green color for table lines
            table.horizontal_char = stylize("-", fg("spring_green_4"))
            table.junction_char = stylize("+", fg("spring_green_4"))
            table.vertical_char = stylize("|", fg("spring_green_4"))

            table.field_names = [header_student_name_id, header_age]

            for student in classroom.students:  # Loop through each student in the classroom
                age = student.calculate_age()
                formatted_age = Person.age_in_years_and_months(age)  # Use the static method from Person class
                name_id = f"{student.full_name} (ID: {student.get_formatted_id()})"

                # Add row to the table
                table.add_row([name_id, formatted_age])

            # Print the table for the current classroom
            print(f"\n{color3}Students in {classroom.get_name()}:{Style.reset}")
            print(table)
        else:
            # If no students in the classroom, print a message
            print(f"\n{color4}No students in {classroom.get_name()}.{Style.reset}")


def count_total_students(classrooms):
   
    """
    Count and print the total number of students across all classrooms.

    Purpose:
        Iterates through the provided list of Classroom instances to calculate the total number of enrolled students.
        Displays the total count in a formatted output.

    Arguments:
        classrooms (list): A list of Classroom instances, each containing a list of enrolled students.

    Example Output:
    Output will print the total number of students in the childcare across all classrooms. 
    e.g. Total number of students: 25

    Example Usage:
        # Sample Data
        classrooms = [
            Classroom("Babies Room (0-2 years)", 0, 2),
            Classroom("Toddlers Room (2-3 years)", 2, 3)
        ]
        students = [
            Student("Harry", "Kane", "2020-01-01", student_id=1),
            Student("Xavi", "Simons", "2019-06-15", student_id=2)
        ]
        classrooms[0].students.append(students[0])  # Assign Harry to Babies Room
        classrooms[1].students.append(students[1])  # Assign Xavi to Toddlers Room

        # Call the function
        count_total_students(classrooms)

        # Expected Output:
        # Total number of students: 2
    """

    total_students = sum(len(classroom.students) for classroom in classrooms)
    print(f"\n{color3}Total number of students: {total_students}{Style.reset}")  


def delete_student(students, classrooms):
    """
    Delete a student by their student ID.

    Purpose:
        Prompts the user to enter a student ID and removes the corresponding student from:
        1. The classroom they are assigned to.
        2. The global list of all students.

    Arguments:
        students (list): The global list containing all Student instances.
        classrooms (list): The list of all Classroom instances, used to locate and remove the student from their assigned classroom.

    Example Usage:
        # Sample Data
        classrooms = [
            Classroom("Babies Room (0-2 years)", 0, 2),
            Classroom("Toddlers Room (2-3 years)", 2, 3)
        ]
        students = [
            Student("Harry", "Kane", "2020-01-01", student_id=1),
            Student("William, "Saliba", "2019-06-15", student_id=2)
        ]
        classrooms[0].students.append(students[0])  # Assign Harry to Babies Room
        classrooms[1].students.append(students[1])  # Assign William to Toddlers Room

        delete_student(students, classrooms)

        # User Interaction
        Input: 1  # User enters 1 as the student ID to delete

        # Expected Outcome
        - Harry Kane is removed from the Babies Room classroom.
        - Harry Kane is removed from the global students list.
        - Prints: "Harry Kane (student ID: 1) has been deleted from the system."

        If the user enters a non-existing ID:
        Input: 3  # User enters 3 as the student ID
        - Prints: "Student with ID 3 not found."
    """
    try:
        # Ask for student ID to delete and ensure it's an integer
        student_id = int(input("Enter the student ID to delete: "))  # Convert input to int
    except ValueError:
        print(f"{color5}Invalid input. Please enter a valid student ID (integer).{Style.reset}")
        return
    except EOFError:
        print(f"\n{color5}Input interrupted. Returning to the previous menu.{Style.reset}")
        return
    except Exception as e:  
        print(f"{color5}An unexpected error occurred: {e}{Style.reset}")
        return
    
    # Find the student in the classrooms' students list
    student_to_delete = None
    classroom_to_delete_from = None

    # Loop through each classroom to find the student
    for classroom in classrooms:
        for student in classroom.students:
            if student.student_id == student_id:  # Ensure comparison is between integers
                student_to_delete = student
                classroom_to_delete_from = classroom
                break  # Exit inner loop once the student is found
        if student_to_delete:
            break  # Exit outer loop once the student is found
    
    if not student_to_delete:
        print(f"Student with ID {student_id} not found.")
        return
    
    # Remove the student from the classroom they are assigned to
    if classroom_to_delete_from:
        classroom_to_delete_from.students.remove(student_to_delete)
        print(f"\n{color3}{student_to_delete.full_name} removed from {classroom_to_delete_from.get_name()}.{Style.reset}")

    # Remove the student from the global students list
    students.remove(student_to_delete)
    print(f"{color3}{student_to_delete.full_name} (student ID: {student_to_delete.student_id}) has been deleted from the system.{Style.reset}")
