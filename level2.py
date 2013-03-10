# Asks the user a question.  Analyse the answer and gives a response
def level1():
    answered = False
    while answered is not True:
        answer = raw_input("Do you like cats or dogs more: ")
        if "cat" in answer:
            print "I like cats more too"
            answered = True
        elif "dog" in answer:
            print "Dogs are cool, but not large dogs"
            answered = True
        else:
            print "That isn't an answer.  Try again"
level1()
