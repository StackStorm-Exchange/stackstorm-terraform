from terraform_base_action_test_case import TerraformBaseActionTestCase
from output import Output
import mock


class OutputTestCase(TerraformBaseActionTestCase):
    __test__ = True
    action_cls = Output

    def test_init(self):
        action = self.get_action_instance({})
        self.assertIsInstance(action, Output)

    @mock.patch("output.os.chdir")
    @mock.patch("lib.action.Terraform.output")
    def test_run(self, mock_output, mock_chdir):
        action = self.get_action_instance({})
        # Declare test input values
        test_plan_path = "/terraform"
        test_terraform_exec = "/usr/bin/terraform"

        # Declare test Terraform.output return values
        expected_result = "result"
        mock_output.return_value = expected_result

        mock_chdir.return_value = "success"

        # Execute the run function
        result = action.run(test_plan_path, test_terraform_exec)

        # Verify the results
        self.assertEqual(result, expected_result)
        self.assertEqual(action.terraform.terraform_bin_path, test_terraform_exec)
        self.assertTrue(mock_output.called)
        mock_chdir.assert_called_with(test_plan_path)
