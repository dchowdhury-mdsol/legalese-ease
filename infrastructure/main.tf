terraform {
  backend "s3" {

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
  name_convention = "${var.product}-${var.environment}"
}

data "aws_caller_identity" "current" {}

resource "aws_dynamodb_table" "dynamodb" {
  name             = "${local.name_convention}"
  billing_mode     = "PROVISIONED"
  read_capacity    = 10
  write_capacity   = 10
  hash_key         = "ID"
  range_key        = "DateTime"
  stream_enabled   = true
  stream_view_type = "NEW_AND_OLD_IMAGES"

  attribute {
    name = "ID"
    type = "N"
  }

  attribute {
    name = "DateTime"
    type = "S"
  }

  attribute {
    name = "Query"
    type = "S"
  }

  attribute {
    name = "QueryType"
    type = "S"
  }

  global_secondary_index {
    name               = "QueryIndex"
    hash_key           = "Query"
    range_key          = "QueryType"
    write_capacity     = 10
    read_capacity      = 10
    projection_type    = "ALL"
  }
}