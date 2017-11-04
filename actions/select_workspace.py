import os
from lib import action

class SelectWorkspace(action.TerraformBaseAction):
    def run(self, planpath, terraform_exec, workspace):
        """
        Select Terraform workspace

        Args:
        - planpath: path of the Terraform files
        - terraform_exec: path of the Terraform bin
        - workspace: The name of the workspace to select

        Returns:
        - dict: Terraform workspace select command output
        """
        os.chdir(planpath)
        self.terraform.terraform_bin_path = terraform_exec
        return_code, stdout, stderr = self.terraform.workspace("select", workspace, planpath)
        output = stdout + "\n" + stderr
        if return_code == 0:
            return (True, output)
        else:
            return (False, output)
