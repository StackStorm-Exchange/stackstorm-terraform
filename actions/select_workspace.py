import os
from lib import action


class SelectWorkspace(action.TerraformBaseAction):
    def run(self, plan_path, terraform_exec, workspace):
        """
        Select Terraform workspace

        Args:
        - plan_path: path of the Terraform files
        - terraform_exec: path of the Terraform bin
        - workspace: The name of the workspace to select

        Returns:
        - dict: Terraform workspace select command output
        """
        os.chdir(plan_path)
        self.terraform.terraform_bin_path = terraform_exec
        return_code, stdout, stderr = self.terraform.workspace("select", workspace,
                                                               '-no-color')
        return self.check_result(return_code, stdout, stderr)
