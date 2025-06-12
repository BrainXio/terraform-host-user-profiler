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
