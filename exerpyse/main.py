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
    sub_parsers = parser.add_subparsers(dest="subcommand")
    sub_parsers.add_parser("start", help="starts the exerpyse program.")
    sub_parsers.add_parser("reset", help="resets the exercise folder.")
    return vars(parser.parse_args())


def configure_logging(config: dict):
    log_format = (
        "%(asctime)s %(levelname)s %(filename)s::%(lineno)d - %(message)s"
    )
    date_fmt = "%Y-%m-%d %H:%M:%S"
    if config["debug"]:
        logging.basicConfig(
            level=logging.DEBUG, format=log_format, datefmt=date_fmt
        )
    else:
        logging.basicConfig(
            level=logging.WARN, format=log_format, datefmt=date_fmt
        )


def run_start(config: dict):
    console = config["console"]
    file_manager = config["file_manager"]

    console.print_greeting()

    file_manager.setup_exercises()


def run_reset(config: dict):
    console = config["console"]
    file_manager = config["file_manager"]

    console.print_greeting()
    ack = console.check_reset()
    if ack:
        console.print_reset()
        file_manager.clear_exercises()
        file_manager.setup_exercises()


_RUNNERS = {
    "reset": run_reset,
    "start": run_start,
}


def run():
    config = parse_cli_args()
    configure_logging(config)
    logging.debug("Config: %s", json.dumps(config, indent=2))

    config["console"] = ConsolePrinter()
    config["file_manager"] = FileManager()

    _RUNNERS[config["subcommand"]](config)


if __name__ == "__main__":
    run()
