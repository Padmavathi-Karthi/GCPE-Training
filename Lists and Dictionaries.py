# Lists
list_1 = ["bacon", "eggs", "cheese"]

list_2 = [
  "banana",
  "pasta",
  "kiwi",
  "mango"
]

print(list_1)
print("What is your favourite breakfast food?")
new_food = input()
list_1.append(new_food)  # "append() will add new items at last in the list"
print(list_1)

list_1.remove("eggs")   #  "remove() will remove specific item"
list_1.pop()            #   "pop() will remove the last item"

# Exercise Group: Method 1
"""Write a program that takes the following inputs:
list item 1
list item 2
list item 3
And then adds all three items to a list called shopping_list, which contains no other items. The input prompts don't matter but it should only ask for three items, one after the other.
Finally, you should print the shopping_list data structure.
print(list_1)"""

list_item_1 = input()
list_item_2 = input()
list_item_3 = input()

shopping_list = [list_item_1, list_item_2,list_item_3]
print(shopping_list)
new_items = input("Add more items!: ")
shopping_list.append(new_items)
print(shopping_list)

# Exercise Group: Method 2, increment, an example of using a counter
shopping_list1 = []
counter = 0
while counter < 20:
  item_2 = input('what do you need?')
  shopping_list1.append(item_2)
  counter = counter + 1

print(shopping_list1)


# Dictionaries
dictionary_1 = {
  "Computer Program": "A series of instructions that can be executed by a computer",
  "Syntax": "The rules we create for computers and programmers to follow to avoid ambiguity and give strict meanings",
  "Programming Language": "A formal set of syntax for writing a computer program"

}

dictionary_2 = {
  "pilot": "James",
  "co-pilot": "Paul",
  "stewards": [
    "Peter",
    "Carol",
    "Jane"
  ],
  "breakfast": list_2,
  "passengers": 203
}