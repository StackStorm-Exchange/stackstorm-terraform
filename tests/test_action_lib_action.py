from terraform_base_action_test_case import TerraformBaseActionTestCase
from lib.action import Action
# Using this to run tests. Otherwise get an error for no run method.
from init import Init
import mock


class ActionTestCase(TerraformBaseActionTestCase):
    __test__ = True
    action_cls = Init

    @mock.patch("lib.action.Terraform")
    def test_init(self, mock_trfm):
        action = self.get_action_instance({})
        self.assertIsInstance(action, Action)
        self.assertEqual(action.terraform, mock_trfm())

    def test_check_result_success(self):
        action = self.get_action_instance({})
        # Declare test input values
        test_return_code = 0
        test_stdout = "Terraform has been successfully initialized!"
        test_stderr = ""

        test_output = test_stdout
        expected_result = (True, test_output)

        # Execute the run function
        result = action.check_result(test_return_code, test_stdout, test_stderr)

        # Verify the results
        self.assertEqual(result, expected_result)

    def test_check_result_fail(self):
        action = self.get_action_instance({})
        # Declare test input values
        test_return_code = 1
        test_stdout = "Initialization failed!"
        test_stderr = "Error details..."

        test_output = test_stdout + "\n" + test_stderr
        expected_result = (False, test_output)

        # Execute the run function
        result = action.check_result(test_return_code, test_stdout, test_stderr)

        # Verify the results
        self.assertEqual(result, expected_result)

    @mock.patch("lib.action.Terraform.output")
    def test_check_result_success_with_output(self, mock_output):
        action = self.get_action_instance({})

        # Set terraform variables for test
        action.terraform.terraform_bin_path = "/usr/bin/terraform"
        action.terraform.working_dir = "/terraform"

        # Declare test input values
        test_return_code = 0
        test_stdout = "Terraform has been successfully initialized!"
        test_stderr = ""

        test_output = dict()
        expected_result = (True, test_output)

        # Execute the run function
        result = action.check_result(
            test_return_code,
            test_stdout,
            test_stderr,
            return_output=True
        )

        # Verify the results
        self.assertEqual(result, expected_result)

    @mock.patch("output.os.chdir")
    @mock.patch("lib.action.Terraform.output")
    def test_check_result_success_with_output(self, mock_output, mock_chdir):
        action = self.get_action_instance({})
        # Declare test input values
        test_return_code = 0
        test_stdout = "Terraform has been successfully initialized!"
        test_stderr = ""
        test_plan_path = "/terraform"
        test_terraform_exec = "/usr/bin/terraform"

        # Declare test Terraform.output return values
        expected_result = "result"
        mock_output.return_value = expected_result

        mock_chdir.return_value = "success"

        # Execute the run function
        result = action.check_result(
            test_return_code,
            test_stdout,
            test_stderr,
            return_output=True
        )

        # Verify the results
        self.assertEqual(result, expected_result)
        self.assertTrue(mock_output.called)
        mock_chdir.assert_called_with(test_plan_path)

    def test_check_result_fail_with_output(self):
        action = self.get_action_instance({})

        # Set terraform variables for test
        action.terraform.terraform_bin_path = "/usr/bin/terraform"
        action.terraform.working_dir = "/terraform"

        # Declare test input values
        test_return_code = 1
        test_stdout = "Initialization failed!"
        test_stderr = "Error details..."

        test_output = None
        expected_result = (False, test_output)

        # Execute the run function
        result = action.check_result(
            test_return_code,
            test_stdout,
            test_stderr,
            return_output=True
        )

        # Verify the results
        self.assertEqual(result, expected_result)

    def test_concat_std_output(self):
        action = self.get_action_instance({})
        # Declare test input values
        test_stdout = "Initialization failed!"
        test_stderr = "Error details..."

        test_output = test_stdout + "\n" + test_stderr

        # Execute the run function
        result = action.concat_std_output(
            test_stdout,
            test_stderr
        )

        # Verify the results
        self.assertEqual(result, test_output)
