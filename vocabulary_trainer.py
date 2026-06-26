"""Simple Console Vocabulary Trainer.Swedish <-> English Translation Practice"""
import json
import random
import os
from pathlib import Path

# LOAD VOVABULARY FROM JSON.    
def load_vocabulary(filename="vocabulary.json"):

    file_path = Path(__file__).resolve().parent / filename

    if not file_path.exists():
        print(f"Error: {filename} not found!")
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
    
# NORMALIZE TEXT FOR COMPARISON: LOWERCASES, STRIP SPACES
def normalize_answer(text):
    return text.lower().strip()

# CHECK IS ANSWER MATCHES THE CORRECT ANSWER. 
def check_answer(user_answer, correct_answer):
    #Normalize both answers
    user = normalize_answer(user_answer)
    correct = normalize_answer(correct_answer)
    
    # Support multiple correct answers separated by '/' or ','
    correct_variants = [normalize_answer(variant) for variant in 
                       correct.replace(',', '/').split('/')]
    
    return user in correct_variants

    # Run a practice session
def practice_session(words, direction='swedish-english'):
    if not words:
        print("No words to practice!")
        return
    
    # Shuffle words for practice
    practice_words = words.copy()
    random.shuffle(practice_words)
    
    correct_count = 0
    incorrect_count = 0
    total = len(practice_words)
    
    print("\n" + "="*50)
    print("VOCABULARY PRACTICE SESSION")
    print("="*50)
    print(f"Total words: {total}")
    print(f"Direction: {direction}")
    print("\nType your answer and press Enter")
    print("Type 'skip' to skip a word")
    print("Type 'quit' to end session early")
    print("="*50 + "\n")
    
    # Determine question and answer based on direction
    for index, word in enumerate(practice_words, 1):
        if direction == 'swedish-english':
            question = word['swedish']
            correct_answer = word['english']
        else:
            question = word['english']
            correct_answer = word['swedish']
        
        # Show progress and question
        print(f"\n[{index}/{total}] Translate: {question}")
        user_answer = input("Your answer: ").strip()
        
        # Handle special commands
        if user_answer.lower() == 'quit':
            print("\nSession ended early.")
            break
        
        if user_answer.lower() == 'skip':
            print(f"⊘ Skipped (Correct answer: {correct_answer})")
            continue
        
        # Check answer
        if check_answer(user_answer, correct_answer):
            print("✓ Correct!")
            correct_count += 1
        else:
            print(f"✗ Incorrect. The correct answer is: {correct_answer}")
            incorrect_count += 1
    
    # Show final results
    answered = correct_count + incorrect_count
    percentage = (correct_count / answered * 100) if answered > 0 else 0
    
    print("\n" + "="*50)
    print("SESSION SUMMARY")
    print("="*50)
    print(f"Total words practiced: {answered}")
    print(f"Correct answers: {correct_count}")
    print(f"Incorrect answers: {incorrect_count}")
    print(f"Score: {percentage:.1f}%")
    print("="*50 + "\n")
    
def print_title_box():
    width = 34

    print()
    print("+" + "=" * width + "+")
    print("|" + "SIMPLE VOCABULARY TRAINER".center(width) + "|")
    print("|" + "SWEDISH <--> ENGLISH".center(width) + "|")
    print("+" + "=" * width + "+")
    print()

# MAIN PROGRAM
def main():
    print_title_box()
    
    # Load vocabulary
    words = load_vocabulary('vocabulary.json')
    
    if not words:
        return
    
    print(f"Loaded {len(words)} vocabulary words.\n")
    
    while True:
        print("\nChoose practice direction:")
        print("1. Swedish → English")
        print("2. English → Swedish")
        print("3. Quit")
        
        choice = input("\nYour choice (1-3): ").strip()
        
        if choice == '1':
            practice_session(words, 'swedish-english')
        elif choice == '2':
            practice_session(words, 'english-swedish')
        elif choice == '3':
            print("\nGoodbye! Happy learning! \n")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == '__main__':
    main()
