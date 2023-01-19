class Speler:

    def __init__(self, input_id, input_hp, input_positie, input_naam, input_balance, input_kills = 0):

        assert len(input_id) == 8 and isinstance(input_id, str), 'Het meegegeven id moet precies 8 karakater bevatten en een string zijn!'
        assert 0 <= input_hp <= 100 and isinstance(input_hp, int), 'De meegegeven HP moet een integer tussen 0 en 100 zijn!'
        assert len(input_naam) > 0 and isinstance(input_naam, str), 'De meegegeven naam mag geen lege string zijn!'
        assert input_balance > 0 and isinstance(input_balance, float) or isinstance(input_balance, int), 'De meegegeven balance moet een float groter dan 0 zijn!'
        assert 0 <= input_kills <= 100 and isinstance(input_kills, int), 'De meegegeven killcount moet een integer tussen 0 en 100 zijn!'
        assert isinstance(input_positie, list) and len(input_positie) == 2 and isinstance(input_positie[0], int) and isinstance(input_positie[1], int), 'De positie moet een list van 2 integers zijn!' 

        self.id = input_id
        self.hp = input_hp
        self.positie = input_positie
        self.naam = input_naam
        self.balance = input_balance
        self.kills = input_kills

    def increaseKillcount(self, getal):
        assert isinstance(getal, int) and 0 <= getal <= 100 and 0 <= self.kills + getal <= 100, 'De meegegeven killcount moet een integer tussen 0 en 100 zijn en mag de regels van de totale killcount niet overtreden!'

        self.kills += getal

    def movePlayer(self, moveset):
        assert isinstance(moveset, tuple) and len(moveset) == 2 and isinstance(moveset[0], int) and isinstance(moveset[1], int), 'geen geldige moveset meegegeven aan functie' 

        self.positie[0] += moveset[0]
        self.positie[1] += moveset[1]

    def __repr__(self):
        return f"Speler '{self.naam}' met ID '{self.id}' en balance €{self.balance:.2f} neemt de positie met coordinaten {self.positie} in terwijl hij {self.hp} HP en {self.kills} kills heeft"

class Team:

    def __init__(self, input_teamnaam, input_teamlijst):
        assert len(input_teamnaam) > 0 and isinstance(input_teamnaam, str), 'De meegegeven teamnaam mag geen lege string zijn!'
        assert isinstance(input_teamlijst, list) and 5 > len(input_teamlijst) > 0, 'De teamlist is niet correct gedefinieerd'
        
        self.id_list = []

        for i in input_teamlijst:
            assert isinstance(i, Speler) and i.id not in self.id_list, 'De teamleden zijn niet correct gedefinieerd'
            self.id_list.append(i.id)

        self.teamnaam = input_teamnaam
        self.teamlijst = input_teamlijst

    def addPlayer(self, player):

        assert isinstance(player, Speler) and 5 > len(self.teamlijst) + 1 > 1, 'De speler is niet correct gedefinieerd of het team zit reeds vol'
        
        assert player.id not in self.id_list, 'De teamleden zijn niet correct gedefinieerd'
        self.id_list.append(player.id)

        self.teamlijst.append(player)

    def removePlayer(self, player):
        assert isinstance(player, Speler) and 4 > len(self.teamlijst) - 1 > 0, 'De speler is niet correct gedefinieerd of het team heeft nog meer 1 speler'
        assert player.id in self.id_list, "Deze speler zit niet in het team"
        self.id_list.remove(player.id)

        self.teamlijst.remove(player)

    def __repr__(self):
        spelerszin = ''

        for i in range(len(self.teamlijst)):
            if i == len(self.teamlijst) - 1:
                spelerszin += f"en {self.teamlijst[i].naam}"
            elif i == len(self.teamlijst) - 2:
                spelerszin += f"{self.teamlijst[i].naam} "
            else:
                spelerszin += f"{self.teamlijst[i].naam}, "
        return f"Het team met de naam {self.teamnaam} heeft op dit moment {len(self.teamlijst)} spelers, namelijk {spelerszin}."


try:
    Andre = Speler("45266345", 80, [50, 40], "TheAmazingAndre", 58.67, 6)
    
    print(Andre)
    
    Andre.increaseKillcount(69)
    
    Andre.movePlayer((50,-20))
    
    print(Andre)
    
    JefkesTeam = Team("De 4 Jeffetiers", [Andre])
    
    Franky = Speler("54375390", 94, [20, -100], "TheFabulousFranky", 12.70, 3)
    
    Polle = Speler("36563561", 20, [140, 10], "ThePatrioticPolle", 19.54, 11)
    
    Morton = Speler("90954352", 58, [50, 10], "TheMarvelousMorton", 82.15, 5)
    
    Sammy = Speler("90958352", 76, [140, 10], "TheSaturnicSammy", 3.88, 1)
    
    JefkesTeam.addPlayer(Franky)
    
    JefkesTeam.addPlayer(Polle)
    
    JefkesTeam.addPlayer(Sammy)
    
    JefkesTeam.removePlayer(Franky)
    
    JefkesTeam.addPlayer(Morton)
    
    print(JefkesTeam)
    
    JefkesTeam.removePlayer(Andre)
    
    print(JefkesTeam)
except AssertionError as er:
    print(er)