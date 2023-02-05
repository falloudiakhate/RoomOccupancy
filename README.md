# Room Occupancy API

This is a RESTful API for collecting and retrieving room occupancy data from various sensors. The API is designed to be flexible and scalable, and it can handle a large number of sensors and observations.

## Features
* Accept incoming sensor data from various sources through a webhook endpoint
* Store sensor data in memory for fast retrieval
* Retrieve sensor data for a specific instant in time or for the current occupancy of a room
* Return a list of all sensors connected to the API

## Endpoints
**POST**
``` api/webhook ```
* An endpoint to be called by People Counters to send the results
of the observations.
The data should be in the following format:

```json
{
    "sensor": "abc",
    "ts": "2022-01-01T00:00:00Z",
    "in_count": 1,
    "out_count": 0
}
``` 

* Retrieve a list of all sensors connected to the API

**GET**
```api/sensors```

* Retrieve the occupancy data for a particular sensor. An optional atInstant query parameter can be used to retrieve data for a specific instant in time.

**GET**
```sensors/<sensor>/occupancy``` or 
```sensors/<sensor>/occupancy?atInstant=<instant>```

## Requirements
```
Django==4.1.3
django-cors-headers==3.13.0
django-extensions==3.0.2
django-filter==22.1
django-rest-swagger==2.2.0
djangorestframework==3.14.0
```

## Installation and Testing

* Clone the repository to your local machine:

```git clone https://github.com/falloudiakhate/RoomOccupancy```

* Navigate to the cloned directory:

```
cd RoomOccupancy
```

* Install the required packages:

```
pip install -r requirements.txt
```

* Run the API:

```
python manage.py runserver
```

* Testing

To run the API tests, use the following command:

```
python manage.py test
```

