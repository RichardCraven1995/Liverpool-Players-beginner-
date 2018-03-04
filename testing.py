# Liverpool players is the class
# within liverpool are defenders, midfielders and attackers (class within a class)
# within the defender, midfielder and attack categories are individual players
# all share the same attributes - pace, shooting, defending, passing

class Liverpool(object):
    pass

    def __init__(self):
        self.name = "Liverpool"
        self.defender = Defender
        self.midfielder = Midfielder
        self.attacker = Attacker


class Defender:(Liverpool)
pass


defender1 = Defender
defender1.position = 'Left Back'
defender1.first_name = 'Andrew'
defender1.surname = 'Robertson'
defender1.defending = 80
defender1.passing = 70
defender1.shooting = 50
defender1.overall = 67

defender2 = Defender
defender2.position = 'Centre Back'
defender2.first_name = 'Dejan'
defender2.surname = 'Llovren'
defender2.defending = 75
defender2.passing = 55
defender2.shooting = 30
defender2.overall = 50

defender3 = Defender
defender3.position = 'Centre Back'
defender3.first_name = 'Virgil'
defender3.surname = 'Van Dijk'
defender3.defending = 90
defender3.passing = 75
defender3.shooting = 65
defender3.overall = 77

defender4 = Defender
defender4.position = 'Right Back'
defender4.first_name = 'Trent'
defender4.surname = 'Alexander-Arnold'
defender4.defending = 75
defender4.passing = 70
defender4.shooting = 70
defender4.overall = 72


class Midfielder(Liverpool):
    pass



    midfielder1 = Midfielder(Liverpool)
    midfielder1.position = 'Central Midfield'
    midfielder1.first_name = 'Jordan'
    midfielder1.surname = 'Henderson'
    midfielder1.defending = 68
    midfielder1.passing = 78
    midfielder1.shooting = 75
    midfielder1.overall = 74


    midfielder2 = Midfielder(Liverpool)
    midfielder2.position = 'Box to Box Midfield'
    midfielder2.first_name = 'Emre'
    midfielder2.surname = 'Can'
    midfielder2.defending = 75
    midfielder2.passing = 75
    midfielder2.shooting = 75
    midfielder2.overall = 75

    midfielder3 = Midfielder(Liverpool)
    midfielder3.positiion = 'Attacking Midfield'
    midfielder3.first_name = 'Alex'
    midfielder3.surname = 'Ox-Chamberlain'
    midfielder3.defending = 65
    midfielder3.passing = 79
    midfielder3.shooting = 78
    midfielder3.overall = 75



if defender1 (>80):
print(True)







