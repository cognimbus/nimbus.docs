Robot platforms
===============================

Check out these awesome robots

   .. image:: _static/img/robots/rover/rover-mini.png
      :width: 200px
      :target: #rover
      :class: hover-popout

   .. image:: _static/img/robots/leo/Leo.png
      :width: 200px
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

- Upgrade Your Project with Rover Robotics' Cutting-Edge Mobile Robots 
- Rover mobile robots are designed to tackle a wide range of applications, from autonomous industrial inspection and mapping to security and surveillance. Explore our range of rugged and customizable robot platforms today and see how they can transform your operations.
- Check out Nimbus ROS2 component for the `Rover Mini  <https://github.com/cognimbus/Nimbus.Library.Components.ROS2/tree/master/rover-mini-driver>`_
- You can run it using 

.. code-block:: bash
   :linenos:

   docker run -it --network=host --privileged -v /etc/udev/rules.d/:/etc/udev/rules.d/ cognimbus/rover-mini-driver:latest ros2 launch roverrobotics_driver mini.launch.py

- Check out `Rover Mini  <https://roverrobotics.com/en-il/products/mini>`_
- To get started with your robot follow `these instructions  <https://roverrobotics.com/en-il/blogs/guides/getting-started-with-the-rover-pro>`_

.. _leo:

   .. raw:: html 

    <div class="image-link">
        <a href="robots.html#rover">
            <img src="_static/img/robots/Leo.png" alt="Image description" />
        </a>
    </div>

Leo Rover 
----------------------------

- Don’t reinvent the wheel every time you want to build a mobile robot. Focus on the functionalities that really matter.
- Leo Rover is a stable mobile robot you can deploy outdoors as it’s watertight and built tough enough for an extreme environment.
- It's an open-source outdoor mobile robot ready for your experimenting.
- Built on Ubuntu + ROS, waterproof, easy to maintain and easy to customize. With 24/7 support and foolproof warranty. Everything any curious mind needs to succeed.
- Check out `Leo Rover  <https://www.leorover.tech/>`_
- To get started with your robot follow `these instructions  <https://www.leorover.tech/documentation/getting-started>`_