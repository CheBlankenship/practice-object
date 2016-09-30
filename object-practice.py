# Practice 1
# class Person(object):
#     def __init__(self,name,email,phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#
# person = Person('Sonny', 'sonny`hotmail.com', '483-485-4948')
#
# print 'name: %s' % person.name
# print 'email: %s' % person.email
# print 'phone: %s' % person.phone

# Practice 2
# class Person(object):
#     def __init__(self,name,email,phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#
# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
# jordan = Person('Jordan', 'jordan`aol.com', '495-586-3456')
#
# print 'name: %s' % sonny.name
# print 'email: %s' % sonny.email
# print 'phon: %s' % sonny.phone
#
# print 'name: %s' % jordan.name
# print 'email: %s' % jordan.email
# print 'phon: %s' % jordan.phone

# Practice 3
# class Person(object):
#     def __init__(self, name):
#         self.name = name
#
#     def greet(self, other_person):
#         print "Hello %s, I am %s!" % (other_person.name, self.name)
#
# sonny = Person('Sonny')
# jordan = Person('Jordan')
# sonny.greet(jordan)
# jordan.greet(sonny)

# Practice 4
# class Vehicle(object):
#     def __init__(self, maker, model, year):
#         self.maker = maker
#         self.model = model
#         self.year = year
#
# car = Vehicle('TOYOTA', 'Aqua', '2015')
# print 'Maker: %s' % car.maker
# print 'Model: %s' % car.model
# print 'Year: %s' % car.year

# Practice 5
# class Vehicle(object):
#     def __init__(self, maker, model, year):
#         self.maker = maker
#         self.model = model
#         self.year = year
#
#     def print_info(self):
#         print "%s %s %s" %(self.maker, self.model, self.year)
#
# car = Vehicle('TOYOTA', 'Aqua', '2015')
#
# car.print_info()

# Practice 6
# class Person(object):
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#
#     def print_contact_info(self):
#         print "%s's email: %s, %s's phone number: %s" % (self.name, self.email, self.name, self.phone)
#
#     # def __repr__(self):
#     #     return '' % (self.name,self.email,self.phone)
#
# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
#
# sonny.print_contact_info()

#  Practice 7
# class Person(object):
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friends = []
#
# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
# jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
#
#
# sonny.friends.append(jordan)
# jordan.friends.append(sonny)
#
# sonny.print_friends()


# Practice 8

# class Person(object):
#     def __init__(self, name, email, phone,):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friends = []
#
#     def add_friend(self,friend):
#         self.friends.append(friend)
#
#     def print_friends(self):
#         print "Friends: "
#         for i in self.friends:
#             print i
#
# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
# jordan = Person('Jordan', 'jordan@zol.com', '495-586-3456')
#
# sonny.add_friend(jordan)
# jordan.add_friend(sonny)
#
# sonny.print_friends()

# Practice 9

# class Person(object):
#     def __init__(self, name,email,phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friends = []
#
#
#     def add_friend(self,friend):
#         self.friends.append(friend)
#
#     def num_friends(self):
#         print len(self.friends)
#
# sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')
# jordan = Person('Jordan', 'jordan@aol.com','495-586-3456')
#
# sonny.add_friend(jordan)
# jordan.add_friend(sonny)
#
# sonny.num_friends()

#  Practice 10

# class Person(object):
#     def __init__(self,name,email,phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friends = []
#         self.greeting_count = 0
#
#     def add_friend(self, friend):
#         self.friends.append(friend)
#
#     def greet(self, friend):
#         self.greeting_count += 1
#         print self.greeting_count
#
#
#
#
# sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')
# jordan = Person('Jordan','jordan@aol.com','495-586-3456')
#
# sonny.add_friend(jordan)
# jordan.add_friend(sonny)
#
#
# sonny.greet(jordan)
# sonny.greet(jordan)
# sonny.greet(jordan)
# sonny.greet(jordan)
