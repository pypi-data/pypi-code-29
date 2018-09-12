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


class TestException(Exception):
    """ An unexpected error occured while running or setting up tests. """

    pass


class TestFailure(Exception):
    """ Tests ran as expected, but either Ansible or idempotency checks failed. """

    @classmethod
    def from_container_id(cls, container=None):
        return cls(get_fail_msg(container))


class AnsibleRoleTester:
    def __init__(self, root_dir, base_name, default_image, extra_vars=None):
        self.root_dir = root_dir
        self.roles_dir = os.path.join(self.root_dir, "roles")
        self.base_name = base_name
        self.default_image = default_image
        self.extra_vars = extra_vars or {}

    def check_role_exists(self, role):
        """ Ensure that a role exists. """
        role_path = os.path.join(self.roles_dir, role)
        if not os.path.isdir(role_path):
            raise TestException(
                "Could not find ansible role directory at %r" % role_path
            )

    def get_docker_name(self, role, image=None):
        """ Given a role, get the itended docker image/container name. """
        image, _, tag = (image or self.default_image).partition(":")
        parts = [self.base_name, image]
        if tag:
            parts.append(tag)
        parts.append(role)
        return "-".join(parts)

    def get_inventory(self, role=None):
        """ Get /etc/ansible/hosts contents for a role. """
        inventory_str = "[local]\nlocalhost ansible_connection=local\n"

        groups = ["docker", self.base_name]
        if role:
            groups.append(self.get_docker_name(role))
        for group in groups:
            inventory_str += "[%s:children]\nlocal\n" % group
        return inventory_str

    def build_dockerfile(self, dockerfile, tag):
        """ Build a docker container from a Dockerfile string. """
        subprocess.run(
            ["docker", "build", "--tag", tag, "--file=-", self.root_dir],
            input=dockerfile.encode("ascii"),
            check=True,
        )

    def get_core_dockerfile(self, image):
        """ Get the core Dockerfile for an image as a string. """
        distro = image.split(":")[0]

        # we can use the same dockerfile for both of these
        if distro == "ubuntu":
            distro = "debian"

        dockerfile_path = os.path.join(
            os.path.dirname(__file__), "docker", "dockerfile-%s.tmpl" % distro
        )

        if not os.path.exists(dockerfile_path):
            raise ValueError("distro not supported: %s" % distro)

        with open(dockerfile_path) as fh:
            template = fh.read()

        return template.format(
            image=image,
            hosts=self.get_inventory().replace("\n", "\\n"),
            apply_role_playbook='[{ hosts: localhost, roles: ["{{ adroit_role }}"] }]',
        )

    def build_core_image(self, pull=False, image=None):
        """ Build the core image. """
        image = image or self.default_image
        if pull:
            subprocess.run(["docker", "pull", image], check=True)
        dockerfile = self.get_core_dockerfile(image)
        self.build_dockerfile(dockerfile, self.get_docker_name("core"))

    def get_base_dockerfile(self):
        """ Get the Dockerfile for the base image. """
        dockerfile_path = os.path.join(
            os.path.dirname(__file__), "docker", "dockerfile-base.tmpl"
        )
        with open(dockerfile_path) as fh:
            template = fh.read()
        return template.format(core_image=self.get_docker_name("core"))

    def build_base_image(self):
        """ Build the base image, which is the core image + the base role. """
        container = self.start_container("base", self.get_docker_name("core"))
        self.run_test_role_playbook("base", container, check_idempotency=False)
        subprocess.run(
            ["docker", "commit", container, self.get_docker_name("base")], check=True
        )
        subprocess.run(["docker", "rm", "-f", container], check=True)

    def start_container(self, role, image):
        """ Start a container for a role. """
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
            self._prepare_container(container, role)
        except:
            subprocess.run(["docker", "rm", "-f", container], check=True)
            raise

        return container

    def _prepare_container(self, container, role):
        inventory_path = "/tmp/inventory-%s" % role
        with open(inventory_path, "w+") as fh:
            fh.write(self.get_inventory(role))
        subprocess.run(
            ["docker", "cp", inventory_path, "%s:/etc/ansible/hosts" % container],
            check=True,
        )
        os.unlink(inventory_path)

        test_vars_path = "/etc/ansible/roles/%s/testing/test_vars.yml" % role
        ln_test_vars = (
            "if [ -e {test_vars_path} ]; then "
            "ln -sf {test_vars_path} /etc/ansible/group_vars/all/; fi"
        ).format(test_vars_path=test_vars_path)
        subprocess.run(
            ["docker", "exec", container, "sh", "-c", ln_test_vars], check=True
        )

    def test_role(self, role):
        """ Start a container and test a role in it. """
        container = None
        try:
            image = self.get_docker_name("base")
            container = self.start_container(role, image)

            # for the base image, this step has already been ran
            if role != "base":
                self.run_test_role_playbook(role, container, check_idempotency=False)

            self.run_test_role_playbook(role, container, check_idempotency=True)

            subprocess.run(["docker", "rm", "-f", container], check=True)
        except Exception as exc:
            if container:
                subprocess.run(["docker", "pause", container], check=True)
            raise TestFailure.from_container_id(container) from exc

    def run_test_role_playbook(self, role, container, check_idempotency=False):
        """ Run playbooks + tests for a role in a running container. """
        cmd = [
            "docker",
            "exec",
            "-t",
            container,
            "ansible-playbook",
            "/etc/ansible/apply-role.yml",
            "-e",
            "adroit_role=%s" % role,
        ]
        for key, val in self.extra_vars.items():
            cmd += ["-e", "%s=%s" % (key, val)]
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
            raise TestException(get_fail_msg(container))
        if check_idempotency and changes > 0:
            msg = "Expected no changes, but found changes=%d in output!\n%s" % (
                changes,
                get_container_paused_msg(container),
            )
            raise TestException(msg)
