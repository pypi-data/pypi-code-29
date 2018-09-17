# -*- coding: utf-8 -*- äöü
from inspect import getargspec
"""
Exception-Klassen für Unitracc, mit Unterstützung von Systemnachrichten

Eigenschaften der von UnitraccBaseException abgeleiteten Klassen:

- Der Docstring wird für die Stringdarstellung verwendet und soll
  %(...)s-Platzhalter für die unterstützten Argumente enthalten
- Für Systemnachrichten wird das Attribut mask_format verwendet,
  das mit Hilfe der .format-Methode verarbeitet wird

Verwendung zum Erzeugen von Systemnachrichten:

try:
    ...
except UnitraccBaseException as e:
    context.getAdapter('message')(**e.message_kwargs())

Der message-Aapter sorgt für die Lokalisierung und erzeugt qua Vorgabe
eine Fehlernachricht;
um dies zu übersteuern, kann ein benanntes Argument messageType übergeben werden.
"""

__all__ = [# UnitraccBaseException und abgeleitet:
           'UnitraccBaseException',
           'UidNotfoundException',
           # (noch) nicht von UnitraccBaseException abgeleitet;
           ## aus Products.unitracc@@password:
           'InvalidPassword',
           'EmptyPassword',
           'PasswordTooShort',
           ]


class UnitraccBaseException(Exception):  # ------------- [ U.B.E. .. [
    """
    Basis-Exception-Klasse, die Ausgabe einer schönen Fehlernachricht
    (message-Adapter) unterstützt
    """
    arg_names = []

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self._save_args(*args, **kwargs)

    def _save_args(self, *args, **kwargs):
        """
        Speichere die Aufrufargumente und stelle sie zur Verfügung:

        - als Attribut _flat_mapping (ein flaches Dict incl. der **kwargs,
          z. B. zum Erzeugen einer Message mit dem message-Adapter
        - als Attribut _raw_mapping, das die Argumente gemäß der
          Klassendefinition organisiert
        """
        self._argspec = argspec = getargspec(type(self).__init__)
        # flaches Dict, incl. "Auflösung" der **kwargs:
        self._flat_mapping = mapping = dict(kwargs)
        done = set(kwargs)
        arglist = list(args)
        for aname in argspec.args[1:]:
            if aname in done:
                continue
            mapping[aname] = arglist.pop(0)
        if argspec.varargs is not None:
            mapping[argspec.varargs] = tuple(arglist)
        else:
            assert not arglist
        # Argumente wie bei Definition angegeben
        # (könnte teilweise auch in einer Klassenmethode gemacht werden):
        remaining_mapping = dict(mapping)
        self._raw_mapping = raw_mapping = {}
        self._raw_mask = raw_mask = []
        for aname in argspec.args[1:]:
            raw_mapping[aname] = remaining_mapping.pop(aname)
            raw_mask.append('%(aname)s=%%(%(aname)s)r' % locals())
        aname = argspec.varargs
        if aname is not None:
            raw_mapping[aname] = tuple(arglist)
            raw_mask.append('*%(aname)s')

        aname = argspec.keywords
        if aname is not None:
            raw_mapping[aname] = tuple(arglist)
            raw_mask.append('**%(aname)s' % locals())
        if raw_mask:
            raw_mask = ', '.join(raw_mask)
            self._raw_mask = '<%s(%s)>' % (self.__class__.__name__, raw_mask)
        else:
            self._raw_mask = '<%s>' % (self.__class__.__name__,)

    def __str__(self):
        """
        String-Darstellung der Exception
        """
        return self.__doc__ % self._raw_mapping

    def __repr__(self):
        return self._raw_mask % self._raw_mapping

    def message_kwargs(self,
                       message=None,
                       messageType='error'):
        """
        Argument-Dict zum Aufruf des message-Adapters,
        der die PloneMessageFactory aufruft -- Schlüssel 'message' und
        'mapping' -- und das Ergebnis direkt an addPortalMessage übergibt
        (verbleibender Schlüssel 'messageType')
        """
        if message is None:
            message = self.mask_format
        return {'message': message,
                'messageType': messageType,
                'mapping': self._flat_mapping,
                }

    def get_mapping(self, flat=False):
        """
        flat -- wenn True, werden etwaige **kwargs-Argumente einsortiert
                           (z. B. für message_kwargs());
                wenn False (Vorgabe), bleiben ihre speziellen Namen aus der
                           Klassendefinition erhalten (z. B. für repr)
        """
        if flat:
            return dict(self._flat_mapping)
        else:
            return dict(self._raw_mapping)
    # ---------------------------------- ] ... UnitraccBaseException ]


class UidNotfoundException(UnitraccBaseException):
    "Object %(uid)r not found"

    mask_format = 'Object ${uid} not found!'
    def __init__(self, uid):
        UnitraccBaseException.__init__(self, uid)

# ---------------------------- [ aus Products.unitracc@@password ... [
class InvalidPassword(ValueError):
    def mkmsg(self, translate, **kwargs):
        self.msg = translate(self.msgmask) % kwargs

    def __str__(self):
        return self.msg

    def __init__(self, translate):
        self.mkmsg(translate)


class EmptyPassword(InvalidPassword):
    msgmask = 'Empty password is not allowed.'


class PasswordTooShort(InvalidPassword):
    msgmask = 'Password is too short; at least %(minlength)r characters required.'

    def __init__(self, translate, minlength):
        self.minlength = minlength
        self.mkmsg(translate, minlength=minlength)
# ---------------------------- ] ... aus Products.unitracc@@password ]


if __name__ == '__main__':
    try:
        raise UidNotfoundException('abc123')
    except UnitraccBaseException as e:
        print str(e)
        print repr(e)
        print e._raw_mask
        print e.get_mapping(0)
        print e.get_mapping(1)
        print e.message_kwargs()
