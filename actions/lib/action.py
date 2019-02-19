from st2common.runners.base_action import Action
from python_terraform import Terraform


class TerraformBaseAction(Action):
    def __init__(self, config):
        """Creates a new BaseAction given a StackStorm config object (kwargs works too)
        Also stores the Terraform class from python_terraform in a class variable
        :param config: StackStorm configuration object for the pack
        :returns: a new BaseAction
        """
        super(TerraformBaseAction, self).__init__(config)
        self.terraform = Terraform()

    def check_result(self, return_code, stdout, stderr):
        """Check the return code from the terraform action and return the output with
        the error message (if there is one)
        :param return_code: return code from the Terraform command that was run
        :param stdout: output from the Terraform command that was run
        :param stderr: error message (if any) from the Terraform command
        :returns: success flag for the st2 action and output from the Terraform command
        """
        output = stdout + "\n" + stderr
        if return_code == 0:
            return (True, output)
        else:
            return (False, output)
