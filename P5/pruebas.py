from PySpice.Unit import *
from PySpice.Spice.Netlist import Circuit
import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()


circuit = Circuit('Parcial SD09')
"""
circuit.V('input', 1, circuit.gnd, 15@u_V)
circuit.R(1, 1, 2, 10@u_kΩ)
circuit.R(2, 1, 3, 10@u_kΩ)
circuit.R(3, 2, circuit.gnd, 10@u_kΩ)
circuit.R(4, 3, circuit.gnd, 10.1@u_kΩ)
# circuit.R(5, 3, 2, 1@u_kΩ)
"""

circuit.V('input', 1, 2, 12@u_V)
circuit.R('R1', 2, circuit.gnd, 1@u_Ω)
circuit.R('R2', 1, circuit.gnd, 10@u_Ω)
circuit.R('R3', 3, circuit.gnd, 3@u_Ω)
circuit.R('R4', 4, 3, 6@u_Ω)
circuit.R('R5', 5, 4, 6@u_Ω)
circuit.R('R6', 1, 5, 4@u_Ω)
circuit.R('R7', 5, 3, 4@u_Ω)


simulator = circuit.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.operating_point()

vr7 = []
vr1 = 0
for node in analysis.nodes.values():
    # Fixme: format value + unit
    print('Node {}: {:4.1f} V'.format(str(node), float(node)))
    if str(node) == '5' or str(node) == '3':
        vr7.append(float(node))
    elif str(node) == '2':
        vr1 = float(node)

r7v = vr7[0] - vr7[1]
print("\nR7 Voltage = {:.3} V".format(r7v))
print("I1 = {:.3} A".format(r7v/4))
print("I = {:.3}".format(vr1/-1))

# print(circuit)


"""
class Resistance:
    def __init__(self, value):
        self.value = value
        self.v = None
        self.i = None

    def __str__(self):
        r = formating(self.value)
        v = formating(self.v)
        i = formating(self.i)
        return f'Ohm={r}\nV={v}V\nI={i}A'

    def current(self, v):
        self.v = v
        self.i = self.v / self.value
        return self.i

    def voltage(self, i):
        self.i = i
        self.v = self.value * self.i
        return self.v


def formating(num):
    if 1e-9 <= num < 1e-6:
        return f'{num*1e9} n'
    elif 1e-6 <= num < 1e-3:
        return f'{num*1e6} μ'
    elif 1e-3 <= num < 1:
        return f'{num*1e3} m'
    elif 1 <= num < 1e3:
        return f'{num} '
    elif 1e3 <= num < 1e6:
        return f'{num/1e3} K'
    elif 1e6 <= num < 1e9:
        return f'{num/1e6} M'
    elif 1e9 <= num < 1e12:
        return f'{num/1e9} G'


r1 = Resistance(250)
r1.current(1.2)
print(r1)
r1.voltage(3)
print(r1)
"""
