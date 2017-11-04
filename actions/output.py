import os
from lib import action

class Output(action.TerraformBaseAction):
    def run(self, plan_path, terraform_exec):
        """
        Output output variables from the state file.

        Args:
        - plan_path: path of the Terraform files
        - terraform_exec: path of the Terraform bin

        Returns:
        - dict: Terraform output command output
        """
        os.chdir(plan_path)
        self.terraform.terraform_bin_path = terraform_exec
        return self.terraform.output(plan_path, -json)
