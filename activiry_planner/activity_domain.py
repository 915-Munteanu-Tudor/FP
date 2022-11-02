class Activity:
    '''
    initialize and create the objects called activity
    '''

    def __init__(self, activity_id, persons_id, date, time, description):
        self.persons_id = persons_id
        self.activity_id = activity_id
        self.date = date
        self.time = time
        self.description = description

    def get_persons_id(self):
        return self.persons_id

    def get_activity_id(self):
        return self.activity_id

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_description(self):
        return self.description

    def __str__(self) -> str:
        return "({0},{1},{2},{3},{4})".format(self.activity_id, self.persons_id, self.date, self.time, self.description)

    def print_activities(self):
        listt = ','.join(self.persons_id)
        # listt1=''.join((self.date))
        print(self.activity_id + " " + listt + ", " + self.date + ", " + "hour: " + self.time + ", " + self.description)

