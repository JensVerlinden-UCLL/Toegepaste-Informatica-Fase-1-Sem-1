# https://dodona.ugent.be/nl/courses/1286/series/14353/activities/2030651884

class Stad:

    def __init__(self, fnaam, finwoners = 5000):
        assert isinstance(fnaam, str) and isinstance(finwoners, int) and 69 < finwoners, "Dit zijn geen correcte waarden" 
        
        self.naam = fnaam
        self.inwoners = finwoners

    def __eq__(self, other):
        
        if not isinstance(other, self.__class__):
            return False
        
        return self.naam == other.naam

    def heeft_meer_inwoners(self, other):

        if not isinstance(other, self.__class__) or self.inwoners <= other.inwoners:
            return False
        
        else: return True
    
    def __str__(self):
        return f"{self.naam} heeft {self.inwoners} inwoners"

class Demografie:

    def __init__(self, fnaamregio, fstedenlijst = []):

        assert isinstance(fnaamregio, str) and isinstance(fstedenlijst, list), "Dit zijn geen correcte waarden"
        for i in fstedenlijst:
            assert isinstance(i, Stad), "De lijst bevat geen stadelementen"

        
        new_stedenlijst = []

        for i in fstedenlijst:
            if i not in new_stedenlijst:
                new_stedenlijst.append(i)
        
        new_stedenlijst.sort(key= lambda steden: steden.inwoners)

        self.naamregio = fnaamregio
        self.stedenlijst = new_stedenlijst

    def voeg_stad_toe(self, stad):

        assert isinstance(stad, Stad), "Dit is geen stad-object"

        if stad not in self.stedenlijst:

            self.stedenlijst.append(stad)

            self.stedenlijst.sort(key= lambda steden: steden.inwoners)


    def bereken_totaal_aantal_inwoners(self):

        aantal = 0

        for i in self.stedenlijst:
            aantal += i.inwoners

        return aantal

    def fusioneer(self, stad1, stad2, fusienaam):

        for i in self.stedenlijst:

            if i.naam == stad1:

                inwoners1 = i.inwoners

                self.stedenlijst.remove(i)

            if i.naam == stad2:

                inwoners2 = i.inwoners

                self.stedenlijst.remove(i)

        self.stedenlijst.append(Stad(fusienaam, inwoners1 + inwoners2))

    def geef_steden_met_minimum_aantal_inwoners(self, aantal):

        minimum_lijst = []

        for i in self.stedenlijst:

            if i.inwoners >= aantal:
                minimum_lijst.append(i)

        return minimum_lijst

    def print_steden_met_minimum_aantal_inwoners(self, aantal):

        zin = ""

        inwonerslijst = self.geef_steden_met_minimum_aantal_inwoners(aantal)

        for i in inwonerslijst:

            if inwonerslijst.index(i) != 0:
                zin += f"\n{i.naam} heeft {i.inwoners} inwoners"

            else: zin += f"{i.naam} heeft {i.inwoners} inwoners"

        print(zin)

    def __str__(self):
         
        zin = f"Regio: {self.naamregio}\nTotaal aantal inwoners: {self.bereken_totaal_aantal_inwoners()}"
        for i in self.stedenlijst:
            zin += f"\n{i.__str__()}"

        return zin

try:
    Woefstad = Stad("Woefstad", 50)
except AssertionError as e:
    print(e.args)