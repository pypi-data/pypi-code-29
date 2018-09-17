# -*- coding: UTF-8 -*-
"""
Basic configuration of the KiCAD XML -> Spice Opus netlister. 

*config* is a dictionary with the following entries:

* ``EnumerateNets`` - when set to ``True`` all nets that are not explicitly 
  named (nets that match the ``RenameNetPattern`` regular expression) are 
  renamed to ``<prefix><number>``. If ``False`` nets keep the names 
  assigned by the CAD tool. All illegal characters are converted to 
  underscores. ``+`` and ``-`` are converted to ``p`` and ``m``, respectively. 
* ``RenameNetPattern`` - nets that match this regular expression
  are renamed to ``<prefix><number>``.  A new name is generated based on 
  ``NetPrefix`` and ``NetNumbeers``. 
* ``NetPrefix`` in the ``<prefix>`` used in renaming. 
* ``NetNumbers`` - number of decimal places used for constructing 
  ``<number>``. Numbers that don't fill all the reserved places are prefixed 
  with zeros. If set to ``None`` the number takes as many places as it 
  requires and no prefixing with zeros takes place. 
* ``GroundNets`` - list of net names that represent the ground. These nets are 
  renamed to ``0``. 
* ``SymbolLib`` - name of the KiCAD library that holds the symbols 
  representing SPICE devices and netlist directives. 
* ``Components`` - list holding the names of the Kicad components that 
  represent netlist directives. These components are not handled by the 
  ``Mapping`` rules. 
* ``SuppressEnd`` - when set to ``True`` the ``.end`` card is not added. 
  This is useful for dumping include files. ``.end`` is never added to files 
  that define a subcircuit. 
* ``Mapping`` - a dictionary that specifies how individual components 
  are mapped to a netlist. An entry in this dictionary has a tuple of the 
  form ``(library, component)`` for key. The value specifies how a 
  component is dumped. If the library member of the key tuple is ``None`` 
  the entry matches components with the specified name from all libraries. 
  When looking for a mapping the netlister searches for an exact match. If 
  it is not found it tries to find an entry with ``(None, component)`` as 
  key. Finally, if that one is also not found the ``Mapping`` entry with 
  ``(None, None)`` for key is (the default) is used. 
  
  Because KiCad stores copies of component definitions in cache files it is 
  recommended that the mapping entries have the form ``(None, component)``. 
  Such entries will match a component regardless of the library where the 
  component is stored. 
  

The following entries are availablefor describing the mapping of one 
component:

* ``NamePrefix`` - SPICE device name prefix (one letter) used for this 
  component. Case is ignored. If a refdes does not start with this letter 
  the name is prefixed with this letter. If set to ``None`` the original 
  KiCad refdes is used. 
* ``SpiceDevice`` - SPICE device name used for this component. 
  Currently not used. 
* ``ValueField`` - specified the name of the field whose value 
  is overridden by the ``Value`` field. If set to ``None`` the ``Value`` 
  field does not correspond to any of the instance parameters. 
  If a field with the same name as given by ``ValueField`` already 
  exists the value of the ``Value`` field will override it. 
  If the parameter is not listed in ``Parameters`` it will not be dumped via 
  ``##PNV()``. You will have to explicitly list it in the ``Pattern`` as 
  ``#PNV(<parameter name>``. 
* ``Parameters`` - the list of field names that correspond to SPICE instance 
  parameters with the same name. 
* ``PinMap`` - the list of pin numbers that specifies how pins are 
  mapped to SPICE instance nodes. 
* ``OutPattern`` - string with macros that specifies how SPICE instance(s) 
  correspondint to a component should be generated. The following macros 
  can be used: 
  
  * ``#REF()`` - refdes of a component with an optionally added prefix 
    letter (see ``NamePrefix``). This refdes is all-lowercase. 
  * ``#REFORIG()`` - original KiCad refdes of a component (lowercase). 
  * ``#PINS()`` - nets corresponding to pins ordered as specified by 
    ``PinMap``. 
  * ``#PINS(pin1 pin2 ...)`` - nets corresponding to listed pins
  * ``#MODEL()`` - SPICE model name (specified by Value or Model field)
  * ``PARAM()`` - expands to ``param:`` if at least one parameter is 
    specified. Otherwise expands to an empty string. 
    Only parameters that are listed under ``Parameters`` in the ``Mapping``
    dictionary or ``Parameters`` field of the component are considered when 
    counting passed parameters. Parameters passed via ``Specification`` field 
    do not count. 
  * ``#PV(field)`` - the value of the specified field. Expands to 
    an empty string if the field is not specified. A field set to ``true`` 
    is treated as a boolean parameter and only the field name is dumped. 
    If it is set to ``false`` it won't appear in the netlist. 
  * ``#PNV(field)`` - same as ``#PV``, except that the field is 
    formated as ``<field name>=<field value>``. Expands to an 
    empty string if the field is not specified. A field set to ``true`` 
    is treated as a boolean parameter and only the field name is dumped. 
    If it is set to ``false`` it won't appear in the netlist. 
  * ``#PNV()`` - equivalent to ``#PNV(f1) #PNV(f2) ...`` where fields
    ``f1``, ``f2``, ... are specified by ``Parameters`` in the component's 
    ``Mapping`` entry. 

All the settings specified for a components mapping can be overridden by 
component's fields with corresponding names. The ``Parameters`` field must 
be given as a space-separated list of parameter names. The ``PinMap`` field 
must be given as a space-separated list of pin numbers. 

The default for ``NamePrefix`` is ``None`` (i.e. all device names are OK). 

The default for ``ValueField`` is ``None``. 

If ``Parameters`` is not defined it is assumed to be an empty list. 

If ``PinMap`` is not defined the pins are dumped in the increasing pin 
number order. 

Not specifying an ``OutPattern`` (either in *config* or as a field) results 
in an error. 

Every element is netlisted in such manner that the value of the 
``Specification`` field is added at the end of the netlist line specifying 
the element. This makes it possible to quickly and easily add arbitrary 
parameters to the elements in the netlist. It is also used by the two 
independent sources for describing the type and the value of the source 
(i.e. AC, DC, PULSE, ...). 
"""

