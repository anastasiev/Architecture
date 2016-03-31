class ConsoleView(object):
    """
    Class shows info on console
    """

    def showIncorrectTeamNameMessage(self):
        """
        Print something
        :return:
        """
        print('Unknown team name')

    def showEnterTeamMessage(self):
        print('Enter team name:')

    def showIncorrectCaseMessage(self):
        print('Please try again')

    def showMatches(self, matches):
        """
        Show list of match
        :param matches:
        :return:
        """
        for match in matches:
            print(
                "%s vs %s - %s:%s on %s/%s/%s in %s" %
                (match.team1, match.team2, match.res1, match.res2,
                 match.date[0], match.date[1], match.date[2], match.country))

    def showMenu(self):
        """
        Show menu cases
        """
        print("""
        1. England
        2. Spain
        3. Ukraine
        4. Select team
        5. Exit
        """)

    def inputFromConsole(self):
        """
        Input from console
        :return:
        """
        return input()

