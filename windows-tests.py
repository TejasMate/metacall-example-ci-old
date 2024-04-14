import yaml
import re
import os
from pathlib import Path
import subprocess

def run_script(script_file):
    process = subprocess.Popen(["expect", script_file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    output, _ = process.communicate()
    return output.decode().strip()

# Get the directory containing the YAML files
yaml_dir = "examples-testing/test-suits"

# Iterate over all YAML files in the directory
for filename in os.listdir(yaml_dir):
    if filename.endswith(".yaml"):
        yaml_path = os.path.join(yaml_dir, filename)

        # Load the YAML file
        with open(yaml_path, "r") as f:
            config = yaml.safe_load(f)

        # Get the project name and code files
        project_name = config["project"]
        code_files = config["code-files"]

        # Create the project directory if it doesn't exist
        project_dir = Path("test-scripts") / project_name
        project_dir.mkdir(parents=True, exist_ok=True)

        # Create script.lua files for each test case
        script_count = 1
        for code_file in code_files:
            file_name = code_file["name"]
            file_path = code_file["path"]
            test_cases = code_file["test-cases"]

            # Get the file extension
            _, file_extension = os.path.splitext(file_name)
            file_extension = file_extension.lstrip(".")

            for test_case in test_cases:
                command = test_case["command"]
                command = re.sub(r'"', r'\\"', command)  # Escape all double quotes with backslash

                # Create the script.lua file in the project directory
                script_file = project_dir.joinpath(f"test-case{script_count}.lua")
                print(script_file)
                with open(str(script_file), "w") as f:
                    f.write('spawn("metacall")\n')
                    f.write(f'sendln("load {file_extension} {file_path}")\n')
                    f.write(f'sendln("{command}")\n')
                    f.write(f'sendln("exit")\n')
                main_output = run_script(script_file)

                output = main_output.replace(" ", "")
                strings_to_replace = ['3m', '9m', '[32m', '[39m', '[1G[0J', '[3G', '[3']
                for string in strings_to_replace:
                    output = output.replace(string, '')

                expout = test_case["expected-stdout"]
                expout = expout.replace("\\", "")

                if expout in output:
                    print(f"Test Case {script_count} has passed")
                else:
                    raise Exception(f"Test Case {script_count} hasn't passed. \nWarning: {main_output}")

                script_count += 1