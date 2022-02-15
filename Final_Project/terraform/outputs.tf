output "dev_server_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.dev_server.public_ip
}

output "prod_server_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.prod_server.public_ip
}
