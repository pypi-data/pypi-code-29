from dli.client import session


def test_session():
    client = session.start_session(
        "2598b390cd846eba6870816d4cadf8420a193bd3e704583488c15e10f6060a123929e8807f637c405ea3036c3d3ce808430ba97ccf20b54c500019533a89aa29",
        "https://10.251.128.148/__api",
        host="catalogue-dev.udpmarkit.net"
    )

    client.get_package("test")


def test_session_2():
    client = session.start_session(
        "2598b390cd846eba6870816d4cadf8420a193bd3e704583488c15e10f6060a123929e8807f637c405ea3036c3d3ce808430ba97ccf20b54c500019533a89aa29",
        "https://catalogue-dev.udpmarkit.net/__api"
    )

    client.get_package("test")
