.. _`Api gateway`:

API Gateway
===========================

General
-------

Create a token in the admin profile when logged in to your organization on the Cogniteam Cloud Platform.

The base URL for the API is https://api.cognimbus.com/apigateway

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
         "Authorization":"bearer": "..."
    }

    Description: Retrieves a list of all robot IDs.

    Response example:
    {
        "RobotDataList":
            [
            {"BasicData":{"Id":"38407b76-39c8-45e2-a89e-180d79dfa7a8","Name":"test1"},"IsOnline":true},
            {"BasicData":{"Id":"bfc681d5-3b16-4669-8930-b1b4756eb057","Name":"test2"},"IsOnline":true} 
            ]
    }   
 
Get a Specific Robot's Details::

    GET /robot/{robotId}

    Description: Fetches details for a specific robot by ID.

    Response example:
    {
        "RobotData": {
            "BasicData": {
                "Id": "459fe5a6-69d4-49a7-aecb-7537e6e4dfae",
                "Name": "AMR-Qualcomm-RB5"
            },
            "IsOnline": false
        },
        "FleetName": "2222222",
        "OrganizationName": "Cogniteam",
        "LastTimeSeen": "2024-09-29T13:07:27.211444Z",
        "Members": {
            "OrgAdmins": {
                "OrgAdmins": [
                    "user@cogniteam.com",
                    ...
                ]
            },
            "SharedUsers": {
                "UserPermissions": [
                    {
                        "UserId": "QA_user2@cogniteam.com",
                        "PermissionType": 1
                    },
                    ....
                ]
            }
        }
}

Robot Metrics
-------------

Get All Metrics::

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

Get Robot Metrics ::

    GET /robot/{robotId}/metric/{metricType}

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

Get All Streams ::

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
    
Get Data from a Specific Stream ::

    GET /robot/{robotId}/stream?componentName={ComponentName}&streamName={StreamName}&source={StreamSourceType}

    Description: Fetches data published on a stream, arriving from a robot (must be "output" direction).

Get empty message ::

    GET /streams/{streamType}/stream

    Description: Get the structure of the desired message by the type.

    { 
        "EmptyMessage": "{ \"header\": { \"seq\": 0, \"stamp\": \"0\", \"frameId\": \"map\" }, \"childFrameId\": \"base_link\", \"pose\": { \"pose\": { \"position\": { \"x\": 0, \"y\": 0, \"z\": 0.0 }, \"orientation\": { \"x\": 0,             \"y\": 0, \"z\": 0, \"w\": 1 } }, \"covariance\": [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] }, \"twist\": { \"twist\": { \"linear\": { \"x\": 0, \"y\":             0, \"z\": 0 }, \"angular\": { \"x\": 0, \"y\": 0, \"z\": 0 } }, \"covariance\": [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] } }" 
    }



Post Data to a Specific Stream ::

    POST /robot/{robotId}/streams/upload-stream

    Description: Post json to a specific stream, time out is 1 second 


     Body: 
        {
            "componentname":"data-publisher",
            "streamname":"gps",
            "source":"1",
            "streamjson":"{"x":"1","y":"2","z":"3"}",
            "datatype":"Nimbus.Messages.geometry_msgs.Point"
        }


Notes
-----

- {robotId} and {streamName} are placeholders for the robot ID and stream name, respectively.
- For methods that modify data (e.g., POST), the request's body should be detailed in the API documentation, specifying required fields and formats.
- Status Codes: Utilize HTTP status codes correctly to indicate the outcome of API calls, e.g., 200 OK, 404 Not Found, 400 Bad Request.
- For testing the API, it is possible to use the following example: curl -v --location --request GET <route> -H "Authorization: Bearer <token>" --header 'u;'
