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

   .. raw:: html 

    <div class="image-link">
        <a href="robots.html#rover">
            <img src="_static/img/robots/Rover.png" alt="Image description" />
        </a>
    </div>

Rover Mini 
----------------------------

- Check out our ROS2 component for the `Rover Mini  <https://github.com/cognimbus/Nimbus.Library.Components.ROS2/tree/master/rover-mini-driver>`_
- You can run it using 

.. code-block:: bash
   :linenos:

   docker run -it --network=host --privileged -v /etc/udev/rules.d/:/etc/udev/rules.d/ cognimbus/rover-mini-driver:latest ros2 launch roverrobotics_driver mini.launch.py


.. _leo:

   .. raw:: html 

    <div class="image-link">
        <a href="robots.html#rover">
            <img src="_static/img/robots/Leo.png" alt="Image description" />
        </a>
    </div>

Leo Rover 
----------------------------

- Check out `Leo Rover  <https://www.leorover.tech/>`_
