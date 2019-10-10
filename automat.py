class Automat:

    class Estat:

        def __init__(self, nom, inicial=False, final=False):
            self.nom = nom
            self.transicions = {}
            self.inicial = inicial
            self.final = final

        def afegir_transicio(self, lletra, estat):
            """ """
            if lletra not in self.transicions.keys():
                self.transicions[lletra] = []
            self.transicions[lletra].append(estat)

        def mostrar_transicions(self):
            """ """
            dicc = {}
            for value in self.transicions:
                destinacions = self.transicions[value]
                if len(destinacions) == 1:
                    dicc[value] = destinacions[0].nom
                else:
                    dicc[value] = []
                    for estat in destinacions:
                        dicc[value].append(estat.nom)
            return dicc

        def to_lletra(self, lletra):
            """ Retorna totes les transicions que té un estat donada una lletra """
            if lletra in self.transicions:
                return self.transicions[lletra]
            return []

        def show(self):
            """ Diu el nom de lestat, si és final o inicial i totes les seves transicions"""
            set = ''
            if self.inicial:
                set += 'I'
            if self.final:
                set += 'F'
            print(self.nom + ' (' + set + ') ' + str(self.mostrar_transicions()))

    def __init__(self):
        self.estats = []

    def is_there_transicio(self, nom_estat, lletra, nom_desti):
        """ Mira si existeix una transició d'un estat donada una lletra a un estat destí"""
        estat = self.get_estat(nom_estat)
        if estat is not None and lletra in estat.transicions.keys():
            return self.get_estat(nom_desti) in estat.transicions[lletra]
        return False

    def get_all_estats(self):
        """ Retorna una llista de tots els estats """
        list = []
        for estat in self.estats:
            list.append(estat)
        return list

    def get_estat(self, nom):
        """ Retorna un estat donat el seu nom """
        for estat in self.estats:
            if estat.nom.__eq__(nom):
                return estat
        return None

    def get_estats_inicials(self):
        """ Dóna una llista amb tots els estats inicials"""
        llista = []
        for estat in self.estats:
            if estat.inicial:
                llista.append(estat)
        return llista

    def get_estats_finals(self):
        """ Dóna una llista amb tots els estats finals"""
        llista = []
        for estat in self.estats:
            if estat.final:
                llista.append(estat)
        return llista

    def afegir_transicio(self, nom_estat, lletra, destinacio):
        """ Afegeix una transicio a un estat donat el seu nom, la lletra i l'estat destí"""
        for estat in self.estats:
            if estat.nom.__eq__(nom_estat):
                estat_destinacio = self.get_estat(destinacio)
                if estat_destinacio is not None:
                    estat.afegir_transicio(lletra, estat_destinacio)

    def afegir_estat(self, estat, inicial=False, final=False):
        """ Afegeix un estat nou. En cas que el nom ja existeixi, mira si l'ha d'actualitzar"""
        if self.get_estat(estat) is None:
            estat = self.Estat(estat, inicial=inicial, final=final)
            self.estats.append(estat)
        else:
            estat = self.get_estat(estat)
            if estat.inicial:
                estat.inicial = inicial
            if estat.final:
                estat.final = final

    def alphabet(self):
        """ Retorna l'alfabet """
        alphabet = []
        for estat in self.estats:
            for transicio in estat.transicions:
                if transicio[0] not in alphabet:
                    alphabet.append(transicio[0])
        return alphabet

    def show(self):
        """ Mostra l'autòmat per pantalla """
        for estat in self.estats:
            print('* ', end='')
            estat.show()

    def is_determinista(self):
        for estat in self.estats:
            for lletra in self.alphabet():
                if lletra.__eq__('l'):
                    return False
                if len(estat.to_lletra(lletra)) != 1:
                    return False
        return True