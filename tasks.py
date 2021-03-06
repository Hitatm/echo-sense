from models import *
from constants import *
import outbox
import handlers
from decorators import deferred_task_decorator

@deferred_task_decorator
def bgRunSensorProcess(sptkey=None):
    from workers import SensorProcessWorker
    logging.info("bgRunSensorProcess: %s" % sptkey)
    if sptkey:
        spt = SensorProcessTask.get(sptkey)
        if spt and spt.should_run():
            worker = SensorProcessWorker(spt)
            worker.run()
        else:
            logging.debug("Can't/shouldn't run task")

