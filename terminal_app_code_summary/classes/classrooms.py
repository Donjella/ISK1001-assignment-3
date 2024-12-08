class Classroom:
    # Represents a classroom with a specific name, age range, and a list of enrolled students.
    # This class is used to define a classroom and manage students within a specified age range.
    # It provides methods to validate if a student's age falls within the classroom's range and to retrieve the classroom's name.

    # method includes __init__, is_valid_for_age and get_name
    
    def __init__(self, name, min_age, max_age):
        # Initialises the classroom with its name, age range, and an empty student list.
        self.name = name # name (str): The name of the classroom.
        self.min_age = min_age # The (int) minimum age for students in this classroom.
        self.max_age = max_age # The (int) maximum age for students in this classroom.
        self.students = [] # students (list): A list to store students assigned to this classroom.

    def is_valid_for_age(self, age):
        """
    Check if a given age falls within the classroom's defined age range.

    Purpose:
        Validates whether a student's age is appropriate for the classroom by comparing it
        to the classroom's minimum and maximum age attributes.

    Arguments:
        age (int): The age of the student to validate.

    Returns:
        bool: True if the student's age falls within the classroom's range, False otherwise.

    Example Usage:
        # Sample Data
        classroom = Classroom("Toddlers Room (2-3 years)", 2, 3)

        # Check if a student with age 2.5 is valid for the classroom
        is_valid = classroom.is_valid_for_age(2.5)
        print(is_valid)  # Output: True

        # Check if a student with age 3.5 is valid for the classroom
        is_valid = classroom.is_valid_for_age(3.5)
        print(is_valid)  # Output: False

        # Practical Application:
        if classroom.is_valid_for_age(student.age):
            classroom.students.append(student)
    """
        return self.min_age <= age < self.max_age

    def get_name(self):
        """
    Retrieve the name of the classroom.

    Purpose:
        Provides the name of the classroom for display or reference purposes.
        This method is useful when identifying or listing classrooms within the application.

    Returns:
        str: The name of the classroom.

    Example Usage:
        # Sample Data
        classroom = Classroom("Babies Room (0-2 years)", 0, 2)

        Usage Example:
        # Retrieve and print the classroom's name
        print(classroom.get_name())  

        Output: "Babies Room (0-2 years)"
        """
        return self.name

# Global list of students
# Purpose: This list is used to store all student instances in the application. 
# Students can be assigned to a classroom based on their age, and this global list ensures they can be accessed from various parts of the application.
students = []

# Initialize the classrooms
# Purpose: These instances represent predefined classrooms categorized by age range. 
# Students will be assigned to these classrooms automatically based on their age.
babies_classroom = Classroom("Babies Room (0-2 years)", 0, 2)
toddlers_classroom = Classroom("Toddlers Room(2-3 years)", 2, 3)
kindergarten_classroom = Classroom("Kindergarten Room(3-5 years)", 3, 5)

# List of classrooms
# Purpose: This list contains all classroom instances. 
# It is used to iterate through classrooms when assigning students or retrieving information about specific classrooms.

# Example Usage - Assign a student to a classroom based on age:
# for student in students:
#     for classroom in classrooms:
#         if classroom.is_valid_for_age(student.age):
#             classroom.students.append(student)
#             break
classrooms = [babies_classroom, toddlers_classroom, kindergarten_classroom]

