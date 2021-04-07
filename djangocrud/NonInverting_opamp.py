import numpy as np

import matplotlib.pyplot as plt


import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()

'''
from PySpice.Plot.BodeDiagram import bode_diagram
from PySpice.Probe.Plot import plot
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *
'''

from .PySpice2.Plot.BodeDiagram import bode_diagram
from .PySpice2.Probe.Plot import plot
from .PySpice2.Spice.Netlist import Circuit
from .PySpice2.Unit import * 
from .PySpice2.Spice.Netlist import SubCircuitFactory


####################################################################################################

from PySpice.Spice.Netlist import SubCircuitFactory
from PySpice.Unit import *

circuit = Circuit('non-inv Operational Amplifier')

#source=circuit.SinusoidalVoltageSource2('input', 'in', circuit.gnd, amplitude='1V')
source=circuit.PulseVoltageSource2('input','in',circuit.gnd,initial_value='-1V',pulsed_value='1V',pulse_width='0.001s',period='0.004s')

circuit.R('R1','inverting_input',circuit.gnd,'1kOhm')

circuit.R('input', 'in', 'inverting_input', 10@u_MΩ)
circuit.VCVS('gain', 1, circuit.gnd, 'in', 'inverting_input', voltage_gain=kilo(1))
circuit.R('P1', 1, 2, 1@u_kΩ)
circuit.VCVS('buffer', 3, circuit.gnd, 2, circuit.gnd, 1)
circuit.R('out', 3, 'output', 10@u_Ω)

circuit.R('RF', 'inverting_input', 'output', 1@u_kΩ)
#circuit.C('CF','inverting_input', 'output', 2@u_uF)
circuit.R('load', 'output', circuit.gnd, 1@u_kΩ)

simulator = circuit.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.transient(start_time=0,step_time=0.00001, end_time=0.008)

print(circuit)
figure, (ax1, ax2) = plt.subplots(2, figsize=(20, 10))

plt.title("non-inv Operational Amplifier")
ax1.set_xlabel('Time [s]')
ax1.set_ylabel('Voltage [V]')
ax1.grid()
ax1.plot(analysis['in'])
ax1.set_ylim(-2,2)

ax2.set_xlabel('Time [s]')
ax2.set_ylabel('Voltage [V]')
ax2.grid()
ax2.plot(analysis.output)
ax2.set_ylim(-5,5)


plt.show()
