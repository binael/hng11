# HNG STAGE2 API

A simple api that requires no form of authentication but uses the HTTP methods: GET, POST, PUT and DELETE to handle data stored in a remove database. This api was implemented as a requirement for stage two completion in hng internship.

#### Functionalities covered by the api
* Create
* Read or Retrieve
* Update
* Delete

## UML Diagram
[](https://github.com/binael/hng11/blob/main/stage_two/uml.png)

---

## Table of Contents
* [Environment](#environment)
* [GET Method](#create)
* [POST Method](#post)
* [PUT Method](#put)
* [DELETE Method](#delete)
* [Limitations](#limitations)
* [Instructions](#instructions)
* [Error Codes and Messages](#error-codes)
* [How To Setup On Localhost](#localhost-run)

## Environment
Note that the environment used in development of this project is python 3.10 and ubuntu 20.04
All tests were done on ubuntu terminal using `curl`

## GET Method
This method handles the retrieval of all or specific objects from the database, displaying it in json format
### Request with id=<int>
```
curl https://binael-hng-stage2.onrender.com/api/1
```
### Response
```
{
	"user_id":1,
	"name":"Odogwu1"
}
```
### Request without id
```
curl https://binael-hng-stage2.onrender.com/api
```
### Response
```
[
	{
		"user_id":1,
		"name":"Odogwu1"
	},
	{
		"user_id":2,
		"name":"Nwannaa"
	}
]
```
### Request header
```
curl -sI https://binael-hng-stage2.onrender.com/api
```
### Response header
```
HTTP/1.1 200 OK
Server: Werkzeug/2.3.7 Python/3.10.12
Date: Fri, 15 Sep 2023 08:24:04 GMT
Content-Type: application/json
Content-Length: 133
Connection: close
```
### Request header
```
curl -sI https://binael-hng-stage2.onrender.com/api -X OPTIONS
```
### Response header
```
HTTP/1.1 200 OK
Server: Werkzeug/2.3.7 Python/3.10.12
Date: Fri, 15 Sep 2023 08:53:32 GMT
Content-Type: text/html; charset=utf-8
Allow: OPTIONS, GET, POST, HEAD
Content-Length: 0
Connection: close
```

## POST Method
This is used to create a new instance in the database. This method only accepts json input to the body, all other will return errors with no update made to the database
### Request
```
curl https://binael-hng-stage2.onrender.com/api -X POST -H 'Content-Type: application/json' -d '{"name": "Udenemmuo"}'
```
### Response
No response on success

## PUT Method
This is used to update an instance in the database. This post only accepts json input to the body, all other will return errors with no update made to the database
### Request
```
curl https://binael-hng-stage2.onrender.com/api/2 -X POST -H 'Content-Type: application/json' -d '{"name": "Udenemmuo"}'
```
### Response
No response on success, you can validate your id using GET request

## DELETE Method
This is used to update an instance in the database. This post only accepts json input to the body, all other will return errors with no update made to the database
### Request
```
curl https://binael-hng-stage2.onrender.com/api/2 -X DELETE
```
### Response
No response on success, you can validate your id using GET request


## Limitations
1. The program accepts `only` json formatted data as the body for the POST and PUT methods
2. The program cannot accept more than one input
3. No matter the number of parameters in a json file, the api will search for only one user_id and the name key-value, all others are not considered or stored


## Error Codes and Messages

### Error Codes

| Status Code | Description |
| ----------- | ----------- |
| 1: 200 | OK |
| 2: 404 | No File Found |
| 3: 500 | Server Error |

### Error Messages

| Error Message | Description |
| ------------- | ----------- |
| 1: FAILED | Could not perform PUT or POST operations
| 2. No File Found | Could not find files to delete |


## How To Setup On Localhost
This whole project is hosted online courtesy of [Render](https://dashboard.render.com/) but to set it up on localhost follow the steps below

1. Clone the repository below and `cd stage_two`
```
git clone https://github.com/binael/hng11
```
2. Make sure that you have your Environment as above and create a python virtual environment
```
	python3 -m venv .venv
```
3. Activate the environment
```
	source .venv/bin/activate
```
4. Install all dependencies by in requirements by running the build command
```
	./build.sh
```
5. Choose any RDM of your choice, set your login and create a database named `flask_app`. set/export environment variable `DATABASE_URL` to connect to the database. Example, I used postgres (make sure to install the database dependent modules)
```
	export DATABASE_URL=postgresql://<username>:<password>@localhost/flask_app
```
6. Finally, run the below to start up the program
```
	python3 app.py
```
