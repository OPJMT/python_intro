types = ("adult","child")
x = True
print("Patient exposed to TB")

while x:
    type = input("Is the patient an adult or a child? [Adult/Child]: ")

    if type.lower() not in types:
        print("Unknown input, try again.")
        continue

    print(type.capitalize())

    if type.lower() == types[0]:
        y = True
        while y:
            adult_answer_1 = input("Has common TB symptoms? [Yes/No]: ")
            if adult_answer_1.lower() == "yes":
                print("Treat as likely TB patient and perform full TB exam")
                y = False
                x = False
            elif adult_answer_1.lower() == "no":
                print("Have patient report back if unwell; return in 1 month for checkup")
                y = False
                x = False
            else:
                print("Unknown input, try again.")
                continue

    if type.lower() == types[1]:
        y = True
        while y:
            child_answer_1 = input("Can TB test be given? [Yes/No]: ")
            if child_answer_1.lower() == "yes":
                print("Administer TB test")
                print("Assess TB test results and child's condition")
                y = False
                x = False
            if child_answer_1.lower() == "no":
                z = True
                while z:
                    child_answer_2 = input("Child well? [Yes/No]: ")
                    if child_answer_2.lower() == "yes":
                        print("6 months preventive isoniazid")
                        print("Have parent bring in if child shows any symptoms")
                        z = False
                        y = False
                        x = False
                    if child_answer_2.lower() == "no":
                        print("Take full history. \nExamine for TB")
                        print("If TB likely diagnosis, treat for TB")
                        print("If other diagnosis more likely, treat as needed and watch for TB symptoms")
                        z = False
                        y = False
                        x = False
                    else:
                        print("Unknown input, try again.")
                        continue
            else:
                print("Unknown input, try again.")
                continue