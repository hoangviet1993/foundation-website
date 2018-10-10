# Copyright 2018 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for processing error reports."""

from core.tests import app_engine_test_base

import main


class FrontendErrorHandlerTest(app_engine_test_base.AppEngineTestBase):
    """Backend integration tests for handling frontend errors."""

    def test_frontend_errors_are_logged(self):
        """Test logging is done once a POST request is processed."""

        errors_log = {
            'error': 'scope errors'
        }

        self.testapp.post_json(main.FRONTEND_ERROR_URL, errors_log)
        with self.assertLogs(None, level='INFO') as cm:
            self.testapp.post_json(main.FRONTEND_ERROR_URL, errors_log)
        self.assertEqual(cm.output, ['ERROR:root:Frontend error: scope errors'])