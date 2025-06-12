# Example: Basic Usage of brainxio/terraform-host-user-profiler

## Overview
This example demonstrates how to use the `brainxio/terraform-host-user-profiler` Terraform module to profile the user environment on the host machine. The module generates a JSON file (`user_profile.json`) containing non-sensitive details such as the username and home directory.

## Prerequisites
- Terraform >= 1.3.0
- Python 3.x installed on the host

## Usage
1. Navigate to the `examples/simple` directory:
   ```bash
   cd examples/simple
   ```
2. Initialize Terraform:
   ```bash
   terraform init
   ```
3. Review the plan:
   ```bash
   terraform plan
   ```
4. Apply the configuration:
   ```bash
   terraform apply
   ```

This will execute the module, run the `user_profile.py` script, and generate `user_profile.json` in the current working directory.

## Example Output
- **File**: `user_profile.json` (e.g., `{"username": "mister-robot", "home_dir": "/home/mister-robot"}`)
- **Terraform Outputs**:
  - `user_profile`: The JSON object with user details
  - `profile_file_path`: Path to `user_profile.json`

## Notes
- The `python_interpreter` variable defaults to `python3`. Adjust if your Python executable has a different name (e.g., `python`).
- Fields are included only if detected; otherwise, they are omitted.
- The module avoids collecting sensitive data for security.
- This example is a reference for integrating the module into larger Terraform configurations. See the main module's documentation for advanced usage.
