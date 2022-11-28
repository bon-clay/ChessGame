from __future__ import annotations
from models import Place, GameState


class App:

    def __init__(self, controller, view, chess_engine):
        self.engine = chess_engine
        self.controller = controller
        self.view = view

    def run(self):
        self._create_game()
        self._main_loop()

    def _main_loop(self):
        while not self.engine.is_game_over():
            self._make_turn()
        self._game_over()

    def _make_turn(self):
        game_state: GameState = self.engine.get_state()
        chosen_figure: Place | None = None
        places: tuple[Place] | None = None

        turn_result: Place | None = None
        while turn_result is not None:
            self.view.prepare(game_state)
            chosen_figure = self.controller.choice_figure(
                game_state)
            places = self.engine.get_places(
                chosen_figure)
            self.view.show_pre_turn(chosen_figure, places)
            turn_result = self.controller.make_turn(places)
        self.engine.make_turn(chosen_figure, turn_result)

    def _create_game(self):
        self.view.create_game()

    def _game_over(self):
        self.view.game_over()


if __name__ == '__main__':
    controller = None
    view = None
    chess_engine = None
    chess_game = App(controller, view, chess_engine)
    chess_game.run()
