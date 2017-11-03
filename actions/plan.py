import os
from lib import action

class Plan(action.BaseAction):
    def run(self, planpath, variable_files):
        """
        Plan the changes required to reach the desired state of the configuration

        Args:
        - planpath: path of the Terraform files
        - var_file: array of Terraform variable files

        Returns:
        - dict: Terraform plan command output
        """
        os.chdir(planpath)
        return_code, stdout, stderr = self.terraform.plan(planpath, var_file=variable_files)
        output = stdout + "\n" + stderr
        if return_code == 0:
            return (True, output)
        elif return_code == 2:
            return (True, output)
        else:
	        return (False, output)
