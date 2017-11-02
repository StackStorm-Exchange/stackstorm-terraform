import os
from lib import action
from python_terraform import *

class ListWorkspaces(action.BaseAction):
    def run(self, planpath):
        os.chdir(planpath)
        return_code, stdout, stderr = self.terraform.workspace("list", planpath)
        output = stdout + "\n" + stderr
        if return_code == 0:
            return (True, output)
        else:
            return (False, output)
