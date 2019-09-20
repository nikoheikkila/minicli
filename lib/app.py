import sys

from typing import Callable, Dict, List, Optional
from .printer import Printer


class App:
    def __init__(self, printer: Printer):
        self.registry: Dict[str, Callable] = {}
        self._printer = printer

    @property
    def printer(self) -> Printer:
        return self._printer

    @staticmethod
    def has_arg(args: List[str], i: int) -> Optional[str]:
        try:
            return args[i]
        except IndexError:
            return None

    def register_commands(self, commands: Dict[str, Callable]):
        for name, closure in commands.items():
            self.registry[name] = closure

    def get_command(self, command: str) -> Optional[Callable]:
        if command in self.registry:
            return self.registry[command]()

        return None

    def run_command(self, args: List[str] = []):
        command_name = "help"

        if self.has_arg(args, 1):
            command_name = args[1]

        command = self.get_command(command_name)

        if command is None:
            self.printer.display(f"ERROR: Command {command_name} not found.")
            sys.exit(1)

        command.handle(*args)
