from lib import action
import os
from python_terraform import *

class CreateWorkspace(action.BaseAction):
    def run(self, planpath, workspace):
      os.chdir(planpath)
      return_code, stdout, stderr = self.terraform.workspace("new", workspace, planpath)
      output = stdout + "\n" + stderr
      if return_code == 0:
        return (True, output)
      else:
        return (False, output)
