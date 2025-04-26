resource "aws_instance" "web_server" {
  ami           = "ami-0f1dcc636b69a6438"  # <- updated AMI for Amazon Linux 2023
  instance_type = var.instance_type
  key_name      = var.key_name

  tags = {
    Name = "DevOpsAssignmentInstance"
  }
}

