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
strawberry server schema -p 4011
```
