provider "aws" {
  region = "us-east-2"
}

terraform {
  backend "s3" {
    bucket = "mike-r-terraform-state"
    key    = "terraform/terraform.tfstate"
    region = "us-east-2"
  }
}

resource "aws_key_pair" "tf-key" {
  key_name   = "ec2-key"
  public_key = var.key_pub
}

resource "aws_instance" "dev_server" {
  ami           = var.instance_ami
  instance_type = var.instance_type
  key_name      = "ec2-key"
  vpc_security_group_ids = [aws_security_group.servers.id]

  tags = {
    Name    = "Development Environment"
    Owner   = var.owner_name
    Project = var.project_name
  }
}

resource "aws_instance" "prod_server" {
  ami           = var.instance_ami
  instance_type = var.instance_type
  key_name      = "ec2-key"
  vpc_security_group_ids = [aws_security_group.servers.id]

  tags = {
    Name    = "Production Environment"
    Owner   = var.owner_name
    Project = var.project_name
  }
}
