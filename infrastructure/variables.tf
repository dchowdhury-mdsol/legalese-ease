variable "region" {
  description = "AWS Default Region"
  type = string
  default = "us-east-1"
}

variable "environment" {
  description = "Deployment environment"
  type = string
}

variable "owner" {
  description = "Owner contact tag for AWS resources"
  type = string
  default = "dchowdhury"
}

variable "product" {
  description = "Product name"
  type = string
  default = "legalese-ease"
}