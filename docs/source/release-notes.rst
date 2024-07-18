.. _`Release notes`:

Release Notes
=============

Release 18/07/2024

.. collapse:: Preset viewing options
----------------------

   We allow for each preset to select whether it is viewable.

   Who can see and modify visibility or presets?
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Outside organization
   ^^^^^^^^^^^^^^^^^^^^

   Developer and Admin of a robot can see and modify presets.

   In Organization
   ^^^^^^^^^^^^^^^

   Admin, User in an organization (with Developer/Admin robot permissions).

   FYI
   ^^^

   We will also soon release the ability to set a preset as default!

.. collapse:: Video manipulation
------------------

   We now allow the user to set the video layout of the camera feed.

   We added settings for:
   - Flip horizontal
   - Flip vertical
   - Rotate 90/180/270

Monitoring page for fleets of robots
------------------------------------

   In the fleet page, we now added a monitoring tab, enabling to monitor multiple robots in the same fleet under one tab.

   How to use it?
   ~~~~~~~~~~~~~~
   1. Enter fleet page.
   2. Go to the monitoring tab.
   3. See an empty page with an add viewer button (same as on robot monitoring).
   4. Select a viewer.
   5. In the settings, you can now select the robot, above the stream selection.
   6. The viewer is added to the fleet monitoring page.

.. collapse:: Map viewer improvements (Center of map)
---------------------------------------

   In the monitoring page of the robot, Map Viewer (google map/GPS view), the initial center of the map is now determined in the following way:
   - Saved last received location from a stream (saved in browser), if not
   - The first GPS location received from the stream, if not
   - The location of the robot (IP-based, if available), if not
   - The middle of the ocean

.. collapse:: Map viewer improvements (viewing settings)
------------------------------------------

   We now moved map/satellite view toggle options to the viewer settings.

.. collapse:: Message template mechanism improvement
--------------------------------------

   Currently, we have two ways to get message templates from stream sources:
   - Via request of the message structure
   - Via reading the first message

   The problem: when the source publishes messages rarely or the stream source is an input, the second way doesn’t work. We now get the message template initiated both ways at the same time.

   Note: If the message field is an array, we will display a spinner next to the array field until a message arrives and the structure is resolved (with a real array or by timeout).

.. collapse:: Bug Fixes
---------

   Online/Offline
   ~~~~~~~~~~~~~~

   When scaling the system, some of the robots experienced disconnection from the cloud and were marked as offline although they reconnected to the new instances. This issue was fixed as part of addressing multiple backend instances.



