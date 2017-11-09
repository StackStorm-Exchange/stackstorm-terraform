import os
from lib import action


class ListWorkspaces(action.TerraformBaseAction):
    def run(self, plan_path, terraform_exec):
        """
        List Terraform workspaces

        Args:
        - plan_path: path of the Terraform files
        - terraform_exec: path of the Terraform bin

        Returns:
        - dict: Terraform workspace list command output
        """
        os.chdir(plan_path)
        self.terraform.terraform_bin_path = terraform_exec
        return_code, stdout, stderr = self.terraform.workspace("list", plan_path)
        output = stdout + "\n" + stderr
        if return_code == 0:
            return (True, output)
        else:
            return (False, output)
