# fleet-graph-fitness

Fleet component: GraphQL subgraph for fitness-related things

So far this has one query, `workouts`, which returns a fixed list of workouts. I'm
focusing on setting up the graphql federation with multiple basic subgraphs first.

## Local Development

### Setup

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run the server

Run on port 4011 because that's what the federation gateway points to for now.

```
uvicorn app.main:app --reload --port 4011
```

## Docker

Build the image

```
docker build -t fleet-graph-fitness:latest .
```

Reference: [FastAPI in Containers - Docker](https://fastapi.tiangolo.com/deployment/docker/#build-a-docker-image-for-fastapi)

### Run the data loading script

Using the postgresql library required extra stuff on mac that was easiest solved by install postgres:
```
brew install postgresql
```

Run the script to clear out the `workouts` table and repopulate it from the `activities.csv` file:
```
python ./insert_activities.py
```