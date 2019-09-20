from lib.app import App
from lib.printer import Printer


class Command:
    def __init__(self):
        self._app = App(Printer())

    @property
    def app(self) -> App:
        return self._app

    def handle(self, *args):
        pass
