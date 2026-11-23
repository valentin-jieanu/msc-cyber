"""From procedural to object-oriented programming.

The Person class from the tutor's notes (classes.pdf, 23 Nov 2026).
Run 1 uses the values from the notes. Run 2 changes the name and the age.
"""


class Person:
    """A person: the data (name, age) and the methods that work with it, in one place."""

    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age    # instance attribute

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def update_age(self, new_age):
        self.age = new_age


if __name__ == "__main__":
    print("Run 1: values from the notes")
    person1 = Person("Eve", 30)
    person1.display()
    person2 = Person("Adam", 99)
    person2.display()
    person2.update_age(15)
    person2.display()

    print()
    print("Run 2: name and age changed")
    person1 = Person("Grace", 85)
    person1.display()
    person2 = Person("Alan", 41)
    person2.display()
    person2.update_age(42)
    person2.display()
