Simulation
==========

Cogniteam's Platform Simulation is designed to enable you to test
your robot behavioral configurations, without consuming cloud
resources. The Simulation is Unity-based and runs on your browser
(client side). The simulation communicates with Cogniteam's Agent,
whether it is deployed on your development PC for your convenience or
on your robot to test in a hardware-in-the-loop fashion. The virtual
environment feeds the robot sensor streams, the configuration serves
as the decision maker, and robot actions are applied in the virtual
environment, completing the sense-think-act cycle of the robot.

Let's explore the different features of the Simulation and how to use
them.

This is an overview of the Simulation Screen


.. image:: _static/img/media/image56.png
   :width: 6.5in
   :height: 3.65694in

Let's explore the menu on the left.

Tools Tab
----------

.. image:: _static/img/media/image57.png
    :width: 3.70833in
    :height: 2.76111in


Inside the Tools tab you can change the quality level of the Simulation to match your PC or robot's hardware capabilities.

.. image:: _static/img/media/image58.png
    :width: 3.70833in
    :height: 1.61389in

You can switch between Camera modes, the camera can follow the robot or you can switch to Free roaming / Top down view.

.. image:: _static/img/media/image59.png
    :width: 2.875in
    :height: 0.91667in

You can switch the rendering mode of the scene to **Data Mode**.
There you can see the data of the sensor instead of the 3D rendering.
This is particularly useful for seeing what the robot“sees” during
development / debug.

.. image:: _static/img/media/image60.png
    :width: 3.86389in
    :height: 0.85417in


.. image:: _static/img/media/image61.png
    :width: 3.24028in
    :height: 1.92778in

.. image:: _static/img/media/image62.png
    :width: 3.23889in
    :height: 1.92778inn

You can place a grid on the environment's ground / floor. This is
particularly useful for measuring sizes of items, different distances
and movements of the robot while debugging.

.. image:: _static/img/media/image63.png
    :width: 3.24028in
    :height: 1.21805in

.. image:: _static/img/media/image64.png
    :width: 2.75in
    :height: 1.86389in

You can manually edit the position of the robot. Click on the edit button next to the “Edit Platform Position” and just point where you want the robot to be

.. image:: _static/img/media/image65.png
    :width: 4.16667in
    :height: 2.34306in

Or you can reset the scene to its starting position by clicking the
Reset button next to the “Reset Scene”.


Devices Tab
-----------
In the Devices tab you can view information about the robot and sensors and modify settings regarding the outgoing streams.

.. image:: _static/img/media/image66.png
    :width: 3.6875in
    :height: 2.36389in

.. image:: _static/img/media/image67.png
    :width: 3.6875in
    :height: 5in

You can:

- view and edit the position and orientation of the sensor.
- change the Rate of stream and the stream name.
- enable or disable the output of a stream.
- Monitor a stream from the simulation by checking the “Display Data” checkbox.

  - You can also do it from the monitoring tab while the robot is in simulation mod


.. image:: _static/img/media/image68.png
   :width: 4.60417in
   :height: 2.58333in
 


Inventory Tab
--------------

You can add to the scene different items that we call “dropables”. These items can be static, e.g., a box, or dynamic, e.g., a person walking. You can choose (static or dynamic) items from our rich Inventory menu and edit their behavior. Just Choose an Item and place it in the environment anywhere you want.


.. image:: _static/img/media/image69.png
   :width: 2.36389in
   :height: 3.58333in

.. image:: _static/img/media/image70.png
    :width: 4.5625in
    :height: 2.5625in

For dynamic objects, you can also select the type of movement logic
you want between“Waypoints”, “Flow” or “Wander”. For instance, if we
choose the “Waypoints“ logic, we can set up points for a person to
travel.

.. image:: _static/img/media/image71.png
    :width: 4.60417in
    :height: 2.58333in


.. image:: _static/img/media/image72.png
    :width: 3.875in
    :height: 2.375in

.. image:: _static/img/media/image73.png
    :width: 3.875in
    :height: 2.375in

You can edit the speed of the person and start by clicking the
“Start” button.

.. image:: _static/img/media/image74.png
    :width: 4.34306in
    :height: 0.70833in

Another example, you can set up a static item and edit its mass:

.. image:: _static/img/media/image75.png
    :width: 4.00972in
    :height: 2.25in


Don't forget to save your modified configuration by clicking the save
icon. Now you can click the Simulate button to start your simulation.

In the popup window you'll need to input the PC / Robot IP.

.. image:: _static/img/media/image76.png
    :width: 3.72917in
    :height: 0.88472in

.. image:: _static/img/media/image77.png
    :width: 3.97917in
    :height: 3.0625in

You can choose a specific scene to start the simulation.

.. image:: _static/img/media/image78.png
    :width: 3.78194in
    :height: 3.22917in

A new tab will open displaying a connection between your robot/pc and
the simulation.

.. image:: _static/img/media/image79.png
    :width: 4.63472in
    :height: 2.61528in

Have fun!
