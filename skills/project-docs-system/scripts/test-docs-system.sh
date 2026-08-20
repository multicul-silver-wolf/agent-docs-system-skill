#!/usr/bin/env bash
set -euo pipefail

script_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)"
tmp_root="$(mktemp -d)"

cleanup() {
  rm -rf "$tmp_root"
}
trap cleanup EXIT

fail() {
  printf 'FAIL: %s\n' "$*" >&2
  exit 1
}

write_doc() {
  path="$1"
  title="$2"
  description="$3"
  mkdir -p "$(dirname "$path")"
  cat >"$path" <<EOF
---
title: $title
description: $description
updateAt: 2026-07-06
---

# $title
EOF
}

write_adr() {
  path="$1"
  title="$2"
  living_basename="$3"
  mkdir -p "$(dirname "$path")"
  cat >"$path" <<EOF
---
title: $title
description: Decision rationale for $title.
updateAt: 2026-08-20
---

# $title

[Current living document](./$living_basename)

## 2026-08-20 Keep context local

Keep durable decision rationale next to the living document it qualifies.
EOF
}

write_bulleted_adr() {
  path="$1"
  title="$2"
  living_basename="$3"
  mkdir -p "$(dirname "$path")"
  cat >"$path" <<EOF
---
title: $title
description: Decision rationale for $title.
updateAt: 2026-08-20
---

# $title

[Current living document](./$living_basename)

## Decision Records

- **Accepted — 2026-08-20 keep-existing-entry-style**: Preserve a customized repository's consistent dated-list format.
EOF
}

append_filler_lines() {
  path="$1"
  count="$2"
  i=1
  while [ "$i" -le "$count" ]; do
    printf 'Filler line %s.\n' "$i" >>"$path"
    i=$((i + 1))
  done
}

make_base_docs() {
  repo="$1"
  write_doc "$repo/docs/DOCS.md" "Project Knowledge Protocol" "Repository docs protocol."
  write_doc "$repo/docs/index.md" "Docs Index" "Repository docs map."
  write_doc "$repo/docs/application/DOCS.md" "Application Protocol" "Application docs protocol."
  write_doc "$repo/docs/application/index.md" "Application" "Application docs map."
}

run_update() {
  "$script_dir/update-docs-catalog.sh" "$1" >/dev/null
}

run_verify_capture() {
  "$script_dir/verify-docs-system.sh" "$1" 2>&1
}

resource_repo="$tmp_root/resource-repo"
make_base_docs "$resource_repo"
write_doc "$resource_repo/docs/application/overview.md" "Overview" "Application overview."
mkdir -p "$resource_repo/docs/assets/homepage/how-it-works"
printf 'fake image bytes\n' >"$resource_repo/docs/assets/homepage/how-it-works/reference.png"
run_update "$resource_repo"
resource_output="$(run_verify_capture "$resource_repo")" || fail "resource directory fixture should verify"
if printf '%s\n' "$resource_output" | grep -q 'WARN:'; then
  fail "resource directory fixture should not emit warnings"
fi

deep_repo="$tmp_root/deep-repo"
make_base_docs "$deep_repo"
write_doc "$deep_repo/docs/application/homepage/index.md" "Homepage" "Homepage docs map."
write_doc "$deep_repo/docs/application/homepage/replication.md" "Replication" "Homepage replication notes."
run_update "$deep_repo"
if ! grep -Fq './replication.md' "$deep_repo/docs/application/homepage/index.md"; then
  fail "recursive catalog updater should update nested index files"
fi
deep_output="$(run_verify_capture "$deep_repo")" || fail "deep indexed docs fixture should verify"
if printf '%s\n' "$deep_output" | grep -q 'WARN:'; then
  fail "deep indexed docs fixture should not emit warnings"
fi

missing_index_repo="$tmp_root/missing-index-repo"
make_base_docs "$missing_index_repo"
write_doc "$missing_index_repo/docs/application/homepage/replication.md" "Replication" "Homepage replication notes."
run_update "$missing_index_repo"
if run_verify_capture "$missing_index_repo" >/dev/null; then
  fail "deep docs without an index should fail verification"
fi

