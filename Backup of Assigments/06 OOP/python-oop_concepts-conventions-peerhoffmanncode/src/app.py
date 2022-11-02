#!/usr/bin/env python
""" This is a program/ game that simulates a Aquarium.
    One fish will be added every turn, as well as a
    selected amount of fish that will be killed every turn.
    When all fish are dead, the game will end. """


class AquariumApp:
    """A aquarium App Class"""

    def __init__(self, fish_count: int, eye_color: str, skin_color: str):
        """Constructor for aquarium app class"""
        self.__dead_fish = 0
        self._swim_count = 0
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.fish_count = fish_count

    def start(self) -> None:
        """Method to add a fish to the Aquarium"""
        if self.fish_count == 0:
            print("There are no alive fish left.")
            return
        self._swim_count += 1

        print(
            str(self.fish_count)
            + " fish are swimming. Their eyes are "
            + self.eye_color
            + " and their skin is "
            + self.skin_color
            + "."
        )
        print(
            "There are "
            + str(self.__dead_fish)
            + " dead fish with them in the aquarium."
        )
        print(
            "The fish have now been swimming "
            + str(self._swim_count)
            + " times."
        )

    def set_died_fish(self, dead_fish_number: int) -> None:
        """A method that sets dead (kills) fish in the Aquarium"""
        if self.fish_count == 0:
            print("All fish are dead.")
            print("GAME OVER")
            print("=====")
            return

        self.fish_count -= dead_fish_number
        self.__dead_fish += dead_fish_number
        if dead_fish_number > 1:
            print(str(dead_fish_number) + " fish have died.")
        elif dead_fish_number == 1:
            print("A fish has died.")
        else:
            print("No fish has died.")


if __name__ == "__main__":
    my_aquarium_app = AquariumApp(fish_count=5, eye_color="blue", skin_color="red")
    my_aquarium_app.start()
    my_aquarium_app.set_died_fish(2)
    my_aquarium_app.start()
    my_aquarium_app.set_died_fish(1)
    my_aquarium_app.start()
    my_aquarium_app.set_died_fish(2)
    my_aquarium_app.start()
    my_aquarium_app.set_died_fish(1)
