import os
from lib import action
from python_terraform import IsFlagged, IsNotFlagged


class Init(action.TerraformBaseAction):
    def run(self, plan_path, terraform_exec, backend, upgrade):
        """
        Initialize a working directory containing Terraform configuration files

        Args:
        - plan_path: path of the Terraform files
        - terraform_exec: path of the Terraform bin
        - backend: backend configuration variable file
        - upgrade: Run init with -upgrade option

        Returns:
        - dict: Terraform init command output
        """
        os.chdir(plan_path)
        self.terraform.terraform_bin_path = terraform_exec

        return_code, stdout, stderr = self.terraform.init(
            plan_path,
            backend_config=backend,
            capture_output=False,
            upgrade=IsFlagged if upgrade else IsNotFlagged
        )

        return self.check_result(return_code, stdout, stderr)
