from LoggerInterface import ImplementLogger


class FileLogger(ImplementLogger):

    def log(self, msg: str):
        text_file = open("log.txt", "w")
        text_file.write("result_message:  %s" % msg)
        text_file.close()

