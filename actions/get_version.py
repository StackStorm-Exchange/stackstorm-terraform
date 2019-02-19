from lib import action


class GetVersion(action.TerraformBaseAction):
    def run(self, terraform_exec):
        """
        Get the Terraform version

        Args:
        - terraform_exec: path of the Terraform bin

        Returns:
        - dict: Terraform version
        """

        self.terraform.terraform_bin_path = terraform_exec
        return_code, stdout, stderr = self.terraform.version()

        return self.check_result(return_code, stdout, stderr)
