"""The same behaviour without a class, in the procedural style used in Units 1-5.

The data is a dictionary and the functions are separate from it,
so every function must be given the data it works on.
"""


def display(person):
    print(f"Name: {person['name']}, Age: {person['age']}")


def update_age(person, new_age):
    person["age"] = new_age


if __name__ == "__main__":
    person2 = {"name": "Alan", "age": 41}
    display(person2)
    update_age(person2, 42)
    display(person2)
