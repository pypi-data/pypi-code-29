from datetime import datetime
from path import Path
import inspect
import pytz

MODEL_DIR = Path(inspect.getsourcefile(lambda: 0)).abspath().parent

TF_LOGS = MODEL_DIR / 'tf_logs'
TF_SAVER = MODEL_DIR / 'tf_saver'

if not TF_LOGS.exists():
    TF_LOGS.mkdir()
if not TF_SAVER.exists():
    TF_SAVER.mkdir()

rome_tz = pytz.timezone('Europe/Rome')
rome_now = datetime.now(rome_tz).strftime("%Y%m%d_%H%M%S")
logdir = TF_LOGS / f'run-{rome_now}'
