from st2common.runners.base_action import Action
from python_terraform import Terraform

class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        self.terraform = Terraform()
