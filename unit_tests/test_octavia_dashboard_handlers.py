# Copyright 2016 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import print_function

import mock

import reactive.octavia_dashboard_handlers as handlers

import charms_openstack.test_utils as test_utils


class TestRegisteredHooks(test_utils.TestRegisteredHooks):

    def test_hooks(self):
        defaults = [
            'charm.installed',
            'config.changed',
            'update-status']
        hook_set = {
            'when': {
                'dashboard_available': (
                    'dashboard.available',),
            },
        }
        # test that the hooks were registered via the
        # reactive.barbican_handlers
        self.registered_hooks_test_helper(handlers, hook_set, defaults)


class TestOctaviaDashboardHandlers(test_utils.PatchHelper):

    def test_dashboard_available(self):
        self.patch_object(handlers.reactive, 'endpoint_from_flag')
        dashboard = mock.MagicMock()
        self.endpoint_from_flag.return_value = dashboard
        handlers.dashboard_available()
        self.endpoint_from_flag.assert_called_once_with('dashboard.available')
        dashboard.publish_plugin_info.assert_called_once_with(
            {'setting-one-key': 'value-one'}, 'priority')
