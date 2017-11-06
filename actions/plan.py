import os
from lib import action

class Plan(action.TerraformBaseAction):
    def run(self, plan_path, terraform_exec, variable_files):
        """
        Plan the changes required to reach the desired state of the configuration

        Args:
        - plan_path: path of the Terraform files
        - terraform_exec: path of the Terraform bin
        - var_file: array of Terraform variable files

        Returns:
        - dict: Terraform plan command output
        """
        os.chdir(plan_path)
        self.terraform.terraform_bin_path = terraform_exec
        return_code, stdout, stderr = self.terraform.plan(plan_path, var_file=variable_files)
        output = stdout + "\n" + stderr
        if return_code == 0:
            return (True, output)
        elif return_code == 2:
            return (True, output)
        else:
            return (False, output)
