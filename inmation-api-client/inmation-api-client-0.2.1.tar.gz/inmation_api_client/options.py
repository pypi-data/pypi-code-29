class Options(dict):
    """ Options """
    def __init__(self, usr=None, pwd=None):
        super().__init__()
        self['usr'] = usr
        self['pwd'] = pwd

    @property
    def usr(self):
        """ get usr property """
        return self['usr']

    @usr.setter
    def usr(self, usr):
        self['usr'] = usr

    @property
    def pwd(self):
        """ get pwd property """
        return self['pwd']

    @pwd.setter
    def pwd(self, pwd):
        self['pwd'] = pwd

    @property
    def tim(self):
        """ get tim (handshakeTimeout in seconds) property """
        if 'tim' in self:
            return self['tim']

    @tim.setter
    def tim(self, tim):
        self['tim'] = tim

    @property
    def ign(self):
        """ get ign (ignore response) property """
        return self['ign']

    @ign.setter
    def ign(self, ign):
        self['ign'] = ign

    @property
    def roe(self):
        """ get roe (return only error) property """
        return self['roe']

    @roe.setter
    def roe(self, roe):
        self['roe'] = roe

    @property
    def fetch(self):
        """ get fetch (write_fetch) property """
        return self['fetch']

    @fetch.setter
    def fetch(self, fetch):
        self['fetch'] = fetch

    @property
    def delay(self):
        """ get delay ((write_delay) AKA pack delay) property """
        return self['delay']

    @delay.setter
    def delay(self, delay):
        self['delay'] = delay

    @property
    def audit(self):
        """ get audit ((write_audit) SuppressAuditWrite property """
        return self['audit']

    @audit.setter
    def audit(self, audit):
        self['audit'] = audit

    @property
    def group(self):
        """ get group (write_group) property """
        return self['group']

    @group.setter
    def group(self, group):
        self['group'] = group

    @property
    def timeo(self):
        """ get timeo (write_timeo) property """
        return self['timeo']

    @timeo.setter
    def timeo(self, timeo):
        self['timeo'] = timeo

    @property
    def percentage_good(self):
        """ get percentage_good property """
        return self['percentage_good']

    @percentage_good.setter
    def percentage_good(self, percentage_good):
        self['percentage_good'] = percentage_good

    @property
    def percentage_bad(self):
        """ get percentage_bad property """
        return self['percentage_bad']

    @percentage_bad.setter
    def percentage_bad(self, percentage_bad):
        self['percentage_bad'] = percentage_bad

    @property
    def treat_uncertain_as_bad(self):
        """ get treat_uncertain_as_bad property """
        return self['treat_uncertain_as_bad']

    @treat_uncertain_as_bad.setter
    def treat_uncertain_as_bad(self, tuab):
        self['treat_uncertain_as_bad'] = tuab

    @property
    def slopped_extrapolation(self):
        """ get slopped_extrapolation property """
        return self['slopped_extrapolation']

    @slopped_extrapolation.setter
    def slopped_extrapolation(self, slopped_ext):
        self['slopped_extrapolation'] = slopped_ext

    @property
    def partial_interval_treatment(self):
        """ get partial_interval_treatment property """
        return self['partial_interval_treatment']

    @partial_interval_treatment.setter
    def partial_interval_treatment(self, pit):
        self['partial_interval_treatment'] = pit
