# Soham Care Web App
<!-- 
## Demo

![screenshot](https://raw.githubusercontent.com/makeavish/SkinCancerPredictor/master/demo.gif) -->

## Getting Started

Create a [virtual env](https://docs.python.org/3/tutorial/venv.html) or [conda env](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/) and install all the required packages

### Requirements

- setuptools>=41.0.0
- scipy==1.4.1
- Flask>=1.1.2
- gunicorn>=20.0.4
- numpy>=1.19.0
- Keras>=2.4.3
- tensorflow-cpu>=2.2.0
- gevent>=20.6.2
- Werkzeug>=1.0.1
- MarkupSafe>=1.1.1
- Jinja2>=2.11.2
- flask-mongoengine>=0.9.5
- dnspython-2.0.0
- flask-restful-0.3.8
- flask-bcrypt-0.7.1
- flask-jwt-extended==3.24.1

## How To Use

After installing all the required packages
From your command line:

```bash
# Clone this repository
$ git clone https://github.com/makeavish/SK216_Soham

# Go into the repository
$ cd SK216_Soham

# Run the app
$ python3 app.py [host] [port] [debug]
```

Arguments are optional

**Default values**
```
host = localhost
port = 5000
debug = False
```

## API

# Backend API

This document describes the backend API.

## Create/ Register user

**Request** : `POST /api/auth/signup`

**Body** :

```json
{
  "id": String,
  "name": String,
  "email": String,
  "password": String,
  "register_date": Date
}
```

### Success response

**Code** : `200`

**Body** :

```json
{
  "id": String
}
```

### Error response

**Code** : `400`

**Body** :

```json
{
  "message": String
}
```

## API

# Backend API

This document describes the backend API.

## Login user

**Request** : `POST /api/auth/login`

**Body** :

```json
{
  "email": String,
  "password": String
}
```

### Success response

**Code** : `200`

**Body** :

```json
{
  "token": String
}
```

### Error response

**Code** : `400`

**Body** :

```json
{
  "message": String
}
```

<!-- 
## Delete user

**Request** : `DELETE /api/user/delete-user/:id`

### Success response

**Code** : `200`

**Body** :

```json
{}
```

### Error response

**Code** : `400`

**Body** :

```json
{
  "message": String
}
``` -->
<!-- 
## Get all users

**Request** : `GET /api/user`

### Success response

**Code** : `200`

**Body** :

```json
[
  {
   "id": String,
    "name": String,
    "email": String,
    "password": String,
    "register_date": Date,
    "crawls":[{"ID":String}]
  }
]
```

### Error response

**Code** : `400`

**Body** :

```json
{
  "message": String
}
``` -->

## Get user

**Request** : `GET /api/user/:id`

**Auth required** : Yes

### Success response

**Code** : `200`

**Body** :

```json
{
  "id": String,
  "name": String,
  "email": String,
  "password": String,
  "register_date": Date,
  "crawls":[{"ID":String}]
},
```

### Error response

**Code** : `400`

**Body** :

```json
{
  "message": String
}
```
<!-- 
## Update user

**Request** : `PUT /api/user/update-user/:id`

**Body** :

```json
{
  "id": String,
  "name": String,
  "email": String,
  "password": String,
  "register_date": Date,
  "crawls":[{"ID":String}]
}
```

### Success response

**Code** : `200`

**Body** :

```json
{
  "id": String
}
``` -->


## Create crawls

**Request** : `POST /api/crawls`

**Body** :

```json
{
  "id": String,
  "Query": String,
  "Results":[{"url":string, "Score":number}],
  "Run Date": Date
}
```

### Success response

**Code** : `200`

**Body** :

```json
{
  "id": String
}
```

### Error response

**Code** : `400`

**Body** :

```json
{
  "message": String
}
```

## Add Crawl ID to user

**Request** : `PUT /api/user/update-user-crawls`

**Body** :

```json
{
  "crawls": "object id"
}
```

### Success response

**Code** : `200`

**Body** :

```json
{
  "id": String
}
```

### Error response

**Code** : `400`

**Body** :

```json
{
  "message": String
}
```

## Get crawl

**Request** : `GET /api/crawls/:id`

### Success response

**Code** : `200`

**Body** :

```json
{
  "id": String,
  "Query": String,
  "Results":[{"url":string, "Score":number}],
  "Run Date": Date
}
```

### Error response

**Code** : `400`

**Body** :

```json
{
  "message": String
}
```

<!-- ## License

[MIT](https://github.com/makeavish/SkinCancerPredictor/blob/master/LICENCE) -->