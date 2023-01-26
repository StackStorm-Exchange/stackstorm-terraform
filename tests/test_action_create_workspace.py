from terraform_base_action_test_case import TerraformBaseActionTestCase
from create_workspace import CreateWorkspace
import mock


class CreateWorkspaceTestCase(TerraformBaseActionTestCase):
    __test__ = True
    action_cls = CreateWorkspace

    def test_init(self):
        action = self.get_action_instance({})
        self.assertIsInstance(action, CreateWorkspace)

    @mock.patch("lib.action.TerraformBaseAction.set_semantic_version")
    @mock.patch("lib.action.TerraformBaseAction.check_result")
    @mock.patch("lib.action.Terraform.__getattr__", create=True)
    def test_run(self, mock_workspace, mock_check_result, mock_version):
        action = self.get_action_instance({})
        # Declare test input values
        test_plan_path = "/terraform"
        test_terraform_exec = "/usr/bin/terraform"
        test_workspace = "test_ws"

        # Declare test Terraform.plan return values
        test_return_code = 0
        test_stdout = "Terraform has been successfully initialized!"
        test_stderr = ""

        mock_version.return_value = '1.1.1'
        action.terraform.workspace.return_value = test_return_code, test_stdout, test_stderr

        expected_result = "result"
        mock_check_result.return_value = expected_result

        # Execute the run function
        result = action.run(test_plan_path, test_terraform_exec, test_workspace)

        # Verify the results
        self.assertEqual(result, expected_result)
        self.assertEqual(action.terraform.terraform_bin_path, test_terraform_exec)
        mock_workspace.assert_called_with("workspace")
        action.terraform.workspace.assert_called_with("new",
                                                      test_workspace,
                                                      "-no-color",
                                                      raise_on_error=False)
        mock_check_result.assert_called_with(test_return_code, test_stdout, test_stderr)
