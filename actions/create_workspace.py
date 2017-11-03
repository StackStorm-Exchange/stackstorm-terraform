import os
from lib import action

class CreateWorkspace(action.BaseAction):
    def run(self, planpath, workspace):
        """
        Create Terraform workspace

        Args:
        - planpath: path of the Terraform files
        - workspace: The name of the workspace to create

        Returns:
        - dict: Terraform workspace new command output
        """
        os.chdir(planpath)
        return_code, stdout, stderr = self.terraform.workspace("new", workspace, planpath)
        output = stdout + "\n" + stderr
        if return_code == 0:
            return (True, output)
        else:
            return (False, output)
