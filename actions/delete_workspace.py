import os
from lib import action

class DeleteWorkspace(action.TerraformBaseAction):
    def run(self, planpath, terraform_exec, workspace):
        """
        Create Terraform workspace

        Args:
        - planpath: path of the Terraform files
        - terraform_exec: path of the Terraform bin
        - workspace: The name of the workspace to delete

        Returns:
        - dict: Terraform workspace delete command output
        """
        os.chdir(planpath)
        self.terraform.terraform_bin_path = terraform_exec
        return_code, stdout, stderr = self.terraform.workspace("delete", workspace, planpath)
        output = stdout + "\n" + stderr
        if return_code == 0:
            return (True, output)
        else:
            return (False, output)
