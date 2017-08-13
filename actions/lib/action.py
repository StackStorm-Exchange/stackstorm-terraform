from st2actions.runners.pythonrunner import Action
from python_terraform import *

class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        self._working_dir = self.config.get('working_dir', '/root')

    def terraform(self,
        return Terraform(working_dir=self._working_dir)
