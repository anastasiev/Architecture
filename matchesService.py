

class MatchesService(object):
    """
    Class implements actions with matches
    """

    def getMatchByCountry(self, matches, countryName):
        """
        Find all matches in selected country
        :param matches:
        :param countryName:
        :return:
        """
        res = []
        for m in matches:
            if m.country == countryName:
                res.append(m)
        return res

    def getMatchByTeam(self, matches, teamName):
        """
        Find all matches in selected team
        :param matches:
        :param teamName:
        :return:
        """
        res = []
        for m in matches:
            if m.team1 == teamName or m.team2 == teamName:
                res.append(m)
        return res
