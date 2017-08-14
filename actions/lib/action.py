from st2actions.runners.pythonrunner import Action
from python_terraform import *

class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        self.terraform = Terraform()
