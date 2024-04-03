# Example CI Workflow

This repository contains a set of GitHub Actions workflows and example test scripts for demonstrating continuous integration (CI) across different operating systems: Linux, macOS, and Windows.

## Directory Structure

```
├── .github/
│   └── workflows/
│       └── action.yml        # GitHub Actions workflow file
├── examples/
│   └── url-shortener-example/
│       ├── __pycache__/
│       │   └── app.cpython-310.pyc
│       ├── app.py            # Example Python application
│       ├── main.js           # Example JavaScript application
│       └── metacall.json     # Configuration file for the example applications
├── linux-tests.sh            # Test script for Linux
├── macos-tests.sh            # Test script for macOS
└── windows-tests.ps1         # Test script for Windows
```

## Workflow

The GitHub Actions workflow file (`.github/workflows/action.yml`) defines three separate jobs, one for each operating system (Linux, macOS, and Windows). Each job performs the following steps:

1. **Set up the environment**: Install the latest version of the required dependencies for running the tests.
2. **Clone repositories**: Clone the `examples` and `examples-test` repositories, which contain the example applications and test cases, respectively.
3. **Run tests**: Execute the respective test script (`linux-tests.sh`, `macos-tests.sh`, or `windows-tests.ps1`) to run the tests against the example applications.

## Test Scripts

- `linux-tests.sh`: This Bash script runs tests for the Linux environment.
- `macos-tests.sh`: This Bash script runs tests for the macOS environment.
- `windows-tests.ps1`: This PowerShell script runs tests for the Windows environment.

These scripts can be customized to include the necessary test cases and assertions for the example applications or any other projects you want to test.

## Examples

The `examples` directory contains sample applications and configurations for testing purposes:

- `url-shortener-example/`: A directory containing an example Python application (`app.py`), a JavaScript application (`main.js`), and a configuration file (`metacall.json`).

Feel free to modify or extend these examples to fit your testing needs.

## Contributing

If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. Contributions are welcome!
