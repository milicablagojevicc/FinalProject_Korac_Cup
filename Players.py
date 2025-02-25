#To make the game more interesting, we will include top 12 of all time that played in these clubs

class Player:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players

partizan_players = [
Player("Bogdan Bogdanovic", 93), Player("Aleksandar Djordjevic", 90),
Player("Predrag Danilovic", 90), Player("Vlade Divac", 89), Player("Miroslav Beric", 85),
Player("Milos Vujanic", 88), Player("Ivo Nakic", 86), Player("Dusan Kecman", 85),
Player("Zeljko Rebraca", 84), Player("Sasa Obradovic", 88), Player("Novica Velickovic", 86),
Player("Dejan Milojevic", 89)
]

zvezda_players = [
Player("Nebojsa Popovic", 85), Player("Bora Stankovic", 83),
Player("Radomir Saper", 86), Player("Milan Bjelogrlic", 84), Player("Radivoj Korac", 90),
Player("Ranko Zeravica", 87), Player("Igor Rakocevic", 86), Player("Filip Petrusev", 83),
Player("Stefan Jovic", 82), Player("Nikola Kalinic", 83), Player("Milos Teodosic", 85),
Player("Nemanja Nedovic", 85)
]

mega_players = [
Player("Nikola Jokic", 90), Player("Vasilije Micic", 87),
Player("Ivica Zubac", 82), Player("Marko Simonovic", 80), Player("Nikola Jovic", 84),
Player("Nikola Djurisic", 78), Player("Ognjen Jaramaz", 76), Player("Nemanja Dangubic", 74),
Player("Rade Zagorac", 75), Player("Bogoljub Markovic", 77), Player("Nikola Ivanovic", 76),
Player("Danilo Andjusic", 83)
]

fmp_players = [
Player("Petar Popovic", 79), Player("Nikola Saranovic", 77),
Player("Ranko Simovic", 81), Player("Filip Barna", 76), Player("Stefan Lazarevic", 84),
Player("Ognjen Kuzmic", 75), Player("Vojislav Stojanovic", 74), Player("Aleksa Stanojevic", 72),
Player("Dusan Radosavljevic", 73), Player("Nikola Gasic", 75), Player("Bojan Tomasevic", 80),
Player("Ognjen Matovic", 71)
]
# Teams
partizan = Team("Partizan Belgrade", partizan_players)
zvezda = Team("Crvena Zvezda", zvezda_players)
mega = Team("Mega Basket", mega_players)
fmp = Team("FMP", fmp_players)

# List of all teams
teams = [partizan, zvezda, mega, fmp]