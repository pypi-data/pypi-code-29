#!/usr/bin/env python
from pysilico.client.abstract_camera_client import AbstractCameraClient,\
    MultipleFrameRetriever, SnapshotEntry
from plico.rpc.abstract_remote_procedure_call import \
    AbstractRemoteProcedureCall
from plico.utils.logger import Logger
from plico.utils.decorator import override, returns, returnsForExample
from pysilico.types.camera_status import CameraStatus
from pysilico.utils.timeout import Timeout
from pysilico.types.camera_frame import CameraFrame
from plico.utils.snapshotable import Snapshotable
from plico.client.serverinfo_client import ServerInfoClient
from plico.client.hackerable_client import HackerableClient



class CameraClient(AbstractCameraClient,
                   HackerableClient,
                   ServerInfoClient):

    def __init__(self,
                 rpcHandler,
                 sockets):
        assert isinstance(rpcHandler, AbstractRemoteProcedureCall)

        self._rpcHandler= rpcHandler
        self._subscriberSocket= sockets.serverSubscriber()
        self._subscriberSocketAddress= sockets.serverSubscriberAddress()
        self._subscriberSocket.disconnect(self._subscriberSocketAddress)
        self._displaySocket= sockets.serverDisplay()
        self._displaySocketAddress= sockets.serverDisplayAddress()
        self._requestSocket= sockets.serverRequest()
        self._statusSocket= sockets.serverStatus()
        self._logger= Logger.of('Camera client')
        HackerableClient.__init__(self,
                                  self._rpcHandler,
                                  self._requestSocket,
                                  self._logger)
        ServerInfoClient.__init__(self,
                                  self._rpcHandler,
                                  self._requestSocket,
                                  self._logger)
        self._shape= None
        self._dtype= None
        self._lastFrame= None


    @override
    @returns(CameraStatus)
    def getStatus(
            self, timeoutInSec=Timeout.GET_FRAME_FOR_DISPLAY_TIMEOUT):
        return self._rpcHandler.receivePickable(
            self._statusSocket,
            timeoutInSec)


    @override
    @returns(CameraFrame)
    def getFrameForDisplay(
            self, timeoutInSec=Timeout.GET_FRAME_FOR_DISPLAY_TIMEOUT):
        return self._rpcHandler.recvCameraFrame(
            self._displaySocket,
            timeoutInSec=timeoutInSec)


    def _getLastAvailableFrame(self):
        self._lastFrame= self._rpcHandler.recvCameraFrame(
            self._subscriberSocket,
            timeoutInSec=Timeout.GET_FRAME_TIMEOUT)
        return self._lastFrame



    @override
    @returns(CameraFrame)
    def getFutureFrames(self,
                        numberOfReturnedImages,
                        numberOfFramesToAverageForEachImage=1,
                        timeoutSec=Timeout.GET_FRAME_TIMEOUT):
        self._subscriberSocket.connect(self._subscriberSocketAddress)
        trashFirst= self._getLastAvailableFrame()
        frames= MultipleFrameRetriever.getFrames(
            numberOfReturnedImages,
            numberOfFramesToAverageForEachImage,
            self._getLastAvailableFrame)
        self._subscriberSocket.disconnect(self._subscriberSocketAddress)
        return frames


    @override
    @returnsForExample((1024, 1024))
    def shape(self):
        status= self.getStatus()
        return (status.frameHeight, status.frameWidth)


    def dtype(self):
        return self.getStatus().dtype


    def subSocket(self):
        return self._subscriberSocket


    @override
    def setExposureTime(self,
                        exposureTimeInMilliSeconds,
                        timeoutSec=Timeout.GET_FRAME_TIMEOUT):
        self._logger.notice("Setting exposure time to %f ms" %
                            exposureTimeInMilliSeconds)
        return self._rpcHandler.sendRequest(
            self._requestSocket, 'setExposureTime',
            [exposureTimeInMilliSeconds],
            timeout=timeoutSec)


    @override
    @returns(float)
    def exposureTime(self):
        return float(self.getStatus().exposureTimeInMilliSec)


    @override
    def getSnapshot(self,
                    prefix,
                    timeoutSec=Timeout.GET_FRAME_TIMEOUT):
        status= self.getStatus(timeoutInSec=timeoutSec)
        self._logger.notice("Getting snapshot for %s " % prefix)
        return self._createSnapshotFromStatus(prefix, status)


    def _createSnapshotFromStatus(self, prefix, status):
        assert isinstance(status, CameraStatus)
        snapshot= {}
        snapshot[SnapshotEntry.CAMERA_NAME]= status.name
        snapshot[SnapshotEntry.EXPOSURE_TIME_MS]= status.exposureTimeInMilliSec
        snapshot[SnapshotEntry.FRAME_WIDTH_PX]= status.frameWidth
        snapshot[SnapshotEntry.FRAME_HEIGHT_PX]= status.frameHeight
        snapshot[SnapshotEntry.BINNING]= status.binning
        return Snapshotable.prepend(prefix, snapshot)



    @override
    def setBinning(self,
                   binning,
                   timeoutSec=Timeout.GET_FRAME_TIMEOUT):
        self._logger.notice("Setting binning to %d " % binning)
        return self._rpcHandler.sendRequest(
            self._requestSocket, 'setBinning',
            [binning],
            timeout=timeoutSec)


    @override
    @returns(int)
    def getBinning(self):
        return int(self.getStatus().binning)


    @override
    def setFrameRate(self, frameRate,
                     timeoutSec=Timeout.GET_FRAME_TIMEOUT):
        self._logger.notice("Setting frameRate to %f" % frameRate)
        return self._rpcHandler.sendRequest(
            self._requestSocket, 'setFrameRate',
            [frameRate],
            timeout=timeoutSec)


    @override
    @returns(float)
    def getFrameRate(self):
        return float(self.getStatus().frameRate)


    @override
    @returns(CameraFrame)
    def getDarkFrame(self, timeoutSec=Timeout.GET_FRAME_TIMEOUT):
        return self._rpcHandler.sendRequest(
            self._requestSocket, 'getDarkFrame',
            [],
            timeout=timeoutSec)


    @override
    def setDarkFrame(self, darkFrame,
                     timeoutSec=Timeout.GET_FRAME_TIMEOUT):
        assert isinstance(darkFrame, CameraFrame)
        return self._rpcHandler.sendRequest(
            self._requestSocket, 'setDarkFrame',
            [darkFrame],
            timeout=timeoutSec)
