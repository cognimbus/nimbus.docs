.. _`Release notes`:

Release Notes
=============
Release 19/08/2024
----------------------

CSV File option for chart viewers
~~~~~~~

    You will now be able to select a CSV file to be used as input for a viewer. This can be:
    
    * A file from the robot
    * A file from the resource page, for example, one that was created by the recording 
    
    Will be available to the following viewers
    
    * Line chart
    * Pie chart
    * Bar chart
    * Area chart
    * Radar chart
    * Scatter chart
    * progress chart



Local monitoring 
~~~~~~~
You will now be able to monitor data directly from the robot (no cloud involved) by knowing its IP, from the browser
  
   Setup
   ^^^^^^^^^^^^^^^^^^^^
   
     Assuming the robot has an agent installed 
     
    * Set password for local connectivity in nimbus.json (/etc/nimbus/nimbus.json)
    * See the local password by running “nimbus session local” on the robot 
    * See the local password in the robot overview (“local” button)
    * the URL is HTTPS://IP/monitoring
    * To enable editing the local monitoring page of the robot 
    * LOCAL_EDIT_MODE in nimbus.json should be set to true.
    * Specific ROS-related settings (domain ID etc…) can be set in nimbus.json



Release 18/07/2024
----------------------

Preset viewing options
~~~~~~~

   We allow for each preset to select whether it is viewable.

   Who can see and modify visibility or presets?
  ^^^^^^^^^^^^^^^^^^^^

   * Outside organization - Developer and Admin of a robot can see and modify presets.
   * In Organization - Admin, User in an organization (with Developer/Admin robot permissions).

   FYI
   ^^^

   We will also soon release the ability to set a preset as default!

Video manipulation
~~~~~~~

   We now allow the user to set the video layout of the camera feed.

   We added settings for:
   ^^^^^^^^^^^^^^^^^^^^

   * Flip horizontal
   * Flip vertical
   * Rotate 90/180/270

   .. image:: _static/img/release/2.png
      :width: 300px
      :target: #rover
      :class: hover-popout

Fleet monitoring page
~~~~~~~

   .. image:: _static/img/release/4.png
      :width: 400px
      :target: #rover
      :class: hover-popout

   In the fleet page, we added a monitoring tab, enabling the monitoring of multiple robots in the same fleet under one tab.

   How to use
   ^^^^^^^^^^^^^^^^^^^^

   1. Enter the fleet page.
   2. Go to the monitoring tab.
   3. See an empty page with an add viewer button (same as on robot monitoring).
   4. Select a viewer.
   5. In the settings, you can select the robot, above the stream selection.
   6. The viewer is added to the fleet monitoring page.

Map viewer improvements
~~~~~~~

   .. image:: _static/img/release/5.png
      :width: 300px
      :target: #rover
      :class: hover-popout

   In the monitoring page of the robot, Map Viewer (google map/GPS view), the initial center of the map is now determined in the following way:
   ^^^^^^^^^^^^^^^^^^^^

   * Saved last received location from a stream (saved in browser), if not
   * The first GPS location received from the stream, if not
   * The location of the robot (IP-based, if available), if not
   * The middle of the ocean
   * We moved map/satellite view toggle options to the viewer settings.

Message structure
~~~~~~~

   Currently, we have two ways to get message templates from stream sources:
    ^^^^^^^^^^^^^^^^^^^^

   * Via request of the message structure
   * Via reading the first message

   The problem: when the source publishes messages rarely or the stream source is input, the second way doesn’t work. We now get the message template initiated both ways.

   Note: If the message field is an array, we will display a spinner next to the array field until a message arrives and the structure is resolved (with a real array or by timeout).

Bug Fixes
~~~~~~~

   Online/Offline
   ^^^^^^^^^^^^^^^^^^^^

   When scaling the system, some of the robots experienced disconnection from the cloud and were marked offline, although they reconnected to the new instances. This issue was fixed by addressing multiple backend instances.

Older release notes 
----------------------

