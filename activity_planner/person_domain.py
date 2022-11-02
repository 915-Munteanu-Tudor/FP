from DataStructure import DataStructure

class Person:

    '''
    this class creates the objects called person and initializes them

    '''
    def __init__(self,person_id,name,phone_number):
        self.person_activities=DataStructure()
        if len(phone_number) !=10:
           raise ValueError("The phone number does not have the correct amount of numbers")
        if not isinstance(name, str):
            raise TypeError("Name must be str")
        self.person_id=person_id
        self.name=name
        self.phone_number=phone_number

    def get_person_id(self):
        return self.person_id
    def get_person_activities(self):
        return self.person_activities

    def get_name(self):
        return self.name

    def get_phone_number(self):
        return self.phone_number

    def __str__(self) -> str:
        return "({0},{1},{2})".format(self.person_id, self.name, self.phone_number)

    def print_person(self):
        print(self.person_id+" "+self.name+", "+self.phone_number)

