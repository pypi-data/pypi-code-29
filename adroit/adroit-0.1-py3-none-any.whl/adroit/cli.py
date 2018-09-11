import argparse
import os.path
import re
import subprocess
import sys


def get_container_paused_msg(container):
    return (
        "A paused container is available for debugging:\n"
        "docker exec -it {cid} /bin/bash"
    ).format(cid=container[:12])


def get_fail_msg(container=None):
    msg = "Ansible role failed to apply, or tests failed!"
    if container:
        msg += " " + get_container_paused_msg(container)
    return msg


def get_apply_role_playbook():
    """ Get a string representation of a playbook that applies a role. """
    return '[{ hosts: localhost, roles: ["{{ role }}"] }]'


def run_test_role_playbook(role, container, check_idempotency=False):
    """ Run playbooks + tests for a role in a running container. """
    cmd = [
        "docker",
        "exec",
        "-t",
        container,
        "ansible-playbook",
        "/etc/ansible/apply-role.yml",
        "-e",
        "role=%s" % role,
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    changes = 0
    for line in proc.stdout:
        sys.stdout.buffer.write(line)
        sys.stdout.buffer.flush()
        match = re.search(rb"change[sd]=(\d+)", line)
        if match:
            changes = int(match.group(1))
    proc.wait()
    if proc.returncode != 0:
        print(get_fail_msg(container))
        sys.exit(1)
    if check_idempotency and changes > 0:
        print("Expected no changes, but found changes=%d in output!" % changes)
        print(get_container_paused_msg(container))
        sys.exit(1)


class TestFailure(Exception):
    @classmethod
    def from_container_id(cls, container=None):
        return cls(get_fail_msg(container))


class AnsibleRoleTester:
    def __init__(self, root_dir, base_name, default_image, env_var):
        self.root_dir = root_dir
        self.roles_dir = os.path.join(self.root_dir, "roles")
        self.base_name = base_name
        self.default_image = default_image
        self.env_var = env_var

    def check_role_exists(self, role):
        role_path = os.path.join(self.roles_dir, role)
        if not os.path.isdir(role_path):
            print("Could not find ansible role directory at %r" % role_path)
            sys.exit(1)

    def get_docker_name(self, role):
        """ Given a role, get the itended docker image/container name. """
        return "%s-%s" % (self.base_name, role)

    def get_inventory(self, role=None):
        """ Get /etc/ansible/hosts contents for a role. """
        ansible_vars = {
            "ansible_connection": "local",
            "docker": "true",
            self.env_var: "docker",
        }
        inventory_str = "[local]\nlocalhost %s\n" % " ".join(
            "=".join(kv) for kv in sorted(ansible_vars.items())
        )

        groups = ["docker", self.base_name]
        if role:
            groups.append(self.get_docker_name(role))
        for group in groups:
            inventory_str += "[%s:children]\nlocal\n" % group
        return inventory_str

    def build_dockerfile(self, dockerfile, tag):
        subprocess.run(
            ["docker", "build", "--tag", tag, "--file=-", self.root_dir],
            input=dockerfile.encode("ascii"),
            check=True,
        )

    def get_core_dockerfile(self, image):
        """ Get a string representation of a Dockerfile for a role. """
        distro, _, version = image.partition(":")
        if not version:
            version = "latest"
        dockerfile_path = os.path.join(
            os.path.dirname(__file__), "docker", "dockerfile-%s.tmpl" % distro
        )
        if not os.path.exists(dockerfile_path):
            raise ValueError("distro not supported: %s" % distro)
        with open(dockerfile_path) as fh:
            template = fh.read()
        return template.format(
            version=version,
            hosts=self.get_inventory().replace("\n", "\\n"),
            apply_role_playbook=get_apply_role_playbook().replace("\n", "\\n"),
        )

    def build_core_image(self, pull=False, image=None):
        """ Build the core image. """
        image = image or self.default_image
        if pull:
            subprocess.run(["docker", "pull", image])
        dockerfile = self.get_core_dockerfile(image)
        self.build_dockerfile(dockerfile, self.get_docker_name("core"))

    def get_base_dockerfile(self):
        dockerfile_path = os.path.join(
            os.path.dirname(__file__), "docker", "dockerfile-base.tmpl"
        )
        with open(dockerfile_path) as fh:
            template = fh.read()
        return template.format(core_image=self.get_docker_name("core"))

    def build_base_image(self):
        """ Build the base image, which is the core image + the base role. """
        container = self.start_container("base", self.get_docker_name("core"))
        run_test_role_playbook("base", container, check_idempotency=False)
        subprocess.run(["docker", "commit", container, self.get_docker_name("base")])
        subprocess.run(["docker", "rm", "-f", container])

    def start_container(self, role, image):
        """ Start a container for a role. """
        inventory_path = "/tmp/inventory-%s" % role
        with open(inventory_path, "w+") as fh:
            fh.write(self.get_inventory(role))

        docker_run_args = [
            "--detach",
            # we don't like this, but it's needed for systemd
            "--privileged",
            "--volume=/sys/fs/cgroup:/sys/fs/cgroup:ro",
            # systemd likes to know that it's running in docker
            "--env",
            "container=docker",
            "--env",
            "PYTHONUNBUFFERED=1",
            "--volume=%s:/etc/ansible/roles:ro" % self.roles_dir,
            "--volume=%s:/etc/ansible/hosts:ro" % inventory_path,
        ]
        cmd = ["/lib/systemd/systemd"]
        res = subprocess.run(
            ["docker", "run"] + docker_run_args + [image] + cmd,
            stdout=subprocess.PIPE,
            check=True,
        )
        container = res.stdout.decode().strip()

        # if any of the following steps fail, make sure the docker container gets
        # cleaned up. the calling function won't be able to as the container
        # variable containing the ID never gets returned
        try:
            test_vars_path = "/etc/ansible/roles/%s/testing/test_vars.yml" % role
            ln_test_vars = (
                "if [ -e {test_vars_path} ]; then "
                "ln -sf {test_vars_path} /etc/ansible/group_vars/all/; fi"
            ).format(test_vars_path=test_vars_path)
            subprocess.run(["docker", "exec", container, "sh", "-c", ln_test_vars])
        except:
            subprocess.run(["docker", "rm", "-f", container])
            raise

        return container

    def test_role(self, role):
        """ Start a container and test a role in it. """
        container = None
        try:
            image = self.get_docker_name("base")
            container = self.start_container(role, image)

            # for the base image, this step has already been ran
            if role != "base":
                run_test_role_playbook(role, container, check_idempotency=False)

            run_test_role_playbook(role, container, check_idempotency=True)

            subprocess.run(["docker", "rm", "-f", container])
        except Exception as exc:
            if container:
                subprocess.run(["docker", "pause", container])
            raise TestFailure.from_container_id(container) from exc


def parse_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("role")
    parser.add_argument(
        "-b",
        "--base-name",
        default="adroit",
        help="Base of names for docker images and containers.",
    )
    parser.add_argument(
        "-d",
        "--default-image",
        default="debian:stretch",
        help="The image to base docker containers on by default.",
    )
    parser.add_argument(
        "-e",
        "--env-var",
        default="env",
        help='An Ansible variable name that gets set to "docker".',
    )
    parser.add_argument(
        "-r",
        "--root-dir",
        default=os.getcwd(),
        help="Root directory of your Ansible setup.",
    )
    parser.add_argument(
        "-s",
        "--skip-build-images",
        action="store_true",
        help="Skip building of the base image(s).",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    tester = AnsibleRoleTester(
        args.root_dir, args.base_name, args.default_image, args.env_var
    )
    tester.check_role_exists(args.role)
    if not args.skip_build_images:
        tester.build_core_image()
        tester.build_base_image()
    tester.test_role(args.role)


if __name__ == "__main__":
    main()
