import os
from lib import action

class Init(action.BaseAction):
    def run(self, planpath, backend):
        """
        Initialize a working directory containing Terraform configuration files

        Args:
        - planpath: path of the Terraform files
        - backend: backend configuration variable file

        Returns:
        - dict: Terraform init command output
        """
        os.chdir(planpath)
        return self.terraform.init(planpath, backend_config=backend)
