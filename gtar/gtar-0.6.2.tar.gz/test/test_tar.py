
import gtar

with gtar.GTAR('dump.tar', 'a') as arch:
    arch.writeStr('test.txt', open('test.txt', 'r').read())
    arch.writeStr('frames/123/foo.txt', 'another test string!\n')

with gtar.GTAR('dump.tar', 'r') as arch:
    for rec in arch.getRecordTypes():
        f = arch.queryFrames(rec)
        print(rec.getPath(), f, [arch.getRecord(rec, frame) for frame in f])
