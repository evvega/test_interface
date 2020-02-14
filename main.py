from FactoryLogger import Logger


def main():
    __msg = str
    msg = 'hola'
    factory_miss: Logger = Logger()
    func = factory_miss.return_result(3)
    func.log(msg=msg)


if __name__ == "__main__":
    main()
