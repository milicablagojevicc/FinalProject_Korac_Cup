#To make the game more interesting, we will include top 12 of all time that played in these clubs

class Player:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players

# Sample players and teams
partizan_players = [
    Player("Zeljko Rebraca", 88), Player("Aleksandar Djordjevic", 92),
    Player("Predrag Danilovic", 90), Player("Nikola Loncar", 78), Player("Miroslav Beric", 75),
    Player("Zoran Stevanovic", 72), Player("Haris Brkic", 80), Player("Ugljesa Kojadinovic", 68),
    Player("Nenad Canak", 70), Player("Sasa Obradovic",  85), Player("Dragan Lukovski", 73),
    Player("Nikola Bulatovic", 77)
]
zvezda_players = [
    Player("Zeljko Rebraca", 88), Player("Aleksandar Djordjevic", 92),
    Player("Predrag Danilovic", 90), Player("Nikola Loncar", 78), Player("Miroslav Beric", 75),
    Player("Zoran Stevanovic", 72), Player("Haris Brkic", 80), Player("Ugljesa Kojadinovic", 68),
    Player("Nenad Canak", 70), Player("Sasa Obradovic",  85), Player("Dragan Lukovski", 73),
    Player("Nikola Bulatovic", 77)
    ]
mega_players = [
    Player("Zeljko Rebraca", 88), Player("Aleksandar Djordjevic", 92),
    Player("Predrag Danilovic", 90), Player("Nikola Loncar", 78), Player("Miroslav Beric", 75),
    Player("Zoran Stevanovic", 72), Player("Haris Brkic", 80), Player("Ugljesa Kojadinovic", 68),
    Player("Nenad Canak", 70), Player("Sasa Obradovic",  85), Player("Dragan Lukovski", 73),
    Player("Nikola Bulatovic", 77)
    ]
fmp_players = [
    Player("Zeljko Rebraca", 88), Player("Aleksandar Djordjevic", 92),
    Player("Predrag Danilovic", 90), Player("Nikola Loncar", 78), Player("Miroslav Beric", 75),
    Player("Zoran Stevanovic", 72), Player("Haris Brkic", 80), Player("Ugljesa Kojadinovic", 68),
    Player("Nenad Canak", 70), Player("Sasa Obradovic",  85), Player("Dragan Lukovski", 73),
    Player("Nikola Bulatovic", 77)
]
mozart_players = [
    Player("Zeljko Rebraca", 88), Player("Aleksandar Djordjevic", 92),
    Player("Predrag Danilovic", 90), Player("Nikola Loncar", 78), Player("Miroslav Beric", 75),
    Player("Zoran Stevanovic", 72), Player("Haris Brkic", 80), Player("Ugljesa Kojadinovic", 68),
    Player("Nenad Canak", 70), Player("Sasa Obradovic",  85), Player("Dragan Lukovski", 73),
    Player("Nikola Bulatovic", 77)
]
spartak_players = [
    Player("Zeljko Rebraca", 88), Player("Aleksandar Djordjevic", 92),
    Player("Predrag Danilovic", 90), Player("Nikola Loncar", 78), Player("Miroslav Beric", 75),
    Player("Zoran Stevanovic", 72), Player("Haris Brkic", 80), Player("Ugljesa Kojadinovic", 68),
    Player("Nenad Canak", 70), Player("Sasa Obradovic",  85), Player("Dragan Lukovski", 73),
    Player("Nikola Bulatovic", 77)
]
vojvodina_players = [
    Player("Zeljko Rebraca", 88), Player("Aleksandar Djordjevic", 92),
    Player("Predrag Danilovic", 90), Player("Nikola Loncar", 78), Player("Miroslav Beric", 75),
    Player("Zoran Stevanovic", 72), Player("Haris Brkic", 80), Player("Ugljesa Kojadinovic", 68),
    Player("Nenad Canak", 70), Player("Sasa Obradovic",  85), Player("Dragan Lukovski", 73),
    Player("Nikola Bulatovic", 77)
]
dunav_players = [
    Player("Zeljko Rebraca", 88), Player("Aleksandar Djordjevic", 92),
    Player("Predrag Danilovic", 90), Player("Nikola Loncar", 78), Player("Miroslav Beric", 75),
    Player("Zoran Stevanovic", 72), Player("Haris Brkic", 80), Player("Ugljesa Kojadinovic", 68),
    Player("Nenad Canak", 70), Player("Sasa Obradovic",  85), Player("Dragan Lukovski", 73),
    Player("Nikola Bulatovic", 77)
    ]
# Teams
partizan = Team("Partizan Belgrade", partizan_players)
zvezda = Team("Crvena Zvezda", zvezda_players)
mega = Team("Mega Basket", mega_players)
fmp = Team("FMP Soccerbet", fmp_players)
mozart = Team("Mozart", mozart_players)
spartak = Team("Spartak", spartak_players)
vojvodina = Team("Vojvodina", vojvodina_players)
dunav = Team("Dunav", dunav_players)

# List of all teams
teams = [partizan, zvezda, mega, fmp, mozart, spartak, vojvodina, dunav]
