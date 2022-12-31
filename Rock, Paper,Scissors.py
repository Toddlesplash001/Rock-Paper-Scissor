import random
game = ['Rock', 'Paper', 'scissor']
user_score = 0
computer_score = 0
while True:
    a = random.choice(game)
    if a == 'Rock':
        print("Whats your choice?")
        b = input()
        if b.lower() == "rock":
            print("You tied")
        if b.lower() == "scissor":
            print("You lost. Better luck next time .")
            computer_score+=1
        if b.lower() == "paper":
            print("You won.You are a legend ")
            user_score+=1
    if a == 'Paper':
        print("Whats your choice?")
        b = input()
        if b.lower() == "paper":
            print("You tied")
        if b.lower() == "rock":
            print("You lost. Better luck next time ")
            computer_score+=1
        if b.lower() == "scissor":
            print("You won.You are a legend ")
            user_score+=1
    if a == 'scissor':
        print("Whats your choice?")
        b = input()
        if b.lower() == "scissor":
            print("You tied")
        if b.lower() == "paper":
            print("You lost. Better luck next time ")
            computer_score+=1
        if b.lower() == "rock":
            print("You won.You are a legend ")
            user_score+=1
    
    c = input("Do you want to continue? (y/n):")
    if c.lower() =="y":
        continue
    else:
        print("Your score is", user_score)
        print("The computer's score is", computer_score)
        if user_score>computer_score:
            print("You won overall")
        elif user_score==computer_score:
            print("You tied overall")
        elif user_score<computer_score:
            print("You lost overall")
        break
            
        
            
            
