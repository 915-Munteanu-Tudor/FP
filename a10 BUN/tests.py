import unittest
from  person_services import Person_Services, Person
from activity_services import Activity, Activity_Services
import datetime

class Tests(unittest.TestCase):
    def test_person_add(self, properties_dict):
        self.sv=Person_Services(properties_dict)

        newpers=["98us","Carlos","0722333444"]
        self.sv.add_person(newpers)


        self.assertEqual(newpers[0], "98us")
        self.assertEqual(newpers[2], "0722333444")
        self.assertEqual(newpers[1], "Carlos")
        #self.assertEqual(len(self.sv.persons), 11)
        newpers1=["iu8","Kevin","0711888999"]
        self.sv.add_person(newpers1)
        self.assertIsNot(newpers, newpers1)
        self.sv.remove_pers("98us")
        self.sv.remove_pers("iu8")


    def test_activity_add(self, properties_dict):
        self.sq=Person_Services(properties_dict)
        self.svv = Activity_Services(self.sq, properties_dict)
        item=["012",["54ydf4,13adfs"],datetime.datetime(2021,3,21),15,"match"]
        it=item[2].strftime("%d %b %Y")
        act = [item[0], item[1], it, str(item[3]), item[4]]
        self.svv.add_activity(act)
        self.assertEqual(act[1], ["54ydf4,13adfs"])
        self.assertEqual(act[0], "012")
        self.assertEqual(act[2], "21 Mar 2021")
        self.assertEqual(act[3], str(15))
        self.assertEqual(act[4], "match")
        #self.assertEqual(len(self.svv.activities), 11)
        self.assertNotIsInstance(act, Activity)
        self.svv.remove_activity("012")