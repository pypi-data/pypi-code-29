
import numpy as np
import gtar

# foo = gtar.GTAR('test.zip', 'a')
# foo.writeBytes('test.arr', np.random.rand(10, 20).tostring(), gtar.CompressMode.NoCompress)

foo = gtar.GTAR('test.zip', 'r')
foo.readBytes('test.arr')
