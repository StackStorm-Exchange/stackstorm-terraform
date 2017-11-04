import os
from lib import action

class Init(action.TerraformBaseAction):
    def run(self, planpath, terraform_exec, backend):
        """
        Initialize a working directory containing Terraform configuration files

        Args:
        - planpath: path of the Terraform files
        - terraform_exec: path of the Terraform bin
        - backend: backend configuration variable file

        Returns:
        - dict: Terraform init command output
        """
        os.chdir(planpath)
        self.terraform.terraform_bin_path = terraform_exec
        return_code, stdout, stderr = self.terraform.init(planpath, backend_config=backend)
        output = stdout + "\n" + stderr
        if return_code == 0:
            return (True, output)
        else:
            return (False, output)
