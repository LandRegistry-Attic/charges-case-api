# Case API

The Case API is a JSON API which stores case objects.

This API holds the functionality for creating the migrating tables, getting data
from the database, converting to JSON and returns as an endpoint.


### Contents

- [Usage](#usage)
- [Getting Started](#getting-started)
- [Changing the migration](#changing-the-migration)
- [Current Model](#current-model)

## Usage
```
get     /                           # automatically redirects to helloworld for app test
get     /helloworld                 # test endpoint for the application
get     /case                       # get all cases
get     /case/<id_>                 # get a cases with an id in the URL
get     /case/<case_id>/property    # Get property for case id
get     /case/<case_id>/borrowers   # Get borrowers for case id
delete  /case/<id_>                 # delete a case with an id in the URL
post    /case                       # Create a case by posting a json object reflecting the model
post    /case/<deed_id>/status      # Updates the status of the case
post    /case/<case_id>/application # Submits deed for registration
post    /case/<case_id>/deed        # Adds deed id to case
post    /case/<case_id>/borrowers   # Add borrowers to borrower table
post    /case/<case_id>/property    # Add property to case

```
> [model](#current-model) for post

## Getting Started
1. Clone the repo
2. In the directory enter the command
```
pip install -r requirements.txt
```

3. Export your database URI
```
export DATABASE_URI=postgresql://username:password@localhost/database
```

4. To run the migration run the command
```
python run.py db upgrade head
```

5. To run the application run the command
```
python run.py runserver
```

## Changing the migration
All you have to do is change/create the related model and run the command

```
python run.py db revision --autogenerate
```

> For some helpful documentation on using alembic go [here](alembic.md)

## Current Model

### Case Model

```
{
  "id": Integer(Primary Key),
  "status": String,
  "created_on": ISO Format DateTime,
  "last_updated": ISO Format DateTime,
  "deed_id": Integer,
  "conveyancer_id": Integer
}
```

e.g.
```
{
  "id": 865604,
  "deed_id": 1,
  "conveyancer_id": 1,
  "status": "the status",
  "last_updated": "2015-06-23T23:37:08.156342",
  "created_on": "2015-06-23T23:37:08.156356"
}
```

### Borrower model

Borrowers are slightly different as you add an array of borrowers

```
{
  "borrowers": [
    {
        "first_name": String,
        "middle_names": String,
        "last_name": String,
        "case_id": Integer(foreign key),
        "mobile_no": String,
        "email_address": String,
        "address": Array(String)
    }
  ]
}
```

e.g.
```
{
  "borrowers": [
    {
      "first_name": "John",
      "middle_names": "Oliver",
      "last_name": "Smith",
      "case_id": 1,
      "mobile_no": "0777777171",
      "email_address": "maddog@thegoogle.com",
      "address": [
          "kennel"
      ]
    }
  ]
}
```
> Note: Because of the foreign key relationship, it will fail if the id of the case does not exist in the table

### Property Model
```
{
  "case_id": Integer(Primary Key)
  "title_number": String,
  "street": String,
  "tenure": String,
  "locality": String,
  "postcode": String,
}
```

e.g.
```
{
  "case_id": 123456
  "title_number": "DN100",
  "street": "a Street",
  "tenure": "Freehold",
  "locality": "A Locality",
  "postcode": "PL6 WDS",
}
```
