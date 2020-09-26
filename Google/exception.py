import urllib.error
import json


class APIException(urllib.error.HTTPError):
    _code = None

    def __init__(self, e: urllib.error.HTTPError = None, message: str = None):
        super()
        if message is not None:
            self.state = False
            self.hdrs = None
            self.fp = None
            self.filename = None
            self.info = {}
            self.msg = message
            self.code = message
            return
        body = e.read().decode("utf-8")
        try:
            body = json.loads(body)
            error = body["error"]
            self.info = error.get("errors", {})
            self.msg = error.get("message", "")
            self.code = error.get("code", "")
            self.state = error.get("status", "")
        except json.decoder.JSONDecodeError:
            pass

    def __str__(self):
        return json.dumps({
            "message": self.msg,
            "code": self.code,
            "status": self.state,
            "reason": self.reason,
            "url": self.filename,
            "info": self.info
        })
