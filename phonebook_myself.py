
phonebook_dict = {
    'bob': '098-765-5432'
}


while True:
    print 'Electronic Phone Book'
    print '====================='
    list = "1.Look up an entry \n2. Set an entry \n3. Delete an entry \n4. List all entries \n5 Save \n6 Quit"
    print list
    choice = int(raw_input('What do you want to do?'))
    if choice == 1:
        name = raw_input('Name? ').capitalize()
    elif choice == 2:
        name = raw_input('Name? ').capitalize()
        phone_number = raw_input('Number? ')
        print "Entry stored for %s" % name
    elif choice == 3:
        name = raw_input('Name?').capitalize()
        del phonebook_dict[name]
        print "Deleted entry for %s" % name
    elif choice == 4:
        print phonebook_dict
    elif choice == 5:
        print "Save"
    elif choice == 6:
        break
        print "Bye"
