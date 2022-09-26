class Address:
  def __init__(self):
    self.__Street=""
    self.__Flat=""
    self.__City=""
    self.__PostCode=""
  def GetStreet(self):
    return self.__Street
  def GetFlat(self):
    return self.__Flat
  def GetCity(self):
    return self.__City
  def GetPostCode(self):
    return self.__PostCode
  def SetStreet(self, street):
    self.__Street = street
  def SetFlat(self, flat):
    self.__Flat = flat
  def SetCity(self, city):
    self.__City = city
  def SetPostCode(self, postcode):
    self.__PostCode = postcode

class Person:
  def __init__(self):
    self.__FirstName=""
    self.__LastName=""
    self.__DateOfBirth=""
  def GetFirstName(self):
    return self.__FirstName
  def GetLastName(self):
    return self.__LastName
  def GetDateOfBirth(self):
    return self.__DateOfBirth
  def SetFirstName(self, firstName):
    self.__FirstName = firstName
  def SetLastName(self, lastName):
    self.__LastName = lastName
  def SetDateOfBirth(self, dateOfBirth):
    self.__DateOfBirth = dateOfBirth

class Phone:
  def __init__(self):
    self.__CellPhone=""
    self.__Landline=""
    self.__WorkPhone=""
  def GetCellPhone(self):
    return self.__CellPhone
  def GetLandline(self):
    return self.__Landline
  def GetWorkPhone(self):
    return self.__WorkPhone
  def SetCellPhone(self, cellPhone):
    self.__CellPhone = cellPhone
  def SetLandline(self, landline):
    self.__Landline = landline
  def SetWorkPhone(self, workPhone):
    self.__WorkPhone = workPhone

class Contacts(Person, Address, Phone):
  def __init__(self):
    self.__Email=""
  def GetEmail(self):
    return self.__Email
  def SetEmail(self, email):
    self.__Email = email
  def ShowContacts(self):
    print("-----Contacts-----")
    print("First name: ", self.GetFirstName())
    print("Last name: ", self.GetLastName())
    print("Date of birth: ", self.GetDateOfBirth())
    print("Cell phone: ", self.GetCellPhone())
    print("Landline: ", self.GetLandline())
    print("Work phone: ", self.GetWorkPhone())
    print("Street: ", self.GetStreet())
    print("Flat: ", self.GetFlat())
    print("City: ", self.GetCity())
    print("Post code: ", self.GetPostCode())
    print("First name: ", self.GetFirstName())
    print("Email: ", self.__Email)
    print("----------")

class Diary:
  def __init__(self, path):
    self.__ContactList=[]
    self.__Path = path
  def LoadContacts(self):
    try:
      file = open(self.__Path, "r")
    except:
      print("ERROR: File Diary doesn't exist")
    else:
      contacts =  file.readlines()
      file.close()
      if(len(contacts)>0):
        for contact in contacts:
          data = contact.split("#")
          if(len(data)==11):
            newcontact = Contacts()
            newcontact.SetFirstName(data[0])
            newcontact.SetLastName(data[1])
            newcontact.SetDateOfBirth(data[2])
            newcontact.SetCellPhone(data[3])
            newcontact.SetLandline(data[4])
            newcontact.SetWorkPhone(data[5])
            newcontact.SetStreet(data[6])
            newcontact.SetFlat(data[7])
            newcontact.SetCity(data[8])
            newcontact.SetPostCode(data[9])
            newcontact.SetEmail(data[10])
            self.__ContactList = self.__ContactList + [newcontact]
            print("INFO: have loaded a total of ", len(self.__ContactList), "contacts")
  def CreateNewContact(self, newcontact):
    self.__ContactList = self.__ContactList + [newcontact]
  def SaveContacts(self):
    try:
      file = open(self.__Path, "w")
    except:
      print("ERROR: can't save")
    else:
      for contact in self.__ContactList:
        contact = Contacts()
        text = text + contact.GetFirstName() + "#"
        text = text + contact.GetLastName() + "#"
        text = text + contact.GetDateOfBirth() + "#"
        text = text + contact.GetCellPhone() + "#"
        text = text + contact.GetLandline() + "#"
        text = text + contact.GetWorkPhone() + "#"
        text = text + contact.GetStreet() + "#"
        text = text + contact.GetFlat() + "#"
        text = text + contact.GetCity() + "#"
        text = text + contact.GetPostCode() + "#"
        text = text + contact.GetEmail() + "\n"
        file.write(text)
      file.close()
  def ShowDiary(self):
    print("########## Diary ##########")
    print("Number of contacts: ", len(self.__ContactList))
    for contact in self.__ContactList:
      contact = Contacts()
      contact.ShowContacts()
    print("###############################################")
  def SearchContactByName(self, firstName):
    listfound = []
    for contact in self.__ContactList:
      contact = Contacts()
      if contact.GetFirstName() == firstName:
        listfound = listfound + [contact]
    return listfound
  def SearchContactByPhone(self, phone):
    listfound = []
    for contact in self.__ContactList:
      contact = Contacts()
      if(contact.GetCellPhone() == phone or contact.GetLandline() == phone or contact.GetWorkPhone() == phone):
        listfound = listfound + [contact]
    return listfound
  def DeleteContactByName(self, firstName):
    finallist = []
    for contact in self.__ContactList:
      contact = Contacts()
      if contact.GetFirstName != firstName:
        finallist = finallist + [contact]
    print("INFO: ", len(self.__ContactList) - len(finallist)," contacts have been deleted ")
    self.__ContactList = finallist
  def DeleteContactByPhone(self, phone):
    finallist = []
    for contact in self.__ContactList:
      contact = Contacts()
      if (contact.GetCellPhone() != phone or contact.GetLandline() != phone or contact.GetWorkPhone() != phone):
        finallist = finallist + [contact]
    print("INFO: ", len(self.__ContactList) - len(finallist)," contacts have been deleted ")
    self.__ContactList = finallist
  def GetOption(text):
    read = False
    while not read:
      try:
        number = int(input(text))
      except ValueError:
        print("ERROR: You have to put a number")
      else:
        read = True
    return number
  def ShowMenu():
    print("""Menu
    1) Show contacts
    2) Search contacts
    3) Create new  contact
    4) Delete contact
    5) Save contact
    6) Exit
    """)
  def SearchContacts(diary):
    print("""
    1) Name
    2) Phone
    3) Go back
    """)