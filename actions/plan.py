import os
from lib import action

class Plan(action.TerraformBaseAction):
    def run(self, planpath, terraform_exec, variable_files):
        """
        Plan the changes required to reach the desired state of the configuration

        Args:
        - planpath: path of the Terraform files
        - terraform_exec: path of the Terraform bin
        - var_file: array of Terraform variable files

        Returns:
        - dict: Terraform plan command output
        """
        os.chdir(planpath)
        self.terraform.terraform_bin_path = terraform_exec
        return_code, stdout, stderr = self.terraform.plan(planpath, var_file=variable_files)
        output = stdout + "\n" + stderr
        if return_code == 0:
            return (True, output)
        elif return_code == 2:
            return (True, output)
        else:
	        return (False, output)
