from terraform_base_action_test_case import TerraformBaseActionTestCase
from plan import Plan
import mock


class PlanTestCase(TerraformBaseActionTestCase):
    __test__ = True
    action_cls = Plan

    def test_init(self):
        action = self.get_action_instance({})
        self.assertIsInstance(action, Plan)

    @mock.patch("lib.action.TerraformBaseAction.set_semantic_version")
    @mock.patch("lib.action.TerraformBaseAction.check_result")
    @mock.patch("lib.action.Terraform.plan")
    def test_run(self, mock_plan, mock_check_result, mock_version):
        action = self.get_action_instance({})
        # Declare test input values
        test_plan_path = "/terraform"
        test_state_file = "/terraform/terraform.tfstate"
        test_target_resources = ["module.resource"]
        test_terraform_exec = "/usr/bin/terraform"
        test_variable_dict = {'key1': 'value1', 'key2': 'value2'}
        test_variable_files = ["/terraform/test.tfvars"]

        # Declare test Terraform.plan return values
        test_return_code = 0
        test_stdout = "Terraform has been successfully initialized!"
        test_stderr = ""

        mock_version.return_value = '1.1.1'
        mock_plan.return_value = test_return_code, test_stdout, test_stderr

        expected_result = "result"
        mock_check_result.return_value = expected_result

        # Execute the run function
        result = action.run(test_plan_path, test_state_file, test_target_resources,
                            test_terraform_exec, test_variable_dict, test_variable_files)

        # Verify the results
        self.assertEqual(result, expected_result)
        self.assertEqual(action.terraform.state, test_state_file)
        self.assertEqual(action.terraform.targets, test_target_resources)
        self.assertEqual(action.terraform.terraform_bin_path, test_terraform_exec)
        self.assertEqual(action.terraform.var_file, test_variable_files)
        self.assertEqual(action.terraform.variables, test_variable_dict)
        mock_plan.assert_called_with(test_plan_path, capture_output=False)
        mock_check_result.assert_called_with(
            test_return_code,
            test_stdout,
            test_stderr,
            return_output=True,
            valid_return_codes=[0, 2]
        )

    @mock.patch("lib.action.TerraformBaseAction.set_semantic_version")
    @mock.patch("lib.action.TerraformBaseAction.check_result")
    @mock.patch("lib.action.Terraform.plan")
    def test_run_exit_code_2(self, mock_plan, mock_check_result, mock_version):
        action = self.get_action_instance({})
        # Declare test input values
        test_plan_path = "/terraform"
        test_state_file = "/terraform/terraform.tfstate"
        test_target_resources = ["module.resource"]
        test_terraform_exec = "/usr/bin/terraform"
        test_variable_dict = {'key1': 'value1', 'key2': 'value2'}
        test_variable_files = ["/terraform/test.tfvars"]

        # Declare test Terraform.plan return values
        test_return_code = 2
        test_stdout = "Terraform has been successfully initialized!"
        test_stderr = ""

        mock_version.return_value = '1.1.1'
        mock_plan.return_value = test_return_code, test_stdout, test_stderr

        expected_result = "result"
        mock_check_result.return_value = expected_result

        # Execute the run function
        result = action.run(test_plan_path, test_state_file, test_target_resources,
                            test_terraform_exec, test_variable_dict, test_variable_files)

        # Verify the results
        self.assertEqual(result, expected_result)
        self.assertEqual(action.terraform.state, test_state_file)
        self.assertEqual(action.terraform.targets, test_target_resources)
        self.assertEqual(action.terraform.terraform_bin_path, test_terraform_exec)
        self.assertEqual(action.terraform.var_file, test_variable_files)
        self.assertEqual(action.terraform.variables, test_variable_dict)
        mock_plan.assert_called_with(test_plan_path, capture_output=False)
        mock_check_result.assert_called_with(
            test_return_code,
            test_stdout,
            test_stderr,
            return_output=True,
            valid_return_codes=[0, 2]
        )
