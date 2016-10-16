# Djangorestframework Microservice Base

This is a base template for a Docker microservice using djangorestframework. It
includes a basic user model with authentication using JWT.

For a pre-built container, you can use:

```
docker run -d dansackett/djangorestframework-base:1.0
```

This is built as a starting point though for building a full REST API. You can
fork this repository and use it to hit the ground running.

## Basic API Interaction

I'm using [HTTPie](https://github.com/jkbrzt/httpie) in the following examples.
When you run your container, you will need to first find the container ID.

```
docker ps
```

Grab the container ID and use it to find the IP address to interact with:

```
docker inspect --format '{{ .NetworkSettings.IPAddress }}' <CONTAINER ID>
```

Once we have that then we can make requests to the API:

```
http GET http://<IP ADDRESS>:8000/api/v1/users/
```

This should return a response. The following endpoints are provided out of the box:

| Endpoint            | Verb    | Result                                          |
|---------------------|---------|-------------------------------------------------|
| /api/v1/users/      | GET     | User List                                       |
| /api/v1/users/      | POST    | Create a new User                               |
| /api/v1/users/{pk}/ | GET     | User Detail                                     |
| /api/v1/users/{pk}/ | PUT     | Update an user                                  |
| /api/v1/users/{pk}/ | PATCH   | Partially Update an User                        |
| /api/v1/users/{pk}/ | DELETE  | Delete an User                                  |
| /api/v1/auth/login/ | POST    | Get a new JWT token based on email and password |

## TODO

As of now, there isn't a persistence with the database used. I will need to
look into how to handle a dynamic DB with the container since it will likely be
another microservice.
