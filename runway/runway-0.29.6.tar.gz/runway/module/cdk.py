"""CDK module."""

import logging
import os
import subprocess
import sys

from . import (
    RunwayModule, run_module_command, use_npm_ci, warn_on_skipped_configs
)
from ..util import change_dir, which

LOGGER = logging.getLogger('runway')


class CloudDevelopmentKit(RunwayModule):
    """CDK Runway Module."""

    def run_cdk(self, command='deploy'):
        """Run CDK."""
        response = {'skipped_configs': False}
        cdk_opts = [command]

        if not which('npm'):
            LOGGER.error('"npm" not found in path or is not executable; '
                         'please ensure it is installed correctly.')
            sys.exit(1)

        if 'DEBUG' in self.context.env_vars:
            cdk_opts.append('-v')  # Increase logging if requested

        if which('npx'):
            # Use npx if available (npm v5.2+)
            LOGGER.debug('Using npx to invoke cdk.')
            # The nested cdk-through-npx-via-subprocess command invocation
            # requires this redundant quoting
            cdk_cmd = ['npx', '-c', "''sls %s''" % ' '.join(cdk_opts)]
        else:
            LOGGER.debug('npx not found; falling back invoking cdk shell '
                         'script directly.')
            cdk_cmd = [
                os.path.join(self.path,
                             'node_modules',
                             '.bin',
                             'cdk')
            ] + cdk_opts

        if self.options.get('environments', {}).get(self.context.env_name):
            if os.path.isfile(os.path.join(self.path, 'package.json')):
                with change_dir(self.path):
                    # Use npm ci if available (npm v5.7+)
                    if self.options.get('skip_npm_ci'):
                        LOGGER.info("Skipping npm ci or npm install on %s...",
                                    os.path.basename(self.path))
                    elif self.context.env_vars.get('CI') and use_npm_ci(self.path):  # noqa
                        LOGGER.info("Running npm ci on %s...",
                                    os.path.basename(self.path))
                        subprocess.check_call(['npm', 'ci'])
                    else:
                        LOGGER.info("Running npm install on %s...",
                                    os.path.basename(self.path))
                        subprocess.check_call(['npm', 'install'])
                    LOGGER.info("Running sls %s on %s (\"%s\")",
                                command,
                                os.path.basename(self.path),
                                # Strip out redundant npx quotes not needed
                                # when executing the command directly
                                " ".join(cdk_cmd).replace('\'\'', '\''))
                    run_module_command(cmd_list=cdk_cmd,
                                       env_vars=self.context.env_vars)
            else:
                LOGGER.info(
                    "Skipping cdk %s of %s; no \"package.json\" "
                    "file was found (need a package file specifying "
                    "aws-cdk in devDependencies)",
                    command,
                    os.path.basename(self.path))
        else:
            response['skipped_configs'] = True
            LOGGER.info(
                "Skipping cdk %s of %s; no config file for "
                "this stage/region found (looking for one of \"%s\")",
                command,
                os.path.basename(self.path),
                ', '.join(gen_sls_config_files(self.context.env_name,
                                               self.context.env_region)))
        return response

    def plan(self):
        """Run cdk diff."""
        result = self.run_cdk(command='diff')
        warn_on_skipped_configs(result, self.context.env_name,
                                self.context.env_vars)

    def deploy(self):
        """Run cdk deploy."""
        result = self.run_cdk(command='deploy')
        warn_on_skipped_configs(result, self.context.env_name,
                                self.context.env_vars)

    def destroy(self):
        """Run cdk destroy."""
        result = self.run_cdk(command='destroy')
        warn_on_skipped_configs(result, self.context.env_name,
                                self.context.env_vars)
