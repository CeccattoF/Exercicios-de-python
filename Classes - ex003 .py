class retangulo():
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def MudarValorLado(self):
        self.ladoA = a
        self.ladoB = b
    
    def RetornarValorLado(self):
        print(f"Valores do retangulo atualizados!\nLado A - {self.ladoA}\nLado B - {self.ladoB}")

    def CalcArea(self):
        self.area = self.ladoA * self.ladoB
        return self.area

    def Calcperimetro(self):
        self.perimetro = (self.ladoA*2) + (self.ladoB*2)
        return self.perimetro

a = float(input("Digite o Lado A:"))
b = float(input("Digite o Lado B:"))

novoretangulo = retangulo(a,b)

novoretangulo.MudarValorLado()
novoretangulo.CalcArea()
novoretangulo.Calcperimetro()
novoretangulo.RetornarValorLado()

print(f"Será necessario {novoretangulo.CalcArea():.2f} m² de ceramica e {novoretangulo.Calcperimetro()} m de rodapé.")
