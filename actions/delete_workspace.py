import os
from lib import action


class DeleteWorkspace(action.TerraformBaseAction):
    def run(self, plan_path, terraform_exec, workspace):
        """
        Create Terraform workspace

        Args:
        - plan_path: path of the Terraform files
        - terraform_exec: path of the Terraform bin
        - workspace: The name of the workspace to delete

        Returns:
        - dict: Terraform workspace delete command output
        """
        os.chdir(plan_path)
        self.terraform.terraform_bin_path = terraform_exec
        return_code, stdout, stderr = self.terraform.workspace("delete", '-force', workspace, 
                                                               plan_path, '-no-color')
        output = stdout + "\n" + stderr
        if return_code == 0:
            return (True, output)
        else:
            return (False, output)
