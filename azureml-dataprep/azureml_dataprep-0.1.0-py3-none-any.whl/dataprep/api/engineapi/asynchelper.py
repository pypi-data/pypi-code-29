# Copyright (c) Microsoft Corporation. All rights reserved.
"""Helpers for running asyncio"""
import sys
import asyncio


def create_event_loop():
    """Returns the correct event loop for the current platform."""
    if sys.platform == "win32":
        loop = asyncio.ProactorEventLoop()
    else:
        loop = asyncio.SelectorEventLoop()

    asyncio.set_event_loop(loop)
    return loop
