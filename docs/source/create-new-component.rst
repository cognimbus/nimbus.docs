.. _`Create new component`:

Create new component
======================

.. _`Nimbus`: index.md
.. _`Create new component`:


Adding Components
-----------------

Overview
~~~~~~~~

You can specify and create customized components (drivers and algorithms) for use in Nimbus. This procedure requires:

- Building a Docker image of the component and uploading it to the user's repository on Docker Hub
- Creating a JSON definition file for the Nimbus component
- Uploading the JSON definition file (and optionally, a visual of the component) to Nimbus

Create a Docker image for the component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prerequisites
~~~~~~~~~~~~~

Nimbus components (device drivers and algorithms) are initially developed and built as application code within ROS1, ROS2, or another robot software development framework of choice. To work within Nimbus, the native application code, its libraries, and dependencies need to be containerized by `Docker`_ (included during Nimbus system installation).

Frequently, the development and target platforms each have different processor operating systems (such as arm64, amd64). In such cases, it is necessary to `install`_ the Docker `buildx`_ CLI plug-in.

As of Docker version 1.13.0, Nimbus exploits Docker's experimental features. To enable this additional functionality, start the Docker daemon with the `--experimental` flag or enable the flag in the `/etc/docker/daemon.json` configuration file:

.. code-block:: json
   :linenos:

   {
    "experimental": true
   }

Create a Dockerfile
~~~~~~~~~~~~~~~~~~

A Dockerfile is a text-based list of commands for building a Docker container image of the native application code.

1. In your working directory, create a file named `Dockerfile` (without any file extension).

2. With a text editor, include these required parameters in the `Dockerfile`:
   - **FROM**: The directory path to the component's application code and dependencies
   - **COPY**: The source and destination directories for copying into the Docker image
   - **RUN**: A sequence of compile/build commands
   - **CMD**: Commands to run the application within the Docker container

An example Dockerfile structure, used by Nimbus, is shown below:

.. code-block:: bash
   :linenos:

   FROM ros:melodic
   COPY ./cogniteam_exploration cogniteam_exploration_ws/src/cogniteam_exploration
   COPY entrypoint.sh /entrypoint.sh
   RUN chmod +x /entrypoint.sh
   ENTRYPOINT [ "/entrypoint.sh" ]
   RUN apt-get update && apt-get install ros-melodic-angles -y && \
       apt-get install ros-melodic-image-geometry -y && \
       apt-get install ros-melodic-tf2 -y  && apt-get install ros-melodic-tf -y && \
       apt-get install ros-melodic-image-transport-plugins -y && \
       apt-get install ros-melodic-image-transport -y && \
       apt-get install ros-melodic-move-base-msgs -y && \
       apt-get install ros-melodic-actionlib-msgs && \
       apt-get install ros-melodic-cv-bridge -y && rm /var/lib/apt/lists/* -rf
   WORKDIR /cogniteam_exploration_ws/
   RUN . /opt/ros/melodic/setup.sh && catkin_make
   CMD  roslaunch exploration exploration.launch --screen

Refer to `here`_ for more details on how to construct a Dockerfile.

3. From a terminal, enter the following commands to build the Docker image:

.. code-block:: bash
   :linenos:

   cd path_of_Dockerfile
   docker buildx create --name <nameOfDockerImage>
   docker buildx use <nameOfDockerImage>
   docker run --privileged --rm tonistiigi/binfmt --install all
   docker buildx inspect --bootstrap

4. From a terminal, log in to your Docker Hub repository with the following command:

.. code-block:: bash
   :linenos:

   sudo docker login

5. To push the Docker image to your Docker Hub repository, from a terminal, enter the following command:

.. code-block:: bash
   :linenos:

   sudo docker buildx build --platform linux/arm64,linux/amd64 -t <nameOfDockerHubRepository>/nameOfDockerImage --push .

Create a component definition JSON file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After creating a Docker image for the new component and uploading it to Docker Hub, running the component within Nimbus requires a JSON file containing a definition of the component's parameters. An annotated template for a typical component definition JSON file is provided `here`_. This example JSON file can be easily modified and renamed for use in your Nimbus projects.

Add the new component to Nimbus Hub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. From the Side bar, click **Components**.
2. Click the Add component button. The **Add Component** screen opens.

   .. image:: https://raw.githubusercontent.com/AriYakir/nimbus.docs/main/nimbus-assets/add-component-screen.png
      :width: 80%
      :alt: Nimbus Hub

3. In the respective text boxes, enter the component's description and relevant tags.
   Optional: From the **Category** drop-down list, select a component category.

4. From the drop-down list, select a license type.
   **Note:** If the **Public** toggle is set, a warning **Please check the license** is displayed.

5. Click JSON upload button and select the component definition JSON file from the directory. The uploaded file's name appears next to the **Upload JSON** button.

6. **Optional:** To upload an image of the component, click **Upload Image**, select the file from the directory, and click **Open**.

   A thumbnail of the uploaded image appears in the **Add Component** pane, and an **Image updated** message is briefly displayed.

7. Use the slider button to select **Private** or **Public**.

   Selecting **Public** will publish the component to Nimbus Hub.

8. Click the **License** box and select a license type.

9. **Optional:** In the **Add tags** text box, add meaningful tag names.
   **Tip:** Providing tags can be useful for finding and grouping related components during a search of your Docker image repository.

10. Click Create button.
    The message **Component has been created** is briefly displayed at the bottom of the screen.

11. To view the newly created component, select **Components** from the Side bar.
    The new component's details appear at the top of the **Your components** list.

.. _Docker: https://www.docker.com
.. _install: https://docs.docker.com/buildx/working-with-buildx
.. _buildx: https://docs.docker.com/buildx/working-with-buildx
.. _here: https://docs.docker.com/
