import io
import json
import base64
import time
import datetime
import base64
import pyasn1.codec.der.decoder
import pyasn1_modules.pem
import pyasn1_modules.rfc5208
import rsa
import urllib.parse

from ...base import Base


class Utility(Base):

    def _load_private_key(self, key, passowrd="notasecret"):
        marker_id, key_bytes =  pyasn1_modules.pem.readPemBlocksFromFile(
            io.StringIO(key),
            (
                '-----BEGIN RSA PRIVATE KEY-----',
                '-----END RSA PRIVATE KEY-----'
            ),
            ('-----BEGIN PRIVATE KEY-----', '-----END PRIVATE KEY-----')
        )

        if marker_id == 0:
            pkey = rsa.key.PrivateKey.load_pkcs1(key_bytes, format='DER')
        elif marker_id == 1:
           key_info, remaining = pyasn1.codec.der.decoder.decode(
                key_bytes, asn1Spec=pyasn1_modules.rfc5208.PrivateKeyInfo()
            )
           if remaining != b'':
                raise ValueError('Unused bytes', remaining)
           pkey_info = key_info.getComponentByName('privateKey')
           pkey = rsa.key.PrivateKey.load_pkcs1(pkey_info.asOctets(), format='DER')
        else:
            raise ValueError('No key could be detected.')
        return pkey

    def get_signature(self, message) -> bytes:
        pkey = self._load_private_key(self.private_key)
        message = message.encode("utf-8")

        sig = rsa.pkcs1.sign(message, pkey, 'SHA-256')
        sig = base64.b64encode(sig)
        return sig

    def signed_url(
        self,
        bucket: str, name: str, method: str = "PUT",
        content_type: str = "application/json", content_md5: str = "", expire: int = 60
    ) -> str:
        expire = datetime.datetime.now() + datetime.timedelta(seconds=expire)
        expire = str(int(time.mktime(expire.timetuple())))
        gs_path = '/{}/{}'.format(bucket, name)
        message = '\n'.join([
            method,
            content_md5,
            content_type,
            expire,
            gs_path
        ])
        sign = self.get_signature(message)
        query = urllib.parse.urlencode({
            'GoogleAccessId': self.client_email,
            'Expires': str(expire),
            'Signature': sign
        })
        return "https://storage.googleapis.com{gs_path}?{query}".format(
            gs_path=gs_path,
            query=query
        )
