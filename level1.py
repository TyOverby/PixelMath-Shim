# Asks the user a question.  Analyse the answer and gives a response
def level1():
    answer = raw_input("Do you like cats or dogs more: ")
    if "cat" in answer:
        print "I like cats more too"
    elif "dog" in answer:
        print "Dogs are cool, but not large dogs"
    else:
        print "Can't you read?"

level1()
