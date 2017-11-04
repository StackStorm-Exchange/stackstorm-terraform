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
        return self.terraform.init(planpath, backend_config=backend)
