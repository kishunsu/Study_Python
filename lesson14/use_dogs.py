from dogs import English_Dog,Japanese_Dog

English_Dog.description()

buddy=English_Dog()
print(buddy.name)
buddy.bark()

jake=English_Dog("Jake")
print(jake.name)
jake.bark()

Japanese_Dog.description()
pochi=Japanese_Dog()
print(pochi.name)
pochi.bark()

shiro=Japanese_Dog("シロ")
print(shiro.name)
shiro.bark()