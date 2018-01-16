phoneBook = {'belleville': {'First Name': 'Hunter',
                        'Number': 8887776666,
                        'City': 'New York'},
            'Aguillon': {'First Name': 'Kiara',
                         'number': 5554443333,
                         'City': 'Los Angeles'}}

def addNewContact(addInformation):
    formattedContactInput = newContactInput.split(',')
    phoneBook[formattedContactInput[1]] = {'firstName': formattedContactInput[0], 'number': formattedContactInput[2], 'city': formattedContactInput[3]}

def retrieveContactInfo(findInformation):
return (phoneBook[formattedContactInput])



userSelection = input("please select from the following options by entering the corresponding number: To create new contact enter 1 - To retrive contact information enter 2, to update an exisiting number enter 3, to delete a contact press 4: ")

if taskToPerform == 1:
    newContactInput = input("please enter the new contact's information seperated by commas, as follows: First name, Last name, phone number, city (i.e: John, Smith, 1234567, Portland)")
    addNewContact(newContactInput)
    print("{} has been added to your phonebook".format(formattedContactInput[1]))

elif taskToPerform == 2:
    contactToRetrieve = input('Please enter the last name of contact you are searching for: ')
    print(retrieveContactInfo(contactToRetrieve))

elif taskToPerform == 3:
    contactToUpdate = input("please enter the number of the contact youd like to update  ")

elif taskToPerform == 4:


#search by phone number
numberToSearch = int(input("enter the phone number you are looking for"))
for contact in phoneBook:
    if contact['number'] == numberToSearch:
        print("we've found {} with this phone number".format())
    print
