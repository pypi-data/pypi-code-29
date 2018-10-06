#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The Downloader internal Module."""
import tarfile
from os import pipe, fdopen
from threading import Thread
import requests
from .cloudevent import CloudEvent
from .cartapi import CartAPI


# pylint: disable=too-few-public-methods
class Downloader(object):
    """Downloader Class."""

    def __init__(self, location, cart_api_url):
        """Create the downloader given directory location."""
        self.location = location
        self.cart_api = CartAPI(cart_api_url)

    def _download_from_url(self, cart_url, filename):
        """Download the cart from the url."""
        def unpack_tarfile(read_pipe):
            """worker thread for unpacking tarfile."""
            cart_tar = tarfile.open(name=None, mode='r|', fileobj=read_pipe)
            cart_tar.extractall(self.location)

        def pipefds():
            """Setup a pipe but return file objects instead."""
            rfd, wfd = pipe()
            rfd = fdopen(rfd, 'rb')
            wfd = fdopen(wfd, 'wb')
            return (rfd, wfd)

        rfd, wfd = pipefds()
        tar_thread = Thread(target=unpack_tarfile, args=(rfd,))
        tar_thread.daemon = True
        tar_thread.start()
        resp = requests.get('{}?filename={}'.format(cart_url, filename))
        for chunk in resp.iter_content(1024 * 1024):
            wfd.write(chunk)
        wfd.close()
        tar_thread.join()

    def cloudevent(self, cloudevent, filename='data'):
        """Handle a cloudevent and return a cart url."""
        self._download_from_url(
            self.cart_api.wait_for_cart(
                self.cart_api.setup_cart(
                    CloudEvent.yield_files(cloudevent)
                )
            ),
            filename
        )
# pylint: enable=too-few-public-methods
