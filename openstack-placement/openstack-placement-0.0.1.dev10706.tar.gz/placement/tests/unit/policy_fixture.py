# Copyright 2012 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import fixtures
from oslo_policy import policy as oslo_policy

import placement.conf
from placement.conf import paths
from placement import policy as placement_policy

CONF = placement.conf.CONF


class PolicyFixture(fixtures.Fixture):
    """Load the default placement policy for tests."""
    def setUp(self):
        super(PolicyFixture, self).setUp()
        policy_file = paths.state_path_def('etc/nova/placement-policy.yaml')
        CONF.set_override('policy_file', policy_file, group='placement')
        placement_policy.reset()
        placement_policy.init()
        self.addCleanup(placement_policy.reset)

    @staticmethod
    def set_rules(rules, overwrite=True):
        """Set placement policy rules.

        .. note:: The rules must first be registered via the
                  Enforcer.register_defaults method.

        :param rules: dict of action=rule mappings to set
        :param overwrite: Whether to overwrite current rules or update them
                          with the new rules.
        """
        enforcer = placement_policy.get_enforcer()
        enforcer.set_rules(oslo_policy.Rules.from_dict(rules),
                           overwrite=overwrite)
