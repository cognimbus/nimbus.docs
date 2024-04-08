Welcome to Cogniteam Cloud Platform documentation  
=======================================

The Unified Cloud Robotic Platform for monitoring, developing, deploying,
and managing a single or a fleet of robots

Contributing to this project
=======================================

- To add images 

```
  .. image:: ../img/<put images in this folder> 
      :width: i.e. 100px or 50%
      :target: <file name>.html#<anchor>, to make an image press redirect to that target
      :class: hover-popout for popping out, or without 
```

- To add a page to the side menu, add a link to it in the hidden toc tree at the end of index.rst
```
  .. toctree::
    :hidden:

    installation-guide
    robots
    sensors
    compute-platforms   
    create-new-component
    create-robot-configuration

```
