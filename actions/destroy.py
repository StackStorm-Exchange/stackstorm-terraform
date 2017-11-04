import os
from lib import action

class Destroy(action.TerraformBaseAction):
    def run(self, planpath, terraform_exec, variable_files):
        """
        Destroy Terraform managed infrastructure

        Args:
        - planpath: path of the Terraform files
        - terraform_exec: path of the Terraform bin
        - var_file: array of Terraform variable files

        Returns:
        - dict: Terraform destroy command output
        """
        os.chdir(planpath)
        self.terraform.terraform_bin_path = terraform_exec
        return_code, stdout, stderr =  self.terraform.destroy(planpath, var_file=variable_files, force="true")
        output = stdout + "\n" + stderr
        if return_code == 0:
            return (True, output)
        else:
	        return (False, output)
