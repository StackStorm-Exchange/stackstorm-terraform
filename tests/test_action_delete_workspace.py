from terraform_base_action_test_case import TerraformBaseActionTestCase
from delete_workspace import DeleteWorkspace
import mock


class DeleteWorkspaceTestCase(TerraformBaseActionTestCase):
    __test__ = True
    action_cls = DeleteWorkspace

    def test_init(self):
        action = self.get_action_instance({})
        self.assertIsInstance(action, DeleteWorkspace)

    @mock.patch("lib.action.TerraformBaseAction.check_result")
    @mock.patch("lib.action.Terraform.__getattr__")
    def test_run(self, mock_workspace, mock_check_result):
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

        expected_result = "result"
        mock_check_result.return_value = expected_result

        # Execute the run function
        result = action.run(test_plan_path, test_terraform_exec, test_workspace)

        # Verify the results
        self.assertEqual(result, expected_result)
        self.assertEqual(action.terraform.terraform_bin_path, test_terraform_exec)
        mock_workspace.assert_called_with("workspace")
        action.terraform.workspace.assert_called_with("delete", "-force", test_workspace,
                                                      "-no-color")
        mock_check_result.assert_called_with(test_return_code, test_stdout, test_stderr)
