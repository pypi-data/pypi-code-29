from remote_sensors.models.request import METHODS


def is_registration(request) -> bool:
    """Evaluate if the message is a Registration request."""
    is_reg = request.method == METHODS['REGISTRATION']
    is_end = request.method == METHODS['END_REGISTRATION']
    return is_reg or is_end
