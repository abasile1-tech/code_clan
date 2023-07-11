from pet import Pet
from pet_shop import PetShop

monty = Pet("Monty","Snake","Python",500)
charles = Pet("Charles", "Dog", "Spaniel", 250)
mrs_norris = Pet("Mrs. Norris", "Cat", "Maine Coon", 100)
pets = [monty, charles, mrs_norris]

cc_pet_shop = PetShop("CodeClan Pet Shop", 0, pets)
