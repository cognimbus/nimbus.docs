Integration
===========

System Integration
-------------------

The Cogniteam Cloud Platform agent is deployed as a service on the edge device, capable of subscribing and publishing data directly to ROS. It is designed to operate independently of ROS on the host and can function within a container environment.

* Cogniteam Cloud Platform agents utilize gRPC for cloud communication.
* WebRTC is supported for low-latency video transmission, operable locally and globally, including in network-isolated environments.
* The agents are optimized for load balancing, enhancing network performance, including the handling of Point Cloud data.

ROS-Based Systems
^^^^^^^^^^^^^^^^^

* For **ROS1 Noetic** and **ROS2 Humble**, no additional code is necessary. Our agent can automatically reflect all available topics from the robot to the cloud.
  * Supports all standard ROS messages.
  * Uses **RTI DDS** for ROS2.
  * Compatible with a wide range of custom messages from our sensor partners.
  * Our solutions team can assist with incorporating non-standard messages as part of our regular support.
  * Support is available for other ROS versions, though minor adjustments may be required if standard message definitions vary.

Non-ROS-Based Systems
^^^^^^^^^^^^^^^^^^^^^

* Cogniteam Cloud Platform agents can stream data from non-ROS sources.
  * The agent supports data streaming from and to CSV formats.
  * Our solutions team can provide custom components to convert data to ROS, deployed and managed by the agent. Examples of past integrations include:
    * **MQTT support** for pole lights.
    * **RTSP support** for IP cameras.
    * Our solutions team can extend native support to other protocols as needed.

Accessing Data
--------------

Once installed, data from an agent can be accessed through various methods:

No Internet Connectivity
^^^^^^^^^^^^^^^^^^^^^^^^

* Terminal access.
* gRPC (e.g., Python integration).
* `Dedicated desktop app <https://docs.cognimbus.com/en/latest/local-agent.html#desktop-app-for-local-connectivity>`_
* `Browser access (localhost/local IP) <https://docs.cognimbus.com/en/latest/local-agent.html#browser-local-connectivity>`_

With Internet Connectivity
^^^^^^^^^^^^^^^^^^^^^^^^^^

* `REST API <https://docs.cognimbus.com/en/latest/api-gateway.html#api-gateway>`_
