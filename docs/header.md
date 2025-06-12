# Host User Profiler Module Overview

This module collects non-sensitive user environment details from the host machine where Terraform is executed. It uses a Python script to gather the current user's username and home directory, outputting the results as a JSON object saved to `user_profile.json`. Sensitive data (e.g., environment variables, credentials) is explicitly excluded to prevent leaks.

## Purpose
The module provides a reusable way to profile the user environment for inventory, auditing, or configuration purposes in infrastructure-as-code workflows.
