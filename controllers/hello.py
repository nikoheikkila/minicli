from .command import Command


class Hello(Command):
    def __init__(self):
        super().__init__()

    def handle(self, *args):
        if self.app.has_arg(args, 2):
            name = args[2]
        else:
            name = "World"

        self.app.printer.display(f"Hello {name}!")
