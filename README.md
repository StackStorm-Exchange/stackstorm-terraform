# Terraform Integration Pack

This integration pack allows StackStorm to control [Terraform](https://www.terraform.io/),
A tool that enables you to safely and predictably create, change, and improve production infrastructure.

Requires `terraform` to be installed on Worker nodes. 

## Configuration

There are currently no configuration parameters.

## Actions
* `terraform.apply`    - Apply the changes required to reach the desired state of the configuration
* `terraform.destroy`  - Destroy the Terraform-managed infrastructure
* `terraform.show`     - Provides human-readable output from a state or plan file
