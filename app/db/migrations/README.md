# How to use alembic

- The Postgres URL is located in alembic.ini.

## Helpful commands
These commands should be run from the directory containing the alembic.ini file, in this case that is {repository_directory}/app
- To create a new revision of the migration

  ```
  alembic revision -m "create case table"
  ```
  
  > this creates a new item in the revisions directory

- To run a migration upgrade/downgrade
  - Upgrade to head

    ```
    alembic upgrade head
    ```

  - Downgrade to the start

    ```
    alembic downgrade base
    ```

  > If successful you should be able to see the changes in your database

- To run a specific migration

  ```
  alembic upgrade 467eda2cd7e0
  ```
  > here 467eda2cd7e0 is the revision id

- To upgrade or roll back relatively

  - Upgrade 1 version from current

    ```
    alembic upgrade +2
    ```

  - Downgrade 1 version from current
  
    ```
    alembic downgrade -1
    ```

- To get your history

  ```
  alembic history
  ```
  
  > you can use the ```--verbose``` parameter to get a more detailed breakdown
