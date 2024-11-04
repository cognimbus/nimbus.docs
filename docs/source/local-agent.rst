Local Agent guide
==================

Installing the agent without internet connectivity
-------------------------------------------------
* Place nimbusd,nimbus in /bin/
* Create a path /etc/nimbus/
* Copy the following to a nimbus.json config file in /etc/nimbus/nimbus.json
 * Change "password" admin to a strong password
 * Save with root-only permissions 
 * Configure local ROS settings (such as ROS_DOMAIN_ID)

.. note::
    
  Nimbusd needs to be restarted to apply changes. If running as a service, use "nimbus system reload" to apply the changes


nimbus.json::

    {
      "apiKey": "",
      "server": "https://api.cognimbus.com",
      "password": "admin",
      "agentStatusInterval": 30,
      "platformInfoInterval": 30,
      "agentStatsInterval": 0,
      "logLimitDays": 5,
      "analyticsInterval": 0,
      "fileServer": "https://api.cognimbus.com/files/",
      "unsecure": false,
      "paths": {
        "nimbusConfig": "/etc/nimbus/nimbus.json",
        "nimbusHome": "/var/lib/nimbus",
        "nimbusRecordings": "/var/lib/nimbus/data/",
        "nimbusLogs": "/var/lib/nimbus/logs/",
        "nimbusData": "/var/lib/nimbus/data/"
      },
      "httpsProxy": "",
      "minLogLevel": "info",
      "logLimitSize": 1,
      "uploadLogToServer": true,
      "dockerAuths": [],
      "agentMetricsInterval": 5,
      "localEditMode": true,
      "localRosIp": "",
      "localRosMasterUri": "",
      "localRos2DomainId": 0
    }


Set agent as systemd Sevice 
------------------

* Create a service file, e.g., /etc/systemd/system/nimbusd.service:

.. code-block:: bash
   :linenos:
    
    [Unit]
    Description=Nimbus Daemon
    After=network.target

    [Service]
    ExecStart=/bin/nimbusd
    Restart=on-failure
    User=nimbus  # Replace with the appropriate user if necessary
    
    [Install]
    WantedBy=multi-user.target

How to Use
^^^^^^^^^^^

1. Save the file and reload the systemd daemon

.. code-block:: bash
   :linenos:

    sudo systemctl daemon-reload

2. Enable the service to start at boot

.. code-block:: bash
   :linenos:

    sudo systemctl enable nimbusd


3. Start the service

.. code-block:: bash
   :linenos:

    sudo systemctl start nimbusd




Set agent as chron Job 
------------------
If you prefer cron, use crontab for scheduling the job:

.. code-block:: bash
   :linenos:

    @reboot /bin/nimbusd

Add this line to your crontab using crontab -e to run /bin/nimbusd on system reboot.



Desktop app for local connectivity 
-------------------------------------------------

.. note::
    
  Experimental

.. _`Nimbus`: index.md
.. _`Nimbus Agent`:

   .. image:: _static/img/Tux.png
      :width: 100px
      :class: hover-popout

* Click here to download deb file -> `X86 Ubuntu linux <https://drive.google.com/file/d/1Lo0jd3TAH43GYRW4-qGltu6x8xfI_uw2/view?usp=drive_link>`_

Browser local connectivity 
-------------------------------------------------

* In your terminal use ifconfig to find your local IP (i.e. 172.28.78.216)
* Open the browser at https://172.28.78.216:19993 and insert your password configured in the nimbus.json file
