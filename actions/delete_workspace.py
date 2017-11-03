import os
from lib import action
from python_terraform import *

class DeleteWorkspace(action.BaseAction):
    def run(self, planpath, workspace):
        """
        Create Terraform workspace

        Args:
        - planpath: path of the Terraform files
        - workspace: The name of the workspace to delete

        Returns:
        - dict: Terraform workspace delete command output
        """
        os.chdir(planpath)
        return_code, stdout, stderr = self.terraform.workspace("delete", workspace, planpath)
        output = stdout + "\n" + stderr
        if return_code == 0:
            return (True, output)
        else:
            return (False, output)
