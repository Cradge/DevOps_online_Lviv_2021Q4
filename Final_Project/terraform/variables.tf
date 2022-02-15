variable "instance_ami" {
  description = "Value of the ami for the EC2 instance"
  type        = string
  default     = "ami-0fb653ca2d3203ac1"
}
variable "instance_type" {
  description = "Value of the instance type for the EC2 instance"
  type        = string
  default     = "t2.micro"
}
variable "owner_name" {
  description = "Instance owner name"
  type        = string
  default     = "Mykhailo Ryzhman"
}
variable "project_name" {
  description = "Instance owner name"
  type        = string
  default     = "CI/CD Pipeline"
}
