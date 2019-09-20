from .command import Command


class Help(Command):
    def __init__(self):
        super().__init__()

    def handle(self, *args):
        self.app.printer.display("Usage: minicli hello [your name]")
