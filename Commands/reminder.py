from Commands import *
import time
import datetime
from threading import Thread
import re


class Reminder(AbstractCommand):

    @property
    def name(self) -> str:
        return 'REMINDER'

    @property
    def help(self) -> str:
        return 'Setting a reminder.\nFor example: REMINDER 2021-12-31 00:00\n'

    def can_execute(self, command: str) -> bool:
        self._match = re.search(rf'^{self.name} (\d\d\d\d)-(\d\d)-(\d\d) (\d\d):(\d\d)$', command)
        return bool(self._match)

    def execute(self):

        def wait():
            while datetime.datetime.now() < time_target:
                time.sleep(1)
            else:
                print('\n<REMINDER> :', notification, '\n==> ')
        try:
            time_target = datetime.datetime.now()
            time_target = time_target.replace(year=int(self._match.group(1)), month=int(self._match.group(2)), day=int(self._match.group(3)), hour=int(self._match.group(4)), minute=int(self._match.group(5)),
                                          second=0,
                                          microsecond=0)
            if datetime.datetime.now() > time_target: raise Exception()
            notification = input('What to remind?\n')
            print('Reminder set')
            th = Thread(target=wait, args=())
            th.start()
        except:
            print('Incorrect set time. Check your input')



