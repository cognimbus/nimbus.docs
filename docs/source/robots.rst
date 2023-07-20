Robot platforms
===============================

Check out our partners robots

   .. image:: ../img/robots/rover/rover-mini.png
      :width: 200px
      :target: #rover
      :class: hover-popout

.. _rover:


----------------------------
.. image:: ../img/robots/Rover.png
   :width: 300px
   :target: https://roverrobotics.com/en-il

- Check out our ROS2 component for the `Rover Mini  <https://github.com/cognimbus/Nimbus.Library.Components.ROS2/tree/master/rover-mini-driver>`_
.. code-block:: bash
   :linenos:

   docker run -it --network=host --privileged -v /etc/udev/rules.d/:/etc/udev/rules.d/ cognimbus/rover-mini-driver:latest ros2 launch roverrobotics_driver mini.launch.py


----------------------------
