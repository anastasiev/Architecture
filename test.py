"""

>>> from view import *

>>> from matchFactory import *

>>> from matchesService import *

>>> ConsoleView().showIncorrectCaseMessage()
Please try again

>>> ConsoleView().showMatches([Match("cont", "team1", "team2", 0, 0, [31, 3, 2016])])
team1 vs team2 - 0:0 on 31/3/2016 in cont

>>> ConsoleView().showIncorrectTeamNameMessage()
Unknown team name

>>> ConsoleView().showEnterTeamMessage() #doctest: +NORMALIZE_WHITESPACE
Enter team name:

>>> MatchesService().getMatchByCountry(MatchFactory().getAllMatches(), "Ukraine")[0] #doctest: +ELLIPSIS
<model.Match object at 0x...>

>>> MatchesService().getMatchByTeam(MatchFactory().getAllMatches(), "Dynamo")[0] #doctest: +ELLIPSIS
<model.Match object at 0x...>

>>> MatchFactory().getAllMatches()[0] #doctest: +ELLIPSIS
<model.Match object at 0x...>

>>> ConsoleView().showMenu() #doctest: +NORMALIZE_WHITESPACE
1. England
2. Spain
3. Ukraine
4. Select team
5. Exit

"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
