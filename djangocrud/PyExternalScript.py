from django.conf import settings
import djangocrud.settings as app_settings

#settings.configure(INSTALLED_APPS=app_settings.INSTALLED_APPS,DATABASES=app_settings.DATABASES)

import django
django.setup()

import json
from djangocrud.api.models import Movie
import sys
import math
from djangocrud.api.models import Movie
'''
from PySpice.Logging import Logging as Logging
from PySpice.Plot.BodeDiagram import bode_diagram
from PySpice.Probe.Plot import plot
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import * 
from PySpice.Spice.Netlist import SubCircuitFactory

'''
from .PySpice2.Logging import Logging as Logging
from .PySpice2.Plot.BodeDiagram import bode_diagram
from .PySpice2.Probe.Plot import plot
from .PySpice2.Spice.Netlist import Circuit
from .PySpice2.Unit import * 
from .PySpice2.Spice.Netlist import SubCircuitFactory


def func33(data):
    print("hello")
    print(data)
    circuit = Circuit('non-inv Operational Amplifier')
    #source=circuit.SinusoidalVoltageSource2('input', 'in', circuit.gnd, amplitude='1V')
    source=circuit.PulseVoltageSource2('input','in',circuit.gnd,initial_value='-1V',pulsed_value='1V',pulse_width='0.001s',period='0.004s')

    circuit.R('R1','inverting_input',circuit.gnd,'1kOhm')

    circuit.R('input', 'in', 'inverting_input', '1MOhm')
    circuit.VCVS('gain', 1, circuit.gnd, 'in', 'inverting_input')
    circuit.R('P1', 1, 2, '1kOhm')
    circuit.VCVS('buffer', 3, circuit.gnd, 2, circuit.gnd, 1)
    circuit.R('out', 3, 'output', '10Ohm')

    circuit.R('RF', 'inverting_input', 'output', '10kOhm')
    #circuit.C('CF','inverting_input', 'output', 2@u_uF)
    circuit.R('load', 'output', circuit.gnd, '1kOhm')

    simulator = circuit.simulator(temperature=25, nominal_temperature=25)
    analysis = simulator.transient(start_time=0,step_time=0.0001, end_time=0.08)

    print(circuit)
    lst=list()
    for i in analysis.output:
        lst.append(i)
    print(lst)
    Movie.objects.update_or_create(title="circuit",desc=circuit,year=13)


