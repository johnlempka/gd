# Sample API Program

## Prerequisites
1. python3

## How to run
This program uses a typical flask setup with python3 `venv`.

To get started, cd into the directory. We'll first create a virtual environment to run in.

```
python3 -m venv venv
. venv/bin/activate
```

Next, install the dependencies with:

```
pip install -r requirements.txt
```

Lastly set the flask environment variable:

```
export FLASK_APP=server.py
```

The entrypoint for this application is `server.py`

### To run the Test Suite

To run the tests, simply run:

```
python3 tests.py
```

### Initialize the db
Before you start the server for the first time, you will want to initalize the db.

There are two scripts you can run here:

```
python3 init_db.py
```

This will create the tables that you need

```
python3 add_sample_data.y
```

This will add some sample data.


### To start the server

```
flask run
```
