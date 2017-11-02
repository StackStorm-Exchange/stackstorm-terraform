# Terraform Integration Pack

This integration pack allows StackStorm to control [Terraform](https://www.terraform.io/),
A tool that enables you to safely and predictably create, change, and improve production infrastructure.

Requires `terraform` to be installed on Worker nodes.

## Configuration

There are currently no configuration parameters.

## Actions
* `terraform.apply`            - Apply the changes required to reach the desired state of the configuration
* `terraform.create_workspace` - Create and switch to a new Terraform workspace
* `terraform.delete_workspace` - Delete a Terraform workspace
* `terraform.destroy`          - Destroy the Terraform-managed infrastructure
* `terraform.init`             - Initialize a working directory containing Terraform configuration files.
* `terraform.list_workspaces`  - List Terraform workspaces
* `terraform.plan`             - Plan the changes required to reach the desired state of the configuration
* `terraform.select_workspace` - Select a Terraform workspace
* `terraform.show`             - Provides human-readable output from a state or plan file
