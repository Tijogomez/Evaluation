class Pet:
    speciesList = ['dog', 'cat', 'horse', 'hamster']

    def __init__(self, species="NONE", name=""):
        if species.lower() not in self.speciesList:
            raise Exception
        self.species = species
        self.name = name

    def str(self):
        if self.name == "":
            return "Species of: {} unnamed".format(self.species)
        return "Species of: {}, named {}".format(self.species, self.name)

class Dog(Pet):
    def __init__(self, name="", chases="Cats"):
        Pet.__init__(self, "Dog", name)
        self.chases = chases

    def str(self):
        if self.name == "":
            return "Species of Dog, unnamed Chases {}".format(self.chases)
        return "Species of: Dog, named {} Chases {}".format(self.name, self.chases)

class Cat(Pet):
    def __init__(self, name="", hates="Dogs"):
        Pet.__init__(self, "Cat", name)
        self.hates = hates

    def str(self):
        if self.name == "":
            return "Species of Cat, unnamed Hates {}".format(self.hates)
        return "Species of: Cat, named {} hates {}".format(self.name, self.hates)

def main():
    dict = {
        "Dog": [],
        "Cat": []
    }
    for i in range(5):
        dict["Dog"].append(Dog("Dog " + str(i)))
    for i in range(3):
        dict["Cat"].append(Cat("Cat " + str(i)))

    print(dict["Dog"][0].str())
    print(dict["Cat"][1].str())
main()
