#!/usr/bin/env bash
# Remove a skill do Data Modeling do Claude Code e do Codex.
# Apaga apenas pastas cujo SKILL.md se chama "data-modeling". Use --all para remover também ~/DataModeling/data-modeling.html.
#   curl -fsSL https://raw.githubusercontent.com/carlos-dataengineer/data-modeling/main/uninstall.sh | bash
set -euo pipefail
ALL="${DATA_MODELING_UNINSTALL_ALL:-0}"
[ "${1:-}" = "--all" ] && ALL=1
for t in "$HOME/.claude/skills/data-modeling" "${CODEX_HOME:-$HOME/.codex}/skills/data-modeling" "$HOME/.agents/skills/data-modeling"; do
  if [ -f "$t/SKILL.md" ] && grep -Eq '^name:[[:space:]]*data-modeling[[:space:]]*$' "$t/SKILL.md"; then
    rm -rf "$t"; echo "  removido: $t"
  fi
done
APP="$HOME/DataModeling/data-modeling.html"
if [ "$ALL" = "1" ] && [ -f "$APP" ]; then
  rm -f "$APP"; rm -f "$HOME/DataModeling/loja-aurora.json"; rmdir "$HOME/DataModeling" 2>/dev/null || true; echo "  removido: $APP"
elif [ -f "$APP" ]; then
  echo "  mantido: $APP (use --all para remover)"
fi
echo "  Data Modeling desinstalado."
