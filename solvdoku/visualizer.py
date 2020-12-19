from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.modalview import ModalView
from kivy.app import App
from kivy.logger import Logger
from kivy.config import Config

from .grid import Grid
from .utils import replace_0_by_space

Config.set('graphics', 'width', '450')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'minimum_width', '400')
Config.set('graphics', 'minimum_height', '550')


class SudokuLayout(GridLayout):
    def __init__(self, grid, **kwargs):
        kwargs["cols"] = 1
        kwargs["rows"] = 1
        kwargs["pos_hint"] = {'center_x': 0.5, 'center_y': 0.5}
        super(SudokuLayout, self).__init__(**kwargs)

        self.grid = grid
        self.boxes = []

        self.draw_grid()

    def draw_grid(self):
        self.clear_widgets()
        layout = GridLayout(cols=3, rows=3, spacing=[5, 5])
        self.add_widget(layout)
        for k, (square, init_square) in enumerate(self.grid.iter_squares()):
            sub_layout = GridLayout(cols=3, rows=3)
            layout.add_widget(sub_layout)
            boxes = []
            for l, (n, init_n) in enumerate(zip(square, init_square)):
                if init_n == 0:
                    x, y = Grid._from_square_to_classic_coord(k, l)
                    btn = ButtonSudoku(
                        self.make_callback_btn(x, y), text=replace_0_by_space(n))
                else:
                    btn = ButtonDisableSudoku(text=str(n))
                boxes.append(btn)
                sub_layout.add_widget(btn)
            self.boxes.append(boxes)

    def reset(self):
        self.grid.reset()
        self.draw_grid()

    def make_callback_btn(self, x, y):
        def callback_on_btn_update(n):
            self.grid.raw_grid[x, y] = int(n)
            self.draw_grid()
        return callback_on_btn_update


class ButtonSudoku(Button):
    def __init__(self, callback, **kwargs):
        kwargs["on_press"] = self.button_callback
        self.callback = callback
        super(ButtonSudoku, self).__init__(**kwargs)

    def button_callback(self, button):
        button.text = ""
        view = PickModal(attach_to=self)
        view.open()


class ButtonDisableSudoku(Button):
    def __init__(self, **kwargs):
        kwargs["background_color"] = (0.5, 0.5, 0.5, 1.0)
        super(ButtonDisableSudoku, self).__init__(**kwargs)


class PickModal(ModalView):
    def __init__(self, **kwargs):
        kwargs["size_hint"] = (None, None)
        kwargs["size"] = (400, 50)
        super(PickModal, self).__init__(**kwargs)
        self.btn = kwargs["attach_to"]

        layout = BoxLayout(orientation='horizontal')
        self.add_widget(layout)
        for i in range(9):
            layout.add_widget(
                Button(text=str(i+1), on_press=self.dismiss))

    def dismiss(self, chosen_nb):
        self.btn.text = chosen_nb.text
        self.btn.callback(chosen_nb.text)
        super(PickModal, self).dismiss()


class MenuLayout(RelativeLayout):
    def __init__(self, grid, reset_callback, **kwargs):
        kwargs["pos_hint"] = {'center_x': 0.5, 'center_y': 0.5}
        super(MenuLayout, self).__init__(**kwargs)

        self.grid = grid
        self.reset_callback = reset_callback

        self.add_widget(
            MenuButton(text="Generate", pos_hint={'center_x': 0.25, 'center_y': 0.5}, on_press=self.on_press_generate))
        self.add_widget(MenuButton(text="Solve",
                                   pos_hint={'center_x': 0.5, 'center_y': 0.5}, on_press=self.on_press_solve))
        self.add_widget(MenuButton(text="Reset",
                                   pos_hint={'center_x': 0.75, 'center_y': 0.5}, on_press=self.on_press_reset))

    def on_press_generate(self, button):
        Logger.info("call back generate")

    def on_press_solve(self, button):
        Logger.info("call back solve")

    def on_press_reset(self, button):
        Logger.info("call back reset")
        self.reset_callback()


class MenuButton(Button):
    def __init__(self, **kwargs):
        kwargs["size_hint"] = (None, None)
        kwargs["width"] = 80
        kwargs["height"] = 30
        super(MenuButton, self).__init__(**kwargs)


class SudokuVisualizer(App):
    def __init__(self, **kwargs):
        super(SudokuVisualizer, self).__init__(**kwargs)
        self.sudoku = Grid([[1, 0, 0, 0, 0, 0, 0, 0, 6],
                            [0, 0, 6, 0, 2, 0, 7, 0, 0],
                            [7, 8, 9, 4, 5, 0, 1, 0, 3],
                            [0, 0, 0, 8, 0, 7, 0, 0, 4],
                            [0, 0, 0, 0, 3, 0, 0, 0, 0],
                            [0, 9, 0, 0, 0, 4, 2, 0, 1],
                            [3, 1, 2, 9, 7, 0, 0, 4, 0],
                            [0, 4, 0, 0, 1, 2, 0, 7, 8],
                            [9, 0, 8, 0, 0, 0, 0, 0, 0]])

        self.init_sudoku = self.sudoku

    def build(self):
        layout = BoxLayout(orientation='vertical')
        sudoku_layout = SudokuLayout(self.sudoku,
                                     size_hint=(None, None), width=400, height=420)
        layout.add_widget(sudoku_layout)
        layout.add_widget(MenuLayout(self.sudoku, sudoku_layout.reset, size_hint=(
            None, None), width=400, height=130))
        return layout


if __name__ == '__main__':
    SudokuVisualizer().run()
