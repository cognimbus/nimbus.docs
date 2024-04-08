Monitoring & Teleoperation Tab
==============================

.. image:: _static/img/media/image21.png
   :width: 6.5in
   :height: 3.79167in

This tab allows you to configure a dashboard that displays multiple views that monitor or control the robot. You can store and load different presets according to user specific needs or taste. When starting fresh, you have one view. You can assign a viewer to this view by clicking the button “add viewer”. You can also use the 3-dot menu to split the view vertically or horizontally and add other views until you are satisfied with the dashboard you have created. You can name your dashboard preset by clicking the pencil icon, or choose an existing preset from the dropdown menu on the left.

.. image:: _static/img/media/image22.png
   :width: 2.20833in
   :height: 1.6875in


When adding a viewer a popup window will appear, allowing you to
select the desired view type and the robot streams that serve as the
input for this view. Each tile depicts a different viewer type.
Clicking the tile will lead the table below to show the available
streams this viewer can display. These streams are either ROS1/2
streams (Topics) that natively run on your robot, or streams
available via the components (dockerized processes) you have
installed though Cogniteams Cloud Platform.

Let's go through each type of viewer.

Viewer Types
------------

.. image:: _static/img/media/image23.png
   :width: 6.5in
   :height: 4.21806in

Let's review each viewer:

.. image:: _static/img/media/image24.png
   :width: 1.63472in
   :height: 1.69861in

Any String / JSON / Numerical output can be displayed in a text format. This is particularly useful for development or debugging processes.

.. image:: _static/img/media/image25.png
   :width: 1.63472in
   :height: 1.69861in

Any stream of 3D data can be displayed, and also layered on top of a map view. This view is particularly useful for displaying the MAP a SLAM process is creating, and to overlay streams such as LIDAR, Point-Cloud, and any other ROS-based Markers available in tools such as RVIZ. 
In addition to viewing the different 3D streams, this viewer also allows you to send navigation commands to the robot. We'll explore these features next.

.. image:: _static/img/media/image26.png
   :width: 1.63472in
   :height: 1.69861in

Use this viewer to display any camera views such as raw streams, compressed streams, left and right views of a stereoscopic camera etc.
You are also able to select the protocol (e.g., WebRTC) and other display configurations to make your viewing experience as smooth as needed for your operations.
As an operator, this type of view is very useful to investigate what the robot is facing.

.. image:: _static/img/media/image27.png
   :width: 1.63472in
   :height: 1.69861in

Similarly to the video viewer, this viewer can display video streams. However, this viewer is also equipped with a virtual joystick, through which you can remotely control the movement of your robot.
You can configure the movement model (e.g., Ackermann / Twist) and assign the robot's input stream that receives these commands.

Data charts:
Area, Bar, Line, Scatter, and Progress Bar

Use the desired chart type to display any data stream you wish your robot to output. It is particularly useful for displaying different ad-hoc KPIs or analytical data your robot collects.

.. image:: _static/img/media/image28.png
   :width: 1.63472in
   :height: 1.69861in

If your robot carries a GPS or other means of reporting its global location then you can use this viewer to display where your robot is located on the global map.

.. image:: _static/img/media/image29.png
   :width: 1.63472in
   :height: 1.69861in

Any particular measurement you would like to display? Whether its speed, acceleration, heading, battery, or any other single value you wish to monitor - this is the viewer for you.

.. image:: _static/img/media/image30.png
   :width: 1.63472in
   :height: 1.69861in

Last but not least is the Buttons viewer in which you can create as many buttons as you wish, and assign each one a different command to be written to a ROS topic. 
This is particularly useful for emergency stops, going to a certain location such as the charging station, etc.
Assign useful commands that are just one click away. 


Each viewer can be configured by selecting the “settings” option in
the 3-dot menu in the top right corner of the view.

Let's go through the different configurations.

**Configuring the Text Viewer**

This is a simple viewer. As such you can only configure the title of the viewer.

.. image:: _static/img/media/image31.png
   :width: 3.50972in
   :height: 2.13472in

This option is available in every viewer settings.

**Configuring the 3D Viewer**

.. image:: _static/img/media/image32.png
   :width: 3.13611in 
   :height: 4.78194in

As mentioned above, this viewer allows you to overlay different layers (e.g., LIDAR, Point-Cloud) on top of a SLAM produced map, and also to send navigation commands to the robot by selecting waypoints across the map.

You can define:

- the stream from which the initial position will be taken as an input. 
- The stream to which goals are sent
- The stream to which waypoints are sent as a route
- Layers you wish to display on top of the map
  
  - Use the “add layer” button to add new layers
  - You can select one from the list of available layers that will be displayed in a popup window.

You can edit each layer:

- Choose to display it or not using the toggle slider
- Delete it by clicking the trashcan icon
- Edit the layer's settings by clicking the gear icon

  - Sometimes you need to define the stream from which a map offset can be read. 
  - This offset is used to align the layer with the map.
  - Note: In the near future, Cogniteam will support ROS TFs 

You can use the top buttons to set an initial position, a new goal or a path. Simply click on the map where you want the robot to go.


.. image:: _static/img/media/image33.png
   :width: 4.15694in
   :height: 2in


**Configuring the Video Viewer**

.. image:: _static/img/media/image34.png
   :width: 2.64583in
   :height: 1.81111in

Currently, our platform supports 2 different protocols you can select to display your video feed: WebRTC and gRPC.
You can read more about these protocols and how they may affect your experience with the robot in our blog post `here <https://cogniteam.com/cloud-based-teleoperation-in-robotics/>`_.

**Configuring the Teleoperation Viewer**

.. image:: _static/img/media/image35.png
   :width: 2.64583in
   :height: 5.9375in

The Teleoperation viewer configuration also allows you to choose between WebRTC and gRPC protocols. However it also allows you to configure how the joystick should control the movement of your robot.

You can choose the following:
- video feed just as in the video viewer.
- the joystick stream to which the movement of the virtual joystick will be written. 
- The frequency (Hz) joystick commands will be sent
- The steering model - Twist or Ackermann
- Linear and angular velocity parameters.

Check the “auto repeat” checkbox to lock the robot in its place by sending a continuous stream of 0s.
Additionally, if your robot possesses a GPS you can set the GPS stream from which the location of the robot will be read.


**Configuring a Chart Viewer or a Single Metric**

All the charts are defined with a stream source, MIN and MAX values, and the data variables to display in the chart.

.. image:: _static/img/media/image36.png
   :width: 3.04167in
   :height: 2.625in


**Configuring the Buttons Viewer**

.. image:: _static/img/media/image37.png
   :width: 2.875in
   :height: 4.77083in

Add buttons by clicking the “Add Action” button
choose the 
- stream source the receives the button command
- The name of the button
- The rate in which the command is sent
- The Deadline (ms) after which the command is aborted
- The color of the button
- The text to be written to the stream upon clicking the button
