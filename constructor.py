class Dog:
    # Class Attribute
    species = 'mammal'

    # Constructor / Initialization Method
    def __init__(self, name, age):
        # Instance Attributes
        self.name = name
        self.age = age

# Creating Dog objects
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

# Accessing instance attributes
print("Philo is {} years old, and Mikey is {} years old.".format(
    philo.age, mikey.age))

# Checking if Philo is a mammal
if philo.species == "mammal":
    print("{} is a {}!".format(philo.name, philo.species))
