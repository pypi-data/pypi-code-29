from westpy import *
session = Session("marco.outatime@gmail.com")
token = session.getToken()
print(token)
status = session.status()
print(status)

geom = Geometry()
geom.setCell((25,0,0),(0,25,0),(0,0,25))

geom.addAtomsFromOnlineXYZ( "http://www.west-code.org/doc/training/methane/CH4.xyz" )

geom.addSpecies( "C", "http://www.quantum-simulation.org/potentials/sg15_oncv/upf/C_ONCV_PBE-1.0.upf")
geom.addSpecies( "H", "http://www.quantum-simulation.org/potentials/sg15_oncv/upf/H_ONCV_PBE-1.0.upf")

gs = GroundState(geom,xc="PBE",ecut=40.0)

gs.generateInputPW()

output = session.run("pw", "pw.in", "pw.out", ["http://www.quantum-simulation.org/potentials/sg15_oncv/upf/C_ONCV_PBE-1.0.upf", "http://www.quantum-simulation.org/potentials/sg15_oncv/upf/H_ONCV_PBE-1.0.upf"], 3 )

print(output)


