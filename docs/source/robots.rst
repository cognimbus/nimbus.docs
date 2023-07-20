Robot platforms
===============================

Check out these awesome robots

   .. image:: ../img/robots/rover/rover-mini.png
      :width: 200px
      :target: #rover
      :class: hover-popout

   .. image:: ../img/robots/leo/Leo.png
      :width: 200px
      :target: #leo
      :class: hover-popout


.. _rover:

Rover Mini 
----------------------------

- Check out our ROS2 component for the `Rover Mini  <https://github.com/cognimbus/Nimbus.Library.Components.ROS2/tree/master/rover-mini-driver>`_
- You can run it using 

.. code-block:: bash
   :linenos:

   docker run -it --network=host --privileged -v /etc/udev/rules.d/:/etc/udev/rules.d/ cognimbus/rover-mini-driver:latest ros2 launch roverrobotics_driver mini.launch.py


Leo Rover 
----------------------------
- Check out `Leo Rover  <https://www.leorover.tech/>`_
