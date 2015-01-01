#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from django.utils.translation import ugettext_lazy as _

from horizon import tables


def get_status(service):
    status = service['status']

    if status is "green":
        return _("OK")
    elif status is "yellow":
        return _("Warning")
    elif status is "red":
        return _("Error")

    return _("Unknown")

class ServiceTable(tables.DataTable):
    name = tables.Column("service",
                         verbose_name=_("Service Name"))
    alarms = tables.Column("alarms",
                           verbose_name=_("Alarm Count"))
    status = tables.Column(get_status,
                           verbose_name=_("Status"))


    def get_object_id(self, datum):
        return datum['id']

    class Meta:
        name = "service_monitoring"
        verbose_name = _("Service Status")
