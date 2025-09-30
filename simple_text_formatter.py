# text = "lorem IPSUM world  "
# # text = " HELLO world"
# text = text.strip().capitalize() + "."
# print(text)


# print(text)  # Lorem ipsum world.
# print(text)  # Hello world.

person_in_room_1 = input("Enter the name of a person in the room: ").strip()
number_1 = input("Enter the last name of someone in the room: ").strip()
adjective_1 = input("Enter an adjective: ").strip()
color = input("Enter a color: ").strip()
noun_1 = input("Enter a noun: ").strip()
plural_type_of_food = input("Enter a plural type of food: ").strip()
noun_2 = input("Enter another noun: ").strip()
verb_ending_with_ing = input("Enter a verb ending with ING: ").strip()
article_of_clothing = input("Enter an article of clothing: ").strip()
adjective_2 = input("Enter another adjective: ").strip()
celebrity = input("Enter the name of a celebrity: ").strip()
number_2 = input("Enter another number: ").strip()
person_in_room_2 = input("Enter the name of another person in the room: ").strip()
noun_3 = input("Enter another noun: ").strip()
person_in_room_3 = input("Enter the name of one more person in the room: ").strip()
occupation = input("Enter an occupation: ")
story = f"""My name is {person_in_room_1} and I am {number_1} years old. If I were president, I'd do a whole bunch of {adjective_1} things:
1. I would drive the biggest {color} car in the country. And that car would go faster than any other {noun_1} in the world!
2. Everyone would eat pepperoni {plural_type_of_food} for dinner.
3. I would live in the Statue of {noun_2} and build a {verb_ending_with_ing} pool at her feet.
4. I would wear a/an {article_of_clothing} on my head... and everyone would say I look {adjective_2} like {celebrity}.
5. School would be open only {number_2} days a year.
6. I would give my friends the best jobs. I would nominate {person_in_room_2} to be secretary of (the) {noun_3}, and {person_in_room_3} could be vice {occupation}!"""
print(story)