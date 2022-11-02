class UserInterface:
    def display_commands(self):
        '''
        prints all the command as a menu
        '''
        print("\nInstructions:\n ADD-PERSON \n SHOW-PERSON \n REMOVE-PERSON \n UPDATE-PERSON \n SEARCH-PERSON \n ADD-ACTIVITY \n SHOW-ACTIVITY \n ACTIVITIES-WITH-PERSON \n ACTIVITIES-AT-DATE \n SEARCH-ACTIVITY \n REMOVE-ACTIVITY \n BUSIEST-DAY \n UPDATE-ACTIVITY \n UNDO \n QUIT\n")

    def command(self):
        '''

        :return: splits the inputed commands in order to return the command and the args
        '''
        self.operations=[]
        self.objects=[]
        self.comm = input("Enter your instruction: ")


        # todo: split for add activity,update and implement split for every functionality starting with...
        if self.comm.startswith("ADD-ACTIVITY") or self.comm.startswith("UPDATE-ACTIVITY"):
            arg = []
            arg1 = []
            pos = self.comm.find(' ')
            c = self.comm[:pos]
            args = self.comm[(pos + 1):]
            args = args.split(',')
            for i in range(1, len(args) - 3):
                arg1.append(args[i])
            arg.append(args[0])
            arg.append(arg1)
            arg.append(args[len(args) - 3])
            arg.append(args[len(args) - 2])
            arg.append(args[len(args) - 1])
            return c, arg
        elif self.comm.startswith("ACTIVITIES-AT-DATE"):
            pos = self.comm.find(' ')
            c = self.comm[:pos]
            args = self.comm[(pos + 1):]
            return c, args
        elif self.comm.startswith("BUSIEST-DAY") or self.comm.startswith("UNDO") or self.comm.startswith("REDO"):
            c=self.comm
            return c, []

        elif self.comm.startswith("ADD-PERSON") or self.comm.startswith("UPDATE-PERSON"):
            pos = self.comm.find(' ')
            c = self.comm[:pos]
            args = self.comm[(pos + 1):]
            args = args.split(',')
            return c, args
        elif self.comm.startswith("REMOVE-PERSON") or self.comm.startswith("REMOVE-ACTIVITY") or self.comm.startswith("SEARCH-ACTIVITY") or self.comm.startswith("SEARCH-PERSON") or self.comm.startswith("ACTIVITIES-WITH-PERSON"):
            self.comm = self.comm.split()
            return self.comm[0], self.comm[1]
        elif self.comm != ("SHOW-PERSON") and self.comm != ("SHOW-ACTIVITY") and self.comm != (
        "QUIT") and self.comm != ("REMOVE-PERSON") and self.comm != ("REMOVE-ACTIVITY") and self.comm != (
        "ADD-PERSON") and self.comm != ("ADD-ACTIVITY") and self.comm != ("UPDATE-PERSON") and self.comm != (
        "UPDATE-ACTIVITY") and self.comm!=("BUSIEST-DAY") and self.comm!=("UNDO") and self.comm!=("SEARCH-ACTIVITY") and self.comm!=("SEARCH-PERSON") and self.comm!=("ACTIVIVITIES-AT-DATE") and self.comm!=("ACTIVITIES-WITH-PERSON"):
            print("Wrong instruction.")

        return self.comm, []

