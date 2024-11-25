.. _`Release notes`:

Release Notes
=============


Release 24/11/2024
----------------------

Support for Azure SSO (Single Sign-on)
~~~~~~~
Azure Single Sign-On (SSO) is a feature provided by Azure Active Directory (Azure AD) that allows users to authenticate once and gain access to multiple applications and services without needing to log in again for each one

   .. image:: _static/img/release/sso.png
      :width: 300px
      :target: #rover
      :class: hover-popout

* In addition to Google SSO, Azure SSO is now also supported


Teleoperation viewer settings are now better!
~~~~~~~

* Improved Teleoperation Settings 
  * The viewer now offers a more seamless and user-friendly experience.
* Support for Joy Message Types
  * Users can now send Joy messages directly through the teleoperation viewer.
  * These messages are generated based on input from a connected physical joystick.

* Automatic Control Model Selection
  * There's no longer a need to manually select a movement control model (e.g., Ackermann or Twist).
  * The system automatically detects and applies the appropriate control model by inferring it from the incoming message type.

This update ensures smoother integration and better adaptability for a wide range of teleoperation setups.

More layer settings options in the 3D viewer
~~~~~~~

More coloring options for point clouds 

   .. image:: _static/img/release/Lidar1.png
      :width: 300px
      :target: #rover
      :class: hover-popout
   .. image:: _static/img/release/Lidar.png
      :width: 300px
      :target: #rover
      :class: hover-popout


Release 29/10/2024
----------------------

3D viewer layer options
~~~~~~~

Improved visualization for device/robot location and coloring options:
A location in 3D can be now visualized and colored. Visualization options include

* Arrow - a simple arrow-like icon with location and direction
* Icon - a selectable icon from a set of icons, direction is shown on the outer perimeter 
* Axis - 3D axis
* Device mesh -  A mesh, uploaded by the user or available in the hub

   .. image:: _static/img/release/3D-rgb1.png
      :width: 300px
      :target: #rover
      :class: hover-popout
   .. image:: _static/img/release/3D-rgb2.png
      :width: 300px
      :target: #rover
      :class: hover-popout

For position layers, we have now a new centering option 

* Clicking it once will keep the view centered
* Clicking it again will keep the view aligned with the position orientation  

   .. image:: _static/img/release/3D-c1.png
      :width: 200px
      :target: #rover
      :class: hover-popout
   .. image:: _static/img/release/3D-c2.png
      :width: 200px
      :target: #rover
      :class: hover-popout
   .. image:: _static/img/release/3D-c3.png
      :width: 200px
      :target: #rover
      :class: hover-popout

Marker editor in 3D viewer
~~~~~~~

Improved usage of markers in the 3D viewer

* In 3d viewer settings, it is now possible to set a stream for marker publishing
* If defined, a new button called “markers” will be enabled
* Once the “marker” button is clicked
 * An empty list below the button will be visible called makers, with options to add, download (JSON all markers), upload (same JSON for all markers), Toggle to see or hide (like layer), delete and a button to send all markers

    .. image:: _static/img/release/3D-markers.png
      :width: 400px
      :target: #rover
      :class: hover-popout


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

