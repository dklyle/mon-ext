#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os

from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tabs

MAX_LOG_LINES = 200


class LogTab(tabs.Tab):
    def get_context_data(self, request):
        # anticipate error
        log = _('Unable to get log for %s service.') % self.name
        lines = []
        try:
            #log = "this is a test\nanother line"
            if os.path.isfile(self.log_filename):
                with open(self.log_filename, "r") as log_file:
                    lines = log_file.readlines()
            if not lines:
                # hack that doesn't work for zipped files, really only here
                # because the rotated Horizon log isn't zipped
                first_rot_log = self.log_filename + ".1"
                if os.path.isfile(first_rot_log):
                    with open(first_rot_log, "r") as log_file:
                        lines = log_file.readlines()
        except Exception:
            exceptions.handle(request, ignore=True)

        # only return the most recent result to keep browser responsive
        if len(lines) > MAX_LOG_LINES:
            log = ''.join(lines[-MAX_LOG_LINES:])
        elif lines:
            log = ''.join(lines)

        return {"service_log": log,
                "service_type": self.name}


class HorizonTab(LogTab):
    name = _("Dashboard")
    slug = "dash_logs"
    template_name = ("log_panel/_log.html")
    log_filename = "/var/log/apache2/horizon_error.log"


class NovaTab(LogTab):
    name = _("Compute")
    slug = "compute_logs"
    template_name = ("log_panel/_log.html")
    log_filename = ''
    preload = False


class CinderTab(LogTab):
    name = _("Volume")
    slug = "volume_logs"
    template_name = ("log_panel/_log.html")
    log_filename = ''
    preload = False


class LogTabs(tabs.TabGroup):
    slug = "logs_tabs"
    tabs = (HorizonTab, NovaTab, CinderTab)
    sticky = True
