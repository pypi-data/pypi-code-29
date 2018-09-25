def generate_random_rot():
    """ generate a random rotation wrt the Haar measure """
    from pyso3.quaternion import quat2rot
    import numpy as np
    q = np.random.randn(4)
    q = q / np.linalg.norm(q)
    return quat2rot(q)
