import os
from lib import action


class Import(action.TerraformBaseAction):
    def run(self, hypervisor_object, plan_path, resource_name, state_file_path,
            terraform_exec, variable_dict, variable_files):
        """
        Import existing infrastructure into a Terraform state

        Args:
        - hypervisor_object: name or path of the hypervisor object to import
        - plan_path: path of the Terraform files
        - resource_name: name of the Terraform resource to import an object into
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
        return_code, stdout, stderr = self.terraform.import_cmd(resource_name, hypervisor_object,
                                                                state=state_file_path,
                                                                var_file=variable_files,
                                                                var=variable_dict)
        return self.check_result(return_code, stdout, stderr)
