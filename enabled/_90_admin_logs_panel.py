# The name of the panel to be added to HORIZON_CONFIG. Required.
PANEL = 'logs_panel'
# The name of the dashboard the PANEL associated with. Required.
PANEL_DASHBOARD = 'admin'
# The name of the panel group the PANEL is associated with.
PANEL_GROUP = 'tools_panel_group'

# Python panel class of the PANEL to be added.
ADD_PANEL = 'log_panel.panel.LogPanel'

ADD_INSTALLED_APPS = ['log_panel']
