class Dog:
    # class variable
    species = "Canine"
    def __init__(self,name,breed):
        #instance variables
        self.name = name
        self.breed = breed

dog_1 = Dog('Buddy','Golden Retriever')
dog_2 = Dog('Luna','French Bulldog')
print(dog_1.name)
print(dog_2.species)
print(dog_2.breed)
print(dog_1.species)

dog_1.species = 'Wolf'
print(dog_1.species)
print(dog_2.species)