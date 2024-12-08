# Feedback Provided

## Feedback 1

**Specific documentation checked:** Documentation for the D&D dice-rolling application by Ben and Andrea  
**Date of feedback provided:** 04/12/2024  
**Who checked it:** Tanya Chukau and Brendon Ang  

**Feedback Provided:**  

Feedback is based on its usefulness and ethical considerations.

### Usefulness:
1. The detailed setup instructions and module breakdown are highly beneficial, especially for developers unfamiliar with Python or terminal apps. However, the inclusion of platform-specific setup instructions (e.g., Linux/macOS) would enhance the application further.  

2. In the introduction, it states, “wish to make a check they roll 2d20” – for someone unfamiliar with the term `2d20`, it would be useful to describe what `2d20` means.

### Ethical Considerations:
1. Industry-relevant standards, such as proper licensing and inclusivity, are partially addressed but need further emphasis to align with the **Copyright Act 1968** and the **Disability Discrimination Act 1992**. Potential copyright issues relate to the use of intellectual property (IP) from Dungeons & Dragons, owned by Wizards of the Coast.  

2. **PEP8:** According to industry best practices, PEP8 advises keeping code at 79 characters or fewer per line and suggests a maximum of 72 characters for inline comments and docstrings. For example, in your code comments, the comment above the `advantage_disadvantage_menu()` function has 225 characters.  

3. **ACM/IEEE Software Engineering Code of Ethics and Professional Practice:** Relevant guidelines/laws/regulations could be mentioned to explain how the dice rolls are unbiased in their randomness.  

### Actions recommended based on feedback with proposed solutions and changes

1. **Proofread and Correct Documentation:** Assign someone to proofread or use tools like Grammarly to refine the documentation. This will also improve accessibility for users.  

2. **Clarify Platform Support:** Possibly include instructions for macOS/Linux for inclusivity.  

3. **Check Copyright Laws and OGL for D&D:** Use terms like “D&D-inspired” or “Tabletop RPG Dice Roller” to clarify that your app is not officially associated with Wizards of the Coast. While certain elements of D&D are protected by copyright, parts of the D&D system are released under the Open Gaming License (OGL), which allows for some use in third-party creations.  

4. **Explanation of Terms:** Providing a clear explanation of terms like `d6` and `d8` (e.g., `d6` refers to a 6-sided die, `d8` refers to an 8-sided die) at the beginning of your documentation or in a prominently visible section would help clarify their meaning for readers. Explicitly stating that the app is unofficial and not endorsed by Wizards of the Coast would clarify to users that the app is independently developed. This avoids misleading users about the origin or endorsement of the app and supports transparency about ownership and affiliation.  

5. **PEP8 Guidelines and Industry Best Practices:** Review the code to ensure the following:  
   - “PEP8 advises keeping code at 79 characters or fewer per line and suggests a maximum of 72 characters for inline comments and docstrings. If your comment is approaching or exceeding that length, then you’ll want to spread it out over multiple lines.”  

6. **Unbiased Dice Rolls:** The ACM/IEEE Software Engineering Code of Ethics and Professional Practice principle 1.3 supports ensuring that the software functions as intended (e.g., random number generation for fair rolls in your game) without misleading or harming users. Hence, this and other relevant laws/regulations/guidelines may be added to support your project’s ethical consideration of fairness and bias. **ISO/IEC 25010:2011 (Software Quality Model):** Reliability and functionality are key attributes under this standard, ensuring software provides consistent and accurate results, such as unbiased dice rolls.

---

**What Was Done Well:**

1. **Comprehensive Dice Functionality:** The app’s functionality to simulate various dice rolls, ranging from standard D&D dice to rolling with advantage and disadvantage options, effectively captures the essential mechanics of Dungeons & Dragons. This feature allows players to seamlessly integrate the app into their campaigns, saving time and reducing complexity during gameplay.

2. **Cheat Sheet Feature:** The cheat sheet function is an excellent addition to the app, allowing users to quickly reference dice combinations needed for specific actions or abilities. This reduces downtime during the game and helps players focus more on the narrative and strategy.

3. **User-Friendly Interface:** The integration of the `colored` module to make terminal outputs visually appealing and easy to follow is a great design choice. It enhances readability and user experience.

