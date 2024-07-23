.. _`Api gateway`:

API Gateway
===========================

General
-------

Create a token in the admin profile when logged in to your organization on the Cogniteam Cloud Platform.

The base URL for the API is https://api.cognimbus.com/ApiGateway

Login to API
------------

Login with API token::

    POST /login

    Body: 
    {
        "usertoken": "..."
    }

    Description: Sends token to login.

    Returns: "bearer"

Robots Management
-----------------

List Robot IDs::

    GET /robots

    Header: 
    {
        "bearer": "..."
    }

    Description: Retrieves a list of all robot IDs.

    Response example:
    {
        "BasicData":
            [
            {"Id":"24029140-aa12-435a-a61f-f61ab1689580","Name":"test_prod1"},
            {"Id":"907809dc-d787-41d6-8e77-163b50784041","Name":"Lynx"},
            {"Id":"eee0b7f1-95f1-44e2-81b3-e671aa319861","Name":"AMR-8"}
            ]
        
    }

Get a Specific Robot's Details::

    GET /robot/{robotId}

    Description: Fetches details for a specific robot by ID.

    Response example:
    {
        "BasicData":{
        "Id":"eee0b7f1-95f1-44e2-81b3-e671aa319861",
        "Name":"AMR-8" },
        "IsOnline":true,"LastTimeSeen":"2024-07-15T10:07:24.613579Z"
        
    }

Robot Metrics
-------------

Get All Metrics (prod)::

    GET /robots/metrics

    Description: Fetches all available metrics.

    Example metrics: cpu, ram, etc.
    Reponse example:
    {
        "Metrics":
            [
            {"MetricType":1,"MetricName":"Cpu"},
            {"MetricType":2,"MetricName":"Ram"},
            {"MetricType":3,"MetricName":"Disk"},
            {"MetricType":4,"MetricName":"Battery"},
            {"MetricType":5,"MetricName":"Odometry"},
            {"MetricType":6,"MetricName":"Traffic"},
            {"MetricType":7,"MetricName":"Storage"},
            {"MetricType":8,"MetricName":"LicenseExpired"},
            {"MetricType":13,"MetricName":"AgentHw"},
            {"MetricType":14,"MetricName":"AgentSw"},
            {"MetricType":100,"MetricName":"Custom"}
            ]
    }

Get Robot Metrics (prod)::

    GET /robot/{robotId}/metric/{metricId}

    Description: Fetches specific metric for robot.

    Example metrics: cpu, ram, etc.

    Reponse example:
    {
        "BasicData":
            {"Id":"eee0b7f1-95f1-44e2-81b3-e671aa319861","Name":"AMR-8"},
        "Metric":
            {"$type":2,"Value":54,"Name":"DoubleMetric"}
    }

Streaming/Unary Data Management
-------------------------------

For streaming or sending commands directly to robots when robots are online. Rate limited to 1 second.

Get All Streams (prod)::

    GET /robot/{robotId}/streams

    Description: Retrieves a list of all available streams for a robot.

    Response fields: streamName, type

    Response example:
    "RobotStreams":
    [
        {
         "ComponentName":"nimbus/realsense-d435",
         "StreamName":"tf_base_link_to_camera_depth_optical_frame",
         "StreamType":"Nimbus.Messages.geometry_msgs.Pose",
         "Direction":"output",
         "StreamSourceType":1
        },
        {
         "ComponentName":"nimbus/ros2-legs-detector",
         "StreamName":"scan",
         "StreamType":"Nimbus.Messages.sensor_msgs.LaserScan",
         "Direction":"input",
         "StreamSourceType":1
        },
        {
         "ComponentName":"nimbus/ros2-legs-detector",
         "StreamName":"legs_visualization_marker",
         "StreamType":"Nimbus.Messages.visualization_msgs.Marker",
         "Direction":"output",
         "StreamSourceType":1
        }
   ]
}
    
Get Data from a Specific Stream (staging)::

    GET /robot/{robotId}/stream?componentName=<YOUR_COMPONENT_NAME>&streamName=<YOUR_STREAM_NAME>&source=<YOUR_STREAM_SOURCE>

    Description: Fetches data from a specific stream for a robot.

Notes
-----

- {robotId} and {streamName} are placeholders for the robot ID and stream name, respectively.
- For methods that modify data (e.g., POST), the body of the request should be detailed in the API documentation, specifying required fields and formats.
- Status Codes: Utilize HTTP status codes correctly to indicate the outcome of API calls, e.g., 200 OK, 404 Not Found, 400 Bad Request.
- For testing the API, it is possible to use the following example: curl -v --location --request GET <route> -H "Authorization: Bearer <token>" --header 'u;'
