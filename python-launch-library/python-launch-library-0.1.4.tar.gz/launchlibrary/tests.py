import launchlibrary as ll

# A simple test file.

a = ll.Api()
#agencies = ll.Agency.fetch(a, name="SpaceX")
#print(agencies[0])
#print(agencies[0].get_type())

launches = ll.Launch.fetch(a, next=5)
#print(launches[0])
#print(launches[0].get_agency())

pad = ll.Pad.fetch(a, id=1)
print(pad)
print("hi")