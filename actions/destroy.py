from lib import action
import os

class Destroy(action.BaseAction):
    def run(self, planpath):
      os.chdir(planpath)
      return self.terraform.destroy(planpath)
