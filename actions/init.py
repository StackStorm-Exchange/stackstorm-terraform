import os
from lib import action


class Init(action.TerraformBaseAction):
    def run(self, plan_path, terraform_exec, backend):
        """
        Initialize a working directory containing Terraform configuration files

        Args:
        - plan_path: path of the Terraform files
        - terraform_exec: path of the Terraform bin
        - backend: backend configuration variable file

        Returns:
        - dict: Terraform init command output
        """
        os.chdir(plan_path)
        self.terraform.terraform_bin_path = terraform_exec
        return_code, stdout, stderr = self.terraform.init(plan_path, backend_config=backend)
        output = stdout + "\n" + stderr
        if return_code == 0:
            return (True, output)
        else:
            return (False, output)
