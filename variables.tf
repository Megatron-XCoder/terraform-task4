variable "instance_type" {
  default = "t2.micro"
}

variable "key_name" {
  description = "SSH Key Pair name"
}

variable "bucket_name" {
  description = "S3 Bucket Name"
}

