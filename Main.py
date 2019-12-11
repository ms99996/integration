"""__Author__= Miguel salinas"""
"""This is my attempt to create a mad lib """

ask = input("welcome to my mad lib, would you like to give it a try? enter "
            "yes or no, the answer is case sensitive: ")
while ask not in ("yes", "no"):
    ask = input("please type a valid input: ")


def get_answers(color, animal, body_parts, verb, verb2, verb3):
    """Creates a mad lib using inputs for variables inside argument. """
    print("there once was a", color, animal, "that had 3", body_parts,
          "it uses one part for", verb, "the next for", verb2,
          "and the last for", verb3)


def main():
    """Asks user age, and many questions to create a mad lib,"""
    if ask == "yes":
        age = int(input("wonderful, please enter your age: "))
        if age >= 16:
            print("your age is", age, "you are old enough to continue")
            color = input("please enter a color: ")
            animal = input("please enter an animal: ")
            body_parts = input("please enter a body part(plural): ")
            verb = input("please enter a verb that ends with 'ing': ")
            verb2 = input("please enter another verb that ends with 'ing': ")
            verb3 = input("please enter one more verb that end with 'ing': ")
            mad_libs = get_answers(color, animal, body_parts, verb, verb2, verb3)
            # I have get_answers to print the mad lib
            # I don't like how return outputs the mad lib
            print(mad_libs)
        else:
            print("sorry but you are not old enough to continue")
    else:
        print("thank you and have a nice day")


main()

