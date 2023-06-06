.. _`Create and deploy configuration`:

Create and deploy configuration
===========================

Overview
--------

The Nimbus **Configuration** tool is used to create a complete specification for a robot type's functionality, defined by its platform, sensors, device drivers, and algorithms. Nimbus configurations can be deployed to a single robot or an entire fleet.

The procedure for configuring a robot requires:

- Specifying and adding devices (robotic platform and sensors)
- Specifying and attaching components (device drivers and algorithms)
- Connecting data streams between component inputs and outputs
- Deploying the configuration to a robot or fleet

Creating a New Configuration
-----------------------------
1. In the Side Bar, click **Configurations**.
2. Click **CREATE NEW CONFIGURATION**.
3. The **Add Configuration** screen is displayed.
4. Set the Configuration name.
5. Click **ADD**.


Adding a robot/sensor
----------------------

1. In the **Robot editor** tab click on the + button.
2. The **Select device** menu is displayed.
3. Enter the name of the robot/sensor or Choose a category and search your robot/sensor from the list.
4. Click on the robot/sensor.
5. Click **CONFIRM**.
6. Place your robot/sensor in the desired position.


Adding components and data streams
----------------------------------

After the robot and sensor devices are specified, it is necessary to attach components (device drivers and algorithms).
When created, components appear as graphical terminal block objects in the **Components** area.

Adding a platform driver
------------------------

1. In the **Component editor** graphical area, click the + button.
2. Enter the name of the robot driver or Choose the robot category and search your robot driver from the list.
3. From the list, select the required driver corresponding to the previously specified robot.
4. From the list, select the required build version.
5. Click **CONFIRM**.
   In the **Components** graphical area, labeled terminal blocks, showing the platform driver's inputs and outputs, appear.
6. In the platform driver terminal block, click the |cogwheel| icon.
7. From the **Required devices** drop-down list, in the **Parameters** window, select the robot platform.
8. Click **Close**.

 

Adding a sensor driver
----------------------

1. In the **Component editor** graphical area, click the + button.
2. Enter the name of the sensor driver or Choose the Drivers category and search your sensor from the list.
3. From the list, select the required sensor driver type.
4. From the list, select the required build version and click **ADD COMPONENT**.
   In the **Components** graphical area, a labeled terminal block, showing the sensor driver outputs, appears.
5. In the sensor driver terminal block, click the |cogwheel| icon.
6. From the **Required devices** drop-down list in the **Parameters** window, select the connected imaging device.
7. Click **Close**.

.. |cogwheel| image:: https://raw.githubusercontent.com/AriYakir/nimbus.docs/main/nimbus-assets/Parameters_control_cogwheel.PNG
   :width: 20%
   :alt: Parameter settings 

Adding an algorithm
-------------------

1. In the **Component editor** graphical area, click the + button.
2. Enter the name of the **Algorithms** or Choose the required algorithm category and search your algorithm from the list.
3. From the list, select the required build version and click **CONFIRM**.
   In the **Components** graphical area, a labeled terminal block, showing the algorithm's inputs and outputs, appears.
4. To modify algorithm parameters, in the terminal block, click **Advanced** and enter new parameter values.
5. Click **Save changes**.

Connecting data streams between components
----------------------------------------

To complete the configuration, data streams must be connected between the input and output terminals of the component blocks.

1. Place your cursor over a component output terminal.
   When it is correctly positioned, the cursor icon changes from a hand to crosshairs.
2. Drag the cursor to an input terminal on the component to be connected, releasing the cursor when the crosshairs icon appears.


**Note**

- When long-clicking with the crosshairs over an input or output terminal of a component, compatible terminals in other components are haloed in green.
- A terminal with a connected stream appears as a filled blue circle.
- Component boxes can be moved and rearranged within the graphical area by dragging with the cursor. Data stream connectors adjust automatically.

Additional actions
------------------

Providing a configuration description
------------------------------------

Including a brief description for your new configuration is optional but recommended if you intend to make the configuration public in the Nimbus Hub.

1. Near the configuration name, click the ! icon.
2. Enter the configuration description in the text box and click **submit**.
   The text box closes, and the description is displayed.

Making a configuration public or private
----------------------------------------

When you make a configuration public, it is visible in the Nimbus Hub.
1. click the |dots| icon.
2. Next to **Private Configuration**, click the slider switch .
   A **Configuration set to public** message is briefly displayed.
3. To revert to private, repeat the above procedure.

.. |dots| image:: https://raw.githubusercontent.com/AriYakir/nimbus.docs/main/nimbus-assets/dots_icon.png
   :width: 100px
   :alt: Parameter settings 

Deploying a configuration
-------------------------

A configuration can be deployed to an individual robot, or to the entire fleet.

1. In the **Configurations** screen, select a configuration.
2. Click **Deploy**.
3. Select the required **Version increment**.
4. From the **Deploy to** drop-down list, select **ROBOT** or **FLEET**.
5. From the **Robot name** or **Fleet name** drop-down list, select a robot or fleet and click **CONFIRM**.
   The message **Configuration has been deployed** is briefly displayed.
