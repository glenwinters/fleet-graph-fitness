import datetime
import time
import typing
import strawberry

import app.db


def get_workouts():
    db_cursor = app.db.connection.cursor()
    db_cursor.execute("SELECT title, extract(epoch from start_timestamp) from workouts;")
    results = db_cursor.fetchall()
    print(results)
    workouts = map(lambda r: Workout(activity=r[0], timestamp=r[1]), results)
    print(workouts)
    return workouts


@strawberry.type
class Workout:
    activity: str
    timestamp: int


@strawberry.type
class Query:
    workouts: typing.List[Workout] = strawberry.field(resolver=get_workouts)


schema = strawberry.federation.Schema(query=Query)
