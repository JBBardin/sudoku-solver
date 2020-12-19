from typing import List
import numpy as np

from .utils import replace_0_by_space

ALL_POSSIBLE_NB = set([1, 2, 3, 4, 5, 6, 7, 8, 9])


class Grid():
    """Data structure to represent
    """

    def __init__(self, grid: List[List[int]] = [[0]*9]*9):
        self.raw_grid = np.array(grid, dtype=int)

    def _get_possible_number(self, x: int, y: int) -> List:
        if self.raw_grid[x, y] != 0:
            return [self.raw_grid[x, y]]
        nb = ALL_POSSIBLE_NB.copy()
        nb.intersection_update(self._get_possible_nb_row(x))
        nb.intersection_update(self._get_possible_nb_column(y))
        nb.intersection_update(self._get_possible_nb_square(x, y))
        return sorted(list(nb))

    def _get_possible_nb_row(self, x: int) -> List:
        return ALL_POSSIBLE_NB.difference(self.raw_grid[x, :])

    def _get_possible_nb_column(self, y: int) -> List:
        return ALL_POSSIBLE_NB.difference(self.raw_grid[:, y])

    def _get_possible_nb_square(self, x: int, y: int) -> List:
        c_x, c_y = Grid._get_square_coord(x, y)
        return ALL_POSSIBLE_NB.difference(self.raw_grid[c_x:c_x+3, c_y:c_y+3].flatten())

    def iter_rows(self):
        for i in range(9):
            yield self.raw_grid[i, :]

    def iter_squares(self):
        for i in range(9):
            c_x = (i // 3) * 3
            c_y = (i % 3) * 3
            yield self.raw_grid[c_x:c_x+3, c_y:c_y+3].flatten()

    @staticmethod
    def _get_square_coord(x: int, y: int) -> [int, int]:
        id_x, id_y = Grid._get_square_id(x, y)
        return id_x*3, id_y*3

    @staticmethod
    def _get_square_id(x: int, y: int) -> [int, int]:
        return x//3, y//3

    def __str__(self):
        string = [f"{'':-<19}"]
        for k in range(9):
            string.append(
                "|" + "|".join(map(replace_0_by_space, self.raw_grid[k, :])) + "|")
            if (k+1) % 3 == 0:
                string.append(f"{'':-<19}")
        return "\n".join(string)


if __name__ == "__main__":
    grid = Grid()
    print(grid)
