# -*- coding: utf-8 -*-

import base64
import logging
import os
import threading
from collections import namedtuple
from contextlib import contextmanager
from urllib.parse import urlparse

import yaml

from .interface import Context, Credentials, Env
from .util import homedir, remote_logger, sys_logger

CredTuple = namedtuple("CredTuple", tuple(Credentials.__abstractmethods__))

EnvProps = tuple(Env.__abstractmethods__) + ("extra",)

StorageConfig = namedtuple(
    "StorageConfig", ("endpoint", "public_endpoint", "bucket", "scope")
)


class EnvTuple(namedtuple("EnvTupleBase", EnvProps)):

    _filtered_keys = ["count", "index", "get", "new"]
    _readonly_keys = ["base_url", "in_cluster", "name"]

    def get(self, key: str, default=None):
        if key in EnvTuple._filtered_keys or key.startswith("_"):
            raise NameError(f"{key} is filtered")

        if key in self._fields:
            return getattr(self, key, default)

        return self.extra.get(key, default)

    def set(self, key: str, value) -> Env:
        if key.startswith("_"):
            raise NameError(f"cannot starts with _, {key}")
        if key in self._fields:
            raise NameError(f"cannot set static property {key}")
        self.extra[key] = value
        return self

    def new(self, **overrides) -> Env:
        props = {self._fields[i]: v for i, v in enumerate(self)}
        props["extra"] = self.extra.copy()

        if overrides:
            props.update(
                {
                    k: overrides[k]
                    for k in self._fields
                    if k in overrides and k not in EnvTuple._readonly_keys
                }
            )
            attrs = list(self.extra.keys())
            props["extra"].update({k: overrides[k] for k in attrs if k in overrides})

        return self.__class__(**props)


assert issubclass(EnvTuple, Env)


def __init_env__() -> EnvTuple:
    cfg_path = os.getenv(
        "REFUNC_CONFIG", os.path.join(homedir, ".refunc", "config.yaml")
    )

    base_url = os.environ.get("REFUNC_GATEWAY_URL", "")
    ns = os.getenv("REFUNC_NAMESPACE", "")
    name = os.getenv("REFUNC_NAME", "")

    pull_logs = os.getenv("REFUNC_DEBUG", False)

    incluster = os.getenv("REFUNC_ENV", False) == "cluster"

    # load ca
    cafile = os.getenv("REFUNC_CA_FILE", os.path.join(homedir, ".refunc", "ca.pem"))
    if cafile and not os.path.exists(cafile):
        sys_logger.warning(f"failed to find ca file in REFUNC_CA_DATA({cafile})")
        cafile = ""

    cadata = os.getenv("REFUNC_CA_DATA", b"")
    if cadata:
        try:
            cadata = base64.decodebytes(cadata.encode("utf-8"))
        except Exception as e:
            sys_logger.warning(f"failed to parse REFUNC_CA_DATA, {e}")
            cadata = b""

    # credentails None if missing
    creds_cfg = {
        "access_key": os.environ.get("REFUNC_ACCESS_KEY", ""),
        "secret_key": os.environ.get("REFUNC_SECRET_KEY", ""),
        "token": os.environ.get("REFUNC_TOKEN", ""),
    }

    # minio config, None if missing
    storage_cfg = {
        "endpoint": os.environ.get("REFUNC_MINIO_ENDPOINT", ""),
        "public_endpoint": os.environ.get(
            "REFUNC_MINIO_PUBLIC_ENDPOINT",
            os.environ.get("S3_ENDPOINT", "https://s3.refunc.io"),
        ),
        "bucket": os.environ.get("REFUNC_MINIO_BUCKET", ""),
        "scope": os.environ.get("REFUNC_MINIO_SCOPE", "/"),
    }

    if incluster:  # in cluster
        name = "{}/{}".format(ns, name)
    elif (
        "JPY_USER" in os.environ or "JUPYTERHUB_USER" in os.environ
    ):  # in jupyter kernel
        env_key = "JUPYTERHUB_USER" if "JUPYTERHUB_USER" in os.environ else "JPY_USER"
        name = os.getenv(env_key)
        sys_logger.debug("current context: jupyter({})".format(name))
        name = "{}/local".format(name)
    elif "REFUNC_APP" in os.environ:  # in app mode
        name = os.getenv("REFUNC_APP")
        sys_logger.debug("current context: app {}".format(name))
        name = "{}/app".format(name)

    if os.path.exists(cfg_path):
        with open(cfg_path) as f:
            cfg = yaml.safe_load(f)

        if not name:
            # load user
            name = "{}/local".format(cfg["username"])
            sys_logger.debug(f"current context: {name}")

        if not base_url:
            base_url = cfg.get("apiURL")

        # override storage config
        store_dict = cfg.get("storage", {})

        def override_storage(key):
            storage_cfg[key] = store_dict.get(key, storage_cfg[key])

        override_storage("endpoint")
        override_storage("bucket")
        override_storage("scope")

        # override credentials
        creds_dict = cfg.get("credentials", {})

        def override_creds(key, key_in_cfg):
            creds_cfg[key] = creds_dict.get(key_in_cfg, creds_cfg[key])

        override_creds("access_key", "accessKey")
        override_creds("secret_key", "secretKey")
        override_creds("token", "token")

        if "caFile" in cfg and os.path.exists(cfg.get("caFile", "")):
            cafile = cfg.get("caFile")

        if "caData" in cfg:
            try:
                data = base64.decodebytes(cfg.get("caData", "").encode("utf-8"))
                cadata = data
            except Exception as e:
                sys_logger.warning("failed to parse cadata in config, {}".format(e))

    if not name:
        raise InvalidEnv(f"canno find configs in {os.path.dirname(cfg_path)}")

    # config local prefix
    if name.endswith("/local"):
        storage_cfg["scope"] = os.path.join(storage_cfg["scope"], name)

    if not base_url:
        base_url = "nats://gw.refunc.io"

    # unify baseURL for nats based RPC
    if "REFUNC_NATS_ENDPOINT" in os.environ:
        if not base_url:
            sys_logger.warning("REFUNC_NATS_ENDPOINT overrides REFUNC_GATEWAY_URL")
        nats_url = "nats://{}".format(os.environ["REFUNC_NATS_ENDPOINT"])
    elif base_url.startswith("nats://"):
        nats_url = base_url
    else:
        sys_logger.warning(f"fallback to http based RPC: {base_url}")
        nats_url = ""

    if nats_url:
        uri = urlparse(nats_url)
        port = uri.port if uri.port else 4222
        # token first
        if creds_cfg["token"]:
            base_url = f"nats://{creds_cfg['token']}@{uri.hostname}:{port}"
        elif creds_cfg["access_key"] and creds_cfg["secret_key"]:
            base_url = f"nats://{creds_cfg['access_key']}:{creds_cfg['secret_key']}@{uri.hostname}:{port}"
        else:
            sys_logger.debug("connect to nats without credentails")

    if cadata and cafile:
        # cadata overrides cafile
        cafile = ""

    remote_logger.propagate = pull_logs
    return (
        EnvTuple(
            name=name,
            context=None,
            base_url=base_url,
            in_cluster=incluster,
            credentials=CredTuple(**creds_cfg),
            callers=[],
            extra={
                "user": name,
                "storage": StorageConfig(**storage_cfg),
                "log_endpoint": "",
                "router_sink": os.getenv("REFUNC_ROUTER_SINK", "refunc"),
                "timeout": int(os.getenv("REFUNC_MAX_TIMEOUT", 0)),
                "raw_request": {},
                "ca_file": cafile,
                "ca_data": cadata.decode(),
            },
            pull_logs=pull_logs,
        ),
        base_url.startswith("nats"),
    )


