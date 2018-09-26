import blinkistconfig.adapters
from blinkistconfig import errors

class Factory:
    @staticmethod
    def by(type):
        adapter = f"{type}Adapter"
        try:
            return getattr(blinkistconfig.adapters, f"{type}Adapter")()
        except AttributeError:
            raise errors.AdapterNotFoundError(f"Adapter {adapter} not found") from None
