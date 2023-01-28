# continue statement
#  stops curent iteration and contuines with next

# declaring variable
num = 0 # index, will start from 0

# while statement w continue
while num < 6:
    num += 1 # incrementing by 1
    if num == 3: #it's not going to show 3, but it will show the others
        continue
    print(num)  # prints..1 2 4 5 6
