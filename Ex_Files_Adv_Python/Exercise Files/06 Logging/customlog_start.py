# Demonstrate how to customize logging output

import logging

# TODO: add another function to log from
def anotherFunction():
    logging.debug("this is debug level message")

def main():
    # set the output file and debug level, and
    # TODO: use a custom formatting specification
    fmtstr = "%(asctime)s: %(levelname)s: %(funcName)s line:%(lineno)d %(message)s"
    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG, filemode="w", format=fmtstr)
    
    logging.info("This is an info-level log message")
    logging.warning("This is a warning-level message")
    anotherFunction()


if __name__ == "__main__":
    main()
