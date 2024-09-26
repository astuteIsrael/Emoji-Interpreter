#  Overview
This project provides a simple command-line tool to convert emoji aliases (e.g., :smile:, :heart:) into actual emojis. It uses the Python emoji library to translate human-readable emoji codes into the emoji symbols that can be displayed on most devices and platforms.

###  Prerequisites:
1. Python 3.x
2. emoji library

###  Installation
1. Clone the repository or download the program.
2. Install the required library using pip
   
##  Usage
To run the script, use the following steps:

1. Run the script in a Python environment:
  python emoji_converter.py

2. Enter a string that includes emoji aliases:
  Enter text with emoji aliases: Hello :wave:, how are you? :smile:

3. The script will output the text with actual emojis:
  Converted Text with emojis: Hello 👋, how are you? 😄

#  Example
Input: I love :pizza: and :smile:
Output: I love 🍕 and 😄

##  Notes:
Ensure the input text uses valid emoji aliases recognized by the emoji library. If the alias is incorrect or not supported, it will remain unchanged in the output.
A comprehensive list of supported emoji aliases can be found in the official emoji library documentation.
