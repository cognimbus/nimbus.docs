Create a token in the admin profile when logged in to your organization on Cogniteam Cloud Platform 

Assuming the base URL for the API is https://api.cognimbus.com/api/v1

Login to API

Login with API token

POST /login

Body: { "token": "..." }

Description: Sends token to login

returns "bearer"

Robots Management

List Robot IDs

GET /robots

Header: { "bearer": "..." }

Description: Retrieves a list of all robot IDs.

Response example

{ "robots": [ { "id": "0cb17861-295f-4882-bec4-1fc5fecc2a2c", "name": "nqwqw" }, { "id": "136315a1-11f6-4ade-9b0a-6d7a26fd021b", "name": "ggggggg" }, { "id": "2807bf84-c210-4a09-b344-d6c41df1ecf7", "name": "jjjjjjj" }, { "id": "34f2b77f-4203-4aa9-8894-8d20910efd45", "name": "JustForStart" }, { "id": "563a6f99-2124-4d5f-a88d-ab50e3eede7e", "name": "pengo_ros1" }, { "id": "a21f4375-36fa-4d7c-85d2-9654671b84df", "name": "TokenRobot200" },

Get a Specific Robot's Details

GET /robots/{robotId}

Description: Fetches details for a specific robot by ID.

Robot 

id 

name

Metrics 

Online/Offline

Last seen

Response example

{ "basicData": { "id": "0cb17861-295f-4882-bec4-1fc5fecc2a2c", "name": "nqwqw" }, "metrics": [ { "Name": "Traffic", "value": 1048576000000, "state": 1 }, { "Name": "AgentMandatoryUpdate", "value": 0, "state": 2 } ], "isOnline": false, "lastTimeSeen": "0001-01-01T00:00:00Z" }

Robot Metrics

Get All Metrics (prod)

GET /robots/metrics

Description: Fetches all available metrics 

ex. cpu,ram,etc..

Get Robot Metrics (prod)

GET /robot/{robotId}/metric/{metricId}

Description: Fetches specific metric for robot

ex. cpu,ram,etc…

Streaming/Unary Data Management

For streaming or sending commands directly to robots

when robots are online

Rate limited to 1sec

Get All Streams (staging)

GET /robot/{robotId}/streams

Description: Retrieves a list of all available streams for a robot.

streamName, type

Get Data from a Specific Stream (staging)

GET /robot/{robotId}/streams/{streamName}

Description: Fetches data from a specific stream for a robot.

Notes

{robotId} and {streamName} are placeholders for the robot ID and stream Name, respectively.

For methods that modify data (e.g., POST), the body of the request should be detailed in the API documentation, specifying required fields and formats.

Status Codes: Utilize HTTP status codes correctly to indicate the outcome of API calls, e.g., 200 OK, 404 Not Found, 400 Bad Request.

Versioning: version the API (e.g., /v1/robot) to manage changes and maintain compatibility.
