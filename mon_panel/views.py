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

from horizon import tables

from mon_panel import tables as mon_tables
from mon_panel.data import services as mock_services


class IndexView(tables.DataTableView):
    table_class = mon_tables.ServiceTable
    template_name = 'mon_panel/index.html'

    def get_data(self):
        services = mock_services.get_mock_data()
        return services
