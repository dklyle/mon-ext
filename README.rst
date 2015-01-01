=======
mon-ext
=======

mon-ext is written as an example for adding panel based extension to OpenStack
Dashboard. The content is not meant for real use. There is additional work
required to actually get this to actually communicate with your log sync and
monitoring solution.


Requirements
============

mon-ext is intended to use only on systems running Horizon


How to try this package
=======================

Use pip to install the package on the server running Horizon. Then either copy
or link the files in ``mon-ext/enabled`` to
``openstack_dashboard/local/enabled``. This step will cause the Horizon service
to pick up the extensions when it starts.

