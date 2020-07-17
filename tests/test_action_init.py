from terraform_base_action_test_case import TerraformBaseActionTestCase
from init import Init
import mock


class InitTestCase(TerraformBaseActionTestCase):
    __test__ = True
    action_cls = Init

    def test_init(self):
        action = self.get_action_instance({})
        self.assertIsInstance(action, Init)

    @mock.patch("list_workspaces.os.chdir")
    @mock.patch("lib.action.TerraformBaseAction.check_result")
    @mock.patch("lib.action.Terraform.init")
    def test_run(self, mock_init, mock_check_result, mock_chdir):
        action = self.get_action_instance({})
        # Declare test input values
        test_plan_path = "/terraform"
        test_terraform_exec = "/usr/bin/terraform"
        test_backend = {'path': '/terraform/terraform.tfstate'}

        # Declare test Terraform.init return values
        test_return_code = 0
        test_stdout = "Terraform has been successfully initialized!"
        test_stderr = ""

        mock_init.return_value = test_return_code, test_stdout, test_stderr

        mock_chdir.return_value = "success"

        expected_result = "result"
        mock_check_result.return_value = expected_result

        # Execute the run function
        result = action.run(test_plan_path, test_terraform_exec, test_backend)

        # Verify the results
        self.assertEqual(result, expected_result)
        self.assertEqual(action.terraform.terraform_bin_path, test_terraform_exec)
        mock_chdir.assert_called_with(test_plan_path)
        mock_init.assert_called_with(
            test_plan_path,
            backend_config=test_backend,
            capture_output=False
        )
        mock_check_result.assert_called_with(test_return_code, test_stdout, test_stderr)
