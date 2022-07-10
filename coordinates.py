from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Coordinates:
	latitude: float
	longitude: float


def get_gps_coordinates() -> Coordinates:
	"""Returns current GPS coordinates"""
	return Coordinates(10, 20)




