import base64
import binascii
import datetime
import hashlib
import json
import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import ciphers
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_der_public_key
from moneyed import Money
from OpenSSL import crypto
from OpenSSL._util import ffi
from OpenSSL._util import lib

from applepie import currencies
from applepie import exceptions


class Parser(object):

    oids = {
        "merchant": "1.2.840.113635.100.6.32",
        "leaf": "1.2.840.113635.100.6.29",
        "intermediate": "1.2.840.113635.100.6.2.14"
    }

    def __init__(self, dataset):
        """This constructor accepts a dataset, which is the paymentData JSON that you receive from Apple"""

        self.backend = default_backend()
        self.version = self.extract_data(dataset, "version")
        self.data = self.extract_data(dataset, "data")
        self.signature = self.extract_data(dataset, "signature")

        headers = dataset.get("header")
        self.transaction_id = self.extract_data(headers, "transactionId")
        self.ephemeral_public_key = self.extract_data(headers, "ephemeralPublicKey")
        self.public_key_hash = self.extract_data(headers, "publicKeyHash")
        self.application_data = self.extract_data(headers, "applicationData")

        if not self.application_data:
            self.application_data = ""

    @staticmethod
    def extract_data(data, field, message=None):
        """Given a dict and a field, grab the field's data and return it when possible.
        If it's not possible, this method will raise an InvalidApplePieData exception, optionally with the message
        parameter given."""

        try:
            return data.get(field)
        except (KeyError, IndexError):
            message = message or "No data found in {0}".format(field)
            raise exceptions.InvalidApplePieData(message)

    def decrypt(self, certificate, private_key, root_certificate=None):
        root_certificate = self.load_root_certificate(root_certificate)
        intermediate_certificate = self.load_intermediate_certificate(self.signature)
        leaf_certificate = self.load_leaf_certificate(self.signature)
        self.verify_chain_of_trust(leaf_certificate, intermediate_certificate, root_certificate)

        certificate = self.load_certificate(certificate)
        private_key = self.load_private_key(private_key)
        self.validate_signature(
            private_key, self.signature, self.ephemeral_public_key,
            self.data, self.application_data, self.transaction_id
        )

        merchant_id = self.gather_merchant_id(certificate)
        shared_secret = self.generate_shared_secret(private_key, self.ephemeral_public_key)
        symmetric_key = self.generate_symmetric_key(merchant_id, shared_secret)

        deciphered = self.decipher(self.data, symmetric_key)
        return deciphered

    def load_root_certificate(self, root_certificate=None):
        if not root_certificate:
            root_certificate = os.path.join(os.path.dirname(os.path.abspath(__file__)), "certs", "AppleRootCA-G3.cer")

        try:
            root_certificate = self.load_certificate(root_certificate)
        except Exception:
            raise exceptions.InvalidCertificate("Invalid Root Certificate")

        return root_certificate

    def load_intermediate_certificate(self, signature):
        certificates = self.load_certificates_from_signature(signature)
        intermediate_certificate = self.find_certificate_by_oid(certificates, self.oids["intermediate"])

        if not intermediate_certificate:
            raise exceptions.InvalidSignature("Invalid Intermediate Certificate")

        return intermediate_certificate

    def load_leaf_certificate(self, signature):
        certificates = self.load_certificates_from_signature(signature)
        leaf_certificate = self.find_certificate_by_oid(certificates, self.oids["leaf"])

        if not leaf_certificate:
            raise exceptions.InvalidSignature("Invalid Leaf Certificate")

        return leaf_certificate

    @staticmethod
    def load_certificates_from_signature(signature):
        signature = base64.b64decode(signature)
        pkcs7 = crypto.load_pkcs7_data(crypto.FILETYPE_ASN1, signature)

        raw_certificates = ffi.NULL

        if pkcs7.type_is_signed():
            raw_certificates = pkcs7._pkcs7.d.sign.cert
        elif pkcs7.type_is_signedAndEnveloped():
            raw_certificates = pkcs7._pkcs7.d.signed_and_enveloped.cert

        certificates = []

        for x in range(lib.sk_X509_num(raw_certificates)):
            certificate = lib.X509_dup(lib.sk_X509_value(raw_certificates, x))
            certificate = crypto.X509._from_raw_x509_ptr(certificate)
            certificate = ApplePieCertificate(certificate)
            certificates.append(certificate)

        return certificates

    @staticmethod
    def find_certificate_by_oid(certificates, oid):
        for certificate in certificates:
            for extension in certificate.x509.extensions:
                if extension.oid.dotted_string == oid:
                    return certificate

        return None

    @staticmethod
    def verify_chain_of_trust(leaf_certificate, intermediate_certificate, root_certificate):
        try:
            trusted_certificate_store = crypto.X509Store()
            trusted_certificate_store.add_cert(root_certificate.certificate)
            trusted_certificate_store.add_cert(intermediate_certificate.certificate)

            trusted_context = crypto.X509StoreContext(trusted_certificate_store, leaf_certificate.certificate)
            trusted_context.verify_certificate()
        except Exception:
            raise exceptions.InvalidCertificate("Couldn't verify SSL chain of trust")

    @staticmethod
    def validate_signature(private_key, signature, ephemeral_public_key, data, application_data, transaction_id):
        # TODO: perform ECDSA validation against the signature
        pass

    def load_certificate(self, certificate):
        loaded = None

        if not loaded:
            try:
                loaded = crypto.load_certificate(crypto.FILETYPE_ASN1, certificate)
            except Exception:
                pass

        if not loaded:
            try:
                loaded = crypto.load_certificate(crypto.FILETYPE_PEM, certificate)
            except Exception:
                pass

        if not loaded:
            with open(certificate, "rb") as certificate_file:
                certificate = certificate_file.read()

            try:
                loaded = crypto.load_certificate(crypto.FILETYPE_ASN1, certificate)
            except Exception:
                pass

            if not loaded:
                try:
                    loaded = crypto.load_certificate(crypto.FILETYPE_PEM, certificate)
                except Exception:
                    pass

        if not loaded:
            raise Exception("Couldn't load certificate")

        certificate = ApplePieCertificate(loaded)
        return certificate

    def load_private_key(self, private_key):
        loaded = None

        try:
            loaded = load_pem_private_key(private_key, None, self.backend)
        except Exception:
            pass

        if not loaded:
            try:
                with open(private_key, "rb") as private_key_file:
                    private_key = private_key_file.read()
                    loaded = load_pem_private_key(private_key, None, self.backend)
            except Exception:
                pass

        if not loaded:
            raise exceptions.InvalidCertificate("Invalid Private Key file")

        return loaded

    def gather_merchant_id(self, certificate):
        for extension in certificate.x509.extensions:
            if extension.oid.dotted_string == self.oids["merchant"]:
                return binascii.unhexlify(extension.value.value[2:])

        raise exceptions.MissingMerchantId()

    def generate_shared_secret(self, private_key, ephemeral_public_key):
        ephemeral_public_key = base64.b64decode(ephemeral_public_key)
        ephemeral_public_key = load_der_public_key(ephemeral_public_key, self.backend)
        shared_secret = private_key.exchange(ec.ECDH(), ephemeral_public_key)

        return shared_secret

    @staticmethod
    def generate_symmetric_key(merchant_id, shared_secret):
        key = hashlib.sha256()
        key.update(b'\0\0\0\1')
        key.update(shared_secret)
        key.update(b'\x0did-aes256-GCM' + b'Apple' + merchant_id)

        return key.digest()

    def decipher(self, encrypted_data, symmetric_key):
        encrypted_data = base64.b64decode(encrypted_data)
        iv_size = 16
        mode = ciphers.modes.GCM(b'\0' * iv_size, encrypted_data[-iv_size:], iv_size)
        decipher = ciphers.Cipher(ciphers.algorithms.AES(symmetric_key), mode, backend=self.backend).decryptor()
        decrypted = decipher.update(encrypted_data[:-16]) + decipher.finalize()
        decrypted = Token(decrypted)

        return decrypted


