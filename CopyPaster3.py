import pyperclip
import re
import keyboard
import time

def increment_number_with_padding(number_str):
    """Increments the numeric part of a string, preserving any leading zeros."""
    padding = ''
    for char in number_str:
        if char == '0':
            padding += char
        else:
            break
    
    number_part = number_str[len(padding):]
    incremented_number = int(number_part) + 1
    
    incremented_number_str = padding + str(incremented_number)
    
    return incremented_number_str

def handle_clipboard_update(e):
    """Listens for the 'V' key press event and updates the clipboard content by incrementing the last number."""
    if e.event_type == 'down' and e.name.lower() == 'v':
        time.sleep(0.1)  # Ensures clipboard content is current
        
        current_clipboard_content = pyperclip.paste()
        
        parts = current_clipboard_content.split("-")
        last_part = parts[-1]

        number_str = re.search(r'\d+$', last_part).group()
        incremented_number_str = increment_number_with_padding(number_str)

        parts[-1] = re.sub(r'\d+$', incremented_number_str, last_part)

        new_clipboard_content = "-".join(parts)
        pyperclip.copy(new_clipboard_content)

keyboard.on_press(handle_clipboard_update)
print("Listening for 'V' key press; increments the last number after '-' in the clipboard content on each 'V' press.")
print("Press 'F12' to exit the program.")

keyboard.wait('f12')