from lib import action


class Output(action.TerraformBaseAction):
    def run(self, plan_path, state_file_path, terraform_exec):
        """
        Output output variables from the state file.

        Args:
        - plan_path: path of the Terraform files
        - terraform_exec: path of the Terraform bin

        Returns:
        - dict: Terraform output command output
        """
        self.terraform.working_dir = plan_path
        self.terraform.terraform_bin_path = terraform_exec
        self.set_semantic_version()
        return self.terraform.output(state=state_file_path)
