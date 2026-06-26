# Language-Vocabulary-Translator
A simple console-based Swedish-English vocabulary trainer built with Python.

## Features

- Loads words from a JSON file
- Supports Swedish to English practice
- Supports English to Swedish practice
- Shows correct and incorrect answers
- Gives a final score summary

A lightweight, console-based vocabulary practice application for language learning. Currently configured for Swedish ⟷ English translation, but easily adaptable to any language pair.

🎯 Overview
Simple Vocabulary Trainer is a minimalist, terminal-based application designed to help language learners practice vocabulary translation. It provides an interactive quiz-style interface where users translate words between two languages, receive immediate feedback, and track their progress.

The application is perfect for:

Daily vocabulary practice
Quick review sessions
Building muscle memory for common words
Self-paced language learning
Offline vocabulary training

✨ Features
Core Functionality
✅ Bidirectional Translation Practice: Practice Swedish → English or English → Swedish
✅ Interactive Quiz Interface: One word at a time with immediate feedback
✅ Smart Answer Checking: Case-insensitive matching with support for multiple correct answers
✅ Progress Tracking: Real-time progress display (e.g., "Word 5 of 10")
✅ Session Statistics: Comprehensive summary with correct/incorrect counts and percentage score

User Experience
✅ Randomized Word Order: Words are shuffled for each session to improve retention
✅ Skip Functionality: Skip difficult words and see the correct answer
✅ Early Exit: End sessions anytime with quit command
✅ Clean Terminal UI: Simple, distraction-free interface with Unicode symbols

Flexibility
✅ JSON-Based Storage: Human-readable data format that's easy to edit
✅ Multiple Answer Variants: Support for synonyms (e.g., "hello / hi / hey")
✅ UTF-8 Support: Full support for special characters (å, ä, ö, ñ, etc.)
✅ No External Dependencies: Uses only Python standard library

🛠️ Technologies & Tools
Programming Language
Python 3.6+: Core language for the application
Standard Library Modules Used
json: Reading and writing vocabulary data to JSON files
random: Shuffling word order for randomized practice sessions
os: File system operations and path handling
Data Format
JSON: Lightweight, human-readable data storage format for vocabulary
Development Tools
Git: Version control
UTF-8 Encoding: For international character support

📥 Installation
Prerequisites
Python 3.6 or higher installed on your system
No external packages or dependencies required!
Steps
Clone the repository:
bash
Copy
git clone https://github.com/YOUR_USERNAME/simple-vocab-trainer.git
cd simple-vocab-trainer
Verify Python installation:
bash
Copy
python3 --version
Should output Python 3.6.0 or higher.
That's it! No additional installation needed.

💾 Data Storage
Storage Format: JSON
The application uses JSON (JavaScript Object Notation) for data storage, providing a simple, human-readable format that's easy to edit and maintain.

File: vocabulary.json
Location: Same directory as vocab_trainer.py

How Data is Saved
Storage Method: File-based JSON storage
Persistence: Vocabulary persists across application restarts
Encoding: UTF-8 for international character support
Manual Editing: You can directly edit vocabulary.json with any text editor

Answer Validation Algorithm
The check_answer() function performs smart answer validation:

Normalization: Both user input and correct answer are:
Converted to lowercase
Stripped of leading/trailing whitespace
Multiple Answer Support: Correct answers can contain multiple variants separated by /, ,, or ;
Example: "hello / hi / hey" accepts any of these answers
Comparison: Normalized user input is checked against all normalized correct variants

Extending Functionality
Easy modifications:

Add more vocabulary to vocabulary.json
Change language pairs by editing JSON keys
Adjust UI messages and formatting
Medium modifications:

Add statistics tracking across sessions
Implement a favorites/difficult words list
Add category/topic filtering
Advanced modifications:

Implement spaced repetition algorithm
Add audio pronunciation support
Create a web-based or GUI version
Add progress persistence across sessions

🚀 Future Enhancements
Potential features for future versions:

 Multi-language support (more than 2 languages)
 Persistent statistics tracking across sessions
 Spaced repetition algorithm (SRS)
 Difficulty levels and categorization
 Import/export functionality (CSV, Excel)
 GUI version (PyQt, Tkinter, or web-based)
 Audio pronunciation support
 Mobile app version
 Cloud synchronization
 Progress visualization and charts
 Timed practice mode
 Accent/diacritic normalization options
