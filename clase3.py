class Curso : 
    def __ init__ (self, titulo):
        self.titulo = titulo
        self.participantes = 0
        self.cupos = 20


    def agregarParticipante (self):
        self.participantes += 1



sql = Curso("Gestion de bases de datos SQL")
print(type(sql))