class InvalidEnv(Exception):
    pass


__base_env, IS_NATS_RPC = __init_env__()
__refunc_exec_ctx = threading.local()


def __push(env: Env):
    assert isinstance(env, Env)
    if not hasattr(__refunc_exec_ctx, "envs"):
        __refunc_exec_ctx.envs = []

    __refunc_exec_ctx.envs.append(env)
    return __refunc_exec_ctx.envs[-1]


def __pop():
    if (
        hasattr(__refunc_exec_ctx, "envs")
        and __refunc_exec_ctx.envs
        and len(__refunc_exec_ctx.envs) > 1
    ):
        return __refunc_exec_ctx.envs.pop()


def current_env() -> Env:
    if not hasattr(__refunc_exec_ctx, "envs") or not __refunc_exec_ctx.envs:
        return __push(__base_env.new())
    return __refunc_exec_ctx.envs[-1]


def push_env(env: Env) -> Env:
    old = current_env()
    __push(env)
    return old


def pop_env() -> Env:
    return __pop()


@contextmanager
def new_env(env: Env, **overrides):
    if env is None:
        env = current_env()
    __push(env.new(**overrides))
    try:
        yield
    finally:
        __pop()


@contextmanager
def use_ctx(ctx: Context):
    assert isinstance(ctx, Context)

    __push(current_env().new(context=ctx))
    try:
        yield
    finally:
        __pop()


@contextmanager
def pull_log(on=True, level=logging.DEBUG):
    oldp = remote_logger.propagate
    oldl = remote_logger.level
    env = current_env().new(pull_log=on)
    __push(env)
    remote_logger.setLevel(level)
    remote_logger.propagate = on
    try:
        yield
    finally:
        __pop()
        remote_logger.propagate = oldp
        remote_logger.setLevel(oldl)


__all__ = ["EnvProps", "EnvTuple", "InvalidEnv", "new_env", "pull_log", "push_env"]

