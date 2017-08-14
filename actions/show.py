from lib import action
import os
from python_terraform import *

class Show(action.BaseAction):
    def run(self, planpath):
      os.chdir(planpath)
      return self.terraform.show(no_color=IsFlagged)
