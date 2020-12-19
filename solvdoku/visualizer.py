from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.logger import Logger
from kivy.config import Config

from .grid import Grid

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

        layout = GridLayout(cols=3, rows=3, spacing=[5, 5])
        self.add_widget(layout)
        for square in grid.iter_squares:
            sub_layout = GridLayout(cols=3, rows=3)
            layout.add_widget(sub_layout)
            boxes = []
            for n in square:
                if n == 0:
                    btn = ButtonSudoku(text="?")
                else:
                    btn = ButtonDisableSudoku(text=str(n))
                boxes.append(btn)
                sub_layout.add_widget(btn)
            self.boxes.append(boxes)


class ButtonSudoku(Button):
    def __init__(self, **kwargs):
        kwargs["on_press"] = self.button_callback
        super(ButtonSudoku, self).__init__(**kwargs)

    def button_callback(self, button):
        button.text = ""


class ButtonDisableSudoku(Button):
    def __init__(self, **kwargs):
        kwargs["background_color"] = (0.5, 0.5, 0.5, 1.0)
        super(ButtonDisableSudoku, self).__init__(**kwargs)


class MenuLayout(RelativeLayout):
    def __init__(self, **kwargs):
        kwargs["pos_hint"] = {'center_x': 0.5, 'center_y': 0.5}
        super(MenuLayout, self).__init__(**kwargs)

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

    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(SudokuLayout(self.grid,
                                       size_hint=(None, None), width=400, height=420))
        layout.add_widget(MenuLayout(size_hint=(
            None, None), width=400, height=130))
        return layout


if __name__ == '__main__':
    SudokuVisualizer().run()
