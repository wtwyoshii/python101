from rich.console import Console

class Logger:
    def __init__(self):
        self.console = Console()

    def log_success(self, message):

        self.console.print(message, style="green")

    def log_error(self, message):

        self.console.print(message, style="red")