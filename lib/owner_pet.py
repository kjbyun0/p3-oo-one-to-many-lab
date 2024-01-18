class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self._owner = owner
        Pet.add_pet(self)

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in Pet.PET_TYPES:
            raise TypeError('pet_type must be one of PET_TYPES!')
        self._pet_type = pet_type

    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        if not isinstance(owner, Owner):
            raise TypeError('owner must be an instance of Owner class!')
        self._owner = owner

    @classmethod
    def add_pet(cls, pet):
        if not isinstance(pet, Pet):
            raise TypeError('pet must be an instance of Pet class!')
        cls.all.append(pet)

class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError('pet must be an instance of Pet class!')
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
    
