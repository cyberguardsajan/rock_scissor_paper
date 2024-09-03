import random

# Initialize scores
win_score = 0
loose_score = 0
draw_score = 0

# Number of rounds
num_rounds = 100

# Game loop
for i in range(num_rounds):
    # Make computer choice
    computer_random_num = random.randint(0, 2)
    if computer_random_num == 0:
        computer_choice = "Scissor"
    elif computer_random_num == 1:
        computer_choice = "Paper"
    elif computer_random_num == 2:
        computer_choice = "Rock"

    # Make my choice
    my_input = input("""
Enter the following according to your choice:
s for scissor
p for paper
r for rock

Enter: """)

    # Map input to choice
    if my_input == "s":
        my_choice = "Scissor"
        my_input_num = 0
    elif my_input == "p":
        my_choice = "Paper"
        my_input_num = 1
    elif my_input == "r":
        my_choice = "Rock"
        my_input_num = 2
    else:
        print("ERROR: Invalid input! Please enter 's', 'p', or 'r'.")
        continue  # Skip the rest of the loop and ask for input again

    # Print choices
    print(f"""
                Yours       VS       Computer
        [-------------------|-----------------------------]
        [                   |                             ]
             {my_choice}            {computer_choice}        
        [                   |                             ]
        [___________________|_____________________________]
        """)

    # Determine result
    if my_input_num == computer_random_num:
        print("Draw")
        status = "draw"
    elif (my_input_num == 0 and computer_random_num == 2) or \
         (my_input_num == 1 and computer_random_num == 0) or \
         (my_input_num == 2 and computer_random_num == 1):
        print("You win")
        status = "win"
    else:
        print("You lose")
        status = "lose"

    # Update scores
    if status == "win":
        win_score += 1
    elif status == "lose":
        loose_score += 1
    else:
        draw_score += 1

# Print final scores
print(f"""
Final Scores:
Wins: {win_score}
Losses: {loose_score}
Draws: {draw_score}
""")
