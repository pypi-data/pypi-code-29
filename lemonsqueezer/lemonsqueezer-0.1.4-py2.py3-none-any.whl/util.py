import asyncio


async def _terminate_or_kill(process, timeout):
    """
    Try to terminate a process. If it does not stop by :param timeout:, kill it

    :return: `True` if terminated, `False` if killed.
    """
    process.terminate()
    try:
        await asyncio.wait_for(process.wait(), timeout)
        return True
    except asyncio.TimeoutError:
        process.kill()
        return False
