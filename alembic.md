# How to use alembic

Alembic is what we use to manage our migrations, we use migrations as a sort of version control for
the database so we can ensure its state is always identical to the origin developers machine
when replicated onto some other machine.

- The Postgres URL is located in the config file

## Helpful commands
These commands should be run from the solution root directory

You can see a list of commands by typing 
  ```
  python run.py db
  ```

- To create a new revision of the migration

  ```
  python run.py db revision -m "create case table"
  ```
  
  > this creates a new item in the revisions directory

- To run a migration upgrade/downgrade
  - Upgrade to head

    ```
    python run.py db upgrade head
    ```

  - Downgrade to the start

    ```
    python run.py db downgrade base
    ```

  > If successful you should be able to see the changes in your database

- To run a specific migration

  ```
  python run.py db upgrade 467eda2cd7e0
  ```
  > here 467eda2cd7e0 is the revision id

- To upgrade or roll back relatively

  - Upgrade 1 version from current

    ```
    python run.py db upgrade +2
    ```

  - Downgrade 1 version from current
  
    ```
    python run.py db downgrade -1
    ```

- To get your history

  ```
  python run.py db history
  ```
  
  > you can use the ```--verbose``` parameter to get a more detailed breakdown