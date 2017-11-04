import os
from lib import action

class Output(action.TerraformBaseAction):
    def run(self, planpath, terraform_exec):
        """
        Output output variables from the state file.

        Args:
        - planpath: path of the Terraform files
        - terraform_exec: path of the Terraform bin

        Returns:
        - dict: Terraform output command output
        """
        os.chdir(planpath)
        self.terraform.terraform_bin_path = terraform_exec
        return self.terraform.output(planpath, -json)
