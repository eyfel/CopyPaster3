# Number-Booster

Screen Text Incrementer
---

**Overview**

The Screen Text Incrementer is a Python-based utility tool designed to automate the process of incrementing numerical values within text copied to the clipboard. By listening for specific keyboard inputs and manipulating clipboard content, it simplifies tasks that involve sequential numbering or updating numerical data in texts. This script is particularly beneficial for professionals working with document numbering, inventory management, or any area requiring systematic numerical adjustments, enhancing efficiency and accuracy with minimal effort.

**Features**

- **Automatic Number Incrementation:** Identifies and increments the last number found in clipboard text, preserving formatting and leading zeros.
- **Keyboard Integration:** Listens for the 'V' key press to trigger number incrementation, facilitating easy and immediate updates.
- **Clipboard Management:** Directly interacts with the system's clipboard, making the incremented number immediately available for pasting.
- **Real-time Activation:** Operates in the background, ready to increment numbers upon a single keystroke, without disrupting ongoing tasks.
- **Easy Termination:** Allows the user to exit the script by pressing the 'F12' key, ensuring control and convenience.

**Executable Version**

The Screen Text Incrementer is also available as a standalone executable program, packaged with PyInstaller for ease of use without the need for a Python environment. This makes it accessible for users who prefer a direct application experience.

- **No Python Setup Required:** Users can run the executable directly from the `dist` directory, eliminating the need for Python installation and library setup.
- **Simple Execution:** The executable provides the same functionality as the script, with no additional configuration needed.

**Dependencies**

- **Python:** Requires Python 3.x for its execution.
- **pyperclip, re, keyboard, time:** Necessary libraries for script operation, bundled into the executable.

**Installation**

1. **Executable Use:** Download the executable from the `dist` folder within the GitHub repository. No installation or Python setup is required for the executable version.

2. **For Python Script:**
   - Ensure Python 3.x is installed on your system.
   - Install the necessary Python libraries using pip: `pip install pyperclip keyboard`

**Usage**

- **Executable Version:** Double-click the executable file in the `dist` directory to start the program. Press 'V' to increment numbers and 'F12' to exit.
- **Python Script:** Run the script in your Python environment. Adjust as necessary for your use case.

**Contributing**

Contributions are highly appreciated. Feel free to fork the repository, make improvements, and submit pull requests. Whether it's refining the logic, enhancing usability, or reporting bugs, your input is valuable in improving this tool for everyone.

**License**

This script is distributed under the MIT License, offering freedom for personal and commercial use, modification, and distribution, provided that the original copyright and license notice are included in all copies or substantial portions of the software.
