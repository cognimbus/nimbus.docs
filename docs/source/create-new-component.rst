.. _`Create new component`:

Create new component
======================

.. _`Nimbus`: index.md
.. _`Create new component`:


Overview
--------

You can specify and create customized components (drivers and algorithms) for use in Nimbus. This procedure requires:

- Building a Docker image of the component and uploading it to the user's repository on Docker Hub
- Creating a JSON definition file for the Nimbus component
- Uploading the JSON definition file (and optionally, a visual of the component) to Nimbus

Create a Docker image for the component
--------------------------------------

Prerequisites
-------------

Nimbus components (device drivers and algorithms) are initially developed and built as application code within ROS1, ROS2, or another robot software development framework of choice. To work within Nimbus, the native application code, its libraries, and dependencies need to be containerized by `Docker`_ (included during Nimbus system installation).

Frequently, the development and target platforms each have different processor operating systems (such as arm64, amd64). In such cases, it is necessary to `install`_ the Docker `buildx`_ CLI plug-in.

As of Docker version 1.13.0, Nimbus exploits Docker's experimental features. To enable this additional functionality, start the Docker daemon with the `--experimental` flag or enable the flag in the `/etc/docker/daemon.json` configuration file:

.. code-block:: json
   :linenos:

   {
    "experimental": true
   }

Create a Dockerfile
------------------

A Dockerfile is a text-based list of commands for building a Docker container image of the native application code.

1. In your working directory, create a file named `Dockerfile` (without any file extension).

2. With a text editor, include these required parameters in the `Dockerfile`:
   - **FROM**: The directory path to the component's application code and dependencies
   - **COPY**: The source and destination directories for copying into the Docker image
   - **RUN**: A sequence of compile/build commands
   - **CMD**: Commands to run the application within the Docker container

An example Dockerfile structure, used by Nimbus, is shown below:

