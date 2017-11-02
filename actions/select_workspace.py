import os
from lib import action
from python_terraform import *

class SelectWorkspace(action.BaseAction):
    def run(self, planpath, workspace):
        """
        Select Terraform workspace

        Args:
        - planpath: path of the Terraform files
        - workspace: The name of the workspace to select

        Returns:
        - dict: Terraform workspace select output
        """
        os.chdir(planpath)
        return_code, stdout, stderr = self.terraform.workspace("select", workspace, planpath)
        output = stdout + "\n" + stderr
        if return_code == 0:
            return (True, output)
        else:
            return (False, output)
