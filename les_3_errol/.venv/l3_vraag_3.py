payments = ("online","offline")
x = True
print("Shopping Cart")

while x:
    payment = input("Payment method? [Online/Offline]: ")

    if payment.lower() not in payments:
        print("Unknown input, try again.")
        continue

    if payment.lower() == payments[0]:
        print(f"{payment.capitalize()}, place purchase order")
        y = True
        while y:
            online_answer_1 = input("Admin User? [Yes/No]: ")
            if online_answer_1.lower() == "yes":
                print("Enter payment details")
                print("Place Order")
                y = False
                x = False
            elif online_answer_1.lower() == "no":
                z = True
                while z:
                    online_answer_2 = input("Approval rules? [Approved/Rejected]: ")
                    if online_answer_2.lower() == "approved":
                        print("Enter payment details")
                        print("Place Order")
                        z = False
                        y = False
                        x = False
                    elif online_answer_2.lower() == "rejected":
                        print("Purchase Order Rejected")
                        z = False
                        y = False
                    else:
                        print("Unknown input, try again.")
                        continue
            else:
                print("Unknown input, try again.")
                continue

    if payment.lower() == payments[1]:
        print(f"{payment.capitalize()}, place purchase order")
        y = True
        while y:
            offline_answer_1 = input("Admin User? [Yes/No]: ")
            if offline_answer_1.lower() == "yes":
                print("Order created automatically")
                y = False
                x = False
            elif offline_answer_1.lower() == "no":
                z = True
                while z:
                    online_answer_2 = input("Approval rules? [Approved/Rejected]: ")
                    if online_answer_2.lower() == "approved":
                        print("Order created automatically")
                        z = False
                        y = False
                        x = False
                    elif online_answer_2.lower() == "rejected":
                        print("Purchase Order Rejected")
                        z = False
                        y = False
                    else:
                        print("Unknown input, try again.")
                        continue
            else:
                print("Unknown input, try again.")
                continue