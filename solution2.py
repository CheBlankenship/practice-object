import pickle
from os.path import exists

if exists('phonebook.pickle') == True:
    print 'Loading phone book.'
    phonebook_file = open('phonebook.pickle', 'r')
    phonebook_dict = pickle.load(phonebook_file)
    phonebook_file.close()
else:
    phonebook_dict = {}

    list = "1\. Loook up an entry \n2\. Set an entry \n3\.Delete an entry \n4\.List of entries \n5\.Save and entries \n6\.Quit"
    print list
    choice = int(raw_input('What do you want to do(1~5)?'))

# Using def======================
    def lookup():
        name = raw_input('Name?').capitalize()
        if name in phonebook_dict:
            phone_number = phonebook_dict(name)
            print "%s's number is %s" % (name, phone_number)
        else:
            print "%s is not in the phonebook." % name

    def set_entry():
        name = raw_input('Name? ').capitalize()
        phone_number = raw_input('phone_number? ')
        phonebook_dict[name] = phone_number
        print "Stored %s's number." % name

    def delete():
        name = raw_input('Name? ').capitalize()
        if name in phonebook_dict:
            del phonebook_dict[name]
            print "Deleated %s's information." % name
        else:
            print "%s is not in the phonebook." % name

    def show():
        for name, phone_number in phonebook_dict.items():
            print "Found %s's number: %s" % (name, phone_number)
    def save():
        phonebook_file = open('phonebook.pickle', 'w')
        pickle.dump(phonebook_dict,phonebook_file)
        phonebook_file.close()
        print "Bye"




if choice == 1:
    lookup()
elif choice == 2:
    set_entry()
elif choice == 3:
    delete()
elif choice == 4:
    show()
elif choice == 5:
    save()
else:
    print "no"
