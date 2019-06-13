import os
from lib import action


class Destroy(action.TerraformBaseAction):
    def run(self, plan_path, state_file_path, terraform_exec,
            variable_dict, variable_files):
        """
        Destroy Terraform managed infrastructure

        Args:
        - plan_path: path of the Terraform files
        - state_file_path: path of the Terraform state file
        - terraform_exec: path of the Terraform bin
        - variable_dict: dictionary of Terraform variables that will overwrite the
            variable files if both are declared
        - variable_files: array of Terraform variable files

        Returns:
        - dict: Terraform destroy command output
        """
        os.chdir(plan_path)
        self.terraform.terraform_bin_path = terraform_exec
        return_code, stdout, stderr = self.terraform.destroy(plan_path, var_file=variable_files,
                                                             var=variable_dict,
                                                             state=state_file_path,
                                                             force="true")
        return self.check_result(return_code, stdout, stderr)
