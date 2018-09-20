from . import units

earth_g = 9.81 * units.m/(units.s*units.s)
earth_radius = 6370.949*units.km
radiation_length = 37 * units.g/units.cm2

avogadro = 6.022e23 / units.mole

speed_of_light_SI = 299792458
speed_of_light = speed_of_light_SI * units.m/units.s
speed_of_light2 = speed_of_light * speed_of_light
planck_SI = 6.62606876e-34
planck_reduced_SI = planck_SI / (2*units.kPi)
planck = planck_SI * units.joule*units.s
planck_reduced = planck_reduced_SI * units.joule*units.s
mu_zero_SI = 4*units.kPi * 1e-7
mu_zero = mu_zero_SI*units.newton/(units.ampere*units.ampere) 

molarGasConstant =  8.3145 * units.joule/(units.mole*units.kelvin) # R: NIST
boltzmann = molarGasConstant / avogadro        # kB = R/Na

dryAirMolar_mass = 28.97 * units.gram/units.mole  # M. Note: R_spec = R/M
N2Molar_mass = 28.0134 * units.gram/units.mole
O2Molar_mass = 31.9989 * units.gram/units.mole
ArMolar_mass = 39.9481 * units.gram/units.mole
CO2Molar_mass = 44.0096 * units.gram/units.mole
H2OMolar_mass = 18.0153 * units.gram/units.mole

N2AirFraction = 780840 * units.perMillion  # Dry air vol. fractions
O2AirFraction = 209460 * units.perMillion  # NASA Earth Fact Sheet.
ArAirFraction =   9340 * units.perMillion  # H2O vapor @ surface is
CO2AirFraction =   380 * units.perMillion  # ~10 000 ppm.

H2OFreezingPoint = 273.15 * units.kelvin

electron_mass = 0.510998902 * units.MeV
mass_conversion_SI = units.eSI / (speed_of_light_SI*speed_of_light_SI);
electron_mass_SI = electron_mass * mass_conversion_SI;

epsilon_zero_SI = 1 / (mu_zero_SI * speed_of_light_SI*speed_of_light_SI)
alpha = (units.eSI*units.eSI) / (4*units.kPi * epsilon_zero_SI * planck_reduced_SI * speed_of_light_SI)
electron_radius_SI = (units.eSI*units.eSI) / (4*units.kPi * epsilon_zero_SI * electron_mass_SI * speed_of_light_SI * speed_of_light_SI)
thomsonCrossSection_SI = 8*units.kPi * electron_radius_SI * electron_radius_SI / 3

proton_mass = 938.272046*units.MeV
neutron_mass = 939.5654133*units.MeV
