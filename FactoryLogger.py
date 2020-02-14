from FileLogger import FileLogger
from ConsoleLogger import ConsoleLogger
from DatabaseLogger import DatabaseLogger


class Logger:
    __switcher = dict

    def return_result(self, selector: int):
        switcher = {
            1: ConsoleLogger(),
            2: FileLogger(),
            3: DatabaseLogger()
        }
        func = switcher.get(selector)
        return func
