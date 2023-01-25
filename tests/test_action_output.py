from terraform_base_action_test_case import TerraformBaseActionTestCase
from output import Output
import mock


class OutputTestCase(TerraformBaseActionTestCase):
    __test__ = True
    action_cls = Output

    def test_init(self):
        action = self.get_action_instance({})
        self.assertIsInstance(action, Output)

    @mock.patch("lib.action.Terraform.output")
    def test_run_state_file(self, mock_output):
        action = self.get_action_instance({})
        # Declare test input values
        test_plan_path = "/terraform"
        test_state_file_path = "/path/to/state/file"
        test_terraform_exec = "/usr/bin/terraform"

        # Declare test Terraform.output return values
        expected_result = "result"
        mock_output.return_value = expected_result

        # Execute the run function
        result = action.run(test_plan_path, test_state_file_path, test_terraform_exec)

        # Verify the results
        self.assertEqual(result, expected_result)
        self.assertEqual(action.terraform.terraform_bin_path, test_terraform_exec)
        self.assertTrue(mock_output.called)
        mock_output.assert_called_with(state=test_state_file_path)

    @mock.patch("lib.action.Terraform.output")
    def test_run_no_state_file(self, mock_output):
        action = self.get_action_instance({})
        # Declare test input values
        test_plan_path = "/terraform"
        test_terraform_exec = "/usr/bin/terraform"

        # Declare test Terraform.output return values
        expected_result = "result"
        mock_output.return_value = expected_result

        # Execute the run function
        result = action.run(test_plan_path, None, test_terraform_exec)

        # Verify the results
        self.assertEqual(result, expected_result)
        self.assertEqual(action.terraform.terraform_bin_path, test_terraform_exec)
        self.assertTrue(mock_output.called)
        mock_output.assert_called_with(state=None)
