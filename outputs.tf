output "user_profile" {
  description = "User profile information as a flattened JSON object with string values, including username, home directory, shell, user ID, primary group, and locale if detected"
  value       = data.external.user_profile.result
}

output "profile_file_path" {
  description = "Path to the generated user profile JSON file"
  value       = local_file.user_output.filename
}
