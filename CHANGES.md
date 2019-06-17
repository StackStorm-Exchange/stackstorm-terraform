# Change Log

## 0.2.6

- Added: variable_dict variable to pipeline workflow

## 0.2.5

- Fixed: requirements.txt was installing an old version of the python-terraform module

## 0.2.4

- Added: action to import objects into terraform files
- Added: state_file_path and variable_dict variables to destroy action

## 0.2.3

- Added: state_file_path variable to plan and apply actions to specify state file to use.
- Added: target_resources variable to plan and apply actions to specify target resources.
- Added: variable_dict variable to plan and apply actions to pass variables to terraform without needing a file.
- Added: tests folder with unit tests for python actions.
- Added: check_result function to lib/action.py that was used in most actions.

## 0.2.2

- Fixed: The `pipeline` and `init` workflows need the `backend` parameter to be an object.

## 0.2.1

- Fixed: The name of the workflow `pipeline` needed to be changed to match what is in the metadata.
- Removed the `no_deploy` calls in plan.  This is now a `fail`.
- Fixed: Calls from the `pipeline` workflow into `plan` and `apply` were using the wrong input name.

## 0.2.0

- Set auto_approve = True for applying changes

## 0.1.0

- First release
