from terraform_base_action_test_case import TerraformBaseActionTestCase
from list_workspaces import ListWorkspaces
import mock


class ListWorkspaceTestCase(TerraformBaseActionTestCase):
    __test__ = True
    action_cls = ListWorkspaces

    def test_init(self):
        action = self.get_action_instance({})
        self.assertIsInstance(action, ListWorkspaces)

    @mock.patch("list_workspaces.os.chdir")
    @mock.patch("lib.action.TerraformBaseAction.check_result")
    @mock.patch("lib.action.Terraform.__getattr__")
    def test_run(self, mock_workspace, mock_check_result, mock_chdir):
        action = self.get_action_instance({})
        # Declare test input values
        test_plan_path = "/terraform"
        test_terraform_exec = "/usr/bin/terraform"
        test_workspace = "test_ws"

        # Declare test Terraform.plan return values
        test_return_code = 0
        test_stdout = "Terraform has been successfully initialized!"
        test_stderr = ""

        action.terraform.workspace.return_value = test_return_code, test_stdout, test_stderr

        mock_chdir.return_value = "success"

        expected_result = "result"
        mock_check_result.return_value = expected_result

        # Execute the run function
        result = action.run(test_plan_path, test_terraform_exec)

        # Verify the results
        self.assertEqual(result, expected_result)
        self.assertEqual(action.terraform.terraform_bin_path, test_terraform_exec)
        mock_chdir.assert_called_with(test_plan_path)
        mock_workspace.assert_called_with("workspace")
        action.terraform.workspace.assert_called_with("list")
        mock_check_result.assert_called_with(test_return_code, test_stdout, test_stderr)
