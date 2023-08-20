# Music Classifier

## How it works

1. We gather a dataset of various genre music.
2. Calculate various metrics for each and save them to a database.
3. By using the same metrics and some cost functions we find most comparable music tracks

## Basic Usage 

### Init Project

1. Create venv

```
python -m venv venv
```


2. Activate venv

```
./venv/Scripts/activate
```


3. Install requirements

```
pip install -r requirements.txt
```

### Setup 

1. To start the database localy you need docker running and then use
```
docker compose up -d
```


2. Once the database is up initialize the schema with
```
docker cp  ./dumps/schema.sql music-db:/schema.sql
docker exec music-db bash -c "psql -U root music < schema.sql"
```

3. Fill the databases
```
python ./utils/init_db.py
```

### Example

- The script asks for a relative path to the track to classify and an integer for the number nearest tracks to find.
- These values can also be manually set by changing the variables in the find_nearest.py file.
- You can also set the desired label of the input track, in that case it will also pring the precission of each function used.


```
python find_nearest.py
```

The output will be in the `out` folder
and the precision will be logged.

## Configuring

### Add a cost function

To add another cost function just add the implementation as a py file in the ./distance_calc/functions.py file and then add it to the enum and dictionary in the ./distance_calc/distance_funcs.py file.


### Add music tracks to dataset

Music tracks to be used for filling up the database must be placed in the ./dataset directory in the appropriate directory based on its genre.

This must be done before running ./utils/init_db.py and if we need another genre, it needs to be added in the labels list in init_db.

The tracks used for testing were found [here](https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification)

### Attributes for distance

```
To change the attributes used for distance calculation, change the `fetchable_attributes` in the  `./utils/fetch_entries.py`
```


