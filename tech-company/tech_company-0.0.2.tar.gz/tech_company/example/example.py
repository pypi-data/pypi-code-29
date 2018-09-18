from tech_company import cloud

if cloud.Cloud.is_working():
    print "Phew. The cloud's working today"
else:
    print "Bad luck. Try your app again later."

if cloud.Cloud.is_working(force=True):
    print "It works fine for me dude"
