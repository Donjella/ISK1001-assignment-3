# Importing third-party libraries (require installation via pip)
import pytest  # Third-party library used for testing. Provides fixtures and test functionality for the application.

# Importing internal modules (created within the project)
from classes.kitchen import Kitchen  # Internal module defining the Kitchen class, which manages the menu data structure.
from functions.kitchen_functions import add_menu_for_day  # Function to add or update the menu for a specific day.

# Define fixture for testing
@pytest.fixture
def kitchen():
    """
    Fixture to provide a fresh instance of Kitchen for testing.

    Purpose:
        Provides a clean and isolated instance of the Kitchen class for each test run. 
        Ensures that test outcomes are not affected by previous tests' state.

    Returns:
        Kitchen: A new instance of the Kitchen class.
    
    Example Usage:
        def test_example(kitchen):
            assert isinstance(kitchen, Kitchen)
    """
    return Kitchen()

# Define test for `add_menu_for_day` function
def test_add_menu_for_day(mocker, kitchen):
    """
    Test the `add_menu_for_day` function for adding a menu to the kitchen.

    Purpose:
        Validates that the `add_menu_for_day` function correctly handles user inputs 
        and updates the menu data structure in the Kitchen instance.

    Arguments:
        mocker (pytest-mock): A pytest plugin to mock inputs for the test.
        kitchen (Kitchen): A fresh Kitchen instance provided by the fixture.

    Test Details:
        - Mock user input for week number, day of the week, and meal details.
        - Call the `add_menu_for_day` function with the mocked inputs.
        - Verify that the menu data structure in the Kitchen instance is updated as expected.

    Assertions:
        - The week number exists in the menu.
        - The specified day of the week (Monday) exists in the menu for that week.
        - Each meal (Breakfast, Lunch, Afternoon Tea) matches the mocked user input.

    Example Input:
        Week number: '1'
        Day of the week: '1' (Monday)
        Breakfast: 'Pancakes'
        Lunch: 'Sandwich'
        Afternoon Tea: 'Cookies'

    Example Output:
        kitchen.menu = {
            '1': {
                'Monday': {
                    'Breakfast': 'Pancakes',
                    'Lunch': 'Sandwich',
                    'Afternoon Tea': 'Cookies'
                }
            }
        }
    """
    # Mock input for week number, day of the week, and meal details
    mocker.patch('builtins.input', side_effect=[
        '1',            # Week number
        '1',            # Day of the week (Monday)
        'Pancakes',     # Breakfast
        'Sandwich',     # Lunch
        'Cookies'       # Afternoon Tea
    ])
    
    # Call `add_menu_for_day` to add a menu to the kitchen
    add_menu_for_day(kitchen)
    
    # Convert week number to string to match the structure of kitchen menu
    week_str = '1'
    
    # Check that the menu was added correctly
    assert week_str in kitchen.menu  # Verify the week exists in the menu
    assert 'Monday' in kitchen.menu[week_str]  # Verify Monday is present in the week's menu
    assert kitchen.menu[week_str]['Monday']['Breakfast'] == 'Pancakes'  # Check breakfast
    assert kitchen.menu[week_str]['Monday']['Lunch'] == 'Sandwich'  # Check lunch
    assert kitchen.menu[week_str]['Monday']['Afternoon Tea'] == 'Cookies'  # Check afternoon tea
