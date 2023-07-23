Robot platforms
===============================

Check out these awesome robots

   .. image:: ../img/robots/rover/rover-mini.png
      :width: 100px
      :target: #rover
      :class: hover-popout

   .. image:: ../img/robots/leo/Leo.png
      :width: 100px
      :target: #leo
      :class: hover-popout


.. _rover:
Rover Mini 
----------------------------
   .. raw:: html
    <div class="image-link">
        <a href=":ref:`target_anchor`">
            <img src="../img/robots/Rover.png" alt="Image description" />
        </a>
    </div>



   .. image:: ../img/robots/Rover.png
      :width: 100px
      :target: #rover
      :class: hover-popout

- Check out our ROS2 component for the `Rover Mini  <https://github.com/cognimbus/Nimbus.Library.Components.ROS2/tree/master/rover-mini-driver>`_
- You can run it using 

.. code-block:: bash
   :linenos:

   docker run -it --network=host --privileged -v /etc/udev/rules.d/:/etc/udev/rules.d/ cognimbus/rover-mini-driver:latest ros2 launch roverrobotics_driver mini.launch.py


.. _leo:
Leo Rover 
----------------------------

 .. image:: ../img/robots/Leo.png
      :width: 100px
      :target: https://www.leorover.tech
      :class: hover-popout


- Check out `Leo Rover  <https://www.leorover.tech/>`_
