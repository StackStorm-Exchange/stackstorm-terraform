import os
from lib import action

class Show(action.TerraformBaseAction):
    def run(self, planpath, terraform_exec):
        """
        Provide human-readable output from a state or plan file

        Args:
        - planpath: path of the Terraform files
        - terraform_exec: path of the Terraform bin

        Returns:
        - dict: Terraform show command output
        """
        os.chdir(planpath)
        self.terraform.terraform_bin_path = terraform_exec
        return_code, stdout, stderr = self.terraform.show(no_color=IsFlagged)
        output = stdout + "\n" + stderr
        if return_code == 0:
            return (True, output)
        else:
	        return (False, output)
