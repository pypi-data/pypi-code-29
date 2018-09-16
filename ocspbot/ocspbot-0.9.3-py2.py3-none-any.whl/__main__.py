#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright © 2017 Felix Fontein.
#
# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""The main CLI interface of OCSP Bot."""

import datetime
import os
import re
import subprocess
import shutil
import sys
import yaml
try:
    from urllib.parse import urlparse
except ImportError:  # Python 2
    from urlparse import urlparse

try:
    FileNotFoundError
except NameError:
    # pylint: disable=redefined-builtin
    FileNotFoundError = IOError

VERSION = "0.9.3"

_DEFAULT_OPENSSL_EXECUTABLE_NAME = 'openssl'
_DEFAULT_OPENSSL_VERSION = (1, 0, 1, 'a')
_OPENSSL_VERSION_1_1_0 = (1, 1, 0, '')


def _run_openssl(args, executable=_DEFAULT_OPENSSL_EXECUTABLE_NAME, input_data=None, return_stderr_and_returncode=False):
    """Execute OpenSSL with the given arguments. Feeds input_data via stdin if given."""
    if input_data is None:
        proc = subprocess.Popen([executable] + list(args), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate()
    else:
        proc = subprocess.Popen([executable] + list(args), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = proc.communicate(input_data)
    if proc.returncode != 0 and not return_stderr_and_returncode:
        raise IOError("OpenSSL Error: {0}\n(args: {1})".format(err.decode('utf-8'), args))
    return (out, err.decode('utf-8'), proc.returncode) if return_stderr_and_returncode else out


def _get_openssl_version(executable=_DEFAULT_OPENSSL_EXECUTABLE_NAME):
    version_string = _run_openssl(['version'], executable=executable).decode('utf-8')
    m = re.match(r'^OpenSSL (\d+)\.(\d+)\.(\d+)([a-z]*)\s+', version_string)
    if not m:
        raise Exception("Cannot identify OpenSSL version from version string '{0}'!".format(version_string))
    return (int(m[1]), int(m[2]), int(m[3]), m[4])


def _get_ocsp_uri(cert, executable=_DEFAULT_OPENSSL_EXECUTABLE_NAME, openssl_version=_DEFAULT_OPENSSL_VERSION):
    """Retrieve the OCSP URL from a certificate. Must be given as path on disk."""
    _ = openssl_version
    cert_data = _run_openssl(['x509', '-in', cert, '-text'], executable=executable).decode('utf-8')
    m = re.search(r'^\s*OCSP - URI:(.*)$', cert_data, flags=re.MULTILINE)
    if m is None:
        raise Exception('Cannot find OCSP responder URI in certificate {cert}!'.format(cert=cert))
    return m.group(1).strip()


def _get_host_from_uri(uri):
    """Extract the hostname from an URI."""
    netloc = urlparse(uri).netloc
    i = netloc.find(':')
    return netloc[:i] if i >= 0 else netloc


def _get_ocsp_response(cert, chain, uri, output, executable=_DEFAULT_OPENSSL_EXECUTABLE_NAME, openssl_version=_DEFAULT_OPENSSL_VERSION):
    """Retrieve the OCSP response for a given certificate.

    ``cert`` and ``chain`` must point to files on disk which contain the certificate
    respectively the certificate chain.

    ``uri`` must be the URI for the OCSP server.

    The resulting OCSP response will be stored at ``output`` on disk.
    """
    if openssl_version < _OPENSSL_VERSION_1_1_0:
        host_header = ['Host', _get_host_from_uri(uri)]
    else:
        host_header = ['Host=' + _get_host_from_uri(uri)]
    _, err, returncode = _run_openssl(['ocsp', '-no_nonce', '-header'] + host_header + ['-issuer', chain, '-cert', cert, '-url', uri, '-noverify', '-respout', output], return_stderr_and_returncode=True, executable=executable)
    if returncode != 0:
        return False, err
    else:
        return True, None


def _verify_ocsp_response(cert, chain, rootchain, output, executable=_DEFAULT_OPENSSL_EXECUTABLE_NAME, openssl_version=_DEFAULT_OPENSSL_VERSION):
    """Verify the OCSP response ``output`` on disk.

    ``cert`` and ``chain`` must point to files on disk which contain the certificate
    respectively the certificate chain. ``rootchain`` must point to the root certificate's chain.
    """
    _ = openssl_version
    out, err, returncode = _run_openssl(['ocsp', '-no_nonce', '-respin', output, '-issuer', chain, '-CAfile', rootchain, '-VAfile', rootchain, '-cert', cert], return_stderr_and_returncode=True, executable=executable)
    if returncode != 0 or ' ERROR: ' in err:
        return False, err
    elif ' ERROR: ' in out.decode('utf-8'):
        return False, out
    else:
        return True, None


def _parse_openssl_text(text, data_type='Data', data_name='data'):
    """Parse OpenSSL text certificate entry."""
    m = re.search(r'^\s*{0}(.*)$'.format(re.escape(data_type)), text, flags=re.MULTILINE)
    if m is None:
        raise Exception('Cannot find "{data_type}" in {data_name}!'.format(data_name=data_name, data_type=data_type))
    return m.group(1).strip()


def _parse_openssl_text_timestamp(text, timestamp_type='timestamp', data_name='data'):
    """Parse OpenSSL text certificate timestamp."""
    timestamp = _parse_openssl_text(text, timestamp_type, data_name)
    date_format = '%b %d %H:%M:%S %Y %Z'
    try:
        return datetime.datetime.strptime(timestamp, date_format)
    except Exception as _:
        raise Exception('Cannot parse "{timestamp_type}" in {data_name}!'.format(data_name=data_name, timestamp_type=timestamp_type))


def _parse_ocsp_response(output, executable=_DEFAULT_OPENSSL_EXECUTABLE_NAME):
    """Parse OCSP response.

    Returns a tuple ``(good, this_update, next_update)`` indicating
    wether the OCSP response is good (``good``), the timestamp of the
    current OCSP response (``this_update``), and the timestamp of the
    next OCSP response (``next_update``).
    """
    ocsp_response = _run_openssl(['ocsp', '-respin', output, '-text', '-noverify'], executable=executable).decode('utf-8')
    data_name = 'OCSP response {output}'.format(output=output)
    cert_status = _parse_openssl_text(ocsp_response, data_type='Cert Status:', data_name=data_name)
    this_update = _parse_openssl_text_timestamp(ocsp_response, timestamp_type='This Update:', data_name=data_name)
    next_update = _parse_openssl_text_timestamp(ocsp_response, timestamp_type='Next Update:', data_name=data_name)
    return cert_status == 'good', this_update, next_update


def _parse_certificate(cert, executable=_DEFAULT_OPENSSL_EXECUTABLE_NAME):
    """Parse certificate for validity period.

    Returns tuple ``(not_before, not_after)`` indicating when the
    certificate is valid.
    """
    cert_data = _run_openssl(['x509', '-in', cert, '-text', '-noout'], executable=executable).decode('utf-8')
    data_name = 'certificate {cert}'.format(cert=cert)
    not_before = _parse_openssl_text_timestamp(cert_data, timestamp_type='Not Before:', data_name=data_name)
    not_after = _parse_openssl_text_timestamp(cert_data, timestamp_type='Not After :', data_name=data_name)
    return not_before, not_after


def _get_date_middle(date_a, date_b, position=0.5):
    """Linearly interpolates two given timestamps."""
    return date_a + (date_b - date_a) * position


def _read(filename):
    """Read content of file."""
    with open(filename, "rb") as f:
        return f.read()


def _default_output_message(msg):
    """Print output message."""
    print(msg)


def _default_warning_message(msg):
    """Print warning message."""
    sys.stderr.write('WARNING: {0}\n'.format(msg))


class CertInfo(object):
    """Store paths of relevant files and OCSP responder URI for a certificate."""

    _cert = None
    _chain = None
    _rootchain = None
    _ocsp_response = None
    _ocsp_responder_uri = None

    def __init__(self, cert, chain, rootchain, ocsp_response, ocsp_responder_uri=None):
        """Create ``CertInfo`` instance.

        Create ``CertInfo`` instance out of a certificate filename
        (``cert``), the certificate chain filename (``chain``),
        the certificate root chain filename (``rootchain``) and
        the OCSP response filename (``ocsp_response``).
        """
        self._cert = cert
        self._chain = chain
        self._rootchain = rootchain
        self._ocsp_response = ocsp_response
        self._ocsp_responder_uri = ocsp_responder_uri

    def cert(self):
        """Return certificate filename."""
        return self._cert

    def chain(self):
        """Return certificate chain filename."""
        return self._chain

    def rootchain(self):
        """Return certificate root chain filename."""
        return self._rootchain

    def ocsp_response(self):
        """Return OCSP response filename."""
        return self._ocsp_response

    def ocsp_responder_uri(self):
        """Return OCSP responser URI or None."""
        return self._ocsp_responder_uri


def conditional_get_ocsp_response_for_certificate(cert_info, min_validity=None, min_validity_pc=None, make_backups=False, output_message=_default_output_message, warning_message=_default_warning_message, executable=_DEFAULT_OPENSSL_EXECUTABLE_NAME, openssl_version=_DEFAULT_OPENSSL_VERSION):
    """Get a new OCSP response for a certificate, if necessary.

    Returns ``True`` in case the OCSP response was updated, ``False`` in case
    it was not, and raises an exception in case of errors.

    ``cert_info`` must be a ``CertInfo`` instance, specifying file names for
    the certificate, its chain, root chain, and OCSP response to be updated.

    If ``min_validity`` is given, it must be a time delta. If the OCSP response is
    valid less than this time delta, a new OCSP response will be retrieved.

    If ``min_validity_pc`` is given, it must be a number between 0 and 1 indicating
    from which point in the OCSP response's validity period a new response will be
    retrieved (0 = at beginning, 1 = at end of validity period).

    If ``make_backups`` is set to ``True``, backups of the OCSP response are made.

    ``output_message`` and ``warning_message`` must be callables with one argument.
    They are called when informational or warning messages need to be shown to the user.

    ``executable`` is the path to the OpenSSL executable.
    """
    # Check if everything's there
    if not os.path.isfile(cert_info.cert()):
        raise Exception('Cannot find certificate file "{cert}"!'.format(cert=cert_info.cert()))
    if not os.path.isfile(cert_info.chain()):
        raise Exception('Cannot find certificate chain file "{chain}"'.format(chain=cert_info.chain()))
    if not os.path.isfile(cert_info.rootchain()):
        raise Exception('Cannot find certificate root chain file "{rootchain}""!'.format(rootchain=cert_info.rootchain()))

    # Parse certificate
    cert_not_before, cert_not_after = _parse_certificate(cert_info.cert(), executable=executable)
    output_message('Certificate is valid from {valid_from} to {valid_to}.'.format(valid_from=cert_not_before, valid_to=cert_not_after))

    # Check whether we need new OCSP response
    need_new_ocsp = False
    has_valid_ocsp = False
    ocsp_next_update = None
    if not os.path.isfile(cert_info.ocsp_response()):
        # Old response doesn't exist
        output_message('OCSP stapling response not found on disk.')
        need_new_ocsp = True
    else:
        # Old response exists. Check it!
        ocsp_cert_good, ocsp_this_update, ocsp_next_update = _parse_ocsp_response(cert_info.ocsp_response(), executable=executable)
        if not ocsp_cert_good:
            # It's not good ==> get new one
            output_message('Current OSCP reponse is not good!')
            need_new_ocsp = True
        else:
            # It's good. Check validity.
            output_message('Current OSCP reponse is good from {valid_from} to {valid_to}.'.format(valid_from=ocsp_this_update, valid_to=ocsp_next_update))
            valid, errormessage = _verify_ocsp_response(cert_info.cert(), cert_info.chain(), cert_info.rootchain(), cert_info.ocsp_response(), executable=executable, openssl_version=openssl_version)
            if not valid:
                # It's not valid ==> get new one
                output_message('Current OCSP response is NOT valid: {reason}'.format(reason=errormessage))
                need_new_ocsp = True
            else:
                # It's valid. Check expiration.
                output_message('Current OCSP response is valid.')
                has_valid_ocsp = True
                middles = []

                # Find timestamps when to renew the OCSP response.
                if min_validity is not None:
                    middles.append(min(cert_not_after, ocsp_next_update) - min_validity)
                if min_validity_pc is not None:
                    middles.append(_get_date_middle(max(cert_not_before, ocsp_this_update), min(cert_not_after, ocsp_next_update), position=1.0 - min_validity_pc))

                # Check whether we are past one of the renewal timestamps
                if middles:
                    middle = min(middles)
                    now = datetime.datetime.now()
                    if now >= middle:
                        # Yes we are: renew!
                        need_new_ocsp = True

                    # Output resolution
                    if not need_new_ocsp:
                        state = 'in the future'
                        resolution = 'do not get new OCSP response.'
                    else:
                        state = 'in the past'
                        resolution = 'get new OCSP response!'
                    output_message('Middle timestamp {middle} lies {state} (now: {now}) ==> {resolution}'.format(state=state, middle=middle, now=now, resolution=resolution))
    # Do we need new OCSP response?
    if not need_new_ocsp:
        return False

    # Retrieve OCSP response
    output_temp = '{0}.new'.format(cert_info.ocsp_response())
    if cert_info.ocsp_responder_uri() is not None:
        uri = cert_info.ocsp_responder_uri()
    else:
        uri = _get_ocsp_uri(cert_info.cert(), executable=executable, openssl_version=openssl_version)
    output_message('Using OCSP responder {uri}.'.format(uri=uri))
    success, errormessage = _get_ocsp_response(cert_info.cert(), cert_info.chain(), uri, output_temp, executable=executable, openssl_version=openssl_version)
    if not success:
        raise Exception('Cannot get new OCSP response: {reason}'.format(reason=errormessage))
    # Check whether response is good
    ocsp_cert_good, new_ocsp_this_update, new_ocsp_next_update = _parse_ocsp_response(output_temp, executable=executable)
    output_message('New OSCP reponse is good from {valid_from} to {valid_to}.'.format(valid_from=new_ocsp_this_update, valid_to=new_ocsp_next_update))
    if not ocsp_cert_good:
        raise Exception('New OCSP response is not good! (Stored as "{new}")'.format(new=output_temp))
    # Check whether response is valid
    valid, errormessage = _verify_ocsp_response(cert_info.cert(), cert_info.chain(), cert_info.rootchain(), output_temp, executable=executable, openssl_version=openssl_version)
    if not valid:
        raise Exception('Got invalid new OCSP response: {reason} (Stored as "{new}")'.format(reason=errormessage, new=output_temp))
    # Compare files (if old response exists and is valid as well)
    if has_valid_ocsp:
        old = _read(cert_info.ocsp_response())
        new = _read(output_temp)
        if old == new:
            warning_message('New OCSP response\'s validity ({validity}) is not longer than the previous one\'s! (In fact, they are identical.)'.format(validity=new_ocsp_next_update))
            return False
    # Make backup if requested
    if make_backups:
        now = datetime.datetime.now()
        output_backup = '{0}-{year:04}{month:02}{day:02}-{hour:02}{minute:02}{second:02}'.format(cert_info.ocsp_response(), year=now.year, month=now.month, day=now.day, hour=now.hour, minute=now.minute, second=now.second)
        try:
            shutil.copyfile(output_temp, output_backup)
        except Exception as e:
            raise Exception('Cannot copy OCSP response "{0}" to "{1}"! ({2})'.format(output_temp, output_backup, e))
    # Move file to correct place
    try:
        if os.path.exists(cert_info.ocsp_response()):
            os.remove(cert_info.ocsp_response())
        os.rename(output_temp, cert_info.ocsp_response())
    except Exception as e:
        raise Exception('Cannot move OCSP response "{0}" to "{1}"! ({2})'.format(output_temp, cert_info.ocsp_response(), e))
    # Check whether response is valid longer
    if ocsp_next_update is not None:
        if new_ocsp_next_update <= ocsp_next_update:
            warning_message('New OCSP response\'s validity ({validity}) is not longer than the previous one\'s!'.format(validity=new_ocsp_next_update))
        else:
            output_message('New OCSP response is valid {longer} longer than the old one.'.format(longer=new_ocsp_this_update - ocsp_this_update))
    return True


class OCSPRenewal(object):
    """Parse OCSP renewal configuration and handle execution."""

    def _open_file(self, filename):
        """Open the given file and keep track of opened files.

        Filenames can contain ``{year}``, ``{month}``, ``{day}``,
        ``{hour}``, ``{minute}`` and ``{second}``, which will be
        replaced by the current timestamp's values.
        """
        if '{' in filename:
            now = datetime.datetime.now()
            filename = filename.format(year='{0:04}'.format(now.year), month='{0:02}'.format(now.month), day='{0:02}'.format(now.day), hour='{0:02}'.format(now.hour), minute='{0:02}'.format(now.minute), second='{0:02}'.format(now.second))
        if filename in self.open_files:
            return self.open_files[filename]
        try:
            f = open(filename, 'w')
            self.open_files[filename] = f
            return f
        except Exception as e:
            raise Exception('Cannot open log file "{0}" for writing ({1})'.format(filename, e))

    def __init__(self, filename):
        """Create a new OCSPRenewal object with configuration loaded from the given location on disk.

        The configuration is loaded, but not interpreted, except for log file information.
        As soon as the object is constructed, ``close()`` must be called to make sure
        all open files are closed.
        """
        self.ocsp_folder = ''
        self.min_validity = None
        self.min_validity_pc = 0.5
        self.threads = 1
        self.stop_on_error = False
        self.make_backups = False
        self.openssl_executable = _DEFAULT_OPENSSL_EXECUTABLE_NAME
        self.domains = {}
        self.openssl_version = None

        # Load config
        try:
            with open(filename, "r") as f:
                self.raw_config = yaml.safe_load(f)
        except FileNotFoundError:
            raise Exception('Cannot find configuration file "{0}"!'.format(filename))

        # Handle output and error log
        self.open_files = {}
        try:
            # Output log
            if 'output_log' in self.raw_config:
                self.output_file = self._open_file(self.raw_config['output_log'])
            else:
                self.output_file = sys.stdout
            # Error log
            if 'error_log' in self.raw_config:
                self.error_file = self._open_file(self.raw_config['error_log'])
            else:
                self.error_file = sys.stderr
        except Exception as _:
            self.close()
            raise

    def close(self):
        """Close all open log files."""
        for f in self.open_files.values():
            try:
                f.close()
            except Exception as _:  # pylint: disable=broad-except
                pass

    def _scan_certs(self, folder, cert_mask, chain_mask, rootchain_mask, ocsp_mask, recursive=True):
        """Search for certificates matching the given masks.

        ``folder`` specifies where to search, and ``recursive`` determines whether
        subfolders will be searched as well.

        ``cert_mask``, ``chain_mask``, ``rootchain_mask`` and ``ocsp_mask`` must be
        strings containing ``{domain}``. If files are found matching ``cert_mask``,
        ``chain_mask`` and ``rootchain_mask`` for some domain string, a ``CertInfo``
        instance is added to the result for this domain string with ``ocsp_mask``
        also adjusted accordingly.
        """
        result = {}
        cert_mask_re = re.compile(re.escape(cert_mask).replace(r'\{domain\}', '(?P<domain>.+?)'))
        for dirpath, _, filenames in os.walk(folder):
            for filename in filenames:
                m = re.match(cert_mask_re, filename)
                if m:
                    domain = m.group('domain')
                    cert_file = os.path.join(dirpath, filename)
                    chain_file = os.path.join(dirpath, chain_mask.format(domain=domain))
                    rootchain_file = os.path.join(dirpath, rootchain_mask.format(domain=domain))
                    ocsp_file = os.path.relpath(os.path.join(dirpath, ocsp_mask.format(domain=domain)), folder)
                    cert_info = CertInfo(cert_file, chain_file, rootchain_file, os.path.join(self.ocsp_folder, ocsp_file))
                    if os.path.exists(cert_info.chain()) and os.path.exists(cert_info.rootchain()):
                        if domain in result:
                            raise Exception('Domain identifier "{0}" appears more than once while {2}scanning folder "{1}"!'
                                            .format(domain, folder, 'recursively ' if recursive else ''))
                        result[domain] = cert_info
            if not recursive:
                break
        return result

    @staticmethod
    def _parse_interval(text):
        """Parse a time interval given as a human-readable string.

        Units second (``s``, ``sec``, ``second``, ``seconds``), minute
        (``m``, ``min``, ``minute``, ``minutes``), hour (``h``, ``hour``,
        ``hours``), day (``d``, ``day``, ``days``) and week (``w``,
        ``week``, ``weeks``) can be used.

        Raises an exception when encountering things it cannot parse.
        """
        result = datetime.timedelta()
        parse_interval_data = {
            datetime.timedelta(seconds=1): {'s', 'sec', 'second', 'seconds'},
            datetime.timedelta(minutes=1): {'m', 'min', 'minute', 'minutes'},
            datetime.timedelta(hours=1): {'h', 'hour', 'hours'},
            datetime.timedelta(days=1): {'d', 'day', 'days'},
            datetime.timedelta(weeks=1): {'w', 'week', 'weeks'},
        }
        parts = text.split(' ')
        while parts:
            part = parts.pop(0)
            found = False
            for delta, endings in parse_interval_data.items():
                for ending in endings:
                    if part.endswith(ending):
                        value = part[:len(part) - len(ending)]
                        try:
                            v = int(value)
                            result += delta * v
                            found = True
                            break
                        except ValueError as _:
                            pass
                if found:
                    break
            if not found:
                try:
                    unit = parts.pop(0)
                    v = int(part)
                    for delta, endings in parse_interval_data.items():
                        if unit in endings:
                            result += v * delta
                            found = True
                            break
                except ValueError as _:
                    pass
            if not found:
                raise Exception('Cannot interpret time interval "{0}"!'.format(part))
        return result

    def _parse_domains(self, raw_config):
        """Parse domains of raw config file."""
        def add_domain(domain, cert_info):
            """Add domain data to configuration."""
            if domain in self.domains:
                raise Exception('Domain identifier "{0}" appears more than once!'
                                .format(domain))
            if not os.path.isfile(cert_info.cert()):
                raise Exception('Cannot find certificate chain "{0}" for domain "{1}"!'
                                .format(cert_info.cert(), domain))
            if not os.path.isfile(cert_info.chain()):
                raise Exception('Cannot find certificate chain file "{0}" for domain "{1}"!'
                                .format(cert_info.chain(), domain))
            if not os.path.isfile(cert_info.rootchain()):
                raise Exception('Cannot find certificate root chain file "{0}" for domain "{1}"!'
                                .format(cert_info.rootchain(), domain))
            if not os.path.isfile(cert_info.ocsp_response()) and os.path.exists(cert_info.ocsp_response()):
                raise Exception('OCSP response file "{0}" for domain "{1}" exists, but is not a file!'
                                .format(cert_info.ocsp_response(), domain))
            # Insert
            self.domains[domain] = cert_info

        # Scan for certificates
        for scan_key_data in raw_config.get('scan_keys', []):
            scan_key_folder = scan_key_data.get('folder', '')
            scan_key_recursive = scan_key_data.get('recursive', True)
            scan_key_cert_mask = scan_key_data.get('cert_mask', '{domain}.pem')
            scan_key_chain_mask = scan_key_data.get('chain_mask', '{domain}-chain.pem')
            scan_key_rootchain_mask = scan_key_data.get('rootchain_mask', '{domain}-rootchain.pem')
            scan_key_ocsp_mask = scan_key_data.get('ocsp_mask', '{domain}.ocsp-resp')
            for domain, cert_info in self._scan_certs(scan_key_folder, scan_key_cert_mask, scan_key_chain_mask,
                                                      scan_key_rootchain_mask, scan_key_ocsp_mask,
                                                      recursive=scan_key_recursive).items():
                add_domain(domain, cert_info)

        # Explicitly listed certificates
        for domain, data in raw_config.get('domains', {}).items():
            if 'cert' not in data:
                raise Exception('Explicit domain "{0}" does not contain "cert" record!'.format(domain))
            if 'chain' not in data:
                raise Exception('Explicit domain "{0}" does not contain "chain" record!'.format(domain))
            if 'rootchain' not in data:
                raise Exception('Explicit domain "{0}" does not contain "rootchain" record!'.format(domain))
            if 'ocsp' not in data:
                raise Exception('Explicit domain "{0}" does not contain "ocsp" record!'.format(domain))
            ocsp_responder_uri = None
            if 'ocsp_responder_uri' in data:
                ocsp_responder_uri = data['ocsp_responder_uri']
                if ocsp_responder_uri == 'certificate':
                    ocsp_responder_uri = None
            add_domain(domain, CertInfo(data['cert'], data['chain'], data['rootchain'],
                                        os.path.join(self.ocsp_folder, data['ocsp']),
                                        ocsp_responder_uri=ocsp_responder_uri))

    def parse(self):
        """Completely parse the configuration.

        Raises exceptions on parse errors.
        """
        # Output folder
        self.ocsp_folder = self.raw_config.get('ocsp_folder', '')

        # Validity value
        min_validity_text = self.raw_config.get('minimum_validity', None)
        if min_validity_text:
            self.min_validity = self._parse_interval(min_validity_text)
        else:
            self.min_validity = None

        # Validity percentage
        self.min_validity_pc = self.raw_config.get('minimum_validity_percentage', None)
        if self.min_validity_pc is not None:
            if self.min_validity_pc < 0 or self.min_validity_pc > 100:
                raise Exception('Minimum validity as percentage must be between 0 and 100!')
            self.min_validity_pc /= 100.0

        # Validity sanity checks
        if self.min_validity is None and self.min_validity_pc is None:
            raise Exception('Minimum validity must be specified at least once!')

        # Threads
        self.threads = self.raw_config.get('parallel_threads', 1)

        # Stop on error
        self.stop_on_error = self.raw_config.get('stop_on_error', False)

        # Backups
        self.make_backups = self.raw_config.get('make_backups', False)

        # OpenSSL executable
        self.openssl_executable = self.raw_config.get('openssl_executable', _DEFAULT_OPENSSL_EXECUTABLE_NAME)

        # Domains
        self.domains = {}
        self._parse_domains(self.raw_config)

        # Includes
        for include in self.raw_config.get('includes', []):
            try:
                for entry in sorted(os.listdir(include)):
                    if os.path.isfile(entry):
                        if entry.endswith('.yaml') or entry.endswith('.yml'):
                            include_fn = os.path.join(include, entry)
                            try:
                                with open(include_fn, "r") as f:
                                    raw_config = yaml.safe_load(f)
                                self._parse_domains(raw_config)
                            except OSError as e:
                                raise Exception('Error while reading included config file "{0}" from disk! ({1})'.format(include_fn, e))
                            except Exception as e:
                                raise Exception('Error while reading included config file "{0}": {1}'.format(include_fn, e))
            except FileNotFoundError:
                self.warning('Cannot find include file "{0}"!'.format(include))
            except OSError as e:  # pylint: disable=duplicate-except
                raise Exception('Error while listing files in include "{0}". ({1})'.format(include, e))

        # Determine OpenSSL version
        self.openssl_version = _get_openssl_version(self.openssl_executable)
        self.output('Detected OpenSSL version {0}.{1}.{2}{3}.'.format(*self.openssl_version))

    @staticmethod
    def _format_message(message, domain=None):
        """Format message with domain."""
        return ('[{domain}] {msg}' if domain else '{msg}').format(domain=domain, msg=message)

    def output(self, message, domain=None):
        """Print log message ``message``.

        If ``domain`` is given, will include it in output message as prefix.
        """
        self.output_file.write(self._format_message(message, domain) + '\n')

    def warning(self, message, domain=None):
        """Print warning message ``message``.

        If ``domain`` is given, will include it in output message as prefix.
        """
        if self.output_file != self.error_file:
            self.output('WARNING: {0}'.format(message), domain=domain)
        self.error_file.write(self._format_message('WARNING: {msg}'.format(msg=message), domain) + '\n')

    def error(self, exception, domain=None):
        """Print error message for exception ``exception``.

        If ``domain`` is given, will include it in output message as prefix.
        """
        if self.output_file != self.error_file:
            self.output('ERROR: {0}'.format(exception), domain=domain)
        self.error_file.write(self._format_message('ERROR: {exception}'.format(exception=exception), domain) + '\n')

    def _process_domain(self, domain, cert_info):
        """Process domain."""
        try:
            result = conditional_get_ocsp_response_for_certificate(cert_info,
                                                                   self.min_validity, self.min_validity_pc,
                                                                   make_backups=self.make_backups,
                                                                   output_message=lambda msg: self.output(msg, domain=domain),
                                                                   warning_message=lambda msg: self.warning(msg, domain=domain),
                                                                   executable=self.openssl_executable,
                                                                   openssl_version=self.openssl_version)
            return 'updated' if result else 'unchanged'
        except Exception as e:  # pylint: disable=broad-except
            self.error(e, domain=domain)
            return 'failure'

    def process(self):
        """Check all OCPS responses specified in configuration.

        Return ``True`` in case everything went well, and ``False`` otherwise.
        """
        def process(domain_data):
            """Internal helper to process one domain."""
            return self._process_domain(domain_data[0], domain_data[1])

        success = True
        unchanged_count = 0
        updated_count = 0
        failed_count = 0
        if self.threads > 1:
            # Multi-threading
            from multiprocessing.pool import ThreadPool
            pool = ThreadPool(processes=self.threads)
            for res in pool.imap_unordered(process, self.domains.items()):
                if res == 'failure':
                    failed_count += 1
                    success = False
                    if self.stop_on_error:
                        pool.terminate()
                elif res == 'updated':
                    updated_count += 1
                elif res == 'unchanged':
                    unchanged_count += 1
            pool.close()
            pool.join()
            import time
            time.sleep(0.5)
            return success
        else:
            # Single-threading
            for domain_data in self.domains.items():
                res = process(domain_data)
                if res == 'failure':
                    failed_count += 1
                    success = False
                    if self.stop_on_error:
                        break
                elif res == 'updated':
                    updated_count += 1
                elif res == 'unchanged':
                    unchanged_count += 1
        self.output('{successmsg}: {unchanged} unchanged OCSP responses, {updated} updated OCSP responses and {failed} failures.'.format(successmsg='Success' if success else 'Failure', unchanged=unchanged_count, updated=updated_count, failed=failed_count))
        return success, unchanged_count, updated_count, failed_count


_HELP_TEXT = R"""OCSP Bot {version}

Syntax: {executable} [ <config file> ] [ -h | -help | --help ] [ -v | -version | --version ]

Processes a list of certificates specified in the configuration to fetch
OCSP responses respectively update OCSP responses.

Returns 0 for success (without changes), a positive return value for the number
of OCSP responses renewed, and negative return values for errors.

The configuration file must be in YAML format (https://en.wikipedia.org/wiki/YAML).
"""


def main(executable, arguments):
    """Execute OCSP Bot.

    ``executable`` will be used for errors and help message.
    ``arguments`` are the command line arguments.
    """
    for arg in arguments:
        if arg in ('-h', '-help', '--help'):
            print(_HELP_TEXT.format(executable=executable, version=VERSION))
            return 0
        if arg in ('-v', '-version', '--version'):
            print("OCSP Bot {version}".format(version=VERSION))
            return 0
    config_filename = "ocspbot.yaml"
    if arguments:
        if len(arguments) > 1:
            print('ERROR: invalid number of arguments')
            print(_HELP_TEXT.format(executable=executable, version=VERSION))
            return -4
        config_filename = arguments[0]
    # Load and parse config
    try:
        parsed_config = OCSPRenewal(config_filename)
    except Exception as e:  # pylint: disable=broad-except
        sys.stderr.write('ERROR: {exception}\n'.format(exception=e))
        return -2
    try:
        try:
            parsed_config.parse()
            success, _, updated_count, _ = parsed_config.process()
            return updated_count if success else -1
        except Exception as e:  # pylint: disable=broad-except
            parsed_config.error(e)
            return -3
    finally:
        parsed_config.close()


sys.exit(main(sys.argv[0], sys.argv[1:]))
