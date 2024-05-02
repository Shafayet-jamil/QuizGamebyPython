print('Do you want to play Quiz Game?') 
decission = input("Write yes or no to play Quiz Game: ")
score = 0
total_question =7
if decission.lower() == "yes":
    print("Let's start Quiz Game: ")

    answer = input("1. What is the capital of Bangladesh? ")
    if answer.lower() == "Dhaka":
        print("Correct answer")
        score+=1
    else:
        print("Wrong answer")

    answer = input("2. What is the largest sea beach in the world? ")
    if answer.lower() == "Cox's Bazar":
        print("Correct answer")
        score+=1
    else:
        print("Wrong answer")    

    answer = input("3.What is computer? ")
    if answer.lower() == "Device":
        print("Correct answer")
        score+=1
    else:
        print("Wrong answer")
    
    answer = input("4.Best mobile game in the world? ")
    if answer.lower() == "Free Fire":
        print("Correct answer")
        score+=1
    else:
        print("Wrong answer")


    answer = input("5.Who is the all time gretest man in the world? ")
    if answer.lower() == "Mohammad SWA":
        print("Correct answer")
        score+=1
    else:
        print("Wrong answer")


    answer = input("6.What is the main weakness of you? ")
    if answer.lower() == "Procastination":
        print("Correct answer")
        score+=1
    else:
        print("Wrong answer")


    answer = input("7.Your favourite mobile? ")
    if answer.lower() == "Walton":
        print("Correct answer")
        score+=1
    else:
        print("Wrong answer")

else: 
    print("As your wish!")      

print("Your total score is: " + str(score))

#calculate the total percentage of the score
percent = (score/total_question)*100
#print the total percentage of the score
print("You got " + str(percent) + "% Marks")