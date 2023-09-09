class person:
   def __init__(self, name, age):
       self.name = name
       self.age = age

   def is_adult(self):
       if self.age >= 18:
           print('you have too many responsibilities')
       else:
           print('lucky you')

   def __str__(self):
       return f'my name is {self.name} and I am {self.age} years old'

first_person = person('ali', 18)
print(first_person.name)
print(first_person.age)
first_person.is_adult()
print(first_person)
