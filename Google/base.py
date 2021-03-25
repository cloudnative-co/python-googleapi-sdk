# -*- coding: utf-8 -*-
# import module snippets
import base64
import cryptography
import cryptography.hazmat.primitives.serialization
import datetime
import http.cookiejar
import io
import json
import os
import sys
import urllib.request
import urllib.parse
from .utilities import request_parameter
from .exception import APIException


class Base(object):
    __client: urllib.request.OpenerDirector = None
    __cookie: http.cookiejar.CookieJar = None
    __username: str = None
    __header: dict = dict()
    __expires_in: datetime.datetime = None
    __token: str = None

    __type: str = None
    __project_id: str = None
    __private_key_id: str = None
    __private_key: str = None
    __client_email: str = None
    __client_id: str = None
    __auth_uri: str = None
    __token_uri: str = None
    __auth_provider_x509_cert_url: str = None
    __client_x509_cert_url: str = None
    __username: str = None
    __expires_in: str = None

    def __init__(
        self,
        type: str = None,
        project_id: str = None,
        private_key_id: str = None,
        private_key: str = None,
        client_email: str = None,
        client_id: str = None,
        auth_uri: str = None,
        token_uri: str = None,
        auth_provider_x509_cert_url: str = None,
        client_x509_cert_url: str = None,
        username: str = None,
        client: object = None,
    ):
        if client is not None:
            self.__client = client.__client
            self.__header = client.__header
            self.__cookie = client.__cookie
            self.__type = client.__type
            self.__project_id = client.__project_id
            self.__private_key_id = client.__private_key_id
            self.__private_key = client.__private_key
            self.__client_email = client.__client_email
            self.__client_id = client.__client_id
            self.__auth_uri = client.__auth_uri
            self.__token_uri = client.__token_uri
            self.__auth_provider_x509_cert_url \
                = client.__auth_provider_x509_cert_url
            self.__client_x509_cert_url = client.__client_x509_cert_url
            self.__username = client.__username
            self.__expires_in = client.__expires_in
        else:
            self.__type = type
            self.__project_id = project_id
            self.__private_key_id = private_key_id
            self.__private_key = private_key
            self.__client_email = client_email
            self.__client_id = client_id
            self.__auth_uri = auth_uri
            self.__token_uri = token_uri
            self.__auth_provider_x509_cert_url = auth_provider_x509_cert_url
            self.__client_x509_cert_url = client_x509_cert_url
            self.__username = username
            self.__cookie = http.cookiejar.CookieJar()
            self.__client = urllib.request.build_opener(
                urllib.request.HTTPCookieProcessor(self.__cookie)
            )
            urllib.request.install_opener(self.__client)

    def load_private_key(self, data: str = None):
        data = data.encode('ascii')
        k = cryptography.hazmat.primitives.serialization.load_pem_private_key(
            data,
            password=None,
            backend=cryptography.hazmat.backends.default_backend()
        )
        return k

    def create_claims(
        self, scopes: list, expire: int = 3600
    ):
        now = datetime.datetime.utcnow()
        delta30 = now + datetime.timedelta(seconds=expire)
        exp = int((delta30 - datetime.datetime(1970, 1, 1)).total_seconds())
        iat = int((now - datetime.datetime(1970, 1, 1)).total_seconds())
        scope = " ".join(scopes)
        payload = {
            'iss': self.__client_email,
            "scope": scope,
            'aud': self.__token_uri,
            'exp': exp,
            "iat": iat,
        }
        if self.__username is not None:
            payload["sub"] = self.__username
        payload = json.dumps(payload, separators=(",", ":")).encode('utf-8')
        return base64.urlsafe_b64encode(payload).replace(b"=", b"")

    def create_jwt_header(self, algorithm="RS256"):
        header = {
            "typ": "JWT",
            "alg": algorithm
        }
        json_header = json.dumps(header, separators=(",", ":")).encode('utf-8')
        return base64.urlsafe_b64encode(json_header).replace(b"=", b"")

    def create_assertion(self, header, claims):
        segments = []
        segments.append(header)
        segments.append(claims)
        key = self.load_private_key(data=self.__private_key)
        signature = key.sign(
            b".".join(segments),
            cryptography.hazmat.primitives.asymmetric.padding.PKCS1v15(),
            cryptography.hazmat.primitives.hashes.SHA256()
        )
        segments.append(base64.urlsafe_b64encode(signature).replace(b"=", b""))
        assertion = b'.'.join(segments)
        return assertion

    def gsuite_autholization(self, scopes: str):
        if self.__expires_in is not None:
            expires_in = self.__expires_in
            now = datetime.datetime.now()
            if expires_in > now:
                self.__header["Authorization"] = self.__token
                self.__header["Content-Type"] = "application/json"
                return

        header = self.create_jwt_header()
        claims = self.create_claims(scopes)
        assertion = self.create_assertion(header, claims)
        url = self.__token_uri
        payload = {
            "assertion": assertion,
            "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer"
        }
        payload = urllib.parse.urlencode(payload).encode()
        args = {
            "url": url,
            "method": "POST",
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            "data": payload
        }
        req = urllib.request.Request(**args)
        try:
            with self.__client.open(req) as res:
                body = res.read()
                body = body.decode("utf-8")
                body = json.loads(body)
                if "access_token" in body:
                    auth = "{token_type} {access_token}".format(**body)
                    self.__token = auth
                    expires_in = int(body["expires_in"])
                    expires_in = datetime.datetime.fromtimestamp(expires_in)
                    self.__expires_in = expires_in
                    self.__header["Authorization"] = auth
        except urllib.error.HTTPError as e:
            raise e

    def encode_multipart(
        self, payload: dict = None, files: dict = None, charset="utf-8"
    ):
        boundary = '----------lImIt_of_THE_fwIle_eW_$'
        bf = io.BytesIO()
        if payload is not None:
            for key, value in payload.items():
                bf.write(('--%s\r\n' % boundary).encode(charset))
                bf.write((
                    'Content-Disposition: form-data; name="%s"' % key
                ).encode(charset))
                bf.write(b'\r\n\r\n')
                if isinstance(value, dict):
                    value = json.dumps(value)
                if isinstance(value, str):
                    value = value.encode(charset)
                bf.write(value)
                bf.write(b'\r\n')
        if files is not None:
            cdisp = 'Content-Disposition: form-data; '\
                    'name="%s"; filename="%s"\r\n'
            for key, value in files.items():
                filename = value["name"]
                bf.write(('--%s\r\n' % boundary).encode(charset))
                bf.write((cdisp % (key, filename)).encode(charset))
                type = mimetypes.guess_type(filename)[0]
                type = type or 'application/octet-stream'
                bf.write(("Content-Type: {}\r\n".format(type)).encode(charset))
                content = value["content"]
                if hasattr(content, "read"):
                    content = content.read()
                bf.write(b'\r\n')
                bf.write(content)
                bf.write(b'\r\n')
        bf.write(('--' + boundary + '--\r\n\r\n').encode(charset))
        bf = bf.getvalue()
        content_type = 'multipart/form-data; boundary=%s' % boundary
        return content_type, bf

    def http_request(
        self,
        method: str, path: str = None, headers: dict = {},
        query: dict = None, payload: dict = None, url: str = None,
        files: dict = None, is_read: bool = True, with_header: bool = False,
        auth_method: str = None, auth_params: dict = {}, charset: str = "utf-8"
    ):
        if auth_method is not None:
            if hasattr(self, auth_method):
                getattr(self, auth_method)(**auth_params)
        if url is None:
            url = "{}://{}/{}".format(self.schema, self.host, path)
        if query is None:
            query = dict()
        if "?" in url:
            q = url.split("?")
            if query is None:
                query = dict()
            for q1 in q[1].split("&"):
                q1 = q1.split("=")
                query[q1[0]] = q1[1]
        if method == "get":
            query["token"] = self.token
        elif method == "post":
            headers["Authorization"] = "Bearer {}".format(self.token)
        if len(query) > 0:
            url = "{}?{}".format(url, urllib.parse.urlencode(query))

        parsed_url = urllib.parse.urlparse(url)
        resource = "{}://{}".format(parsed_url.scheme, parsed_url.netloc)

        args = {
            "url": url,
            "method": method.upper()
        }
        ctype = headers.get('Content-Type', None)
        if ctype == "multipart/form-data":
            ctype, payload = self.encode_multipart(payload, files, charset)
            headers["Content-Type"] = ctype
            args["data"] = payload
        elif ctype == "application/octet-stream":
            args["data"] = payload
        elif payload is not None:
            try:
                payload = json.dumps(payload).encode('utf-8')
                headers["Content-Type"] = "application/json; charset=UTF-8"
            except TypeError as e:
                try:
                    payload = urllib.parse.urlencode(payload).encode()
                except Exception as e:
                    pass
            args["data"] = payload
        else:
            payload = b""
        args["headers"] = dict(self.__header, **headers)
        print(args["headers"])
        req = urllib.request.Request(**args)
        try:
            with self.__client.open(req) as res:
                head = dict(res.info())
                if is_read:
                    body = res.read()
                    try:
                        body = body.decode("utf-8")
                    except UnicodeDecodeError:
                        if with_header:
                            return body, head
                        return body
                    try:
                        body = json.loads(body)
                        if with_header:
                            return body, head
                        return body
                    except Exception as e:
                        if with_header:
                            return body, head
                        return body
                return res
        except urllib.error.HTTPError as e:
            raise APIException(e)

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username
        self.__expires_in = None
        self.__token = None
        self.__headers = {}
        self.__cookie = http.cookiejar.CookieJar()
        self.__client = urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(self.__cookie)
        )
        urllib.request.install_opener(self.__client)

    @property
    def private_key(self):
        return self.__private_key

    @property
    def client_email(self):
        return self.__client_email
