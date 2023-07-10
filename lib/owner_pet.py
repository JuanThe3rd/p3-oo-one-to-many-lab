class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        if pet_type in self.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception
        
        if isinstance(owner, Owner) or owner == None:
            self.owner = owner
        else:
            raise Exception

        self.add_pet(self)

    def add_pet(cls, pet):
        cls.all.append(pet)

class Owner:
    def __init__(self, name):
        self.name = name
        self.get_sorted_pets = self.sort_pets_by_name

    def pets(self):
        return Pet.all

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception

    @classmethod
    def sort_pets_by_name(self):
        sorted_names = sorted([pet.name for pet in Pet.all])
        sorted_pets = []

        for name in sorted_names:
            for pet in Pet.all:
                if pet.name == name:
                    sorted_pets.append(pet)

        return sorted_pets
