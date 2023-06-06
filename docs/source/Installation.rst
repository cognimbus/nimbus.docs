.. _`Connecting Your Robot to Nimbus`:

Connecting Your Robot to Nimbus
===============================

.. _`Nimbus`: index.md
.. _`Nimbus Agent`:


Connecting a Robot to Nimbus
----------------------------

Overview
~~~~~~~~

To manage and interact with a robot, the Nimbus agent must be installed.

The Nimbus agent:

- Connects robots to Nimbus cloud services
- Installs Nimbus system software and dependencies
- Installs and manages robot configurations (devices and components)
- Gathers platform data and monitors robot status
- Enables robots to be controlled from Nimbus

Install the Nimbus agent
~~~~~~~~~~~~~~~~~~~~~~~~

To create a new robot instance and install the Nimbus agent on your target platform (robot).

1. In the **MAIN** (navigation) pane, click **+ Add Robot**.

   Alternative: in the **Robots** screen, click **+ Create new robot**.

2. Enter a unique name for your new robot.

3. If you wish immediately to assign the new robot to a fleet, select a fleet from the drop-down list.

   If no fleet is selected or no fleets are available, the robot is assigned to the default fleet: **Private**.

4. Click **Advanced**.

5. Optional. From the **Configuration** drop-down list, select an existing configuration.

   The default is an empty configuration.

6. Enter a license key.

   If using the Nimbus free plan, from the **Free** license panel, click **APPLY**.

   **Note**: If you create more than 2 robots, a `purchased license`_ is required.

7. Click **+Create**.

   A new robot instance is created and assigned to the designated fleet.

   A Linux command, containing a unique API key, is displayed. This API key is also emailed to you.

8. Your new robot's name appears in the **All my robots** list.

9. To install the Nimbus agent, copy the displayed Linux command and execute it from a terminal connected to your robot.

   In the Navigation panel, under **ONLINE**, the robot's name is listed with a green indicator. This confirms connection to Nimbus. In the **Robots** screen, the ![ ](/nimbus-assets/Deployed_robot_icon.PNG "Deployed robot") icon appearing next to the robot's name also confirms that the robot is connected.

**Note**: To display the agent installation line, enter the command ``nimbus system link``.

.. _`purchased license`: https://www.cognimbus.com/pricing
