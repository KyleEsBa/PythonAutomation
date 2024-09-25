import os
import subprocess

class Runner:
    def __init__(self, feature_dir='src.resources.features'):
        """Initialize the runner with the directory containing feature files."""
        self.feature_dir = feature_dir

    def run(self):
        """Run the Behave tests."""
        command = f'behave {self.feature_dir}'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
        return result.returncode

    def clean(self):
        """Perform any cleanup if needed (optional)."""
        # For example, remove temporary files or directories
        pass
