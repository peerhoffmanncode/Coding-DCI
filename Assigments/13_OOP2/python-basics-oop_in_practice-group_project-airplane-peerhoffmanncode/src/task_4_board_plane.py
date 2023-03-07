from airplane import Airplane
from task_2_passenger import Pilot, Crew, Passenger


def board_plane(person_object, *args):

    if isinstance(person_object, Pilot):
        Airplane().pilot = person_object
    elif isinstance(person_object, Crew):
        Airplane().crew.append(person_object)
    elif isinstance(person_object, Passenger):
        Airplane().passengers[args[0]].append(str(person_object))
    else:
        raise ValueError("Invalid person type")
