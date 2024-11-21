import argparse
import json
import logging

from .console import ConsolePrinter
from .file_manager import FileManager

def parse_cli_args():
    parser = argparse.ArgumentParser(
        prog="exerpyse",
        description="Learn Python by exercise.",
        epilog="Made with <3 by Sivam Pasupathipillai.",
    )
    parser.add_argument("--debug", dest="debug", action="store_true")
    sub_parsers = parser.add_subparsers()
    start_parser = sub_parsers.add_parser("start", help="start the exerpyse program.")
    return vars(parser.parse_args())


def configure_logging(config: dict):
    log_format = "%(asctime)s %(levelname)s %(filename)s::%(lineno)d - %(message)s"
    date_fmt = "%Y-%m-%d %H:%M:%S"
    if config["debug"]:
        logging.basicConfig(level=logging.DEBUG, format=log_format, datefmt=date_fmt)
    else:
        logging.basicConfig(level=logging.WARN, format=log_format, datefmt=date_fmt)


def run():
    config = parse_cli_args()
    configure_logging(config)

    logging.debug("Config: %s", json.dumps(config, indent=2))

    console = ConsolePrinter()
    console.print_greeting()

    file_manager = FileManager(console)
    file_manager.setup_exercises()


if __name__ == "__main__":
    run()
