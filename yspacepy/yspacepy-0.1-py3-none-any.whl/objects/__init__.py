
from astropy import units as u

class Object:
    def __init__(self, props):
        self.name   = props['name']
        self.mass   = props['mass']
        self.radius = props['radius']
        self.dists  = props['dists']
    
    def dist(self, to):
        if to in self.dists:
            return self.dists[to]
        else:
            return 'n/a'

    def to_string(self):
        print("[{}] radius: {:.3e}, mass: {:.3e}".format(self.name, self.mass, self.radius))


sun = Object({
        'name': 'Sun',
        'mass': 1.989e30 * u.kg,
        'radius': 695508 * u.km,
        'dists': {'earth': 1.496e8 * u.km, 'jupiter': 778.5e6 * u.km, 'neptune': 4.495e9 * u.km} })

earth = Object({
          'name': 'Earth',
          'mass': 5.972e24 * u.kg,
          'radius': 6371 * u.km,
          'dists': {'sun': 1.496e8 * u.km, 'moon': 384400 * u.km} })
    
moon = Object({
         'name': 'Moon',
         'mass': 7.348e22 * u.kg,
         'radius': 1737 * u.km,
         'dists': {'earth': 384400 * u.km} })
    
jupiter = Object({
            'name': 'Jupiter',
            'mass': 1.898e27 * u.kg,
            'radius': 69911 * u.km,
            'dists': {'sun': 778.5e6 * u.km} })

neptune = Object({
            'name': 'Neptune',
            'mass': 1.024e26 * u.kg,
            'radius': 24622 * u.km,
            'dists': {'sun': 4.495e9 * u.km} })
