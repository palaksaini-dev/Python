print ("welcome to my computer quiz !")

play = input ("Do you want to play ? ")

if play.lower() != "yes":
    quit()

print ("Okay! Let's play :)")
score = 0


question = input ("what does CPU stand for ?")

if question.lower() == 'central processing unit':
    print ("Correct! ")
    score += 1
else :
    print ("Incorrect!")
    

question = input ("what does HTML stand for ?")

if question.lower() == 'hyper text markup language':
    print ("Correct!")
    score += 1
else :
    print ("Incorrect!")
    

question = input ("what does CSS stand for ?")

if question.lower() == 'cascading style sheet':
    print ("Correct!")
    score += 1
else : 
    print ("Incorrect!")
    

question = input ("what does RAM stand for ?")

if question.lower() == 'random access memory':
    print ("Correct!")
    score += 1
else :
    print ("Icorrect !")

question = input("Which programming language is known for its simple and readable syntax? ")

if question.lower() == 'python':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    

print ("your got" + str (score) + "questions correct!")
print ("your got" + str ((score / 5) * 100) + "%")