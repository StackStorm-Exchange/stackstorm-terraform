import os
from lib import action
from python_terraform import IsFlagged


class Apply(action.TerraformBaseAction):
    def run(self, plan_path, state_file_path, target_resources, terraform_exec,
            variable_dict, variable_files):
        """
        Apply the changes required to reach the desired state of the configuration.

        Args:
        - plan_path: path of the Terraform files
        - state_file_path: path of the Terraform state file
        - target_resources: list of resources to target from the configuration
        - terraform_exec: path of the Terraform bin
        - variable_dict: dictionary of Terraform variables that will overwrite the
            variable files if both are declared
        - variable_files: array of Terraform variable files

        Returns:
        - dict: Terraform output command output
        """
        os.chdir(plan_path)
        self.terraform.state = state_file_path
        self.terraform.targets = target_resources
        self.terraform.terraform_bin_path = terraform_exec
        self.terraform.var_file = variable_files
        self.terraform.variables = variable_dict

        return_code, stdout, stderr = self.terraform.apply(
            plan_path,
            skip_plan=True,
            auto_approve=IsFlagged,
            capture_output=False
        )

        return self.check_result(return_code, stdout, stderr, return_output=True)
