from st2common.runners.base_action import Action
from dda_python_terraform import Terraform
import json
import os


class TerraformBaseAction(Action):

    def __init__(self, config):
        """Creates a new BaseAction given a StackStorm config object
        (kwargs works too). Also stores the Terraform class from
        dda_python_terraform in a class variable
        :param config: StackStorm configuration object for the pack
        :returns: a new BaseAction
        """
        super(TerraformBaseAction, self).__init__(config)
        self.terraform = Terraform()

    def check_result(self, return_code, stdout, stderr, return_output=False,
                     valid_return_codes=None):
        """Check the return code from the terraform action and return the
        output with the error message (if there is one)
        :param return_code: return code from the Terraform command that was run
        :param stdout: output from the Terraform command that was run
        :param stderr: error message (if any) from the Terraform command
        :param return_output: whether to return the results of
                              `terraform output` command
        :param valid_return_codes: list of valid return codes
        :returns: success flag for the st2 action and output from the
                  Terraform command
        """
        if valid_return_codes is None:
            valid_return_codes = [0]
        if return_output:
            output = None
            if return_code in valid_return_codes:
                output = self.terraform.output(state=self.terraform.state)
        else:
            output = TerraformBaseAction.concat_std_output(stdout, stderr)

        # Capture success status vs valid return codes and return result
        success = (return_code in valid_return_codes)
        return success, output

    def set_semantic_version(self):
        """Set the semantic version string on the dda terraform library.
        This is called with each action in case the different exec is
        set.
        """
        # Get the verison of terraform
        _, stdout, _ = self.terraform.version(json=True)
        version = json.loads(stdout)['terraform_version']
        self.terraform.terraform_semantic_version = version

    @staticmethod
    def concat_std_output(stdout, stderr):
        """Combines stdout and stderr from terraform execution,
        one or the other can be None
        :param stdout: results from stdout
        :param stderr: results from stderr
        :returns: string concatenation
        """
        output = None
        if stderr or stdout:
            output = ''
            if stdout:
                output += stdout
            if stderr:
                if stdout:
                    output += "\n"
                output += stderr

        return output

    def set_env_variable_dict(self, env_variable_dict=None):
        try:
            if env_variable_dict:
                for env_var_name in env_variable_dict.keys():
                    value = str(env_variable_dict.get(env_var_name))
                    os.environ[str(env_var_name)] = f"{value}"
            return True
        except:
            return False