4. **Practical Use of JSON for Saving Combinations:** The use of JSON to save and load dice combinations demonstrates good practice in managing data within the app. This feature is particularly useful for users who want to save their custom dice combos for future use, making it more convenient during campaigns.

## Feedback 2

# Feedback Provided

## Feedback 2

**Specific Documentation Checked:** Documentation for Tilley’s currency converter app  
**Date of Feedback Provided:** 04/12/2024  
**Who Checked It:** Tanya Chukau and Brendon Ang  

**Feedback Provided:**  

Feedback is based on usefulness and ethical considerations.

### Usefulness and Ethical Considerations:
1. **User-Friendly Error Handling:** Incorporating error messages for invalid currency codes will improve the app’s usability, particularly for users who may not be familiar with currency codes. This approach ensures users know exactly what went wrong, fostering a positive experience and increasing user confidence in the app.  

2. **Module-Level Docstring:** While the top-level docstring "This class module captures the from_currency, to_currency, amount, rate, and description of the conversion item." provides details on what the module/file contains, it can be expanded to better summarise the overall content of the module/file.  

3. **Clarity on the Class:** The current docstring describing the class states, “This class represents a currency conversion.” This could be expanded for better clarity and detail.  

4. **Ethical Data Handling:** Including a section in the README that explains how the app ensures fair exchange rates and outlines how users' data is managed addresses important ethical concerns such as transparency and privacy. Ethical data handling is essential for maintaining user trust and adhering to relevant regulations, including the **General Data Protection Regulation (GDPR)** and the **Privacy Act 1988** in Australia. These regulations safeguard personal information and require transparency in data collection and processing. Ensuring compliance with these regulations ensures the app meets legal obligations and respects user privacy.

---

### Actions recommended based on feedback with proposed solutions and changes
1. **Error Handling:** To improve the user experience, consider adding user-friendly error messages in the `CurrencyConverter` class. This update could reduce user frustration and enhance their experience.  

2. **Ethical Considerations in README:**  
   - Add a section in the README that explains how the app ensures fair exchange rates, such as outlining the sources and methods used to determine these rates.  
   - Briefly explain how user data is handled, particularly in compliance with privacy laws like the GDPR and the Privacy Act 1988. These laws require clear communication about how data is processed and stored, ensuring the application is both legally compliant and trustworthy.  

3. **Module-Level Docstring:** Expand the docstring to include a more detailed description. For example:  
   *“This module defines a `ConversionItem` class that encapsulates the details of a currency conversion. It includes attributes such as the source and target currencies, the amount to be converted, the exchange rate applied, and a description of the transaction. It also provides methods to return the conversion details as a JSON dictionary and as a styled string for terminal output.”*  

4. **Clarity on the `ConversionItem` Class:** The class docstring could be updated to distinguish it as a data structure rather than a function performing the conversion. The core functionality of currency conversion lies in the `currency_converter_functions.py` module. Suggested docstring:  
   *“This class represents a currency conversion structure, encapsulating details about a specific transaction. This class provides attributes to store information about the currencies involved, the amount to be converted, the exchange rate applied, and an optional description of the transaction.”*

---

**What Was Done Well:**  

1. **User-Friendly Interface:** The app has a great interface, making it easy for users to quickly understand how to convert currencies without unnecessary confusion. It is clear and straightforward to use, which is great for user experience and accessibility.  

2. **Efficient Currency Conversion:** The conversion process is quick and efficient, providing real-time results without delays. This is essential for users needing accurate and fast conversions, especially while travelling.  

3. **Clean and Well-Structured Code:** The code is well-organised and easy to follow. The classes and methods are clearly defined, making it simple to maintain and extend in the future if needed.  

4. **Great Use of Object-Oriented Programming:** The app demonstrates strong use of object-oriented principles. The `CurrencyConverter` class provides a clear and modular way of handling currency data. This structure will be beneficial for adding additional features or currencies in the future, such as support for cryptocurrencies or a larger variety of currencies.  

5. **Consistent Formatting:** The README file uses consistent formatting, enhancing readability. Code snippets, headings, and bullet points are well-presented, keeping the document clean and professional. The README provides a clear and concise overview of the app's purpose and functionality, making it easy for new users to understand what the app does right away.  

6. **Well-Structured Documentation:** The structure of the README is well-organised. Sections such as installation and usage instructions are arranged nicely, ensuring users can easily navigate through the document.
