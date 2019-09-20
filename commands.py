from lib.app import App
from lib.printer import Printer
from controllers.hello import Hello
from controllers.help import Help

app = App(Printer())

commands = {"help": Help, "hello": Hello}

app.register_commands(commands)
