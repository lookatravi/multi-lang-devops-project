output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.main.id
}

output "private_subnet_ids" {
  description = "Private subnet IDs"
  value       = aws_subnet.private[*].id
}

output "public_subnet_ids_cidrs" {
  description = "Public subnet CIDRs"
  value       = aws_subnet.public[*].cidr_block
  
}