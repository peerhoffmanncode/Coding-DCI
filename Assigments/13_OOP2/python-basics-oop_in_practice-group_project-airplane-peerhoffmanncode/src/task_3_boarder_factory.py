from task_2_passenger import Pilot, Crew, Passenger


class BoarderFactory:
    """Factory to create passanger types"""

    @staticmethod
    def create_object(boarder_type, *args, **kwargs):
        """Factory method"""

        if boarder_type.lower() == "pilot":
            return Pilot(*args, **kwargs)
        elif boarder_type.lower() == "crew":
            return Crew(*args, **kwargs)
        elif boarder_type.lower() == "passenger":
            return Passenger(*args, **kwargs)
        else:
            raise ValueError("Invalid boarder type!")
