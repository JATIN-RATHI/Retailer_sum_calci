if __name__ == '__main__':
    print("PRESS 'q' to get the sum of all value entered.\n")
    sum = 0
    while True:
        num = input("\nEnter the price of item : ").capitalize()
        if num == "Q":
            print(f"Total amount to be paid is {sum} \n\t Thankyou for shopping")
            break
        else:
             sum += int(num)
             print(f"Order Total : {sum}")
