resource "vault_policy" "admin_ns_policies" {
  for_each = fileset("${path.module}/policies", "*.hcl")
  name     = trimsuffix(each.value, ".hcl")

  policy = file("policies/${each.value}")
}