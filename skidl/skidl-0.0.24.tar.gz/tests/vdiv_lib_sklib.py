from skidl import Pin, Part, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

vdiv_lib = SchLib(tool=SKIDL).add_parts(*[
        Part(name='R',dest=TEMPLATE,tool=SKIDL,description='Resistor',keywords='r res resistor',ref_prefix='R',num_units=1,fplist=['R_*', 'R_*'],do_erc=True,footprint='Resistors_SMD:R_0805',pins=[
            Pin(num='1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.PASSIVE,do_erc=True)])])