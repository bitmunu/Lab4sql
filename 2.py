from nopers import *
session = factory()

names = ["GamersEnergyRefillers", "CatsFightingArmor", "DogsSuperFood"]

for s in names:
    c = Department()
    c.department_name = s
    session.add(c)

session.commit()

