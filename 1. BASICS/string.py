# declaring variable and giving it a string value (words, texts)
name = "Aaliyah" # all strings are written in "quotations"
surname = "Jardien"

print("My name is", name + surname)
# print("My name is"(name + surname)) invalid syntax

# printing the which data type this variable is
print(type(name))

# fetching characters from a string
# using same range syntax but not range fucntion
# declaring variable with string
txt = "Hello World"

# declaring new variable that gets certain characters from the string
fetc = txt[0] #..returns first value of the string
              # must use square brackets when having range
print(fetc)

# get characters from index 2 to index 4 (ollo)
ftch = txt[2:5] # starts at 2nd indexed number and ends at 5th to show the 4th
                # use semi colon instead of comma, you use comma for range
print(ftch)

# note that a space is also counted in an index
# returns string without blankspace at beginning or end

txxt = "Hello World"

# getting texts back without the blankspaces
getxt = txxt.strip()

print(getxt)

# converting characters in a variable to uppercase
uptext = "hello WOrld"

# declaring a separate variable to put the characters in CAPS
uptext = uptext.upper()
# then printing
print(uptext)

# printing one time with the txt.upperfucntion
print(txxt.upper()) #this also works

# converting txt to lowercase
# putting function in print statement one time
print(txxt.lower())

# noice

# replacing a character within the string with a different character
# replace the h with a j

print(txxt.replace("H", "Hi H"))

# insert the correct contect to add a placeholder {} for the age parameter
# declaring variable with age
age = 20

# declaring variable with a string and adding a parameter
new_text = "My name is Aaliyah, and I am {} years old."

print(new_text.format(age))

# creating an input for the variable
# name and age input
your_name = (input("Please enter your name:"))

# your_age = int(input("Please enter your age:"))

your_text = "My name is {}"

# your_details = (your_name+your_age)

print(your_text.format(your_name))

# what does "find" do & how can i use it
