from LoggerInterface import ImplementLogger


class ConsoleLogger(ImplementLogger):
    def log(self, msg: str):
        print(msg)
