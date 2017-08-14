# Terraform Integration Pack

This integration pack allows StackStorm to control [Terraform](http://packer.io),
a tool for creating machine and container images for multiple platforms
from a single source configuration.

Requires `terraform` to be installed on Worker nodes. See _configuration_ for
additional details.

## Configuration

Copy the example configuration in [packer.yaml.example](./packer.yaml.example)
to `/opt/stackstorm/configs/packer.yaml` and edit as required.

It may contain this configuration:

* `exec_path` - full path to packer binary (default: /usr/local/bin/packer)
* `atlas_token` - Hashicorp Atlas token, needed for `push` action.
* `variables` - variables passed to Packer. Takes a dict

You can also use dynamic values from the datastore. See the
[docs](https://docs.stackstorm.com/reference/pack_configs.html) for more info.

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`

## Actions
* `terraform.apply`    - Build images from a packer template
* `terraform.destroy`      - Takes a template and finds backwards
                      incompatible parts of it and brings it
                      up to date so it can be used with the
                      latest version of Packer
* `terraform.show`  - Takes a template and outputs the
                      various components a template defines