__all__ = [ "config" ]

config={
	'EnumerateNets': True, 
	'RenameNetPattern': r"^Net-\(", 
	'NetPrefix': "net", 
	'NetNumbers': 3, 
	'GroundNets': ["GND", "GNDA", "GNDD", "GNDPWR", "GNDREF"], 
	'SuppressEnd': False, 
	# Device mapping
	"Mapping": {
		(None, "RES"): {
			"NamePrefix": "R", 
			"SpiceDevice": "r", 
			"ValueField": None,
			"Parameters" : [ "r", "temp", "tc", "tc1", "tc2", "m" ],
			"PinMap": [ 1, 2 ],
			"OutPattern": "#REF() (#PINS()) #PNV() #PV(Specification)"
		},
		(None, "RES_SEMI"): {
			"NamePrefix": "R", 
			"SpiceDevice": "r", 
			"ValueField": None,
			"Parameters" : [ "w", "l", "temp", "tc", "tc1", "tc2", "m" ],
			"PinMap": [ 1, 2 ],
			"OutPattern": "#REF() (#PINS()) #MODEL() #PNV() #PV(Specification)"
		},
		(None, "CAP"): {
			"NamePrefix": "C", 
			"SpiceDevice": "c", 
			"ValueField": None,
			"Parameters" : [ "c", "ic", "m" ],
			"PinMap": [ 1, 2 ],
			"OutPattern": "#REF() (#PINS()) #PNV() #PV(Specification)"
		},
		(None, "CAP_SEMI"): {
			"NamePrefix": "C", 
			"SpiceDevice": "c", 
			"ValueField": None,
			"Parameters" : [ "w", "l", "ic", "m" ],
			"PinMap": [ 1, 2 ],
			"OutPattern": "#REF() (#PINS()) #MODEL() #PNV() #PV(Specification)"
		},
		(None, "IND"): {
			"NamePrefix": "L", 
			"SpiceDevice": "l", 
			"ValueField": None,
			"Parameters" : [ "l", "ic", "m" ],
			"PinMap": [ 1, 2 ],
			"OutPattern": "#REF() (#PINS()) #PNV() #PV(Specification)"
		},
		(None, "IND_COUPLING"): {
			"NamePrefix": "K", 
			"SpiceDevice": "k", 
			"ValueField": None,
			"Parameters" : [ "k" ],
			"PinMap": [ 1, 2 ],
			"OutPattern": "#REF() (#PV(Ind1) #PV(Ind2)) #PNV() #PV(Specification)"
		},
		(None, "DIO"): {
			"NamePrefix": "D", 
			"SpiceDevice": "d", 
			"ValueField": None,
			"Parameters" : [ "area", "pj", "m", "off", "ic", "temp" ],
			"PinMap": [ 1, 2 ],
			"OutPattern": "#REF() (#PINS()) #MODEL() #PNV() #PV(Specification)"
		},
		(None, "NPN"): {
			"NamePrefix": "Q", 
			"SpiceDevice": "npn", 
			"ValueField": None,
			"Parameters" : [ "area", "m", "off", "ic", "icvbe", "icvce", "temp" ],
			"PinMap": [ 1, 2, 3 ],
			"OutPattern": "#REF() (#PINS()) #MODEL() #PNV() #PV(Specification)"
		},
		(None, "PNP"): {
			"NamePrefix": "Q", 
			"SpiceDevice": "pnp",
			"ValueField": None,
			"Parameters" : [ "area", "m", "off", "ic", "icvbe", "icvce", "temp" ],
			"PinMap": [ 1, 2, 3 ], 
			"OutPattern": "#REF() (#PINS()) #MODEL() #PNV() #PV(Specification)"
		}, 
		# TODO: 4-pin BJT
		(None, "NMOS"): {
			"NamePrefix": "M", 
			"SpiceDevice": "nmos", 
			"ValueField": None,
			"Parameters" : [
				"w", "l", "ad", "as", "pd", "ps", "nrd", "nrs", "m", 
				"off", "nqsmod", "ic", "icvds", "icvgs", "icvbs", 
				"vth0_absdelta", "u0_reldelta", "check", "geo", "temp"
			],
			"PinMap": [ 1, 2, 3, 4 ],
			"OutPattern": "#REF() (#PINS()) #MODEL() #PNV() #PV(Specification)"
		},
		(None, "PMOS"): {
			"NamePrefix": "M", 
			"SpiceDevice": "pnp",
			"ValueField": None,
			"Parameters" : [
				"w", "l", "ad", "as", "pd", "ps", "nrd", "nrs", "m", 
				"off", "nqsmod", "ic", "icvds", "icvgs", "icvbs", 
				"vth0_absdelta", "u0_reldelta", "check", "geo", "temp"
			],
			"PinMap": [ 1, 2, 3, 4 ], 
			"OutPattern": "#REF() (#PINS()) #MODEL() #PNV() #PV(Specification)"
		}, 
		(None, "NJF"): {
			"NamePrefix": "J", 
			"SpiceDevice": "njf", 
			"ValueField": None,
			"Parameters" : [ "area", "m", "off", "ic", "icvds", "icvgs", "temp" ],
			"PinMap": [ 1, 2, 3 ],
			"OutPattern": "#REF() (#PINS()) #MODEL() #PNV() #PV(Specification)"
		},
		(None, "PJF"): {
			"NamePrefix": "J", 
			"SpiceDevice": "pjf", 
			"ValueField": None,
			"Parameters" : [ "area", "m", "off", "ic", "icvds", "icvgs", "temp" ],
			"PinMap": [ 1, 2, 3 ],
			"OutPattern": "#REF() (#PINS()) #MODEL() #PNV() #PV(Specification)"
		},
		(None, "NMF"): {
			"NamePrefix": "Z", 
			"SpiceDevice": "nmf", 
			"ValueField": None,
			"Parameters" : [ "area", "m", "off", "ic", "icvds", "icvgs" ],
			"PinMap": [ 1, 2, 3 ],
			"OutPattern": "#REF() (#PINS()) #MODEL() #PNV() #PV(Specification)"
		},
		(None, "PMF"): {
			"NamePrefix": "Z", 
			"SpiceDevice": "pmf", 
			"ValueField": None,
			"Parameters" : ["area", "m", "off", "ic", "icvds", "icvgs"],
			"PinMap": [ 1, 2, 3 ],
			"OutPattern": "#REF() (#PINS()) #MODEL() #PNV() #PV(Specification)"
		},
		(None, "SW"): {
			"NamePrefix": "S", 
			"SpiceDevice": "sw", 
			"ValueField": None,
			"Parameters" : [ "on", "off", "m" ],
			"PinMap": [ 1, 2, 3, 4 ],
			"OutPattern": "#REF() (#PINS()) #MODEL() #PNV() #PV(Specification)"
		},
		(None, "CSW"): {
			"NamePrefix": "W", 
			"SpiceDevice": "csw", 
			"ValueField": None,
			"Parameters" : [ "on", "off", "m" ],
			"PinMap": [ 1, 2 ],
			"OutPattern": "#REF() (#PINS() #PV(Ctlvsrc)) #MODEL() #PNV() #PV(Specification)"
		},
		(None, "ISRC"): {
			"NamePrefix": "I", 
			"SpiceDevice": "isrc", 
			"ValueField": None,
			"Parameters" : [ "dc", "ac", "acmag", "acphase", "pulse", "sin", "exp", "pwl", "sffm", "m", "nolift" ],
			"PinMap": [ 1, 2 ],
			"OutPattern": "#REF() (#PINS()) #PNV() #PV(Specification)"
		},
		(None, "VSRC"): {
			"NamePrefix": "V", 
			"SpiceDevice": "vsrc", 
			"ValueField": None,
			"Parameters" : [ "dc", "ac", "acmag", "acphase", "pulse", "sin", "exp", "pwl", "sffm", "m", "nolift" ],
			"PinMap": [ 1, 2 ],
			"OutPattern": "#REF() (#PINS()) #PNV() #PV(Specification)"
		},
		(None, "VSRC_NONLIN"): {
			"NamePrefix": "B", 
			"SpiceDevice": "asrc", 
			"ValueField": None,
			"Parameters" : [ "v", "m" ], 
			"PinMap": [ 1, 2 ],
			"OutPattern": "#REF() (#PINS()) #PNV() #PV(Specification)"
		}, 
		(None, "ISRC_NONLIN"): {
			"NamePrefix": "B", 
			"SpiceDevice": "asrc", 
			"ValueField": None,
			"Parameters" : [ "i", "m" ], 
			"PinMap": [ 1, 2 ],
			"OutPattern": "#REF() (#PINS()) #PNV() #PV(Specification)"
		},
		(None, "VCVS"): {
			"NamePrefix": "E", 
			"SpiceDevice": "vcvs", 
			"ValueField": None,
			"Parameters" : [ "gain", "m" ],
			"PinMap": [ 1, 2, 3, 4 ],
			"OutPattern": "#REF() (#PINS()) #PNV() #PV(Specification)"
		}, 
		(None, "CCCS"): {
			"NamePrefix": "F", 
			"SpiceDevice": "cccs", 
			"ValueField": None,
			"Parameters" : [ "gain", "m" ],
			"PinMap": [ 1, 2 ],
			"OutPattern": "#REF() (#PINS() #PV(Ctlvsrc)) #PNV() #PV(Specification)"
		}, 
		(None, "VCCS"): {
			"NamePrefix": "G", 
			"SpiceDevice": "vccs", 
			"ValueField": None,
			"Parameters" : [ "gain", "m" ],
			"PinMap": [ 1, 2, 3, 4 ],
			"OutPattern": "#REF() (#PINS()) #PNV() #PV(Specification)"
		},
		(None, "CCVS"): {
			"NamePrefix": "H", 
			"SpiceDevice": "ccvs", 
			"ValueField": None,
			"Parameters" : [ "gain", "m" ],
			"PinMap": [ 1, 2 ],
			"OutPattern": "#REF() (#PINS() #PV(Ctlvsrc)) #PNV() #PV(Specification)"
		},
		(None, "LOSSLESS_LINE"): {
			"NamePrefix": "T", 
			"SpiceDevice": "tra", 
			"ValueField": None,
			"Parameters" : [ "z0", "td", "f", "nl", "ic", "v1", "v2", "i1", "i2", "rel", "abs", "m" ],
			"PinMap": [ 1, 2, 3, 4 ],
			"OutPattern": "#REF() (#PINS()) #PNV() #PV(Specification)"
		},
		(None, "LOSSY_LINE"): {
			"NamePrefix": "O", 
			"SpiceDevice": "tra", 
			"ValueField": None,
			"Parameters" : [ "ic", "v1", "v2", "i1", "i2", "m" ],
			"PinMap": [ 1, 2, 3, 4 ],
			"OutPattern": "#REF() (#PINS()) #MODEL() #PNV() #PV(Specification)"
		}, 
		(None, "URC_LINE"): {
			"NamePrefix": "U", 
			"SpiceDevice": "urc", 
			"ValueField": None,
			"Parameters" : [ "l", "n", "m" ],
			"PinMap": [ 1, 2, 3 ],
			"OutPattern": "#REF() (#PINS()) #MODEL() #PNV() #PV(Specification)"
		},
		
		# By default a device is treated as a subcircuit
		# Pins are ordered by their pinnum
		# Value is the subcircuit definition name
		# Valid parameters are specified by 'Specification' field of symbol
		# If Model field is specified it overrides Value and sets the model name
		(None, None): {
			"NamePrefix": "X",
			"SpiceDevice": "subcircuit",  
			"ValueField": "Model", 
			"Parameters": [], 
			"OutPattern": "#REF() (#PINS()) #MODEL() #PARAM() #PNV() #PV(Specification)"
		}
	}
}

