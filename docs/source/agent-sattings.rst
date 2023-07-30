.. _`Agent settings`:

Agent settings
===========================

General
--------

- **Synchronize configuration** - enable the robot to synchronize with the last configuration from the cloud.

- **Enable records auto-delete** - automatically delete records from the robot after they have been uploaded to the cloud.

Log and Analytics
--------

- **Log level selection** - choose the log level to be published from the robot

  - TRACE

  - DEBUG

  - INFO [default]

  - WARNING

  - ERROR

- **Log limit by days** - if the log limit value is set to x, the agent keeps only logs from x days ago.

- **Log limit by size** - if the total log size is over the limit, the agent will remove the oldest logs until the total size is within the size limit value.
- **Enable/Disable uploading of logs to Nimbus cloud.**


Notifications
--------

**How do the notifications works?**

- Notification will be sent every time the value crosses the threshold.

- Re-notification will be sent as long as the value persists for over 160 minutes above the threshold

- Re-notifications will be sent no more than 3 times

- For built-in notifications (CPU, RAM, Disk) the value has to persist for at least 10 seconds

- Additional notifications can be configured by clicking  on the [+ADD] button and choosing condition for specific field inside the component’s stream.

Cloud Provider
--------
cloud provider for data upload

- Nimbus cloud - by default the cloud provider will set to Nimbus cloud. 

  - All the robot resources be automatically upload and saved on nimbus cloud

- AWS S3 - set as cloud provider a given AWS S3 bucket be setting the bucket details(access key,secret key,bucket name and region.

  - All the robot resources be automatically upload and saved on this bucket
