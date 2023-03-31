from lib import action
from dda_python_terraform import IsFlagged


class Destroy(action.TerraformBaseAction):
    def run(self, plan_path, state_file_path, target_resources, terraform_exec,
            variable_dict, variable_files, env_variable_dict):
        """
        Destroy Terraform managed infrastructure

        Args:
        - plan_path: path of the Terraform files
        - state_file_path: path of the Terraform state file
        - target_resources: list of resources to target from the configuration
        - terraform_exec: path of the Terraform bin
        - variable_dict: dictionary of Terraform variables that will overwrite
            the variable files if both are declared
        - variable_files: array of Terraform variable files
        - env_variable_dict: array dedicated for sensitive environment variables

        Returns:
        - dict: Terraform destroy command output
        """
        self.set_env_variable_dict(env_variable_dict)
        self.terraform.working_dir = plan_path
        self.terraform.terraform_bin_path = terraform_exec
        self.set_semantic_version()
        self.terraform.targets = target_resources
        return_code, stdout, stderr = self.terraform.destroy(
            var_file=variable_files,
            var=variable_dict,
            state=state_file_path,
            force=IsFlagged,
            capture_output=False,
            raise_on_error=False
        )

        return self.check_result(
            return_code,
            stdout,
            stderr,
            return_output=True)