class ApplePieCertificate(object):

    def __init__(self, certificate):
        self.certificate = certificate
        self.x509 = self.certificate.to_cryptography()


class Token(object):

    def __init__(self, parsed):
        self.data = json.loads(parsed)
        self.cardholder_name = self.get_cardholder_name(self.data)
        self.card_number = self.get_card_number(self.data)
        self.expiration_date = self.get_expiration(self.data)
        self.amount = self.get_amount(self.data)
        self.manufacturer = self.data.get("deviceManufacturerIdentifier", "")
        self.payment_data_type = self.data.get("paymentDataType", "")
        self.payment_data = self.data.get("paymentData", {})

    @staticmethod
    def get_cardholder_name(parsed):
        return parsed.get("cardholderName", "")

    @staticmethod
    def get_card_number(parsed):
        return parsed.get("applicationPrimaryAccountNumber", "")

    @staticmethod
    def get_expiration(parsed):
        expiration = parsed.get("applicationExpirationDate", "")
        if not expiration:
            return None

        if len(expiration) != 6:
            return None

        year = 2000 + int(expiration[0:2])
        month = int(expiration[2:4])
        day = int(expiration[4:])

        expiration = datetime.datetime(year, month, day, hour=23, minute=59, second=59, microsecond=999)

        return expiration

    @staticmethod
    def get_amount(parsed):
        amount = parsed.get("transactionAmount", 0)
        currency = parsed.get("currencyCode", "")
        currency = currencies.LOOKUP.get(currency, "USD")

        amount = Money(amount=amount, currency=currency)
        return amount
