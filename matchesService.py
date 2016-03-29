

class MatchesService(object):

    def getMatchByCountry(self, matches, countryName):
        res = []
        for m in matches:
            if m.country == countryName:
                res.append(m)
        return res

    def getMatchByTeam(self, matches, teamName):
        res = []
        for m in matches:
            if m.team1 == teamName or m.team2 == teamName:
                res.append(m)
        return res

