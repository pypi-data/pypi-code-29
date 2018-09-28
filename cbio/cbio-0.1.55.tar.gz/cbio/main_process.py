import os
import subprocess
import time
from .utils import utils


class BioTask:

    def __init__(self, config, tool_name, logger=None):
        """Creation of the class

        The basic configuration of the class must be set.
        """

        # Launch the methods that are going to build the entire class
        # configuration
        mode = os.environ['MODE']

        self.logger = logger
        self.config = config
        self.configure_tool(config)
        self.log.info(f"Created {type(self).__name__} class")
        self.tool_config = self.config['tools_conf'][tool_name]
        self.log.debug(f"{type(self).__name__} - {self.tool_config}")
        self.tool_name = tool_name
        self.make_tests()
        self.sampleID = self.set_sample_id()

        self.software = self.set_software()
        self.tool_software = self.assign_softwares()

        if mode != 'TEST':
            self.loggerApi = logger
        else:
            self.logger = None

        self.threads = self.set_threads()
        self.tmp_folder = self.set_tmp_folder()
        # self.software = self.tool_config['software']
        self.pid = 0
        self.cmd, self.rm_cmd = "", ""

    def assign_softwares(self):
        # using_softwares = self.config["using_software"]
        softwares = {}
        # for software in using_softwares.keys():
        #
        #     for subprogram in using_softwares[software]:
        #         softwares[subprogram['name']] = self.software[software][subprogram['version']][subprogram['name']]

        for software in self.tool_config['software']:
            for name in self.software[software['name']][software['version']].keys():
                softwares[name] = self.software[software['name']][software['version']][name]

        return softwares

    def set_sample_id(self):
        """Method to return the id of the analyzed case"""

        if "sampleID" in self.config['process_conf']['sample'].keys():
            sample_id = self.config['process_conf']['sample']['sampleID']
        else:
            sample_id = self.config['process_conf']['sample']['trioID']

        return sample_id

    def get_software(self, name, version):
        return self.software[name][version]

    def set_tmp_folder(self):
        """Method to set a temporal folder"""
        if 'tmp_folder' in self.config['process_conf']:
            tmp_folder = self.config['process_conf']['tmp_folder']
        else:
            tmp_folder = "/tmp/"

        return tmp_folder

    def set_threads(self):
        """Method to set the threads used by the tool. Number of threads should be"""
        if 'threads' in self.tool_config['tool_conf']:
            threads = self.tool_config['tool_conf']['threads']
        elif 'threads' in self.config['process_conf']:
            threads = self.config['process_conf']['threads']
        else:
            threads = "1"

        try:
            int(threads)
        except ValueError:
            raise Exception("Number of threads could not be converted to integer")

        try:
            assert(int(threads) <=0)
        except AssertionError as ass_err:
            print(ass_err)
        else:
            pass
        finally:
            pass

        return threads

    def set_pid(self, pid):
        self.pid = pid

    def set_software(self):
        software = {
            "bwa-mem": {
                "v0.7.15": {
                    "bwa-mem": self.config['softdata']['software']['paths']['BWAPATH']
                }
            },


            "samtools": {
                "v1.7": {
                    "samtools": self.config['softdata']['software']['paths']['SAMTOOLSPATH'],
                }
            },

            "htslib": {
                "v1.7": {
                    "bgzip": self.config['softdata']['software']['paths']['BGZIPPATH'],
                    "tabix": self.config['softdata']['software']['paths']['TABIXPATH'],
                }
            },

            "freebayes": {
                "v1.1.0": {
                    "freebayes": self.config['softdata']['software']['paths']['FREEBAYESPATH'],
                }
            },

            "annovar": {
                "v20160205": {
                    "ANNOVAR": self.config['softdata']['software']['paths']['ANNOVARPATH'],
                }
            },

            "bedtools": {
                "v2.26.0": {
                    "bedtools": self.config['softdata']['software']['paths']['BEDTOOLSPATH'],
                }
            },
            "picard": {
                "v2.9.0": {
                    "picard": self.config['softdata']['software']['paths']['PICARDPATH']
                }
            },
            "snpsift": {
                "v4.3k": {
                    "snpsift": self.config['softdata']['software']['paths']['SNPSIFTPATH'],
                    "snpeff": self.config['softdata']['software']['paths']['SNPEFFPATH'],
                }
            },

            "fastQC": {
                "v0.11.5": {
                    "fastQC": self.config['softdata']['software']['paths']['FASTQCPATH'],
                }
            },

            "bbduk": {
                "v37.56": {
                    "bbduk": self.config['softdata']['software']['paths']['BBDUKPATH'],
                }
            },

            "RTG": {
                "v3.8.4": {
                    "RTG": self.config['softdata']['software']['paths']['RTGPATH']
                }
            },

            "vcfallelicprim": {
                "v0.0": {
                    "vcfallelicprim": self.config['softdata']['software']['paths']['VCFALLELICPRIM'],
                }
            },

            "vt": {
                "v0.1": {
                    "VT": self.config['softdata']['software']['paths']['VT'],
                }
            },
            "sort_bed": {
                "v0.1": {
                    "sort_bed": self.config['softdata']['software']['paths']['SORTBED'],
                }
            },

            "gemini": {
                "v0.20.1": {
                    "gemini": self.config['softdata']['software']['paths']['GEMINIPATH'],
                }
            },

            "vep": {
                "v92.1": {
                    "vep": self.config['softdata']['software']['paths']['VEPPATH'],
                }
            },

            "vardict": {
                "v1.5.1": {
                    "vardict": self.config['softdata']['software']['paths']['VARDICT1_5_1']
                },
                "v1.5.2": {
                    "vardict": self.config['softdata']['software']['paths']['VARDICT1_5_2']
                },
                "v1.5.3": {
                    "vardict": self.config['softdata']['software']['paths']['VARDICT1_5_3']
                },
            },
            "vardict-script": {
                "v1.5.1": {
                    "vardictsomatic": self.config['softdata']['software']['paths']['VARDICTSOMATIC'],
                    "vardictpaired": self.config['softdata']['software']['paths']['VARDICTPAIRED'],
                    "vardictsb": self.config['softdata']['software']['paths']['VARDICTRSB'],
                    "vardictvar2vcf": self.config['softdata']['software']['paths']['VARDICTVAR2VCF'],
                }
            },

            "igvtools": {
                "v2.3.98": {
                    "igvtools": self.config['softdata']['software']['paths']['IGVTOOLS'],
                }
            },

            "bamclipper": {
                "v1.0.0": {
                    "bamclipper": self.config['softdata']['software']['paths']['BAMCLIPPER'],
                }
            },

            "cutprimers": {
                "v1.2": {
                    "cutprimers": self.config['softdata']['software']['paths']['CUTPRIMERSPATH'],
                }
            },
            "bcl2fastq": {
                "v0.0.0": {
                    "bcl2fastq": self.config['softdata']['software']['paths']['BCL2FASTQPATH'],
                }
            },

            "agent": {
                "v4.0.1": {
                    "agent": self.config['softdata']['software']['paths']['AGENTPATH'],
                }
            },
            "lumpy": {
                "v0.2.12": {
                    "LUMPYPATH": self.config['softdata']['software']['paths']['LUMPYPATH'],
                    "LUMPYPATH_PAIRED": self.config['softdata']['software']['paths']['LUMPYPATH_PAIRED'],
                    "LUMPYPATH_SPLITREADS": self.config['softdata']['software']['paths']['LUMPYPATH_SPLITREADS'],
                },
            },
            "samblaster": {
                "v0.1.24": {
                    "samblaster": self.config['softdata']['software']['paths']['SAMBLASTERPATH'],
                }
            },
            "IMEGEN": {
                "v0.0": {
                    "IMEGEN": ""
                }
            },
            "qualimap": {
                "v0.0": {
                    "qualimap": ""
                }
            },

            # Other
            "REFERENCE_GENOME": self.config['softdata']['ref'][self.build],
            "HUMANDB": self.config['softdata']['dbs']['ANNOVARINFO'],
            "NEXTERAPE": os.path.join("/DATA/biodata/NexteraPE-PE.fa"),
            "VEPCACHE": self.config['softdata']['software']['paths']['VEPCACHE'],
            "VEPDB": self.config['softdata']['dbs']['VEPDB'],
        }

        return software

    def build_global_params(self):
        # Options
        if 'sampleID' in self.config:
            self.sampleID = self.config['sampleID']
        elif 'assay' in self.config:
            self.assay = self.config['assay']
        else:
            raise Exception('There must be a sample or an assay')

        self.build = self.config['process_conf']['build']

        # Other
        self.REFERENCE_GENOME = self.config['softdata']['ref'][self.build]
        self.HUMANDB = self.config['softdata']['dbs']['ANNOVARINFO']
        self.NEXTERAPE = os.path.join("/DATA/biodata/NexteraPE-PE.fa")
        self.VEPCACHE = self.config['softdata']['software']['paths']['VEPCACHE']
        self.VEPDB = self.config['softdata']['dbs']['VEPDB']

    def configure_tool(self, config):
        self.config = config
        self.log = utils.set_log(__name__, config['log_files'])

        self.build_global_params()

    def make_tests(self):
        self.check_reference_genome()

    def run(self):
        import time
        start = time.time()

        if self.config['process_conf']['sample']['modality'] == 'Trios':
            if 'sample' in self.tool_config['tool_conf'].keys():
                name = type(self).__name__ + ' - ' + self.tool_config['tool_conf']['sample']
            else:
                name = type(self).__name__
        else:
            name = type(self).__name__

        # Only talk to the API when a logger exists
        if self.logger:
            self.loggerApi.iniciar_paso(name, self.config['process_conf']['sample']['modality'], self.log)

        # Execute the tool
        self.run_process()

        # Finalyze process and calculate time
        end = time.time()
        execution_time = str(round(end - start, 2))
        self.log.debug(f'__time__ - {name} - {execution_time} s')

        # Only talk to the API when a logger exists
        if self.logger:
            self.loggerApi.finalizar_paso(name, self.config['process_conf']['sample']['modality'], self.log)
            self.loggerApi.informar(f"{name} result")

    def check_reference_genome(self):
        """
        Function that checks the reference genome used by the user. By the time,
        just a list of reference genomes could be used to do the mapping of
        sequences.

        Parameters
        ----------
        user_ref : str
            String with the reference genome that is going to be used

        Returns
        -------
        user_ref : str
            Same string validated
        """
        if self.build in ['GRCh37', "GRCh38", "hg19", "hg38", "hs37d5"]:
            return self.build
        else:
            raise Exception("Version \"" + self.build + "\" still not available")

    def build_rm_cmd(self):
        return ''

    def build_cmd(self):
        raise Exception("Method 'build_cmd' is  not set.")

    def cmd_run(self, mode=3):

        cmd = self.build_cmd()
        rm_cmd = self.build_rm_cmd()

        # If dry_run, don't run the process, just print it
        if self.config['DRY_RUN'] is True:
            self.log.info('Generating CLI command...')
            self.log.info(cmd)

        else:
            if mode == 1:
                self.log.info('Running command...')
                process = subprocess.Popen(cmd, shell=True, executable='/bin/bash',
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.log.info(f"Initializing process {type(self).__name__} - PID: {process.pid}")
                self.set_pid(process.pid)

                out = None
                err = None
                lines = []

                self.log.debug("Printing software log:")
                while out != "" or err != "":
                    out = process.stdout.readline()
                    err = process.stderr.readline()
                    out = out.decode("utf-8").strip('\n')
                    err = err.decode("utf-8").strip('\n')
                    self.log.debug(err)
                    lines.append(out)

                return lines

            elif mode == 2:
                os.system(cmd)

            elif mode == 3:
                f_stdout = open("/tmp/full.stdout.log", "w+")
                f_stderr = open("/tmp/full.stderr.log", "w+")
                # Using pipe in command could block the stdout, see this post:
                # https://thraxil.org/users/anders/posts/2008/03/13/Subprocess-Hanging-PIPE-is-your-enemy/
                # https://www.reddit.com/r/Python/comments/1vbie0/subprocesspipe_will_hang_indefinitely_if_stdout/
                self.log.info('Running command...')
                process = subprocess.Popen(cmd, shell=True, executable='/bin/bash',
                                           stdout=f_stdout, stderr=f_stderr)
                self.log.info(f"Initializing process {type(self).__name__} - PID: {process.pid}")
                self.set_pid(process.pid)

                while process.poll() is None:
                    time.sleep(5)

                f_stdout.close()
                f_stderr.close()

                if process.returncode != 0:

                    # If a temporal folder has been used, try to retrieve a removing command
                    if rm_cmd != '':
                        self.log.debug(f"Process {type(self).__name__} failed. Command failed running")
                        self.log.debug(f"Activation of removal of temporal files...")
                        f_stdout = open("/tmp/full.stdout.log", "w+")
                        f_stderr = open("/tmp/full.stderr.log", "w+")
                        p = subprocess.Popen(rm_cmd, shell=True, executable='/bin/bash', stdout=f_stdout,
                                             stderr=f_stderr)
                        while process.poll() is None:
                            time.sleep(5)

                        f_stdout.close()
                        f_stderr.close()

                    raise Exception(f"Process {type(self).__name__} failed. Command failed running")

        self.log.info(f"Finished process {type(self).__name__} with exit status 0")

    def run_cmd_get_output(self, cmd):
        process = subprocess.Popen(cmd, shell=True, executable='/bin/bash',
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        out = None
        err = None
        lines = []

        while out != "" or err != "":
            out = process.stdout.readline()
            err = process.stderr.readline()
            out = out.decode("utf-8").strip('\n')
            err = err.decode("utf-8").strip('\n')
            lines.append(out)

        return lines

    def get_task_options(self):
        return self.tool_config