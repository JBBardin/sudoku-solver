from solvdoku.grid import Grid
import numpy as np


class TestGrid():

    def test_init(self):
        grid = Grid()
        assert np.all(grid.raw_grid == 0)
        assert grid.raw_grid.shape == (9, 9)

        grid = Grid([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                     [1, 2, 3, 4, 5, 6, 7, 8, 9],
                     [1, 2, 3, 4, 5, 6, 7, 8, 9],
                     [1, 2, 3, 4, 5, 6, 7, 8, 9],
                     [1, 2, 3, 4, 5, 6, 7, 8, 9],
                     [1, 2, 3, 4, 5, 6, 7, 8, 9],
                     [1, 2, 3, 4, 5, 6, 7, 8, 9],
                     [1, 2, 3, 4, 5, 6, 7, 8, 9],
                     [1, 2, 3, 4, 5, 6, 7, 8, 9]])
        print(grid.raw_grid[:, 0])
        assert np.all(grid.raw_grid[:, 0] == 1)
        assert np.all(grid.raw_grid[:, 1] == 2)
        assert np.all(grid.raw_grid[:, 2] == 3)
        assert np.all(grid.raw_grid[:, 3] == 4)
        assert np.all(grid.raw_grid[:, 4] == 5)
        assert np.all(grid.raw_grid[:, 5] == 6)
        assert np.all(grid.raw_grid[:, 6] == 7)
        assert np.all(grid.raw_grid[:, 7] == 8)
        assert np.all(grid.raw_grid[:, 8] == 9)

    def test_get_square_id(self):
        assert Grid._get_square_id(0, 1) == (0, 0)
        assert Grid._get_square_id(2, 5) == (0, 1)
        assert Grid._get_square_id(1, 8) == (0, 2)
        assert Grid._get_square_id(3, 0) == (1, 0)
        assert Grid._get_square_id(4, 3) == (1, 1)
        assert Grid._get_square_id(5, 7) == (1, 2)
        assert Grid._get_square_id(6, 2) == (2, 0)
        assert Grid._get_square_id(7, 4) == (2, 1)
        assert Grid._get_square_id(8, 6) == (2, 2)

    def test_get_square_coord(self):
        assert Grid._get_square_coord(0, 1) == (0, 0)
        assert Grid._get_square_coord(2, 5) == (0, 3)
        assert Grid._get_square_coord(1, 8) == (0, 6)
        assert Grid._get_square_coord(3, 0) == (3, 0)
        assert Grid._get_square_coord(4, 3) == (3, 3)
        assert Grid._get_square_coord(5, 7) == (3, 6)
        assert Grid._get_square_coord(6, 2) == (6, 0)
        assert Grid._get_square_coord(7, 4) == (6, 3)
        assert Grid._get_square_coord(8, 6) == (6, 6)

    def test_get_possible_nb_square(self):
        grid = Grid([[1, 2, 3, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 4, 5, 6, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 7, 8, 9],
                     [4, 5, 6, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 7, 8, 9, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 2, 3],
                     [7, 8, 9, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 2, 3, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 4, 5, 6]])

        assert grid._get_possible_nb_square(2, 2) == set([4, 5, 6, 7, 8, 9])
        assert grid._get_possible_nb_square(2, 5) == set([1, 2, 3, 7, 8, 9])
        assert grid._get_possible_nb_square(2, 8) == set([4, 5, 6, 1, 2, 3])
        assert grid._get_possible_nb_square(4, 2) == set([1, 2, 3, 7, 8, 9])
        assert grid._get_possible_nb_square(4, 5) == set([4, 5, 6, 1, 2, 3])
        assert grid._get_possible_nb_square(4, 8) == set([4, 5, 6, 7, 8, 9])
        assert grid._get_possible_nb_square(7, 2) == set([4, 5, 6, 1, 2, 3])
        assert grid._get_possible_nb_square(7, 5) == set([4, 5, 6, 7, 8, 9])
        assert grid._get_possible_nb_square(7, 8) == set([1, 2, 3, 7, 8, 9])

    def test_get_possible_nb_column(self):
        grid = Grid([[1, 2, 3, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 4, 5, 6, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 7, 8, 9],
                     [4, 5, 6, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 7, 8, 9, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 2, 3],
                     [7, 8, 9, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 2, 3, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 4, 5, 6]])

        assert grid._get_possible_nb_column(0) == set([2, 3, 5, 6, 8, 9])
        assert grid._get_possible_nb_column(1) == set([1, 3, 4, 6, 7, 9])
        assert grid._get_possible_nb_column(2) == set([1, 2, 4, 5, 7, 8])
        assert grid._get_possible_nb_column(3) == set([2, 3, 5, 6, 8, 9])
        assert grid._get_possible_nb_column(4) == set([1, 3, 4, 6, 7, 9])
        assert grid._get_possible_nb_column(5) == set([1, 2, 4, 5, 7, 8])
        assert grid._get_possible_nb_column(6) == set([2, 3, 5, 6, 8, 9])
        assert grid._get_possible_nb_column(7) == set([1, 3, 4, 6, 7, 9])
        assert grid._get_possible_nb_column(8) == set([1, 2, 4, 5, 7, 8])

    def test_get_possible_nb_row(self):
        grid = Grid([[1, 2, 3, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 4, 5, 6, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 7, 8, 9],
                     [4, 5, 6, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 7, 8, 9, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 2, 3],
                     [7, 8, 9, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 2, 3, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 4, 5, 6]])

        assert grid._get_possible_nb_row(0) == set([4, 5, 6, 7, 8, 9])
        assert grid._get_possible_nb_row(1) == set([1, 2, 3, 7, 8, 9])
        assert grid._get_possible_nb_row(2) == set([4, 5, 6, 1, 2, 3])
        assert grid._get_possible_nb_row(3) == set([1, 2, 3, 7, 8, 9])
        assert grid._get_possible_nb_row(4) == set([4, 5, 6, 1, 2, 3])
        assert grid._get_possible_nb_row(5) == set([4, 5, 6, 7, 8, 9])
        assert grid._get_possible_nb_row(6) == set([4, 5, 6, 1, 2, 3])
        assert grid._get_possible_nb_row(7) == set([4, 5, 6, 7, 8, 9])
        assert grid._get_possible_nb_row(8) == set([1, 2, 3, 7, 8, 9])

    def test_get_possible_number(self):
        grid = Grid([[1, 2, 3, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 4, 5, 6, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 7, 8, 9],
                     [4, 5, 6, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 7, 8, 9, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 2, 3],
                     [7, 8, 9, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 2, 3, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 4, 5, 6]])

        assert grid._get_possible_number(1, 0) == [8, 9]
        assert grid._get_possible_number(4, 5) == [9]
        assert grid._get_possible_number(5, 5) == [4, 5]
        assert grid._get_possible_number(8, 4) == [7, 9]
