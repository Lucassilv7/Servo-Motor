from servos import Servos

print("----- Informe os valores dos torques -----")
valor_profundor = float(input('Torque do profundor: '))
valor_aileron = float(input('Torque do aileron: '))
valor_leme = float(input('Torque do leme: '))
valor_triquilha = float(input('Torque da triquilha: '))

servo = Servos(valor_profundor, valor_aileron, valor_leme, valor_triquilha)

print("----- Arquivos Gerados -----")
print("VEJA O MESMO DIRETÓRIO QUE DEIXOU O EXECUTAVEL")
servo.profundor()
servo.aileron()
servo.leme()
servo.triquilha()
