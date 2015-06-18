# Conveyancer API

This API provides the endpoints for the conveyancer data and creates the case table via migrations

## Getting started

- You need to set an environment variable setting your database URI

  example

  ```
  export DATABASE_URI=postgresql://user:password@localhost/databasename
  ```

- This application uses python3, if you dont have python3 you can install it using [homebrew](http://brew.sh/) (Mac) but running the command

  ```
  brew install python3
  ```

- Install the application dependancies

  ```
  pip install -r requirements.txt
  ```

- To run the migrations you will need to be in the app directory, here you can run

  ```
  alembic upgrade head
  ```

  > There is more detail on using alembic in app/db readme

## Running the application

When this is complete you can run the application by running

```
gunicorn "app:create_manager().app"
```
