from ll_shell import LLShell
from ll_mem_map_if import LLMemMapIf
#x = LLShell('serial', port='/dev/ttyACM0')
#print(x.read_bytes(88, size=1))
x = LLMemMapIf('../mem_map/philip_mem_map.csv','serial', port='/dev/ttyACM0')
print(x.read_reg('adc.0.mode'))
