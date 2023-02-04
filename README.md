Room Occupancy API

This is a RESTful API for collecting and retrieving room occupancy data from various sensors. The API is designed to be flexible and scalable, and it can handle a large number of sensors and observations.

Features
Accept incoming sensor data from various sources through a webhook endpoint
Store sensor data in memory for fast retrieval
Retrieve sensor data for a specific instant in time or for the current occupancy of a room
Return a list of all sensors connected to the API

Endpoints


api/sensors

GET

Retrieve a list of all sensors connected to the API

api/occupancy/<sensor>/
GET
Retrieve the occupancy data for a particular sensor. An optional atInstant query parameter can be used to retrieve data for a specific instant in time.

/webhook_listener/
POST
Accept incoming sensor data from various sources. The data should be in the following format:

json
Copy code
{
    "sensor": "abc",
    "ts": "2022-01-01T00:00:00Z",
    "in_count": 1,
    "out_count": 0
}
Requirements
Python 3.x
Django
Django Rest Framework
Installation
Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/<username>/room_occupancy_api.git
Navigate to the cloned directory:
bash
Copy code
cd room_occupancy_api
Install the required packages:
Copy code
pip install -r requirements.txt
Run the API:
Copy code
python manage.py runserver
Testing
To run the API tests, use the following command:

bash
Copy code
python manage.py test API
Contributing
Contributions are welcome! If you would like to contribute to the project, please open a pull request.

License
This project is licensed under the MIT License.
