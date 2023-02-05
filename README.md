# Room Occupancy API

This is a RESTful API for collecting and retrieving room occupancy data from various sensors. The API is designed to be flexible and scalable, and it can handle a large number of sensors and observations.
The goal of this task is to implement a simplified back-end application that may be used to
both collect and provide the data from an IoT network.

## Features
* Accept incoming sensor data from various sources through a webhook endpoint
* Store sensor data in memory for fast retrieval
* Retrieve sensor data for a specific instant in time or for the current occupancy of a room
* Return a list of all sensors connected to the API

## API SWAGGER DOCS

* Link : [https://falloudiakhate.pythonanywhere.com/api/docs](https://falloudiakhate.pythonanywhere.com/api/docs)

![sqaresense](https://user-images.githubusercontent.com/53915792/216819124-fef1bcae-fc68-4ab3-a072-142bb96b09fb.png)


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

![webhook](https://user-images.githubusercontent.com/53915792/216819264-70d286cc-edd2-4fec-a505-d51a6ebd5499.png)


* Retrieve a list of all sensors connected to the API

**GET**
```api/sensors```

![sensors](https://user-images.githubusercontent.com/53915792/216819375-4ed5ad54-fae9-42a3-aee8-1d61795f27e5.png)


* Retrieve the occupancy data for a particular sensor. An optional atInstant query parameter can be used to retrieve data for a specific instant in time.

**GET**
```sensors/<sensor>/occupancy``` or 
```sensors/<sensor>/occupancy?atInstant=<instant>```


![occu](https://user-images.githubusercontent.com/53915792/216819476-93872565-ab02-4413-80a7-df145075b82a.png)

## Requirements

**Django Rest Framework (DRF)** is a popular, powerful, and flexible framework for building RESTful APIs in Django. It provides a lot of built-in functionality for creating APIs, including serialization, request parsing, authentication, and more. DRF makes it easy to create a RESTful API quickly and efficiently, and it provides a lot of functionality that would otherwise need to be built from scratch.

In the Room Occupancy project, DRF can be used to provide a RESTful API for retrieving occupancy data and for updating the occupancy data via a webhook. The serialization features of DRF can be used to easily validate incoming data and convert it into the desired format for storage. The authentication features of DRF can be used to secure the API and ensure that only authorized clients can access the occupancy data. Additionally, the request parsing features of DRF can be used to extract and validate parameters from API requests.



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
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

* Testing

To run the API tests, use the following command:

```
python manage.py test
```

