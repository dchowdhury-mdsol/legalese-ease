terraform {
  backend "s3" {
    bucket = "${var.product}-${var.environment}"
    key    = "terraform"
    region = var.region
  }
}

provider "aws" {
  region = var.region
  default_tags {
    tags = {
      Environment = var.environment
      Owner       = var.owner
      Product     = var.product
      Region      = var.region
    }
  }
}

locals {
  naming = "${var.product}-${var.environment}"
}

data "aws_caller_identity" "current" {}

resource "aws_dynamodb_table" "dynamodb" {
  name           = "${locals.naming}"
  billing_mode   = "PROVISIONED"
  read_capacity  = 10
  write_capacity = 10
  hash_key       = "QueryID"
  range_key      = "QueryType"
  stream_enabled = true

  attribute {
    name = "QueryID"
    type = "S"
  }

  attribute {
    name = "QueryType"
    type = "S"
  }

  attribute {
    name = "Query"
    type = "S"
  }

  attribute {
    name = "QueryResponse"
    type = "S"
  }
}

