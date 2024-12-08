import pytest  # External library used for writing and running tests.
from functions.student_functions import add_student  # Internal module function for adding a student with validations and classroom assignments.
from classes.classrooms import Classroom  # Internal class used to create and manage classroom instances.

# Pytest fixture for initializing a list of classroom instances.
@pytest.fixture
def classrooms():
    """
    Purpose: Provides a reusable fixture that initializes a list of predefined Classroom instances.
    Each classroom has a specific age range for student assignments.

    Example Usage:
        def test_some_function(classrooms):
            # classrooms can now be used in the test case.
    """
    return [
        Classroom("Babies Room (0-2 years)", 0, 2),
        Classroom("Toddlers Room (2-3 years)", 2, 3),
        Classroom("Kindergarten Room (3-5 years)", 3, 5)
    ]

@pytest.fixture
def students():
    """
    Purpose: Provides a reusable fixture that initializes an empty list to store Student instances.

    Example Usage:
        def test_some_function(students):
            # students can now be used in the test case.
    """
    return []

def test_add_student(mocker, students, classrooms):
    """
    Purpose: Tests the functionality of the `add_student` function by mocking user input 
    and validating that the student is correctly added to the students list with all attributes.

    Steps:
        1. Mocks user input for a student (name, allergies, guardian details, etc.).
        2. Calls the `add_student` function.
        3. Verifies that the student is successfully added to the students list.
        4. Checks that all attributes (e.g., name, guardian details, allergies) are set correctly.

    Mocked Input Details:
        - First Name: 'Kylian'
        - Last Name: 'Mbappe'
        - Birthday: '2023-01-01' (age-based classroom assignment validation)
        - Allergies: 'Peanut', 'Dairy'
        - Guardian: Name - 'Mary Lamb', Contact Number - '0406346693', Email - 'mary@example.com'

    Assertions:
        - Ensures that the student is added to the students list.
        - Validates the first name, guardian email, and allergies.
    """
    # Mock 'inputs' for the student details and follows all validation from actual add student_function
    mocker.patch('builtins.input', side_effect=[
        'Kylian',      # First name
        'Mbappe',     # Last name
        '2023-01-01', # Birthday
        'yes',        # Yes for question asking for any allergies
        'Peanut',     # Input allergy
        'yes',         # yes when asking for any more allergies
        'Dairy',       # Input allergy
        'no',          # no when asking for any more allergies
        'Mary',       # Guardian's first name
        'Lamb',       # Guardian's last name
        '0406346693',  # Guardian's contact number - needs to be 
        'mary@example.com'  # Guardian's contact email
    ])
    
    # Call `add_student`
    add_student(students, classrooms)
    
    # Check that the student has been added (matching the input above to pass)
    assert len(students) == 1 # test that student is added to students list
    assert students[0].get_fname() == 'Kylian' # Verify student's first name
    assert students[0].guardian.get_guardian_contact_email() == 'mary@example.com' # Verify student's last name
    assert students[0].get_allergies() == ['Peanut', 'Dairy'] # Verify student's allergies