from lib import action
import os

class Plan(action.BaseAction):
    def run(self, planpath, variable_files):
      os.chdir(planpath)
      return_code, stdout, stderr = self.terraform.plan(planpath, var_file=variable_files)
      output = stdout + "\n" + stderr
      if return_code == 0:
        return (True, output)
      elif return_code == 2:
        return (True, output)
      else:
	    return (False, output)
