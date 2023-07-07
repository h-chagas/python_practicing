# Nested while loop

building = 1

while building <= 5:
    print(f"The postman entered in the building {building}.")
    flat = 1
    while flat <= 7:
        print(f"The postman delivered mails to the flat n. {flat}")
        flat += 1
    print(f"The postman exited from the building {building}")
    building += 1
        