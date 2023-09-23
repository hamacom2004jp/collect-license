from pathlib import Path
import logging
import logging.config
import traceback
import sys
import yaml


PGM_DIR = Path("collectlicense")
APP_ID = 'collectlicense'
CMD = None

def load_config():
    global CMD
    logging.config.dictConfig(yaml.safe_load(open(PGM_DIR / "logconf.yml", encoding='UTF-8').read()))
    logger = logging.getLogger('main')
    with open(PGM_DIR / 'config.yaml') as f:
        config = yaml.safe_load(f)
        c = config['collectlicense']['common']
        CMD = c['CMD']
    return config, logger

def mkdirs(dir_path:Path):
    if not dir_path.exists():
        dir_path.mkdir(parents=True)
    if not dir_path.is_dir():
        raise BaseException(f"Don't make diredtory.({str(dir_path)})")
    return dir_path

def e_msg(e:Exception, logger):
    tb = sys.exc_info()[2]
    logger.error(traceback.format_exc())
    return e.with_traceback(tb)

