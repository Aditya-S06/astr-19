class Animal:
    def __init__(self, type, name, lengthOfLeg, lengthOfArm, numOfEyes, tail, furry):
        self.type = type
        self.name = name
        self.lengthOfLeg = lengthOfLeg
        self.lengthOfArm = lengthOfArm
        self.numOfEyes = numOfEyes
        self.tail = tail
        self.furry = furry

    def getInfo(self):
        print(f"The animal is a: {self.type}")
        print(f"The {self.type}'s name is: {self.name}")
        print(f"The length of its leg is: {self.lengthOfLeg}inches")
        print(f"The length of its arm is: {self.lengthOfArm}inches")
        print(f"The number of eyes it has is: {self.numOfEyes}")
        print(f"Does the animal have a tail?: {self.tail}")
        print(f"Is the animal furry?: {self.furry}")

dog = Animal("Dog", "Daisy", 16.5, 14.6, 2, True, True)

print(dog.getInfo())