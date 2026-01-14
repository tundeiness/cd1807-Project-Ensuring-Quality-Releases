#!/bin/bash
export ARM_CLIENT_ID="$CLIENT_ID"
export ARM_CLIENT_SECRET="$CLIENT_SECRET"
export ARM_TENANT_ID="$TENANT_ID"
export ARM_SUBSCRIPTION_ID="$SUBSCRIPTION_ID"
echo "Environment variables set. Run: source terraform-env.sh"