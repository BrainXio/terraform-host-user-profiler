<!-- BEGIN_TF_DOCS -->
# Host User Profiler Module Overview

This module collects non-sensitive user environment details from the host machine where Terraform is executed. It uses a Python script to gather the current user's username and home directory, outputting the results as a JSON object saved to `user_profile.json`. Sensitive data (e.g., environment variables, credentials) is explicitly excluded to prevent leaks.

## Purpose
The module provides a reusable way to profile the user environment for inventory, auditing, or configuration purposes in infrastructure-as-code workflows.

## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 1.3.0 |
| <a name="requirement_external"></a> [external](#requirement\_external) | >= 2.2.0 |
| <a name="requirement_local"></a> [local](#requirement\_local) | >= 2.4.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_external"></a> [external](#provider\_external) | >= 2.2.0 |
| <a name="provider_local"></a> [local](#provider\_local) | >= 2.4.0 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [local_file.user_output](https://registry.terraform.io/providers/hashicorp/local/latest/docs/resources/file) | resource |
| [external_external.user_profile](https://registry.terraform.io/providers/hashicorp/external/latest/docs/data-sources/external) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_python_interpreter"></a> [python\_interpreter](#input\_python\_interpreter) | Python interpreter to use (e.g., 'python3') | `string` | `"python3"` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_profile_file_path"></a> [profile\_file\_path](#output\_profile\_file\_path) | Path to the generated user profile JSON file |
| <a name="output_user_profile"></a> [user\_profile](#output\_user\_profile) | User profile information as a flattened JSON object with string values, including username, home directory, shell, user ID, primary group, and locale if detected |

## Additional Notes

- Requires Python 3.x on the host; no external Python libraries are used.
- The module supports Linux, Windows, and macOS hosts. User details are detected using standard Python libraries (`getpass`, `os`, `locale`, `grp`) and system commands (`whoami`, `net user`, `powershell`).
- Adjust `python_interpreter` if the Python 3 executable has a different name (e.g., `python`).
- The JSON output is a flattened map with string values to comply with Terraform's `external` data source requirements (e.g., `{"username": "mister-robot", "home_dir": "/home/mister-robot", "shell": "/bin/bash", "user_id": "1000", "primary_group": "users", "locale": "en-US"}`).
- Fields (`username`, `home_dir`, `shell`, `user_id`, `primary_group`, `locale`) are included only if detected; otherwise, they are omitted.
- No sensitive data (e.g., environment variables, credentials) is collected to ensure security. Only safe fields like username, home directory, shell, user ID, primary group, and locale are included.
- Detection methods:
  - Username: `getpass.getuser()` or `os.getlogin()`.
  - Home directory: `os.path.expanduser("~")` or `USERPROFILE` (Windows).
  - Shell: `SHELL` environment variable (Linux/macOS) or `ComSpec`/PowerShell check (Windows).
  - User ID: `os.getuid()` (Linux/macOS) or `whoami /user` (Windows).
  - Primary Group: `grp.getgrgid()` (Linux/macOS) or `net user` (Windows).
  - Locale: `locale.getlocale()`, `LANG` (Linux/macOS), or `Get-Culture` (Windows).
- Generate documentation with `make docs`, which runs `terraform-docs` with headers and footers from `docs/`.
- CI/CD is handled by GitHub Actions workflows (`.github/workflows/lint.yml` for linting and `.github/workflows/validate.yml` for validation).
- See `examples/simple/README.md` for a basic usage example of the module.
- If unexpected files (e.g., `project.json`) appear, ensure they are excluded in `.gitignore` or manually removed before committing.

## Resources
- [Terraform External Data Source](https://registry.terraform.io/providers/hashicorp/external/latest/docs/data-sources/external)
- [Terraform Local Provider](https://registry.terraform.io/providers/hashicorp/local/latest/docs)
<!-- END_TF_DOCS -->