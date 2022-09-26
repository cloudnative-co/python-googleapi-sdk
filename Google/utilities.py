import base64
import datetime
import importlib
import inspect
import io
import json
import re


def normalization(args):
    result = {}
    for ky, value in args.items():
        if ky == "self":
            continue
        if value is None:
            value = "null"
        elif isinstance(value, str):
            value = value.replace('"', '\\"')
            value = '"{}"'.format(value)
        elif isinstance(value, datetime.datetime):
            value = value.timestamp()
        elif isinstance(args[ky], dict):
            value = json.dumps(value)
        elif isinstance(args[ky], list):
            value = json.dumps(value)
        elif isinstance(value, bool):
            value = "true" if value else "false"
        elif isinstance(value, bytes):
            value = base64.b64encode(value)
            value = '"{}"'.format(value)
        result[ky] = value
    return result


def remove_none(params: dict):
    result = {}
    for k, v in params.items():
        if v is None:
            continue
        if isinstance(v, dict):
            v = remove_none(v)
            if v is None:
                continue
        elif isinstance(v, list):
            tmp_lst = []
            for v1 in v:
                if isinstance(v1, dict):
                    v1 = remove_none(v1)
                    if v1 is None:
                        continue
                tmp_lst.append(v1)
            if len(tmp_lst) == 0:
                continue
            v = tmp_lst
        result[k] = v
    if len(result) == 0:
        return None
    return result


def request_parameter(args: dict):
    map_path = args["self"].__module__.split(".")[:-1]
    map_path.append("maps")
    map_path = ".".join(map_path)

    mdl_map = importlib.import_module(map_path)
    parameter_maps = mdl_map.Maps

    m_name = args["self"].__module__
    c_name = args["self"].__class__.__name__
    m_name = inspect.stack()[1].function
    if c_name not in parameter_maps:
        return None
    if m_name not in parameter_maps[c_name]:
        return None
    req_map = parameter_maps[c_name][m_name]
    auth_method = None
    if hasattr(args["self"], "auth_method"):
        auth_method = args["self"].auth_method
    if "auth_method" in req_map:
        auth_method = req_map["auth_method"]

    auth_params = dict()
    if "auth_params" in req_map:
        auth_params = req_map["auth_params"]
    method = req_map["method"]
    url = req_map["url"]
    url = url.format(**args)
    query = None
    payload = None
    files = None

    if "files" in args:
        files = args.pop("files")
    params = normalization(args)

    if "query" in req_map:
        query = parameter_maps[c_name][m_name]["query"]
        query = query.format(**params)
        try:
            query = json.loads(query, strict=False)
        except json.decoder.JSONDecodeError as e:
            start = e.pos - 10
            start = 0 if start <= 0 else start
            end = e.pos + 10
            end = len(query) if len(query) >= end else end
            raise e
        query = remove_none(query)
    if "payload" in req_map:
        payload = parameter_maps[c_name][m_name]["payload"]
        payload = payload.format(**params)
        try:
            payload = json.loads(payload, strict=False)
        except json.decoder.JSONDecodeError as e:
            start = e.pos - 10
            start = 0 if start <= 0 else start
            end = e.pos + 10
            end = len(payload) if len(payload) >= end else end
            raise e
        payload = remove_none(payload)
    result = {
        "method": method,
        "url": url,
        "query": query,
        "payload": payload,
        "files": files,
        "auth_method": auth_method,
        "auth_params": auth_params
    }
    return result

