# Copyright (c) Microsoft Corporation. All rights reserved.
import certifi
import json
import os
from urllib.request import Request, urlopen

try:
    from applicationinsights import TelemetryClient
    from applicationinsights.channel import SynchronousSender, SynchronousQueue, TelemetryChannel

    class _CustomTelemetrySender(SynchronousSender):
        # Adapted from SynchronousSender.send, with two changes:
        # 1) Pass in root certificates from certifi so that HTTPS connections succeed on Spark clusters.
        # 2) If sending fails, don't queue again. It will hang the job forever if AppInsights is unreachable.
        def send(self, data_to_send):
            request_payload = json.dumps([a.write() for a in data_to_send])
            request = Request(self.service_endpoint_uri, bytearray(request_payload, 'utf-8'), {
                'Accept': 'application/json',
                'Content-Type': 'application/json; charset=utf-8'
            })

            # noinspection PyBroadException
            try:
                urlopen(request, timeout=self.send_timeout, cafile=certifi.where())
            except Exception:
                pass


    def create_telemetry_client():
        try:
            instrumentation_key = os.environ["AZUREML_INSTRUMENTATION_KEY"]
        except KeyError:  # missing instrumentation key
            return None

        return TelemetryClient(
            instrumentation_key,
            TelemetryChannel(queue=SynchronousQueue(_CustomTelemetrySender())))


except ImportError:  # missing applicationinsights module
    def create_telemetry_client():
        return None
