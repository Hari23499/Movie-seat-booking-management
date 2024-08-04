def layout_making():
    for i in range(1, 201):
        seat.append(i)


def layout_style():
    for i in range(len(seat)):
        print(seat[i], end="\t")
        if (i + 1) % 10 == 0:
            print()


def result():
    while True:
        n = int(input("How many seats do you need to book:-"))
        s = []
        for i in range(n):
            s.append(int(input("Enter seat number:-")))
        flag = 0
        for i in s:
            if i not in seat:
                flag = 1
                break
        if flag == 0:
            for i in s:
                seat[i - 1] = "BK"
            print("Your seats have been booked")
            print("--------------------NEW SEAT LAYOUT------------------")
            layout_style()
        else:
            print("All seats are not available")
        ch = input("Enter Y to continue and N to exit:-")
        if (ch == "Y" or ch == "y"):
            continue
        elif (ch == "N" or ch == "n"):
            break


seat = []
layout_making()
print("--------------------SEAT LAYOUT------------------")
layout_style()
result()
print("THANK YOU FOR BOOKING SEATS")