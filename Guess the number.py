#n=18
#Number of guesses=9
#Print the number of guesses left
#No of guesses he took
#Game over

n=18
for i in range(9):
    num=int(input("Enter the number\n"))
    chances_left=8-i
    if num==n:
        print("Congrats! you entered a right number")
        break
    if chances_left == 0:
        print("Game Over")
    else:

        print("Try again!!")
        print("No.of chances left",8-i)
        continue
print("No.of chances you took",i+1)

#output
'''Enter the number
23
Try again!!
No.of chances left 8
Enter the number
12
Try again!!
No.of chances left 7
Enter the number
34
Try again!!
No.of chances left 6
Enter the number
23
Try again!!
No.of chances left 5
Enter the number
12
Try again!!
No.of chances left 4
Enter the number
34
Try again!!
No.of chances left 3
Enter the number
34
Try again!!
No.of chances left 2
Enter the number
23
Try again!!
No.of chances left 1
Enter the number
23
Game Over
No.of chances you took 8

Process finished with exit code 0'''