valid_adr_repo="$tmp_root/valid-adr-repo"
make_base_docs "$valid_adr_repo"
write_doc "$valid_adr_repo/docs/application/overview.md" "Overview" "Application overview."
printf '\n## Decision history\n\n- [Decision rationale](./overview.adr.md)\n' >>"$valid_adr_repo/docs/application/overview.md"
write_adr "$valid_adr_repo/docs/application/overview.adr.md" "Overview Decisions" "overview.md"
write_doc "$valid_adr_repo/docs/application/legacy.md" "Legacy" "Customized ADR entry style."
printf '\n## Decision history\n\n- [Decision rationale](./legacy.adr.md)\n' >>"$valid_adr_repo/docs/application/legacy.md"
write_bulleted_adr "$valid_adr_repo/docs/application/legacy.adr.md" "Legacy Decisions" "legacy.md"
printf '\n## Decision history\n\n- [Repository decisions](./DOCS.adr.md)\n' >>"$valid_adr_repo/docs/DOCS.md"
write_adr "$valid_adr_repo/docs/DOCS.adr.md" "Repository Decisions" "DOCS.md"
run_update "$valid_adr_repo"
printf '\n## Optional history navigation\n\n- [Overview decisions](./overview.adr.md)\n' >>"$valid_adr_repo/docs/application/index.md"
if grep -Fq '.adr.md' "$valid_adr_repo/docs/index.md"; then
  fail "generated root catalog should omit ADR companions"
fi
generated_application_catalog="$(sed -n '/<!-- BEGIN:docs-generated-catalog -->/,/<!-- END:docs-generated-catalog -->/p' "$valid_adr_repo/docs/application/index.md")"
if printf '%s\n' "$generated_application_catalog" | grep -Fq '.adr.md'; then
  fail "generated scope catalog should omit ADR companions"
fi
valid_adr_output="$(run_verify_capture "$valid_adr_repo")" || fail "valid bidirectionally linked ADR companions should verify"
if printf '%s\n' "$valid_adr_output" | grep -q 'WARN:'; then
  fail "valid ADR companion fixture should not emit warnings"
fi

inline_adr_repo="$tmp_root/inline-adr-repo"
make_base_docs "$inline_adr_repo"
write_doc "$inline_adr_repo/docs/application/overview.md" "Overview" "Application overview."
printf '\n## Decision Records\n\n### Keep this inline\n' >>"$inline_adr_repo/docs/application/overview.md"
run_update "$inline_adr_repo"
inline_adr_output="$(run_verify_capture "$inline_adr_repo")" && fail "inline Decision Records should fail verification"
if ! printf '%s\n' "$inline_adr_output" | grep -Fq 'living document must not contain an inline Decision Records section'; then
  fail "inline Decision Records failure should explain the companion-file rule"
fi

orphan_adr_repo="$tmp_root/orphan-adr-repo"
make_base_docs "$orphan_adr_repo"
write_adr "$orphan_adr_repo/docs/application/missing.adr.md" "Missing Decisions" "missing.md"
run_update "$orphan_adr_repo"
orphan_adr_output="$(run_verify_capture "$orphan_adr_repo")" && fail "orphan ADR companion should fail verification"
if ! printf '%s\n' "$orphan_adr_output" | grep -Fq 'ADR companion has no adjacent living document'; then
  fail "orphan ADR failure should identify the missing living document"
fi

empty_adr_repo="$tmp_root/empty-adr-repo"
make_base_docs "$empty_adr_repo"
write_doc "$empty_adr_repo/docs/application/overview.md" "Overview" "Application overview."
printf '\n[Decision rationale](./overview.adr.md)\n' >>"$empty_adr_repo/docs/application/overview.md"
write_doc "$empty_adr_repo/docs/application/overview.adr.md" "Overview Decisions" "Decision rationale."
printf '\n[Current living document](./overview.md)\n' >>"$empty_adr_repo/docs/application/overview.adr.md"
run_update "$empty_adr_repo"
empty_adr_output="$(run_verify_capture "$empty_adr_repo")" && fail "ADR companion without a decision entry should fail verification"
if ! printf '%s\n' "$empty_adr_output" | grep -Fq 'ADR companion must contain at least one recognizable dated history entry'; then
  fail "empty ADR failure should require a dated decision entry"
fi

missing_living_link_repo="$tmp_root/missing-living-link-repo"
make_base_docs "$missing_living_link_repo"
write_doc "$missing_living_link_repo/docs/application/overview.md" "Overview" "Application overview."
write_adr "$missing_living_link_repo/docs/application/overview.adr.md" "Overview Decisions" "overview.md"
run_update "$missing_living_link_repo"
missing_living_link_output="$(run_verify_capture "$missing_living_link_repo")" || fail "living document without its ADR link should warn without failing verification"
if ! printf '%s\n' "$missing_living_link_output" | grep -Fq 'living document should link to its ADR companion'; then
  fail "missing living-to-ADR link warning should be explicit"
