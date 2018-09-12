# Copyright 2018, Bryan Thornbury
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import argparse, os
from command import Command


def getLocalIp():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    localIp = s.getsockname()[0]
    s.close()

    print("[Local IP] " + localIp)

    return localIp


def pushImage(dockerImageName, sshHost, sshIdentityFile, sshPort, localIp):
    # Setup remote docker registry
    print("Setting up secure private registry... ")
    registryCommandResult = Command("ssh", [
        "-i", sshIdentityFile,
        "-p", sshPort,
        sshHost,
        "docker run -d -v /etc/docker-push-ssh/registry:/var/lib/registry "
        "--name docker-push-ssh-registry -p 127.0.0.1:5000:5000 registry"
    ]).execute()

    if registryCommandResult.failed():
        print("ERROR")
        print(registryCommandResult.stdout)
        print(registryCommandResult.stderr)
        return

    print("Establishing SSH Tunnel...")
    # Establish ssh tunnel
    sshTunnelCommandResult = Command("ssh", [
        "-N",
        "-L", localIp + ":5000:localhost:5000",
        "-i", sshIdentityFile,
        sshHost
    ]).execute(waitForExit=False)

    try:
        print("Tagging image for push...")
        Command("docker", [
            "tag",
            dockerImageName,
            localIp + ":5000/" + dockerImageName
        ]).environment_dict(os.environ).execute()

        print("Pushing Image from local host...")
        pushDockerImageCommandResult = Command("docker", [
            "push",
            localIp + ":5000/" + dockerImageName
        ]).environment_dict(os.environ).execute()

        if pushDockerImageCommandResult.failed():
            print("Error Pushing Image: Ensure " + localIp + ":5000 is added to your insecure registries.")
            print("More Details (OS X): "
                  "https://stackoverflow.com/questions/32808215/where-to-set-the-insecure-registry-flag-on-mac-os")

            print(pushDockerImageCommandResult.stdout)
            print(pushDockerImageCommandResult.stderr)
            return

        print("Pulling and Retagging Image on remote host...")
        pullDockerImageCommandResult = Command("ssh", [
            "-i", sshIdentityFile,
            "-p", sshPort,
            sshHost,
            "docker pull " + "localhost:5000/" + dockerImageName +
            " && docker tag localhost:5000/" + dockerImageName + " " + dockerImageName
        ]).execute()

        if pullDockerImageCommandResult.failed():
            print("ERROR")
            print(pullDockerImageCommandResult.stdout)
            print(pullDockerImageCommandResult.stderr)
            return

    finally:
        print("Cleaning up...")
        Command("ssh", [
            "-i", sshIdentityFile,
            "-p", sshPort,
            sshHost,
            "docker rm -f docker-push-ssh-registry"
        ]).execute()

        Command("kill", [
            str(sshTunnelCommandResult.pid)
        ]).execute()

        Command("docker", [
            "image", "rm",
            localIp + ":5000/" + dockerImageName
        ]).environment_dict(os.environ).execute()


def main():
    parser = argparse.ArgumentParser(description="A utility to securely push a docker image from your local host to a "
                                                 "remote host over ssh without using docker save/load or needing to "
                                                 "setup a private registry.")

    parser.add_argument("ssh_host", help="Host to push docker image to. (ex. username@myhost.com)")

    parser.add_argument("docker_image", help="Docker image name to push.")

    parser.add_argument("-i", "--ssh-identity-file", type=str,
                        help="[required] Path to the ssh identity file on your local host. "
                             "Required, password auth not supported.")

    parser.add_argument("-p", "--ssh-port", type=str, help="[optional] Port on ssh host to connect to. (Default is 22)", default="22")

    parser.add_argument("-l", "--local-ip", type=str, help="[optional] Ip Address of your local host. Important for systems where "
                                                           "docker is run inside a VM (mac, windows). "
                                                           "If not provided, a best effort is used to obtain it.")

    args = parser.parse_args()

    assert args.ssh_identity_file is not None

    localIp = args.local_ip or getLocalIp()
    print("[REQUIRED] Ensure " + localIp + ":5000 is added to your insecure registries.")

    pushImage(args.docker_image, args.ssh_host, args.ssh_identity_file, args.ssh_port, localIp)


if __name__ == "__main__":
    main()
