# Change Log

## 0.2.1
- Fixed: The name of the workflow `pipeline` needed to be changed to match what is in the metadata.
- Removed the `no_deploy` calls in plan.  This is now a `fail`.
- Fixed: Calls from the `pipeline` workflow into `plan` and `apply` were using the wrong input name.

## 0.2.0

- Set auto_approve = True for applying changes

## 0.1.0

- First release
