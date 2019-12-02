# Miguel Salinas
# this is my attempt at a madlib 
ask = input("welcome to my madlib, would you like to give it a try? enter yes or no, the answer is case sensitive: ")
while ask not in ("yes", "no"):
    ask = input("please type a valid input: ") 

def getAnswers(color,animal,bodyParts,verb,verb2,verb3):
    print("there once was a",color, animal, "that had 3",bodyParts, " it uses one part for ", verb, "the next for ",verb2,"and the last for",verb3)
def main():
    if (ask == "yes"):
        Age = int(input("wonderfull, please enter your  age: "))
        if(Age >= 16):
            print (" your age is", Age, "you are old enough to continue")
            Color =input("please enter a color: ")
            Animal =input("please enter an animal: ")
            Bodyparts =input("please enter a bodypart(plural): ")
            Verb =input("please enter a verb that ends with 'ing': ")
            Verb2 =input("please enter another verb that ends with 'ing': ")
            Verb3 =input("please enter one more verb that end with 'ing': ")
            makeMadLib = getAnswers(Color,Animal,Bodyparts,Verb,Verb2,Verb3)
            print(makeMadLib) 
        else:
            print("sorry but you are not old enough to continue")
    else:
        print("thank you and have a nice day")

main()
