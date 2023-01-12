import os
from lib import action


class CreateWorkspace(action.TerraformBaseAction):
    def run(self, plan_path, terraform_exec, workspace):
        """
        Create Terraform workspace

        Args:
        - plan_path: path of the Terraform files
        - terraform_exec: path of the Terraform bin
        - workspace: The name of the workspace to create

        Returns:
        - dict: Terraform workspace new command output
        """
        os.chdir(plan_path)
        self.terraform.terraform_bin_path = terraform_exec
        self.set_semantic_version()
        return_code, stdout, stderr = self.terraform.workspace("new", workspace,
                                                               '-no-color',
                                                               raise_on_error=False)
        return self.check_result(return_code, stdout, stderr)
