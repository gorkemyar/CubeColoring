class Point:
    def __init__(self, dimension_count: int, coordinates: list[int]):
        self.dimension_count = dimension_count
        self.coordinates = coordinates
    
    def __str__(self) -> str:
        return str(self.coordinates)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return self.coordinates == other.coordinates and self.dimension_count == other.dimension_count
    
    def __hash__(self) -> int:
        return hash(str(self.coordinates))
    
    def distance(self, other: object) -> int:
        if not isinstance(other, Point):
            return -1
        if self.dimension_count != other.dimension_count:
            return -1
        return sum([abs(self.coordinates[i] - other.coordinates[i]) for i in range(self.dimension_count)])
    


class Edge:
    def __init__(self, point1: Point, point2: Point) -> None:
        self.point1: Point = point1
        self.point2: Point = point2
        self.color: str = "gray"
    
    def __str__(self) -> str:
        return self.color + " " + str(self.point1) + " - " + str(self.point2)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Edge):
            return False
        return self.point1 == other.point1 and self.point2 == other.point2

    def __hash__(self) -> int:
        return hash(str(self.point1) + str(self.point2))
        
    def get_points(self) -> list[Point]:
        return [self.point1, self.point2]

    def get_color(self) -> str:
        return self.color
    
    def set_color(self, color: str) -> None:
        self.color = color

    def get_vector(self) -> list[int]:
        return [abs(self.point2.coordinates[i] - self.point1.coordinates[i]) for i in range(self.point1.dimension_count)]
    
    def is_adjacent(self, other: object) -> bool:
        if not isinstance(other, Edge):
            return False
        points = set(self.get_points() + other.get_points())
        return len(points) == 3

    def is_perpendicular(self, other: object) -> bool:
        if not isinstance(other, Edge):
            return False
        return self.is_adjacent(other) and sum([self.get_vector()[i] * other.get_vector()[i] for i in range(self.point1.dimension_count)]) == 0

    def _distance_helper(self, other: object) -> float:
        if not isinstance(other, Edge):
            return False
        
        points1 = self.get_points()
        points2 = other.get_points()
        dist = [points1[0].distance(points2[0]), points1[0].distance(points2[1]), points1[1].distance(points2[0]), points1[1].distance(points2[1])]

        return  dist.count(1) == 2 and dist.count(2) == 2
    
    def is_parallel(self, other: object) -> bool:
        if not isinstance(other, Edge):
            return False
        return self._distance_helper(other) and self.get_vector() == other.get_vector()

    
