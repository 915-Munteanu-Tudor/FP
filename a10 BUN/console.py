from commands import UserInterface
from person_services import Person_Services
from activity_services import Activity_Services
from tests import Tests
import datetime

class Run_cmd:

    def load_properties(self, filepath, sep='=', comment_char='#'):

        props = {}
        with open(filepath, "rt") as f:
            for line in f:
                l = line.strip()
                if l and not l.startswith(comment_char):
                    key_value = l.split(sep)
                    key = key_value[0].strip()
                    value = sep.join(key_value[1:]).strip().strip('"')
                    props[key] = value
        return props

    #TODO: WHEN UPDATE UPDATE PERSON ACTIVITY LIST(IF AFTER UPDATE OVERLAP->MESSAGE, NO UPDATE) !!!
    #TODO: FIX REDO FOR BOTH UPDATES
    #TODO:MOVE UNDO AND REDO IN A SEPARATE CLASS

    def ui_run(self):
        '''

        :return: uses the commands and the args in order to run the program
        '''
        self.properties_dict = self.load_properties('settings.properties')
        self.servicep=Person_Services(self.properties_dict)
        self.servicea=Activity_Services(self.servicep , self.properties_dict)
        self.ui1=UserInterface()
        self.tst=Tests()
        self.redo_list=[]
        self.redo_objects=[]


        try:
            self.tst.test_person_add(self.properties_dict)
            self.tst.test_activity_add(self.properties_dict)
        except TypeError as te:
            print(te)


        while True:
            self.ui1.display_commands()
            c, a =self.ui1.command()
            if c=="ADD-PERSON":
                self.servicep.add_person(a)
                self.redo_list.clear()
                self.redo_objects.clear()

            elif c=="SHOW-PERSON":
                self.servicep.show()
            elif c=="SEARCH-PERSON":
                self.servicep.search_person(a)
            elif c=="REMOVE-PERSON":
                   self.servicep.remove_pers(a)
                   for activity in self.servicea.activities:
                       for person in activity.persons_id:
                           if person==a:
                               activity.persons_id.remove(a)
                               self.servicea.write_text_file1("act1.txt")
                               self.redo_list.clear()
                               self.redo_objects.clear()


            elif c=="UPDATE-PERSON":
                self.servicep.update(a)
                self.redo_list.clear()
                self.redo_objects.clear()
            elif c == "ADD-ACTIVITY":
                ok = True
                ok1 = False
                for i in a[1]:
                    if i not in self.servicep.id_list:
                        ok = False
                if a[0] not in self.servicea.act_id:
                    ok1 = True
                if ok == True and ok1 == True:
                    self.servicea.add_activity(a)
                    #self.servicea.assign_activities()
                    self.servicea.act_id.append(a[0])
                    self.redo_list.clear()
                    self.redo_objects.clear()
                else:
                    print("the activity id is not unique or the person id does not exist")
            elif c == "SHOW-ACTIVITY":
                self.servicea.show_activity()
            elif c=="SEARCH-ACTIVITY":
                self.servicea.search_activity(a)
            elif c=="ACTIVITIES-AT-DATE":
                self.servicea.activies_at_a_date(a)
            elif c=="ACTIVITIES-WITH-PERSON":
                #self.servicea.assign_activities()
                self.servicea.act_with_a_person(a)
            elif c == "REMOVE-ACTIVITY":
                self.servicea.remove_activity(a)
                self.servicea.act_id.remove(a)
                self.redo_list.clear()
                self.redo_objects.clear()
            elif c=="BUSIEST-DAY":
                self.servicea.busiest_day()
            elif c == "UPDATE-ACTIVITY":
                self.servicea.update_activity(a)
                self.redo_list.clear()
                self.redo_objects.clear()
            elif c=="UNDO":
                if len(self.servicep.operations_list) == 0:
                    print("No more undos to perform!")
                elif self.servicep.operations_list[len(self.servicep.operations_list) - 1].startswith("ADD-ACTIVITY"):
                    self.servicea.remove_activity(self.servicep.objects[len(self.servicep.operations_list) - 1])
                    self.redo_list.append("ADD-ACTIVITY")
                    self.redo_objects.append(self.servicea.argz)
                    self.servicea.write_text_file1("act1.txt")
                    for i in range(2):
                        self.servicep.objects.pop(len(self.servicep.operations_list) - 1)
                        self.servicep.operations_list.pop(len(self.servicep.operations_list) - 1)
                elif self.servicep.operations_list[len(self.servicep.operations_list) - 1].startswith(
                        "REMOVE-ACTIVITY"):
                    self.servicea.add_activity(self.servicep.objects[len(self.servicep.operations_list) - 1])
                    self.redo_list.append("REMOVE-ACTIVITY")
                    self.redo_objects.append(self.servicea.idr[0])
                    self.servicea.write_text_file1("act1.txt")
                    for i in range(2):
                        self.servicep.objects.pop(len(self.servicep.operations_list) - 1)
                        self.servicep.operations_list.pop(len(self.servicep.operations_list) - 1)
                    self.servicea.argz.pop(len(self.servicea.argz) - 1)
                elif self.servicep.operations_list[len(self.servicep.operations_list) - 1].startswith("ADD-PERSON"):
                    self.servicep.remove_pers(self.servicep.objects[len(self.servicep.operations_list) - 1])
                    self.redo_list.append("ADD-PERSON")
                    self.redo_objects.append(self.servicep.argz)
                    self.servicep.write_text_file("persons1.txt")
                    for i in range(2):
                        self.servicep.objects.pop(len(self.servicep.operations_list) - 1)
                        self.servicep.operations_list.pop(len(self.servicep.operations_list) - 1)
                elif self.servicep.operations_list[len(self.servicep.operations_list) - 1].startswith("REMOVE-PERSON"):
                    self.servicep.add_person(self.servicep.objects[len(self.servicep.operations_list) - 1])
                    self.redo_list.append("REMOVE-PERSON")
                    self.redo_objects.append(self.servicep.ar[0])
                    self.servicep.write_text_file("persons1.txt")
                    for i in range(2):
                        self.servicep.objects.pop(len(self.servicep.operations_list) - 1)
                        self.servicep.operations_list.pop(len(self.servicep.operations_list) - 1)
                    self.servicep.argz.pop(len(self.servicep.argz) - 1)
                elif self.servicep.operations_list[len(self.servicep.operations_list) - 1].startswith("UPDATE-PERSON"):
                    self.servicep.update(self.servicep.objects[len(self.servicep.operations_list) - 1])
                    self.up=[]
                    self.up.append(self.servicep.objects[len(self.servicep.operations_list) - 1])
                    self.redo_list.append("UPDATE-PERSON")
                    self.redo_objects.append(self.servicep.argz1)
                    self.servicep.write_text_file("persons1.txt")
                    for i in range(2):
                        self.servicep.objects.pop(len(self.servicep.operations_list) - 1)
                        self.servicep.operations_list.pop(len(self.servicep.operations_list) - 1)

                elif self.servicep.operations_list[len(self.servicep.operations_list) - 1].startswith(
                        "UPDATE-ACTIVITY"):
                    self.servicea.update_activity(self.servicep.objects[len(self.servicep.operations_list) - 1])
                    self.redo_list.append("UPDATE-ACTIVITY")
                    self.redo_objects.append(self.servicea.argz1)
                    self.servicea.write_text_file1("act1.txt")
                    for i in range(2):
                        self.servicep.objects.pop(len(self.servicep.operations_list) - 1)
                        self.servicep.operations_list.pop(len(self.servicep.operations_list) - 1)
                    #self.servicea.argz1.pop(len(self.servicea.argz1) - 1)
            elif c=="REDO":
                if len(self.redo_list)==0:
                    print("No more redos to perform!")
                elif self.redo_list[len(self.redo_list) - 1].startswith("ADD-PERSON"):
                    self.servicep.add_person(self.redo_objects[len(self.redo_objects)-1])
                    self.servicep.objects.append(self.redo_objects[len(self.redo_objects)-1][0])
                    self.redo_objects.pop(len(self.redo_list) - 1)
                    self.redo_list.pop(len(self.redo_list) - 1)
                    self.servicep.operations_list.append("ADD-PERSON")

                    self.servicep.write_text_file("persons1.txt")
                    self.servicep.argz.pop(len(self.servicep.argz) - 1)
                elif self.redo_list[len(self.redo_list) - 1].startswith("REMOVE-PERSON"):
                    self.servicep.remove_pers(self.redo_objects[len(self.redo_objects)-1])
                    self.servicep.operations_list.append("REMOVE-PERSON")
                    self.servicep.objects.append(self.servicep.ar)
                    self.redo_objects.pop(len(self.redo_list) - 1)
                    self.servicep.write_text_file("persons1.txt")
                    self.redo_list.pop(len(self.redo_list) - 1)
                elif self.redo_list[len(self.redo_list) - 1].startswith("UPDATE-PERSON"):
                    self.servicep.update(self.redo_objects[len(self.redo_objects) - 1])
                    self.servicep.operations_list.append("UPDATE-PERSON")
                    self.servicep.objects.append(self.redo_objects[len(self.redo_objects) - 1])
                    self.redo_objects.pop(len(self.redo_list)-1)
                    self.redo_list.pop(len(self.redo_list) - 1)
                    self.servicep.write_text_file("persons1.txt")

                elif self.redo_list[len(self.redo_list) - 1].startswith("ADD-ACTIVITY"):
                    self.servicea.add_activity(self.redo_objects[len(self.redo_objects) - 1])
                    self.servicep.operations_list.append("ADD-ACTIVITY")
                    self.servicep.objects.append(self.redo_objects[len(self.redo_objects) - 1][0])
                    self.redo_objects.pop(len(self.redo_list) - 1)
                    self.redo_list.pop(len(self.redo_list) - 1)
                    self.servicea.write_text_file1("act1.txt")
                elif self.redo_list[len(self.redo_list) - 1].startswith("REMOVE-ACTIVITY"):
                    self.servicea.remove_activity(self.redo_objects[len(self.redo_objects) - 1])
                    self.servicep.operations_list.append("REMOVE-ACTIVITY")
                    self.servicep.objects.append(self.servicea.idr)
                    self.redo_objects.pop(len(self.redo_list) - 1)
                    self.redo_list.pop(len(self.redo_list) - 1)
                    self.servicea.write_text_file1("act1.txt")
                elif self.redo_list[len(self.redo_list) - 1].startswith("UPDATE-ACTIVITY"):
                    self.servicea.update_activity(self.redo_objects[len(self.redo_objects) - 1])
                    self.servicep.operations_list.append("UPDATE-ACTIVITY")
                    self.servicep.objects.append(self.redo_objects[len(self.redo_objects)-1])
                    self.redo_objects.pop(len(self.redo_list) - 1)
                    self.redo_list.pop(len(self.redo_list) - 1)
                    self.servicea.write_text_file1("act1.txt")
                #todo update person not good


            elif c=="QUIT":
                break

