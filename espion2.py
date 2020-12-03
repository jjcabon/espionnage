# Créé par prof, le 29/11/2020
class Espion:
    def __init__(self,numero,message):
        self.numero=numero
        self.message=message
        self.Gauche=None
        self.Droite=None
    def __str__(self):
        return(str(self.numero))
    def insert(self,numero,message):
        if numero<=self.numero:
            if self.Gauche is None:
                self.Gauche=Espion(numero,message)
            else:
                self.Gauche.insert(numero,message)
        elif numero>=self.numero:
            if self.Droite is None:
                self.Droite=Espion(numero,message)
            else:
                self.Droite.insert(numero,message)
    def inf_parcours(self):
        if not(self.Gauche is None):
            self.Gauche.inf_parcours()
        print(self.message)
        if not(self.Droite is None):
             self.Droite.inf_parcours()
    def pref_parcours(self):
        print(self.message)
        if not(self.Gauche is None):
            self.Gauche.pref_parcours()
        if not(self.Droite is None):
             self.Droite.pref_parcours()
    def suff_parcours(self):
        if not(self.Gauche is None):
            self.Gauche.suff_parcours()
        if not(self.Droite is None):
             self.Droite.suff_parcours()
        print(self.message)



racine=Espion(7,'6c')
racine.insert(5,'65')
racine.insert(10,'61')
racine.insert(4,'65')
racine.insert(12,'6d')
racine.insert(6,'48')
racine.insert(9,'61')
racine.insert(1,'64')
racine.insert(11,'64')
racine.insert(14,'69')
racine.insert(13,'65')
racine.insert(3,'6f')
racine.insert(2,'43')
racine.insert(8,'78')
racine.insert(15,'63')
print("parcours infixe")
racine.inf_parcours()
print("parcours préfixe")
racine.pref_parcours()
print("parcours suffixe")
racine.suff_parcours()
"7061756c".decode("hex")
print("436f646548657861646563696d616c".decode("hex"))
