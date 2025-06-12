terraform {
  required_version = ">= 1.3.0"
}

module "user_profile" {
  source             = "../../"
  python_interpreter = "python3"
}

output "user_profile" {
  value = module.user_profile.user_profile
}

output "profile_file_path" {
  value = module.user_profile.profile_file_path
}
