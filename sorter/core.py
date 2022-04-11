import pathlib
import configparser
import logging
from rich.logging import RichHandler

config = "settings.ini"

logging.basicConfig(filename='example.log',
                    encoding='utf-8', level=logging.DEBUG)

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")


def mkdirs(root=pathlib.Path('.')):
    for key in config['FILETYPES']:
        d = (root / key)

        if d.exists():
            log.info(f"{d} exists. skipping")
            pass
        else:
            log.info(f"creating {d}")
            d.mkdir()

    return None


def move_files(root=pathlib.Path('.')):

    for file_type in config["FILETYPES"]:
        log.info(f"Processing: {file_type}")

        # dangerous figure out something better
        for file_format in eval(config.get("FILETYPES", file_type)):
            log.info(f"Processing: {file_format}")
            files = root.glob(file_format)

            for f in files:
                log.info(f"Moving {f} to {root / file_type / f.name}")
                f.rename(root / file_type / f.name)

    log.info("finished")
    return None
