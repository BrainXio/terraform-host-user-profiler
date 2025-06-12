data "external" "user_profile" {
  program = [var.python_interpreter, "${path.module}/files/user_profile.py"]
}

resource "local_file" "user_output" {
  content  = jsonencode(data.external.user_profile.result)
  filename = "${path.cwd}/user_profile.json"
}
