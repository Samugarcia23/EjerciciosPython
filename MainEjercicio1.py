import Persona

nombre=str(input("Introduce tu nombre: "))
edad=int(input("Introduce tu edad: "))
DNI=str(input("Introduce tu DNI: "))
sexo=str(input("Introduce tu sexo (H/M): "))
peso=int(input("Introduce tu peso: "))
altura=float(input("Introduce tu altura en cm: "))
objeto = Persona.Persona(nombre, edad, DNI, sexo, peso, altura)
resImc=objeto.calcularIMC()
resEdad=objeto.mayorDeEdad();
if resImc==1:
    print("Gordooooooo")
elif resImc==0:
    print("Ta bien")
elif resImc==-1:
    print("Tienes que comer mas")
if resEdad==True:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
print("Nombre: "+str(objeto.nombre)+" Edad: "+str(objeto.edad)+" DNI: "+str(objeto.DNI)+" Sexo: "+str(objeto.sexo)+" Peso: "+str(objeto.peso)+" Altura: "+str(objeto.altura))