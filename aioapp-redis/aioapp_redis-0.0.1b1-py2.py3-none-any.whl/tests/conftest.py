import gc
import time
import asyncio
import socket
import pytest
import aioredis
from compose.service import ImageType
from compose.project import Project
from aioapp.app import Application

COMPOSE_REDIS_PORT = 19831


@pytest.fixture(scope='session')
def event_loop():
    asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    gc.collect()
    loop.close()


@pytest.fixture(scope='session')
def loop(event_loop):
    return event_loop


def pytest_addoption(parser):
    parser.addoption("--redis-addr", dest="redis_addr",
                     help="Use this redis instead of docker image "
                          "if specified",
                     metavar="redis://host:port/db")
    parser.addoption('--show-docker-logs', dest="show_docker_logs",
                     action='store_true', default=False,
                     help='Show docker logs after test')


@pytest.fixture(scope='session')
def redis_override_addr(request):
    return request.config.getoption('redis_addr')


@pytest.fixture(scope='session')
async def docker_compose(loop, request,
                         docker_project: Project,
                         redis_override_addr):
    async def check_redis(url):
        conn = await aioredis.create_connection(url, loop=loop)
        conn.close()
        await conn.wait_closed()

    checks = {
        (
            'redis',
            'REDIS_DSN',
            redis_override_addr,
            'redis://127.0.0.1:%d/1?encoding=utf-8' % COMPOSE_REDIS_PORT,
            check_redis
        ),
    }

    result = {}

    fns = []
    to_start = []
    for svc, name, override, url, fn in checks:
        if override:
            result[name] = override
        else:
            to_start.append(svc)
            fns.append((fn, url))
            result[name] = url

    if not to_start:
        yield result
    else:
        containers = docker_project.up(to_start)

        if not containers:
            raise ValueError("`docker-compose` didn't launch any containers!")

        try:
            timeout = 60
            start_time = time.time()
            print()
            print('Waiting for docker services...')
            last_err = None
            while start_time + timeout > time.time():
                try:
                    await asyncio.gather(*[fn(url) for fn, url in fns],
                                         loop=loop)
                    break

                except Exception as err:
                    last_err = err
                    await asyncio.sleep(1, loop=loop)
            else:
                last_err_type = type(last_err)
                raise TimeoutError(f'Unable to start all container services'
                                   f' within {timeout} seconds. Last error:'
                                   f' {last_err} ({last_err_type})')
            print('Docker services are ready')
            yield result
        finally:

            # Send container logs to stdout, so that they get included in
            # the test report.
            # https://docs.pytest.org/en/latest/capture.html
            for container in sorted(containers, key=lambda c: c.name):
                if request.config.getoption('show_docker_logs'):
                    header = f"Logs from {container.name}:"
                    print(header)
                    print("=" * len(header))
                    print(
                        container.logs().decode("utf-8", errors="replace") or
                        "(no logs)"
                    )
                    print()

            docker_project.down(ImageType.none, False)


@pytest.fixture(scope='session')
def redis(docker_compose):
    return docker_compose['REDIS_DSN']


def get_free_port(protocol='tcp'):
    family = socket.AF_INET
    if protocol == 'tcp':
        type = socket.SOCK_STREAM
    elif protocol == 'udp':
        type = socket.SOCK_DGRAM
    else:
        raise UserWarning()

    sock = socket.socket(family, type)
    try:
        sock.bind(('', 0))
        return sock.getsockname()[1]
    finally:
        sock.close()


@pytest.fixture()
async def app(loop):
    app = Application(loop=loop)
    yield app
    await app.run_shutdown()
