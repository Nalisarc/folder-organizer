#!/usr/bin/env python3
  import pathlib
  import configparser
  import logging
  from rich.logging import RichHandler

    FILETYPES = {
        "Documents": ("*.pdf","*.epub","*.mobi"),
        "Music": ("*.mp3","*.ogg","*.wav"),
        "Pictures": ("*.jpeg","*.jpg","*.png"),
        "Videos": ("*.mp4","*.mkv"),
        "Archives": ("*.zip", "*.tar", "*.gzip", "*.7z")
    }

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

    def movefiles():
        for ftype in FILETYPES:
            for fformat in FILETYPES[ftype]:
                filelist = glob(fformat)
                for f in filelist:
                    os.rename(f, ftype+"/"+f)
        return None

  def main():
      if len(os.listdir(".")) == 0:
          #print("Empty Directory. Exiting")
          return 1
      mkdirs()
      movefiles()
      return 0

  if __name__ == '__main__':
      s = main()
      sys.exit(s)
