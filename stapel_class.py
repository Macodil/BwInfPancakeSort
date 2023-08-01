from dataclasses import dataclass


@dataclass
class Stapel:
    n: int  # Größe des Pfannkuchenstapels
    p: int  # geschätzte maximale Anzahl an Wendungen

    ###########################################################################################
    ## bildet eine Liste, die Listen, die alle möglichen Anordnungen der Ursprungsliste nach ##
    ##                      x Tauschen enthalten, enthält. (x <= p)                          ##
    ##    die Anordnung wird durch eine Liste mit der Reihenfolge der Indexe repräsentiert   ##
    def __post_init__(self):
        self.wendungen = [[] for i in range(self.p + 1)]
        self.wendungen[0] = [list(range(self.n))]
        for anzahl_wendungen in range(1, self.p + 1):
            for current_wendung in self.wendungen[anzahl_wendungen - 1]:
                current = current_wendung[1:]
                if current not in self.wendungen[anzahl_wendungen]:
                    self.wendungen[anzahl_wendungen] += [current]
                for position_wendung in range(self.n - anzahl_wendungen):
                    current = current_wendung[position_wendung::-1] + current_wendung[position_wendung + 2:]
                    if current not in self.wendungen[anzahl_wendungen]:
                        self.wendungen[anzahl_wendungen] += [current]
    
    #############################################################
    ## Methode die die genaue Anzahl an nötigen Wendeoperation ##
    ##      einer gegebenen Liste der Länge n zurückgibt       ##
    def try_out(self, s: list[int]) -> int:
        for p in range(self.p + 2):
            for elm in self.wendungen[p]:
                correct_order = True
                for i in range(len(elm) - 1):
                    if s[elm[i]] > s[elm[i + 1]]:
                        correct_order = False
                if correct_order:
                    return p
        return -1