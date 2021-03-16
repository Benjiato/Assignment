# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combinedname=name1 + name2
lower_string_name=combinedname.lower()

t=lower_string_name.count("t")
r=lower_string_name.count("r")
u=lower_string_name.count("u")
e=lower_string_name.count("e")

true= t+r+u+e

l=lower_string_name.count("l")
o=lower_string_name.count("o")
v=lower_string_name.count("v")
e=lower_string_name.count("e")

love=l+o+v+e
true_love= str(true) + str(love)

print(f"your true love score is {true_love}%")
