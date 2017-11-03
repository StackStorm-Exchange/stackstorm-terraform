import os
from lib import action

class Destroy(action.BaseAction):
    def run(self, planpath, variable_files):
        """
        Destroy Terraform managed infrastructure

        Args:
        - planpath: path of the Terraform files
        - var_file: array of Terraform variable files

        Returns:
        - dict: Terraform destroy command output
        """
        os.chdir(planpath)
        return_code, stdout, stderr =  self.terraform.destroy(planpath, var_file=variable_files, force="true")
        output = stdout + "\n" + stderr
        if return_code == 0:
            return (True, output)
        else:
	        return (False, output)
