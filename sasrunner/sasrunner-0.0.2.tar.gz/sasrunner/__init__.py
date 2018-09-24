import subprocess
import pipes

class SAS(object):
    """
    Scaffolding to accept arbitrary SAS commandline options.

    All options defined here for 9.3: 
        https://support.sas.com/documentation/cdl/en/hostunx/63053/HTML/default/viewer.htm#n0nnsvhnt2jwevn1fha4dz2n4g0y.htm

    Example:
    =======

    # You'd like to call SAS with -nolog and -sysin
    sas = SAS('nolog', sysin='/wrds/some/sas/path.sas')

    All flag options (-nolog, -nodms, etc.) must be passed in
    before keyword args are provided.
    """
    def __init__(self, *flags, **options):
        flag_options = []
        for flag in flags:
            if flag.startswith('-'):
                flag_options.append(flag)
            else:
                flag_options.append('-{}'.format(flag))

        options_with_args = []
        for key, value in options.iteritems():
            options_with_args.append('-{}'.format(key))
            options_with_args.append(pipes.quote(value))

        self.invocation = ['sas'] + flag_options + options_with_args

    def run(self):
        r = subprocess.Popen(self.invocation, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.stdout, self.stderr = r.communicate()
        self.returncode = r.returncode
    
    def __str__(self):
        return 'SAS call: {}'.format(' '.join(self.invocation))

