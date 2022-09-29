from Gerador import Gerador
from GeradorCongLinear import GeradorCongLinear


print("hello")
#gerador = Gerador()
gerador = GeradorCongLinear()
gerador.generate(16807, 192)

values = gerador.getGeneratedValues()
print(values)




