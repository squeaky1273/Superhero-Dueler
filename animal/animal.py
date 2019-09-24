class Animal:
  def __init__(self, name, sleep_duration):
    self.name = name
    self.sleep_duration = sleep_duration

  def sleep(self):
    print(
      "{} sleeps for {} hours".format(
          self.name,
          self.sleep_duration))

  def eat(self):
    print('{} is eating'.format(self.name))

  def drink(self):
    print('{} is drinking'.format(self.name))

class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

my_dog = Dog("Sophie", 12)
my_dog.sleep()
my_dog.bark()