fi

missing_adr_link_repo="$tmp_root/missing-adr-link-repo"
make_base_docs "$missing_adr_link_repo"
write_doc "$missing_adr_link_repo/docs/application/overview.md" "Overview" "Application overview."
printf '\n[Decision rationale](./overview.adr.md)\n' >>"$missing_adr_link_repo/docs/application/overview.md"
write_adr "$missing_adr_link_repo/docs/application/overview.adr.md" "Overview Decisions" "wrong-living-file.md"
run_update "$missing_adr_link_repo"
missing_adr_link_output="$(run_verify_capture "$missing_adr_link_repo")" || fail "ADR companion without its living-document link should warn without failing verification"
if ! printf '%s\n' "$missing_adr_link_output" | grep -Fq 'ADR companion should link back to its living document'; then
  fail "missing ADR-to-living link warning should be explicit"
fi

five_hundred_repo="$tmp_root/five-hundred-repo"
make_base_docs "$five_hundred_repo"
write_doc "$five_hundred_repo/docs/application/overview.md" "Overview" "Application overview."
append_filler_lines "$five_hundred_repo/docs/application/overview.md" 493
run_update "$five_hundred_repo"
five_hundred_output="$(run_verify_capture "$five_hundred_repo")" || fail "a 500-line document should still verify"
if printf '%s\n' "$five_hundred_output" | grep -Fq 'recommended maximum: 500'; then
  fail "a document at exactly 500 author-maintained lines should not warn"
fi

five_hundred_one_repo="$tmp_root/five-hundred-one-repo"
make_base_docs "$five_hundred_one_repo"
write_doc "$five_hundred_one_repo/docs/application/overview.md" "Overview" "Application overview."
append_filler_lines "$five_hundred_one_repo/docs/application/overview.md" 494
run_update "$five_hundred_one_repo"
five_hundred_one_output="$(run_verify_capture "$five_hundred_one_repo")" || fail "a 501-line document should warn without failing verification"
for expected in 'docs/application/overview.md' '501 author-maintained lines' 'recommended maximum: 500' 'bounded-context or subdomain boundaries' '1 warning(s)'; do
  if ! printf '%s\n' "$five_hundred_one_output" | grep -Fq "$expected"; then
    fail "501-line warning should include: $expected"
  fi
done

generated_catalog_repo="$tmp_root/generated-catalog-repo"
make_base_docs "$generated_catalog_repo"
i=1
while [ "$i" -le 510 ]; do
  write_doc "$generated_catalog_repo/docs/application/doc-$i.md" "Document $i" "Catalog fixture $i."
  i=$((i + 1))
done
run_update "$generated_catalog_repo"
if [ "$(wc -l <"$generated_catalog_repo/docs/application/index.md" | tr -d ' ')" -le 500 ]; then
  fail "generated catalog fixture should exceed 500 physical lines"
fi
generated_catalog_output="$(run_verify_capture "$generated_catalog_repo")" || fail "large generated catalogs should verify"
if printf '%s\n' "$generated_catalog_output" | grep -Fq 'recommended maximum: 500'; then
  fail "generated catalog lines should be excluded from the size warning"
fi

multiple_large_repo="$tmp_root/multiple-large-repo"
make_base_docs "$multiple_large_repo"
write_doc "$multiple_large_repo/docs/application/first.md" "First" "First oversized document."
write_doc "$multiple_large_repo/docs/application/second.md" "Second" "Second oversized document."
append_filler_lines "$multiple_large_repo/docs/application/first.md" 494
append_filler_lines "$multiple_large_repo/docs/application/second.md" 494
run_update "$multiple_large_repo"
multiple_large_output="$(run_verify_capture "$multiple_large_repo")" || fail "multiple oversized documents should warn without failing verification"
for expected in 'docs/application/first.md' 'docs/application/second.md' '2 warning(s)'; do
  if ! printf '%s\n' "$multiple_large_output" | grep -Fq "$expected"; then
    fail "multiple oversized warnings should include: $expected"
  fi
done

printf 'Docs system script tests passed.\n'
