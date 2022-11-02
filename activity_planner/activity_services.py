from activity_domain import Activity
from person_services import Person_Services, Person
import datetime
import copy
import pickle
from bucket import Bucket,keep,gnome_sort
from copy import deepcopy


class Activity_Services(Person_Services):

    def __init__(self, pserv,properties):

        '''
        initialize the activity list
        '''
        self.properties_dict = properties
        self.activities = []
        self.pserv = pserv
        self.act_id = []
        lisst = [["001", ["8h8td", '54ydf4'], datetime.datetime(2020, 11, 13), 9, "hangout"],
                 ["002", ['54ydf4'], datetime.datetime(2020, 11, 13), 15, "shopping"],
                 ["003", ["8h8td", 'f3rfs'], datetime.datetime(2020, 11, 12), 15, "meeting"],
                 ["004", ["4dsfv", "12fascxz"], datetime.datetime(2020, 12, 23), 12, "playing tennis"],
                 ["005", ['12fascxz', 'h43tu8'], datetime.datetime(2020, 12, 23), 13, "ice-skating"],
                 ["006", ["h4g53t", "32dgfg"], datetime.datetime(2021, 1, 17), 11, "trip"],
                 ["007", ["12fascxz"], datetime.datetime(2020, 12, 12), 8, "play"],
                 ["008", ["4dsfv"], datetime.datetime(2020, 12, 12), 23, "holiday with family"],
                 ["009", ["13adfs", "54ydf4", "h4g53t"], datetime.datetime(2020, 12, 12), 16, "debate club"],
                 ["010", ["8h8td"], datetime.datetime(2020, 12, 19), 7, "general house cleaning"]]

        if self.properties_dict['repository'] == 'inmemory':
            self.start_with_list(lisst)
        elif self.properties_dict['repository'] == 'textfiles':
            self.start_with_textfile(self.properties_dict['activities'])
            self.write_pickle_file('act1.pickle')
        elif self.properties_dict['repository'] == 'binaryfiles':
            self.activities = self.start_with_pickle(self.properties_dict['activities'])
            for activ in self.activities:
                for person in self.pserv.persons:
                    if person.person_id in activ.persons_id:
                        person.person_activities.append(activ)
                self.act_id.append(activ.activity_id)
            self.write_text_file1('act1.txt')


        #self.start_with_list(lisst)
        #self.activities = self.start_with_pickle(self.properties_dict['activities'])
        #self.start_with_textfile(self.properties_dict['activities'])
        self.pserv.operations_list.clear()
        self.pserv.objects.clear()

    def write_pickle_file(self,filename):
        with open(filename,'wb') as f:
            pickle.dump(self.activities,f)

    def start_with_pickle(self,filename):
        with open(filename, 'rb') as f:
            loaded_list = pickle.load(f)
        return loaded_list

    def start_with_list(self,lisst):
        for item in lisst:
            it = item[2].strftime("%d %b %Y")
            act = [item[0], item[1], it, str(item[3]), item[4]]
            self.add_activity(act)
            self.act_id.append(item[0])
        self.write_text_file1('act1.txt')
        self.write_pickle_file('act1.pickle')



    def line_to_activity(self,line):
        arguments = []
        line = line[:-1]
        line.strip()
        charlist = line.split(',', 1)
        arguments.append(charlist[0])
        personlist = charlist[1].split(']')
        # print(personlist[0])
        personlist[0] = personlist[0][2:]
        personlist[0] = personlist[0][:-1]
        # print(personlist[0])
        a2 = personlist[0].split(',')
        for i in range(len(a2)):
            a2[i] = a2[i].replace("'", "")
            a2[i] = a2[i].replace(" ", "")
        # print(a2)
        arguments.append(a2)

        personlist[1] = personlist[1][1:]
        lastlist = personlist[1].split(',')
        datelist = lastlist[0].split(' ')

        arguments.append(lastlist[0])
        arguments.append(lastlist[1])
        arguments.append(lastlist[2])
        self.add_activity(arguments)

    def start_with_textfile(self,filename):
        with open(filename,'r') as f:
            for line in f:
                if(len(line)>5):
                    self.line_to_activity(line)
            f.close()


    def add_activity(self, argz):
        activitate_adaugata = Activity(argz[0], argz[1], argz[2], argz[3], argz[4])
        ok = True
        for person in self.pserv.persons:
            if person.person_id in activitate_adaugata.persons_id:
                # print(person.person_activities)
                for activ in person.person_activities:
                    if (((activ.date == activitate_adaugata.date) or (activitate_adaugata.date == activ.date)) and (
                            activ.time.strip() == activitate_adaugata.time.strip())):
                        print("Person " + person.name + " already has an activity at that time.")
                        ok = False
                        break

        if ok is True:
            self.idr=[]
            self.idr.append(argz[0])
            self.idr.append(argz[1])
            self.idr.append(argz[2])
            self.idr.append(argz[3])
            self.idr.append(argz[4])
            self.pserv.operations_list.append("ADD-ACTIVITY")
            self.pserv.objects.append(argz[0])
            self.activities.append(activitate_adaugata)
            self.write_text_file1("act1.txt")
            self.write_pickle_file('act1.pickle')
        for person in self.pserv.persons:
            if person.person_id in activitate_adaugata.persons_id:
                person.person_activities.append(activitate_adaugata)

    def remove_activity(self, id):
        '''

        :return: the new list after removing the activity with a certain id
        '''
        gasit=0
        id = id.strip()
        for activity in self.activities:
            if activity.activity_id == id:
                print("Removing activity ", end='')
                self.activities.remove(activity)
                activity.print_activities()
                gasit = 1
                self.pserv.operations_list.append("REMOVE-ACTIVITY")
                self.write_text_file1("act1.txt")
                self.write_pickle_file('act1.pickle')
                self.argz=[]
                self.argz.append(activity.activity_id)
                self.argz.append(activity.persons_id)
                self.argz.append(activity.date)
                self.argz.append(activity.time)
                self.argz.append(activity.description)
                self.pserv.objects.append(self.argz)

                for person in self.pserv.persons:
                    if person.person_id in activity.persons_id:
                          person.person_activities.remove(activity)
                break
        if gasit == 0:
            print("this activity does not exist")

    def show_activity(self):
        '''

        :return: prints all the activities in the list
        '''
        for activity in self.activities:
            activity.print_activities()

    def update_activity(self, argz):
        '''

        :return: the new list which contains the activity with a certain id updated
        '''
        for act in self.activities:
            if act.activity_id == argz[0]:
                self.pserv.operations_list.append("UPDATE-ACTIVITY")
                self.argz1=[]
                self.argz1.append(act.activity_id)
                self.argz1.append(act.persons_id)
                self.argz1.append(act.date)
                self.argz1.append(act.time)
                self.argz1.append(act.description)
                self.pserv.objects.append(self.argz1)
                act.description = argz[4]
                act.time = argz[3]
                act.date = argz[2]
                act.persons_id = argz[1]
                self.write_text_file1("act1.txt")
                self.write_pickle_file('act1.pickle')
                found = 1
                break

        if found == 0:
            print("the id does not exist!")

    def search_activity(self, word):
        found = False
        for act in self.activities:
            # k=act.time.split(" ")
            if str(word) in act.time:
                act.print_activities()
                found = True
            if str(word) in act.date:
                act.print_activities()
                found = True
            if word in act.description:
                act.print_activities()
                found = True
                '''
            else:
                j=act.description.split(" ")
                if str(word) in j:
                    act.print_activities()
                    found=True
                '''
        if found == False:
            print("Any activity could not be found!")

    def activies_at_a_date(self, data):
        k = 0
        self.lat=[]
        #self.lst=[]
        for act in self.activities:
            if act.date == data:
                self.lat.append(act)
                #self.lst=sorted(self.lat.date.items(), key=lambda item: item[0])
                act.print_activities()
                k += 1
        '''
        if k!=0:
            for ac in range(len(self.lat)-1):
                for ac1 in range (ac+1,len(self.lat)):
                    if self.lat[ac1].date<self.lat[ac].date:
                       self.lat[ac1], self.lat[ac]=self.lat[ac], self.lat[ac1]
        '''
        if k == 0:
            print("There are no activities in that day!")
        '''
        else:
            for i in self.lat:
                print(i)
        '''

    def act_with_a_person(self, name):
        # todo
        found=0
        for ps in self.pserv.persons:
            if name==ps.name:
                found=1
        if found==0:
            print("This person does not exist!")
        else:
            for activ in self.activities:
                for pers in self.pserv.persons:
                    if (pers.person_id in activ.persons_id) and (pers.name in name):
                        print(activ)

    def busiest_day(self):

        self.frequency = {}
        self.fr = {}
        for act in self.activities:
            if act.date not in self.frequency.keys():
                it = act.date
                self.frequency[it] = [int(1)]
                self.frequency[it].append([int(act.time)])

            else:
                self.frequency[it][0] += 1
                self.frequency[it][1].append(int(act.time))
        self.fr = dict(sorted(self.frequency.items(), key=lambda item: item[1], reverse=True))
        for i in self.fr:
            sl = []
            ls = []
            sl = copy.deepcopy(self.fr[i][1])
            gnome_sort(sl,len(sl)-1)
            self.fr[i][1] = copy.deepcopy(sl)
            '''
        for k in self.fr.keys():
            print(k)
            print(self.fr[k])
            '''
        for k in self.fr.keys():
            print(k)
            print("free time intervals: ")
            activity = self.fr[k][1]
            for j in range(len(activity)):
                if len(activity)==1:
                    print("0-"+str(activity[0]))
                    print(str(activity[0])+"-24")
                else:
                    if j==0:
                        print("0-"+str(activity[j]))
                    elif j==len(activity)-1:
                        print(str(activity[j-1])+"-"+str(activity[j]))
                        print(str(activity[j])+"-24")
                    else:
                        print(str(activity[j-1])+"-"+str(activity[j]))


    def test_act_service(self):
        a = Activity("011", ["12fascxz", "4dsfv"], datetime.datetime(2020, 10, 23), 15, "playing csgo")
        if a.activity_id == "011":
            assert True
        else:
            assert False
        self.add_activity(a)
        if len(self.activities) == 11:
            assert True
        else:
            assert False
        self.update_activity(["011", ["54ydf4", "32dgfg"], datetime.datetime(2020, 10, 22), 16, "date"])
        if self.activities[11].description == "date":
            assert True
        else:
            assert False
        self.remove_activity("011")
        if len(self.activities) == 11:
            assert True
        else:
            assert False

    def write_text_file1(self, file_name):
        f = open(file_name, "w")
        try:
            for act in self.activities:
                act_str = act.activity_id + "," + str(act.persons_id) + "," + act.date + "," + act.time +"," + act.description +"\n"
                f.write(act_str)
            f.close()
        except Exception as e:
            print("An error occurred -" + str(e))

    def read_text_file1(self, file_name):
        try:
            f = open(file_name, "r")
            args = f.readline().strip()
            while len(args) > 0:
                arg = []
                arg1 = []
                args = args.split(',')
                for i in range(1, len(args) - 3):
                    arg1.append(args[i])
                arg.append(args[0])
                arg.append(arg1)
                arg.append(args[len(args) - 3])
                arg.append(args[len(args) - 2])
                arg.append(args[len(args) - 1])
                self.add_activity(arg)
                args = f.readline().strip()
            f.close()
        except IOError as e:

            print("An error occured - " + str(e))
            raise e

        return self.activities



