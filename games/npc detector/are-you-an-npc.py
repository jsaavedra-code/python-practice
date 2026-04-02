# This program detects if you are an NPC or you are a main character (basic)
# Please answer the following questions to find out

print("Welcome to the Basic NPC Detector")
print("This program will ask you a series of questions to determine if you are an NPC (Non-Player Character) or a main character in your own life.")
print("Press Enter to start the test.")
input()  # Wait for the user to press Enter
score =0

# The questions  1 to 5 will be answered with "yes" or "no". Please answer honestly for the most accurate result.
print("Please answer the following questions with 'yes' or 'no'.")

# Question 1
print("Do you question why you do what you do?")
answer1 = input().lower()
if answer1 == "yes":
    score += 1

# Question 2
print("Have you ever changed an important opinion through your own thinking?")
answer2 = input().lower()
if answer2 == "yes":
    score += 1

# Question 3
print("Do you feel comfortable doing something just because 'everyone else is doing it?'")
answer3 = input().lower()
if answer3 == "no":
    score += 1

# Question 4
print("Do you notice patterns in the way others behave?")
answer4 = input().lower()
if answer4 == "yes":
    score += 1

# Question 5
print("Do you care more about understanding than just being right?")
answer5 = input().lower()
if answer5 == "yes":
    score += 1

# The questions 6 to 10 will be open questions.
# The answers will be scored based on the depth of thought and self-awareness they demonstrate.
# Please answer honestly for the most accurate result.
main_character_words = ["because", "since", "i prefer", "i think", "i feel", "i feel like", "i believe",
"in my case", "for me", "it depends, but", "although", "however", "though", "except", "unless", "usually",
"sometimes", "lately", "recently", "what matters to me", 'i value', "i care about", "i am into", "i realized", 
"what i mean", "i noticed", "i used to", "the reason is", "i guess, but",]

npc_words = ["idk", "i don't know", "whatever", "normal", "anything", "everything", "nothing",
"just chilling", "having fun", "hanging out", "listening to music", "the usual", "same as everyone", "not much",
"i guess", "maybe", "i'm fine", "i'm good", "i'm okay", "just because", "all kinds of things", "stuff", "things", 
"i just like",]

print("Now, please answer the following open-ended questions.") 
print("Your answers will be scored based on the depth of thought and self-awareness they demonstrate.")

# This function evaluates the answer based on the presence of certain keywords that indicate a main character or NPC mindset.
def evaluate_answer(answer):
    main_count = 0
    npc_count = 0

    for word in main_character_words:
        if word in answer:
            main_count += 1   
    for word in npc_words:
        if word in answer:
            npc_count += 1

    if main_count - npc_count >= 2:
        return 1  # Main character
    elif npc_count - main_count >= 2:
        return -1 # NPC
    else:
        return 0 # Neutral

# Question 6
print("What do you like to do in your free time? and why?")
answer6 = input().lower()
score += evaluate_answer(answer6)

# Question 7
print("What do you like about yourself, but what would you like to change?")
answer7 = input().lower()
score += evaluate_answer(answer7)

# Question 8
print("What do you do when you want something but it doesn't make sense?")
answer8 = input().lower()
score += evaluate_answer(answer8)

# Question 9
print("What do you do when you are bored?")
answer9 = input().lower()
score += evaluate_answer(answer9)

# Question 10
print("Why did you choose to study what you are studying or work in the field you are working in?")
answer10 = input().lower()
score += evaluate_answer(answer10)

# Final result
print("Analyzing your existance...")
if score >= 8:
    print("Congratulations! You are a main character.")
elif score >= 4:
    print("You are mid, check that out.")
else:
    print("NPC detected, womp womp.")
