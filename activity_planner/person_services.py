from person_domain import Person
import pickle

class Person_Services:

    def __init__(self):
        '''
        initialize rhe list of persons
        '''
        self.persons=[]
        self.id_list=[]
        self.objects=[]
        self.operations_list=[]
        self.redo_objects=[]
        lisst = [["8h8td", "Mike", "0765477211"], ["54ydf4", "Luke", "0784332156"],
                 ["32dgfg", "Juan", "0754321567"], ["h43tu8", "Marry", "0723312557"],
                 ["4dsfv", "Simon", "0734342567"],
                 ["12fascxz", "Jullietta", "0721787923"],
                 ["13adfs", "Maya", "0765231890"], ["h4g53t", "Noah", "0784562873"],
                 ["hmbs43t", "Amalia", "0734562189"], ["f3rfs", "Jack", "0753249170"]]
        for item in lisst:
            newperson = Person(item[0], item[1], item[2])
            self.persons.append(newperson)
            self.id_list.append(item[0])
        self.write_text_file("persons1.txt")


    def add_person(self, argz):
        '''

        :return: the new list after adding a new person
        '''
        if argz[0] not in self.id_list:
           person_id = argz[0]
           name = argz[1]
           phone_number = argz[2]
           newperson = Person(person_id, name, phone_number)
           self.persons.append(newperson)
           self.id_list.append(argz[0])
           self.operations_list.append("ADD-PERSON")
           self.objects.append(newperson.person_id)
           self.ar=[]
           self.ar.append(person_id)
           self.ar.append(name)
           self.ar.append(phone_number)
           self.write_text_file("persons1.txt")
        else:print("the person you want to add does not have an unique id")



    def show(self):
        '''
        prints all the persons list
        '''
        for person in self.persons:
            person.print_person()

    def remove_pers(self, word):
        '''

        :param word:
        :return: remove the person in the list which has the id equal to the given word
        '''
        word = word.strip()
        gasit=0
        for person in self.persons:

            if person.person_id==word:
                print("Removing person ", end='')
                person.print_person()
                self.persons.remove(person)
                gasit=1
                self.operations_list.append("REMOVE-PERSON")
                self.argz=[]
                self.argz.append(person.person_id)
                self.argz.append(person.name)
                self.argz.append(person.phone_number)
                self.objects.append(self.argz)
                self.write_text_file("persons1.txt")
                #self.redo_objects.append(self.argz)

        if gasit==0:
           print("this id person to be removed does not exist")
        for i in self.id_list:
            if i==word:
                self.id_list.remove(i)
                break

    def update(self,argz):
        '''

        :return: updates the name and the phone number to a person with a certain id
        '''
        found=0
        for person in self.persons:
            if person.person_id==argz[0]:
                self.operations_list.append("UPDATE-PERSON")
                self.argz1=[]
                self.argz1.append(person.person_id)
                self.argz1.append(person.name)
                self.argz1.append(person.phone_number)
                self.objects.append(self.argz1)
                person.phone_number=argz[2]
                person.name=argz[1]
                found=1
                self.write_text_file("persons1.txt")
                break
        if found==0:
            print("the id does not exist!")

    def search_person(self,word):
        found=False
        for person in self.persons:
            if word in person.name or word in person.phone_number:
                print(person)
                found=True
        if found==False:
            print("Any person can't be found!")



    def test_pers_service(self):

      s=Person("123","John","0712345678")
      if s.person_id=="123":
         assert True
      else: assert False
      self.add_person(s)
      if len(self.persons)==11:
          assert True
      else: assert False
      self.update(["123","Jackson","0755666777"])
      if self.persons[11].name=="Jackson":
          assert True
      else: assert False
      self.remove("123")
      if len(self.persons)==10:
          assert True
      else: assert False

    def write_text_file(self, file_name):
        f = open(file_name, "w")
        try:
            for p in self.persons:
                person_str = str(p.person_id) + "," + p.name+ "," + p.phone_number+ "\n"
                f.write(person_str)
            f.close()
        except Exception as e:
            print("An error occurred -" + str(e))

    def read_text_file(self, file_name):
        try:
            f = open(file_name, "r")
            line = f.readline().strip()
            while len(line) > 0:
                line = line.split(",")
                self.add_person(line)
                line = f.readline().strip()
            f.close()
        except IOError as e:

            print("An error occured - " + str(e))
            raise e

        return self.persons




