from lib import action
from dda_python_terraform import IsFlagged, IsNotFlagged


class Init(action.TerraformBaseAction):
    def run(self, plan_path, terraform_exec, backend, upgrade, env_variable_dict):
        """
        Initialize a working directory containing Terraform configuration files

        Args:
        - plan_path: path of the Terraform files
        - terraform_exec: path of the Terraform bin
        - backend: backend configuration variable file
        - upgrade: Run init with -upgrade option
        - env_variable_dict: array dedicated for sensitive environment variables

        Returns:
        - dict: Terraform init command output
        """
        self.set_env_variable_dict(env_variable_dict)
        self.terraform.working_dir = plan_path
        self.terraform.terraform_bin_path = terraform_exec
        self.set_semantic_version()

        return_code, stdout, stderr = self.terraform.init(
            backend_config=backend,
            capture_output=False,
            upgrade=IsFlagged if upgrade else IsNotFlagged,
            raise_on_error=False
        )

        return self.check_result(return_code, stdout, stderr)
