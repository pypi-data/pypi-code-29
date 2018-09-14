import dpaypy as pstn

_shared_dpay_instance = None


def shared_dpay_instance():
    """ This method will initialize _shared_dpay_instance and return it.
    The purpose of this method is to have offer single default dPay instance that can be reused by multiple classes.
    """
    global _shared_dpay_instance
    if not _shared_dpay_instance:
        _shared_dpay_instance = pstn.DPay()  # todo: add dpaypy config
    return _shared_dpay_instance


def set_shared_dpay_instance(dpay_instance):
    """ This method allows us to override default dPay instance for all users of
    _shared_dpay_instance.
    """
    global _shared_dpay_instance
    _shared_dpay_instance = dpay_instance
