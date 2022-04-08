import pathlib
import configparser
import logging
from rich.logging import RichHandler
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
CONFIGFILE = "settings.ini"

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")

def mkdirs(root=pathlib.Path('.')):
    for key in config['FILETYPES']:
        d = root / key
        
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

        for file_format in eval(config.get("FILETYPES", file_type)): #dangerous figure out something better
            log.info(f"Processing: {file_format}")
            files = root.glob(file_format)

            for f in files:
                log.info(f"Moving {f} to {root / file_type / f.name}")
                f.rename(root / file_type / f.name)

    log.info("finished")
    return None
    

def write_default_config(config=CONFIGFILE):
    
    config = configparser.ConfigParser()
    config["DEFAULT"] = {}
    config["FILETYPES"] = {
        "documents": ("*.pdf","*.epub","*.mobi","*.docx","*.pptx","*.xslx"),
        "music": ("*.mp3","*.ogg","*.wav"),
        "pictures": ("*.jpeg","*.jpg","*.png"),
        "videos": ("*.mp4","*.mkv"),
        "archives": ("*.zip", "*.tar", "*.gzip", "*.7z")}

    with open("settings.ini", 'w') as configfile:
        config.write(configfile)
        return None
    raise IOError

config = configparser.ConfigParser()
config.read(CONFIGFILE)
