from lib import action
import os

class Destroy(action.BaseAction):
    def run(self, planpath, variable_files):
      os.chdir(planpath)
      return_code, stdout, stderr =  self.terraform.destroy(planpath, var_file=variable_files, force=true)
      output = stdout + "\n" + stderr
      if return_code == 0:
        return (True, output)
      else:
	    return (False, output)
