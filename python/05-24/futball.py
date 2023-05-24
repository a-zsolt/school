class Focista:
    def __init__ (self, nev, post, csapat):
        self.nev = nev
        self.post = post
        self.csapat = csapat

    def csapat_neve(self):
        if self.csapat == "Real Madrid":
            return("R")
        elif self.csapat == "Manchester City":
            return("M")
        else:
            return
        

print(Focista('Asd', 'ASD', 'Real Madrid').csapat_neve())