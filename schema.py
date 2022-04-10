import typing
import strawberry

def get_workouts():
    return [
        Workout(
            activity='run',
            timestamp=1649609012,
        ),
        Workout(
            activity='basketball',
            timestamp=1649695412,
        ),
    ]

@strawberry.type
class Workout:
    activity: str
    timestamp: int

@strawberry.type
class Query:
    workouts: typing.List[Workout] = strawberry.field(resolver=get_workouts)

schema = strawberry.federation.Schema(query=Query)
