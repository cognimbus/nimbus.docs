Local Agent guide
==================

Installing the agent without internet connectivity
-------------------------------------------------
* Place nimbusd in /bin/
* Create a path /etc/nimbus/
* copy the following to a nimbus.json config file in /etc/nimbus/nimbus.json
  - Change "password" admin to a strong password
  - Provide root only permissions 

.. code-block:: 

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

* Run /bin/nimbusd as a daemon using chron or as a service in your Linux 

Desktop app for local connectivity 
-------------------------------------------------

Browser connectivity 
-------------------------------------------------
