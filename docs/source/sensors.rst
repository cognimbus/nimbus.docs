Sensors
===============================

Check out these awesome lidars

   .. image:: _static/img/sensors/olei2D.png 
      :width: 200px
      :target: #olei-2d-lidar
      :class: hover-popout

   .. image:: _static/img/sensors/olei3D.png
      :width: 200px
      :target: #olei-3d-lidar
      :class: hover-popout

   .. image:: _static/img/sensors/Velodyne_Puck-1.png
      :width: 200px
      :target: #velodyne
      :class: hover-popout

   .. image:: _static/img/sensors/lakibeam.png
      :width: 200px
      :target: #richbeam
      :class: hover-popout

.. _olei:

   .. raw:: html 

    <div class="image-link">
        <a href="sensors.html#olei-2d-lidar">
            <img src="_static/img/sensors/olei_logo.png" alt="Image description" />
        </a>
    </div>


Olei 2D Lidar
----------------------------
- LR-1BS is based on our proven 1B development platform to meet developed in the industrial and commercial industries for cost and size requirements. It can satisfy the vast majority need for mobile robots and automatic guided vehicles (AGV) for safe obstacle avoidance.
- LR-1BS is suitable for application needs in diferent industries, such as robotics, security and surveillance, industrial automation and smart logistics.
- You can test it using 

.. code-block:: bash
   :linenos:

    docker run -it --network=host cognimbus/olei-lidar-driver:foxy ros2 launch ros2_ouster ole2dv2_launch.py laser_frame:=laser lidar_ip:=192.168.1.100 computer_ip:=192.168.1.10 lidar_port:=2368 imu_port:=9866
   

Olei 3D Lidar
----------------------------
- LR-16F is a small size and multi-channel LiDAR developed by OLEI-Systems with proprietary technologies. LR-16F has 360°(Horizontal) and ±15°(Vertical) scanning angles, 100mdetection range. It is primarily designed for a variety of industrial autonomous applications such as AGV, Automatic Forklift, Patrol Robots, and Inspection Robots. It can also be used for other applications such as mobile mapping, 3D measurement etc.
- LR-16F LiDAR has undergone rigorous calibration, inspection and verifcation processes performed by professional laboratories.OLEI strives to provide reliable, high quality, rugged and robust sensor products to customers.
- You can test it using 
- 
.. code-block:: bash
   :linenos:

    docker run -it --network=host cognimbus/olei-lidar-driver:foxy ros2 launch ros2_ouster ole3dv2_launch.py laser_frame:=laser lidar_ip:=192.168.1.100 computer_ip:=192.168.1.10 lidar_port:=2368 imu_port:=9866


.. _velodyne:

   .. raw:: html 

    <div class="image-link">
        <a href="sensors.html#velodyne">
            <img src="_static/img/sensors/velodyne_logo.webp" alt="Image description" />
        </a>
    </div>

Velodyne Puck
----------------------------
- LR-16F is a small size and multi-channel LiDAR developed by OLEI-Systems with proprietary technologies. LR-16F has 360°(Horizontal) and ±15°(Vertical) scanning angles, 100mdetection range. It is primarily designed for a variety of industrial autonomous applications such as AGV, Automatic Forklift, Patrol Robots, and Inspection Robots. It can also be used for other applications such as mobile mapping, 3D measurement etc.
- LR-16F LiDAR has undergone rigorous calibration, inspection and verifcation processes performed by professional laboratories.OLEI strives to provide reliable, high quality, rugged and robust sensor products to customers.
- You can test it using 
- 
.. code-block:: bash
   :linenos:

   docker run -it --network=host cognimbus/velodyne-vlp-16 roslaunch velodyne_pointcloud VLP16_points.launch frame_id:=laser device_ip:=192.168.1.201 --screen

.. _richbeam:

   .. raw:: html 

    <div class="image-link">
        <a href="sensors.html#richbeam">
            <img src="_static/img/sensors/richbeam.png" alt="Image description" />
        </a>
    </div>

Lakibeam 
----------------------------
- With 70% reflectivity, the detection distance can reach 15 meters. dToF industrial single-line laser radar has a data sampling rate of up to 18 kHz (10 Hz), which is not affected by outdoor light environment. It is suitable for hotel lobby, supermarket, factory park and other scenes.

.. code-block:: bash
   :linenos:

   docker run -it --network=host cognimbus/ros1-richbeam-lakibeam-driver ros2 launch lakibeam1 lakibeam1_scan.launch.py inverted:=false hostip:=0.0.0.0 port:=2368 angle_offset:=0 scanfreq:=30 filter:=3 laser_enable:=true scan_range_start:=45 scan_range_stop:=315
