#!/usr/bin/env bash
# Packs the brand-builder skill for upload in the Claude app (folder with SKILL.md at its root).
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p dist && rm -f dist/brand-builder.zip
(cd skills && zip -qr ../dist/brand-builder.zip brand-builder)
echo "dist/brand-builder.zip"
