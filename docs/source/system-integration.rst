Integration
========

Integrating a new Device / Robot into the system 
--------------------

Our agent is installed as a service on the edge device and subscribes/publishes data to ROS  

* For ROS1 noetic or ROS2 humble no code is needed. Our agent will be able to reflect all available topics from the robot automatically to the cloud
 * We support all of the standard ROS messages
 * For ROS2 we utilize RTI DDS  
 * We support a vast number of custom messages from our sensor partners 
 * Our solution team can help to add any non-standard messages in the system as part of our regular support
 * Other ROS versions are also supported but there might be a small number of cases where the standard message definition is not aligned
* Our agent can support streaming data from non-ROS sources 
 * Our agent knows how to stream data from and to CSV
 * We can create components to translate data to ROS. These components are deployed with the agent and managed by it. Past integrated examples are 
  * MQTT support for pole lights
  * RTSP support for IP cameras
  * Our solution team can help add native support for other protocols given a need

Accessing Data 
--------------------

Once an agent is installed its data can be accessed in many ways

No internet connectivity 
^^^^^^^^^^^^^^^^^^^^^^^^^^
* Terminal 
* GRPC (i.e. python)
* Browser (localhost/local IP)
* Dedicated desktop app 

With internet connectivity 
^^^^^^^^^^^^^^^^^^^^^^^^^^
* REST API
