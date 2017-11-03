import os
from lib import action
from python_terraform import *

class Show(action.BaseAction):
    def run(self, planpath):
        """
        Provide human-readable output from a state or plan file

        Args:
        - planpath: path of the Terraform files

        Returns:
        - dict: Terraform show command output
        """
        os.chdir(planpath)
        return_code, stdout, stderr = self.terraform.show(no_color=IsFlagged)
        output = stdout + "\n" + stderr
        if return_code == 0:
            return (True, output)
        else:
	        return (False, output)
