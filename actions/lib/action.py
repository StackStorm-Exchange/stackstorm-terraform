from st2common.runners.base_action import Action
from python_terraform import Terraform


class TerraformBaseAction(Action):
    def __init__(self, config):
        super(TerraformBaseAction, self).__init__(config)
        self.terraform = Terraform()