.. code-block:: bash
   :linenos:

   FROM ros:melodic
   COPY ./cogniteam_exploration cogniteam_exploration_ws/src/cogniteam_exploration
   COPY entrypoint.sh /entrypoint.sh
   RUN chmod +x /entrypoint.sh
   ENTRYPOINT [ "/entrypoint.sh" ]
   RUN apt-get update && apt-get install ros-melodic-angles -y && \
       apt-get install ros-melodic-image-geometry -y && \
       apt-get install ros-melodic-tf2 -y  && apt-get install ros-melodic-tf -y && \
       apt-get install ros-melodic-image-transport-plugins -y && \
       apt-get install ros-melodic-image-transport -y && \
       apt-get install ros-melodic-move-base-msgs -y && \
       apt-get install ros-melodic-actionlib-msgs && \
       apt-get install ros-melodic-cv-bridge -y && rm /var/lib/apt/lists/* -rf
   WORKDIR /cogniteam_exploration_ws/
   RUN . /opt/ros/melodic/setup.sh && catkin_make
   CMD  roslaunch exploration exploration.launch --screen

Refer to `here`_ for more details on how to construct a Dockerfile.

3. From a terminal, enter the following commands to build the Docker image:

.. code-block:: bash
   :linenos:

   cd path_of_Dockerfile
   docker buildx create --name <nameOfDockerImage>
   docker buildx use <nameOfDockerImage>
   docker run --privileged --rm tonistiigi/binfmt --install all
   docker buildx inspect --bootstrap

4. From a terminal, log in to your Docker Hub repository with the following command:

.. code-block:: bash
   :linenos:

   sudo docker login

5. To push the Docker image to your Docker Hub repository, from a terminal, enter the following command:

.. code-block:: bash
   :linenos:

   sudo docker buildx build --platform linux/arm64,linux/amd64 -t <nameOfDockerHubRepository>/nameOfDockerImage --push .

Create a component definition JSON file
--------------------------------------

After creating a Docker image for the new component and uploading it to Docker Hub, running the component within Nimbus requires a JSON file containing a definition of the component's parameters. An annotated template for a typical component definition JSON file is provided `here`_. This example JSON file can be easily modified and renamed for use in your Nimbus projects.

.. code-block:: yaml
   :linenos:

   /**
    *  IMPORTANT When adapting this template for use in your application, please ensure to delete all comment fields (including this). Only valid JSON parameter:value pairs should remain!
    */   
   {
      "name": "nimbus/hector",          ### Required, Component name
      "type": "COMPONENT_TYPE_COMPONENT",## Defines the type of the component (component/driver) inputs: "COMPONENT_TYPE_COMPONENT"/"COMPONENT_TYPE_DRIVER"
      "className": "Ros1Component",     ### Rquired, Component class, inputs: "Ros1Component"/"Ros2Component"  ### check with agent about native components
      "instanceName": "",               ### Optinal, set by default to the component name
      "description": "2D laser scan mapping using Hector mapping algorithm",
      "start": "START_MODE_AUTO",       ### Optional, defines if the component will load automatically("START_MODE_AUTO") or manualy("START_MODE_MANUAL")
      "environment": {                  ### When using Docker, "environment" represents the Docker image of the component
         "name": "",                     ### For visualization on log messages
         "ipAddress": "",                ### Should not be changed and depends on the NetworkHost field    ###consider to remove
         "state": "ENVIRONMENT_STATE_UNLOADED", ### Generated automatically,                               ###consider to remove 
         "message": "",                  ### Defines at runtime, dont need to fill                         ###consider to remove
         "progress": 0,                  ### Progress of componenet loading, defined at runtime            ###consider to remove
         "requiredDevices": [],          ### Already filled at the json and overrided by it                ###consider to remove
         "ports": [],                    ### Defined by the device port in device class                    ###consider to remove
         "hostIpAddress": "",            ### Also depends on network host field                            ###consider to remove
         "variables": [                  ### Optional, Linux bash variables
         "name=value"
         ],
         "dockerInfo": {
         "image": "hector1:latest",    ### Sets the repository name and image name inside Docker hub
         "commands": [                 ### Used to pass parameters to the component Docker container when it is launched
            "roslaunch",
            "hector_mapping",
            "hector_mapping.launch",
            "map_resolution:=${map_resolution}",
            "map_size:=${map_size}",
            "base_frame:=${base_frame}"
         ],
         "privileged": true,             ### Allows Docker permission to read and write to all devices on the robot computer.
         "gpu": false,                   ### Allows Docker acccess to the the device's GPU
         "networkHost": false,           ### Allows Docker access to host's networking namespace
         "binds": [                      ### Can be used to mount directory/device on the host machine to the Docker container
         {
            "source": "/dev/video0",    ### Location of the device/folder at the host 
            "target": "/dev/video0"     ### Target location at the Docker container
         }
         ],
         "user": ""                      ### Sets the username or UID used and optionally the groupname or GID for the specified command.
         },
         "log": "",                      ### Lin (Probably defines at runtime, need to check)
         "convertedCommands": "",        ### Visaulization for nimbus comp, not rellevant to user
         "onExit": "IGNORE"              ### Check if relevant!!
      },
      "parameters": {                   ### Parameters passed to the launch file (actual parameter names depend
                                       ### on the particular component).
         "parameters": [
         {
            "name": "map_resolution",   ### Parameter name. Must be the same as in the "commands" section, above
            "description": "",          ### Optional
            "category": "Static",       ### Dont need to change
            "node": "",                 ### Lin
            "doubleValue": 0.1          ### Parameter data type
         },
         {
            "name": "map_string",
            "description": "",
            "category": "",
            "node": "",
            "stringValue": "string-value"
         },
         {
            "name": "int_param",
            "description": "",
            "category": "",
            "node": "",
            "integerValue": 1
         },
         {
            "name": "bool_param",
            "description": "",
            "category": "",
            "node": "",
            "booleanValue": "true"
         }
         ]
      },
      ### In this section, the parameters represent messages in the Nimbus format that can enter and exit the component.
      ### Nimbus messages viewed on Nimbus web are equivalent to ROS messages published between components.
      "streams": {
         "inputStreams": [
         {
            "name": "scan",                              ### Nimbus stream name
            "type": "",                                  ### Fills automatically when ros topic is defined, otherwise needs to be defined (ROS message type)
            "description": "",                           
            "streamMode": "STREAM_MODE_TOPIC",           ### Defines stream type (topic/service) inputs: "STREAM_MODE_TOPIC"/"STREAM_MODE_SERVICE"
            # are we still support this?
            "cloud": {
               "id": "123",
            "download_policy": {
                     "min_download_interval": "10000"
                     }
            },
            "ros_topic": {
               "topic": "/scan",                          ### The topic name used inside the ROS workspace
               "type": "Messages.sensor_msgs.LaserScan",  ### ROS message stream type
               "qosProfile": ""                           ### ROS2 parameter, documentation: https://docs.ros.org/en/humble/Concepts/About-Quality-of-Service-Settings.html
                                                         ### Check if we're taking this parameter in count
            },
         "latched": false,                              ### If set to true, saves the last published message
         "maxRate": 0,                                  ### Defines the component's max publish rate from the agent to the backend   ### max rate should be defined by us and not by user!
         "expectedRate": 0                              ### Seems that this parameter doenst do anything       ###check
         }
         ],
         "outputStreams": [
         {
            "name": "map",
            "type": "",
            "description": "",
            "streamMode": "STREAM_MODE_TOPIC",
            "ros_topic": {
               "topic": "/map",
               "type": "Messages.nav_msgs.OccupancyGrid",
               "qosProfile": ""                          
            },
         "latched": false,
         "maxRate": 0,
         "expectedRate": 0
         },
         ]
      },
      ### This section allows the component to view all devices using other components.
      ### Using the ROS tf package, Nimbus maintains the relationship between the coordinate frames of connected
      ### devices and the platform's base frame (e.g., base_link).
      "ros": {
         "base_frame": "base_link",  ### Platform's base frame
         "rate": 10.0,               ### rate of TF meseeages publish
         "publishTfDevices":true,    ### ???
         "rosMasterUri": "",         ### Equals to: export ROS_MASTER_URI=http://ip:11311 command
         "rosIp": "",                ### Equals to: export ROS_IP=ip command
         "autoDetectIp": false       ### ????
      }
   }
   ##### Additional parameters
      "inputStreams": [
         {
            "name": "odom",
            "type": "Nimbus.Core.Messages.Ros1.Messages.nav_msgs.Odometry", ### "type" can be the Odometry stream or Pose stream.
            "ros_tf": {  ,                          ###  Transforms the input Odometry stream to the reference frame inside the component.
               "base_frame": "odom",
               "child_frame": "base_link",
               "rate": 10.0
            }
         }
         ],
      "outputStreams": [
         {
            "name": "robot_pose",
            "type": "Messages.geometry_msgs.Pose",  ### "type" can be Odometry stream or Pose stream
            "ros_tf": {                             ### Transforms the tf output stream of the component to the reference frame
               "base_frame": "map",                  ### Of the robot pose.
               "child_frame": "base_link",
               "rate": 10.0
            }
         }
         ],
   ### The section is used for configuring the component to access a particular device.
   ### the device is identified by "productId" and "vendorId"
   "requiredDevices": [
         {
         "name": "laser",                    ### Device name
         "info": {
            "type": "USB_PORT_TYPE_SERIAL",   ### Device type
            "productId": "ea60",              ### Device product id
            "vendorId": "10c4",               ### Device vendor id
            "revision": "",
            "serial": "",
            "vendorName": "",
            "productName": "",
            "attributes": {},
            "ports": [],
            "id": ""
         },
         "attachedDevice": {
         },
         "mountAs": "/dev/ttyUSB0"           ### Used by Docker to launch the device driver file
         }
      ]
   #########################################################
   ### OPTION FOR RUNNING ROS COMPONENTS WITHOUT DOCKER ####
   #########################################################
   ### Using the modified "environment" and "parameters" sections, below, you can run a component as a native ROS process.
   ### without the need to dockerize. This requires ROS to be installed on the robot's computer.
   ###
   ### Substitute this "environment" section in the above script when using a local component (ROS without docker):
   {
      "environment": {
         "rosLocalInfo": {
            "PackageName": "hector_mapping",          ### The name of the package that containes the launch file we want to execute
            "launchFile": "mapping_default.launch",   ### The name of the launch file that we want to execute
            "rosVersion": "",                         ### The ros version that installed on the robot's computer
            "dependencies": [],
            "workspaceSetup": "/opt/ros/melodic/setup.bash",  ### The full path of the setup.bash file which is located in the workspace that we want to "source"
            "required": true,
            "arguments": {}
         },
      "parameters": {
         "parameters": [
         {
            "name": "ros_ip",               ### The IP address of the computer or network on which ROS is running
            "stringValue": "192.168.1.32"
         },
         {
            "name": "ros_master_uri",       ### The IP address set to the XML-RPC URI of the ROS Master
            "stringValue": "http://192.168.1.32:11311"
         }
         ]
      },
~~~

Add the new component to Nimbus Hub
----------------------------------

1. From the Side bar, click **Components**.
2. Click the Add component button. The **Add Component** screen opens.

   .. image:: https://raw.githubusercontent.com/AriYakir/nimbus.docs/main/nimbus-assets/add-component-screen.png
      :width: 80%
      :alt: Nimbus Hub

3. In the respective text boxes, enter the component's description and relevant tags.
   Optional: From the **Category** drop-down list, select a component category.

4. From the drop-down list, select a license type.
   **Note:** If the **Public** toggle is set, a warning **Please check the license** is displayed.

5. Click JSON upload button and select the component definition JSON file from the directory. The uploaded file's name appears next to the **Upload JSON** button.

6. **Optional:** To upload an image of the component, click **Upload Image**, select the file from the directory, and click **Open**.

   A thumbnail of the uploaded image appears in the **Add Component** pane, and an **Image updated** message is briefly displayed.

7. Use the slider button to select **Private** or **Public**.

   Selecting **Public** will publish the component to Nimbus Hub.

8. Click the **License** box and select a license type.

9. **Optional:** In the **Add tags** text box, add meaningful tag names.
   **Tip:** Providing tags can be useful for finding and grouping related components during a search of your Docker image repository.

10. Click Create button.
    The message **Component has been created** is briefly displayed at the bottom of the screen.

11. To view the newly created component, select **Components** from the Side bar.
    The new component's details appear at the top of the **Your components** list.

.. _Docker: https://www.docker.com
.. _install: https://docs.docker.com/buildx/working-with-buildx
.. _buildx: https://docs.docker.com/buildx/working-with-buildx
.. _here: https://docs.docker.com/
