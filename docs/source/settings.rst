Settings
========

By now you saw how easy it is to view different robot streams and
send different remote actions from anywhere in the world. Now, it is
time to delve into more details as we explore the settings tab.

General Settings
----------------

In the **General Settings** frame you can tick the following
checkboxes:

**Synchronize configuration**
On restart pull the latest configuration version from the cloud and
update the robot. As you may recall, a configuration is the
behavioral graph that we promised to discuss later, and we will. If
you check this option, and indeed used our low-code configuration,
then whenever the robot restarts, it automatically checks if it has
the most updated version of its configuration, and downloads and
deploys it automatically if needed.

**Enable records auto-delete**
Delete records from the robot automatically after uploading them to
the cloud. Any records the robot may store can be uploaded to the
cloud once the robot is online. To save local storage, check this
option.

**Remap ROS topics**
Allow to automatically remap topics for better performance. ???

Cloud Provider
--------------

Next you can select a cloud provider. You can either choose Cogniteam's Cloud and let us take care of all the configurations, OR provide the necessary details for your AWS - S3 Cloud to store the information there.

.. image:: _static/img/media/image38.png
   :width: 3.19722in
   :height: 2.71944in

Notification Rules
------------------
Next you can set up the Notification rules.

.. image:: _static/img/media/image39.png
   :width: 3.10278in
   :height: 2.91667in


How do the notifications work?
- Notification will be sent every time the value crossed the threshold
- Re-notification will be sent as long as the value persists for over 160 min above the threshold
- Re-notifications will be sent no more than 3 times
- For built-in notifications (CPU, RAM, Disk) the value has to persist for at least 10 seconds

.. image:: _static/img/media/image39.png
   :width: 3.10278in
   :height: 2.91667in

Beside defining the threshold for CPU/ RAM/ Disk related notifications, you can set up stream monitoring rules.
Simply choose a stream source, a data field within this source, a conditional operator and a threshold value.
That's it. A notification will be sent whenever that threshold is crossed.


Log and Analytics
-----------------

.. image:: _static/img/media/image41.png
   :width: 5in
   :height: 3.36528in

You can choose the Log Level:

+-----------------------------------+-----------------------------------+
|    **Log Level**                  |    **Description**                |
+===================================+===================================+
|    Trace                          |    The TRACE log level is used to |
|                                   |    provide the most detailed and  |
|                                   |    fine-grained information about |
|                                   |    the execution flow of a        |
|                                   |    program, often used for        |
|                                   |    troubleshooting and debugging  |
|                                   |    purposes                       |
+-----------------------------------+-----------------------------------+
|    Debug                          |    DEBUG log level is utilized to |
|                                   |    output detailed information    |
|                                   |    that is helpful for debugging, |
|                                   |    typically providing insights   |
|                                   |    into the internal workings of  |
|                                   |    the software, but not          |
|                                   |    necessary for regular          |
|                                   |    operation.                     |
+-----------------------------------+-----------------------------------+
|    Info (default)                 |    INFO log level is used to      |
|                                   |    convey general, high-level     |
|                                   |    information about the          |
|                                   |    application's state or         |
|                                   |    important events, helping      |
|                                   |    users understand the system's  |
|                                   |    overall behavior.              |
+-----------------------------------+-----------------------------------+
|    Warning                        |    WARNING log level indicates    |
|                                   |    potential issues or situations |
|                                   |    that may lead to problems in   |
|                                   |    the future but do not          |
|                                   |    necessarily disrupt the        |
|                                   |    current operation. It serves   |
|                                   |    as a cautionary level.         |
+-----------------------------------+-----------------------------------+
|    Error                          |    ERROR log level signifies the  |
|                                   |    occurrence of a significant    |
|                                   |    problem or error during the    |
|                                   |    execution of the program,      |
|                                   |    indicating a failure in a      |
|                                   |    specific operation or          |
|                                   |    functionality. It usually      |
|                                   |    requires attention to address  |
|                                   |    and resolve the issue.         |
+-----------------------------------+-----------------------------------+


Use the sliders to limit the log file size (MB) and by days. You can
check the checkbox to enable the automatic upload of the collected
logs and analytics files to the cloud when the robot is online.

Docker Registry
---------------

You can set up the URL of your docker registry here.

Finally you can click on the “save changes” button at the bottom of
the screen to set any changes.

Next we are going to explore what are Cogniteam-Platform's Components
and configurations.
