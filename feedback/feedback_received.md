# Feedback Received
## Feedback instance 1

**Specific documentation checked:** Childcare Management App – README documentation and code comments  
**Date of feedback received:** 05/12/2024   
**Who checked it:** Ben and Andrea  
**Feedback Provided:**  
*  *Code Comments* - The code comments are comprehensive, well-structured, and adhere to industry best practices, including PEP8 standards. They are clean, detailed, and easy to follow, making the code highly accessible for developers.  
* *README* - The README file is exceptionally thorough, providing clear and detailed installation instructions alongside comprehensive explanations of the application's features. It effectively guides users through the setup and usage process.  
* *Ethical Considerations* -  Privacy concerns are thoughtfully addressed, with specific references to relevant laws and regulations. Accessibility was also mentioned with measures implemented to ensure inclusivity. 

**Reflection and actions to do based on the feedback:**  

While the feedback received was overwhelmingly positive, with minimal suggestions for improvement regarding the documentation or code comments, the feedback provided by Ben and Andrea inspired a realization - we could further enhance the application's accessibility features. Specifically, for future iterations of the application, we can improve terminal user accessibility by incorporating optional but consistent color schemes, ensuring a more inclusive and user-friendly experience for all users.

For example, we can introduce an optional setting to disable colored output for better accessibility or switch to a high-contrast color style or theme for improved readability by adding a toggle to enable or disable colors. 

```python
# Add a toggle for enabling/disabling colors
USE_COLORS = True  # Set to False to disable colored output

def get_color(color_code):
    return color_code if USE_COLORS else ""

# Example usage
# Else with an empty string avoids unnecessary style reset if USE_COLORS is set to false
print(f"{get_color(color3)}Welcome to the Childcare Management Application{Style.reset if USE_COLORS else ''}") 
```

## Feedback instance 2

**Specific documentation checked:** Childcare Management App – README documentation and code comments  
**Date of feedback received:** 06/12/2024   
**Who checked it:** Tilley and Declan Flynn  
**Feedback Provided:**  
*  *Code Comments* - The functions are well-documented with clear purposes, arguments, and examples. However, Tilley suggested that the examples of returned results could be further elaborated, particularly by including visual examples such as JSON structures for functions like save_menu and save_students.
* *README* - The README is detailed and comprehensive, with a great overview of the app's purpose, target audience, and features. The documentation is clean and easy to follow, with clear installation steps and code snippets.

**Reflection and actions to do based on the feedback:**  

The feedback was incredibly insightful, and we recognized an opportunity to improve our code comments and README by including JSON output examples. This enhancement provides a clearer understanding of how the application stores and handles data.

To implement this, we updated the comments for functions like save_menu and save_students in file_functions.py to include structured JSON examples of the saved data. This clarifies what the saved data looks like and how the application's persistence mechanisms work. Additionally, we extended the README documentation to include these JSON examples in the application features section, helping reviewers and users visualize the results.

An extract of the example for save_students function in the file_functions.py before feedback received:

```python
Example with JSON Output:
        save_students(students) -> Saves all valid students to 'data/students.json'.
```

Example for save_students function in the file_functions.py after feedback received and implemented to reflect JSON structures:

 ```python
Example usage with JSON Output:
    save_students(students) -> Saves all valid students to 'data/students.json'.

JSON Output Example:
    [
        {
            "student_id": 1,
            "fname": "John",
            "lname": "Doe",
            "birthday": "2015-03-25",
            "allergies": ["Peanuts", "Shellfish"],
            "guardian": {
                "fname": "Jane",
                "lname": "Doe",
                "contact_number": "0412345678",
                "contact_email": "jane.doe@example.com"
            }
        },
        {
            "student_id": 2,
            "fname": "Alice",
            "lname": "Smith",
            "birthday": "2017-07-12",
            "allergies": [],
            "guardian": {
                "fname": "Bob",
                "lname": "Smith",
                "contact_number": "0498765432",
                "contact_email": "bob.smith@example.com"
            }
        }
    ]
```

## Feedback instance 3

**Specific documentation checked:** Childcare Management App –  code and code comments  
**Date of feedback received:** 06/12/2024   
**Who checked it:** Evan and Jack  
**Feedback Provided:**  
*  Code comments and codes: Feedback highlighted that the project is clean, well built and easy to understand by users with very detailed comments. Nevertheless, while the codes and comments are well-written, Evan suggested that we can use the `dateutil` library to calculate age instead of doing it manually. Specifically mentioning that we can use `dateutil` instead of
```age_in_years = (datetime.now() - birthday_date).days // 365``` in line 71 of the add_student function within your student_functions.py file.


**Reflection and actions to do based on the feedback:**  

Upon reflection, the suggestion to use the `dateutil` library to calculate age will introduce a more accurate and robust method for handling date and time calculations. Currently, the manual calculation of age uses the division of the number of days by 365. It offers a good approximation but lacks precision for edge cases such as leap years and varying month lengths. Adopting *dateutil* would enhance the reliability and accuracy of the application, particularly for age-based classroom assignments.

Therefore, future actions can include implementing the `relativedelta` class from the `dateutil` libary to to handle differences between two dates or to manipulate dates by adding or subtracting specific time intervals. Unlike simple arithmetic operations, `relativedelta` accounts for calendar-based complexities, such as varying month lengths and leap years.  

Overall, implementing this feedback to enhance the application for future improvements involves further development and testing. These tests should focus on addressing various edge cases, including scenarios such as birthdays near the end of February (to ensure proper handling of leap years) and a variety of year-month combinations to validate accuracy across diverse date inputs. By incorporating these improvements, the application's reliability and accuracy will be enhanced, while also reducing redundant or repetitive code. This will align the functionality more closely with real-world scenarios, further strengthening its practical value.

## Feedback Instance 4

**Specific documentation checked:** Childcare Management App - README.md  
**Date of feedback received:** 06/12/2024  
**Who checked it:** Evan  

**Feedback Provided:**  
Evan reviewed the README.md file and praised it as being very well-written, informative, and comprehensive. The document clearly outlined laws and licensing, installation steps, and the purpose of the application. However, he suggested adding a more detailed explanation of how to clone or fork the repository, as this would improve accessibility for developers who may be less familiar with the process.

**Reflection and actions to do based on the feedback:**  

Upon reflection, the suggestion to expand the README.md with more detailed instructions for cloning or forking the repository is valuable for improving the usability of the documentation. While the current README.md file is thorough, this enhancement will ensure that developers of varying experience levels can seamlessly set up the project.

**Actions implemented to address feedback:**
1. **Expanded the "Cloning/Forking the Repository" Section in the project's [README](https://github.com/Donjella/ISK1001-assignment-3):**  
   - Included a step-by-step guide for cloning the repository using Git, including terminal commands.
   - Added instructions for forking the repository, with details on how to do so through GitHub's interface.
   - Provided screenshots to visually guide users through the process.


