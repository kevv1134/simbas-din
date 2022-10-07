import random
#Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number_names = len(names)
random_choice = random.randint(0, number_names - 1)
person_paying = names[random_choice]
print(f"{person_paying} is paying")
