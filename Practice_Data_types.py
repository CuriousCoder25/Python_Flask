#day 3
#Lists, tuples, dictionaries, and sets

# Tuple
# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.

# Example
summer_fruits = ("WaterMelon","Mango", "Lychee", "Gooseberry")

print(summer_fruits)
print(len(summer_fruits))
print(summer_fruits[0])

#there are different formats in which tuple's elements can be displayed
print("\n")
summer_fruitsl = ["Pineapple", "Papaya", "Muskmelon", "Jamun", "Plum"]

print(summer_fruitsl)
print(len(summer_fruitsl))
print(summer_fruitsl[3],"\n")

for n in summer_fruitsl:
    i=0
    print(summer_fruitsl[i])
    i=i+1

    #slicing - range