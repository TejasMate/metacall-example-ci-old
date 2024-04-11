# MetaCall Example CI

This repository contains a set of automated tests for the "string-manipulation" example in the MetaCall. The tests are implemented using a Python script that generates and runs test suits expect scripts to verify the expected behavior of the example.

## Prerequisites

- Python 3.x
- MetaCall CLI installed and available in the system's PATH

## Setup

1. Clone the `examples` and `examples-testing` repository from the MetaCall's GitHub:
   ```
   git clone https://github.com/metacall/examples.git
   ```
   ```
   git clone https://github.com/metacall/examples-testing.git
   ```

3. Verify the file paths in the `test.py` script:
   - Make sure the `yaml_dir` variable is set to `"examples-testing/test-suits"`.
   - Ensure the `project_dir` is set to `Path("test-scripts") / project_name`.

## Running the Tests

To run the automated tests, execute the following command from the `metacall-example-ci` directory:

```
python test.py
```

The script will iterate through the YAML configuration files in the `examples-testing/test-suits` directory, generate the expect scripts, and run the tests. If all tests pass, you should see a success message for each test case.

## CI Behavior

The `test.py` script is designed to raise an exception if any of the test cases fail. This behavior is useful for integrating the script into a continuous integration (CI) pipeline, where the failure of any test case should cause the build to fail.

If a test case fails, the script will print a message indicating the failed test case(s) and raise an exception with the list of failed test cases

## Contributing

If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

This README file provides an overview of the project, including the prerequisites, setup instructions, and instructions for running the automated tests. Feel free to modify the content as per your specific requirements.
