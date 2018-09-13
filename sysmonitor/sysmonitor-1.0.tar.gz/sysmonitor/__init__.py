"""
sysmonitor agent package

This agent should run on the hosts to monitor.

The agent can be extended to use third-party interfaces and authentications
modules.

From upstream, it can report the status via two interfaces:
    * push (notification): Sends a HTTP request to a remote server
    * REST API: Serves a REST API where other systems can interact with

From upstream, it has the following features:
    * System resource status: It reports system load, disk, RAM and SWAP
    * Systemd status: It reports systemd unit states
    * Command and script execution: It allows to execute commands and scripts
        on the host
"""
