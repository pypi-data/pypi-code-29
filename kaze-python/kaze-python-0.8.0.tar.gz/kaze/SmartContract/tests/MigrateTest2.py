from boa.interop.kaze.Storage import GetContext, Get
from boa.interop.kaze.Runtime import Notify
ctx = GetContext()


def Main(key):

    print("hello")

    Notify(key)

    val = Get(ctx, key)

    return val
