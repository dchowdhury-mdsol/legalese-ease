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
  hash_key         = "QueryID"
  range_key        = "QueryType"
  stream_enabled   = true
  stream_view_type = "NEW_AND_OLD_IMAGES"
  
  global_secondary_index {
    name            = "QueryIndex"
    hash_key        = "Query"
    projection_type = "ALL"  # You can choose the appropriate projection type
    read_capacity   = 10
    write_capacity  = 10
  }

  global_secondary_index {
    name            = "QueryResponseIndex"
    hash_key        = "QueryResponse"
    projection_type = "ALL"  # You can choose the appropriate projection type
    read_capacity   = 10
    write_capacity  = 10
  }

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

