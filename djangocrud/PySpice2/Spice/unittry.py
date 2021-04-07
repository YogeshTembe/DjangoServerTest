#from ..Math import rms_to_amplitude, amplitude_to_rms
#from ..Tools.StringTools import join_list, join_dict, str_spice, str_spice_list
from ..Unit import as_s, as_V, as_A, as_Hz
#from .BasicElement import VoltageSource, CurrentSource



sel=[(0, 0), (10@u_ms, 0), (11@u_ms, 3@u_V), (20@u_ms, 3@u_V), (30@u_ms, 2@u_V)]

sel.values = sum(([as_s(t), sel.__as_unit__(x)] for (t, x) in values), [])
sel.repeate_time = as_s(repeate_time)
sel.delay_time = as_s(delay_time)
print(sel)
