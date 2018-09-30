from systemdspawner import SystemdSpawner

class H2OSpawner(SystemdSpawner):
    def get_args(self):
        """Return the arguments to be passed after self.cmd

        Doesn't expect shell expansion to happen.
        """
        args = []

        # add for h2o
        args.append('--context_path=/user/%s' % self.user.name)

        # --port=54321 --[self.args]
        _args = super(SystemdSpawner, self).get_args()

        # --context_path=/user/%s [ --port=54321 --[self.args] ]
        args.extend(_args)
        return args
