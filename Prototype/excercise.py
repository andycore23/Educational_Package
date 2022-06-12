"""Sample Garden module"""
from typing import List, Union


class Garden:
    """docstring"""

    def __init__(self, area: Union[float, None] = None):
        self._plants: List[str] = []
        self._area = area

    def get_garden_area(self) -> Union[float, None]:
        """
        Metoda, która zwraca obszar garden. Bez tej metody,
        mamy po prostu zmienną, a ona robi robotę i programista
        wie, że ona zwraca obszar akurat
        """
        return self

    def get_all_plants(self) -> List[str]:
        """
        Without this, All variables of an object are not connected to one thing
        Returns list of all plants in the garden.
        :return plants: List of plants
        """
        return self._plants

    def add_plant(self, plant_name: str) -> None:
        """
        Appends given plant to the garden plants list.
        :param plant: plant name
        :return None:
        """
        self._plants.append(plant_name)


if __name__ == "__main__":
    garden = Garden(10.3)  # obieakt A
    print(garden.get_garden_area())  # obieakt A
    garden.add_plant("Sunflower")  # obieakt A
    garden.add_plant("Lily")  # obieakt A
    print(garden.get_all_plants())  # obieakt A

    Nikol_garden = Garden(5.0)
    print(Nikol_garden)
    Nikol_garden.add_plant("Romsahka")
    Nikol_garden.add_plant("Tulipan")
    print(Nikol_garden.get_all_plants())
