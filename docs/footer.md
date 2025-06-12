## Additional Notes

- Requires Python 3.x on the host; no external Python libraries are used.
- The module supports Linux, Windows, and macOS hosts. Username and home directory are detected using standard Python libraries (`getpass`, `os`).
- Adjust `python_interpreter` if the Python 3 executable has a different name (e.g., `python`).
- The JSON output is a flattened map with string values to comply with Terraform's `external` data source requirements (e.g., `{"username": "mister-robot", "home_dir": "/home/mister-robot"}`).
- Fields (`username`, `home_dir`) are included only if detected; otherwise, they are omitted.
- No sensitive data (e.g., environment variables, credentials) is collected to ensure security.
- Generate documentation with `make docs`, which runs `terraform-docs` with headers and footers from `docs/`.
- CI/CD is handled by GitHub Actions workflows (`.github/workflows/lint.yml` for linting and `.github/workflows/validate.yml` for validation).
- See `examples/simple/README.md` for a basic usage example of the module.
- If unexpected files (e.g., `project.json`) appear, ensure they are excluded in `.gitignore` or manually removed before committing.

## Resources
- [Terraform External Data Source](https://registry.terraform.io/providers/hashicorp/external/latest/docs/data-sources/external)
- [Terraform Local Provider](https://registry.terraform.io/providers/hashicorp/local/latest/docs)
