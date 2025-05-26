import random

# List of tuples containing (medical_term, definition)
flashcards = [
    ("Hypertension", "High blood pressure, which can lead to heart disease."),
    ("Aneurysm", "An abnormal bulge or ballooning in the wall of a blood vessel."),
    ("Osteoporosis", "A condition where bones become brittle and fragile from loss of tissue."),
    ("Arthritis", "Inflammation of one or more joints, causing pain and stiffness."),
    ("Cardiomyopathy", "Disease of the heart muscle that makes it harder for the heart to pump blood."),
    ("Diabetes", "A disease that occurs when your blood glucose, also called blood sugar, is too high."),
    ("Hepatitis", "Inflammation of the liver, often caused by a viral infection."),
    ("Anemia", "A condition where you don't have enough healthy red blood cells to carry adequate oxygen to your body's tissues."),
    ("Sepsis", "A life-threatening condition caused by an infection that spreads throughout the body."),
    ("Asthma", "A condition in which your airways narrow and swell and may produce extra mucus.")
]

def start_quiz():
    score = 0
    random.shuffle(flashcards)  # Shuffle the flashcards to randomize the order of questions
    total_questions = len(flashcards)

    print("Welcome to the Medical Terminology Flashcard Quiz!")
    print("Try to match the correct definition to the medical term.\n")

    for i, (term, correct_definition) in enumerate(flashcards, 1):
        print(f"Question {i}: What is the definition of '{term}'?")
        
        # Show all possible options
        print("\nOptions:")
        options = random.sample([correct_definition] + [definition for _, definition in flashcards if definition != correct_definition], 3)
        random.shuffle(options)
        
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
        
        # Get user's answer
        try:
            answer = int(input("Your answer (1/2/3): "))
            if options[answer - 1] == correct_definition:
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect! The correct answer is: {correct_definition}\n")
        except (ValueError, IndexError):
            print("Invalid input. Please choose a valid option.\n")

    # Final Score
    print(f"Your final score: {score}/{total_questions}")
    print("Thanks for playing!")

if __name__ == "__main__":
    start_quiz()