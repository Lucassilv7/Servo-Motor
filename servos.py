import pandas as pd
class Servos:

    lista_servos = {'Es9251': {'torque_nominal': 0.27, 'massa': 2.50}, 'Power HD HD 1900A': {'torque_nominal': 1.50, 'massa': 9},
                     'Corona CS929MG': {'torque_nominal': 2.20, 'massa': 12.50}, 'Corona DS939HV': {'torque_nominal': 2.6, 'massa': 12.50},
                     'Corona DS-939MG': {'torque_nominal': 2.70, 'massa': 12.50}, 'Tower pro MG90S': {'torque_nominal': 2.20, 'massa': 13.40},
                     'Aerostar micro analog AS170MG': {'torque_nominal': 3.50, 'massa': 17.50}, 'Turnigy S306g-HV': {'torque_nominal': 3.10, 'massa': 21},
                     'Corona DS238HV': {'torque_nominal': 4, 'massa': 22}, 'Corona CS238MG': {'torque_nominal': 4.60, 'massa': 22},
                     'Futaba S3004': {'torque_nominal': 4.10, 'massa': 37}, 'Hextronik HX5010': {'torque_nominal': 6.50, 'massa': 39},
                     'Hitec Hs- 322': {'torque_nominal': 3.70, 'massa': 43}, 'Hitec Hs-645MG': {'torque_nominal': 9.60, 'massa': 55.20},
                     'Hitec Hs- 625': {'torque_nominal': 6.80, 'massa': 55.20}, 'Turnigy 9150 MG': {'torque_nominal': 15.80, 'massa': 61},
                     'Hitec Hs-7965MG': {'torque_nominal': 10, 'massa': 61.80}
                     }
    p = 0
    a = 0
    l = 0
    t = 0

    servos_profundor = []
    servos_aileron = []
    servos_leme = []
    servos_triquilha = []

    def __init__(self, torque_profundor, torque_aileron, torque_leme, torque_triquilha):
        self.torque_P = torque_profundor
        self.torque_A = torque_aileron
        self.torque_L = torque_leme
        self.torque_T = torque_triquilha

    def profundor(self):
        for servo, valor in self.lista_servos.items():
            if self.torque_P <= valor['torque_nominal']:
                if self.p <= valor['massa']:
                    self.p = valor['massa']
                    self.servos_profundor.append([servo, valor['torque_nominal'], valor['massa']])

        resultado = pd.DataFrame(self.servos_profundor, columns=['Servo', 'Torque(kg.cm)', 'Massa(g)'])
        resultado.to_excel('Profundor.xlsx', index=False)




    def aileron(self):
        for servo, valor in self.lista_servos.items():
            if self.torque_A <= valor['torque_nominal']:
                if self.a <= valor['massa']:
                    self.a = valor['massa']
                    self.servos_aileron.append([servo, valor['torque_nominal'], valor['massa']])

        resultado = pd.DataFrame(self.servos_aileron, columns=['Servo', 'Torque(kg.cm)', 'Massa(g)'])
        resultado.to_excel('Aileron.xlsx', index=False)

    def leme(self):
        for servo, valor in self.lista_servos.items():
            if self.torque_L <= valor['torque_nominal']:
                if self.l <= valor['massa']:
                    self.l = valor['massa']
                    self.servos_leme.append([servo, valor['torque_nominal'], valor['massa']])

        resultado = pd.DataFrame(self.servos_leme, columns=['Servo', 'Torque(kg.cm)', 'Massa(g)'])
        resultado.to_excel('Leme.xlsx', index=False)

    def triquilha(self):
        for servo, valor in self.lista_servos.items():
            if self.torque_T <= valor['torque_nominal']:
                if self.t <= valor['massa']:
                    self.t = valor['massa']
                    self.servos_triquilha.append([servo, valor['torque_nominal'], valor['massa']])

        resultado = pd.DataFrame(self.servos_triquilha, columns=['Servo', 'Torque(kg.cm)', 'Massa(g)'])
        resultado.to_excel('Triquilha.xlsx', index=False)