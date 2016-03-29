from view import *
from matchFactory import *
from matchesService import *
import coverage

class MatchesController(object):
    def __init__(self):
        self.view = ConsoleView()
        self.factory = MatchFactory()
        self.service = MatchesService()

    def navigation(self):
        inp = ""
        matches = self.factory.getAllMatches()
        while (True):
            self.view.showMenu()
            inp = self.view.inputFromConsole()
            if(inp == '1'):
                self.view.showMatches(self.service.getMatchByCountry(matches, "England"))
            elif(inp == '2'):
                self.view.showMatches(self.service.getMatchByCountry(matches, "Spain"))
            elif(inp == '3'):
                self.view.showMatches(self.service.getMatchByCountry(matches, "Ukraine"))
            elif(inp == '4'):
                self.view.showEnterTeamMessage()
                teamName = self.view.inputFromConsole()
                matchesTeam = self.service.getMatchByTeam(matches, teamName)
                if(not matchesTeam):
                    self.view.showIncorrectTeamNameMessage()
                else:
                    self.view.showMatches(matchesTeam)
            elif(inp == '5'):
                exit()
            else:
                self.view.showIncorrectCaseMessage()

