<#
.SYNOPSIS
  Remove a skill do Data Modeling do Claude Code e do Codex.
.DESCRIPTION
  Apaga apenas pastas cujo SKILL.md se chama "data-modeling". A ferramenta em ~/Data Modeling fica,
  a menos que voce use -All. Os boards salvos no navegador nao sao tocados.
.EXAMPLE
  irm https://raw.githubusercontent.com/carlos-dataengineer/data-modeling/main/uninstall.ps1 | iex
.EXAMPLE
  .\uninstall.ps1 -All
#>
[CmdletBinding()]
param([switch]$All)
$ErrorActionPreference = 'Stop'
if ($env:DATA_MODELING_UNINSTALL_ALL -eq '1') { $All = $true }

$codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
$targets = @(
  (Join-Path $HOME '.claude/skills/data-modeling'),
  (Join-Path $codexHome 'skills/data-modeling'),
  (Join-Path $HOME '.agents/skills/data-modeling')
)
foreach ($t in $targets) {
  $m = Join-Path $t 'SKILL.md'
  if ((Test-Path $m) -and ((Get-Content $m -Raw -Encoding UTF8) -match '(?m)^name:\s*data-modeling\s*$')) {
    Remove-Item -Path $t -Recurse -Force
    Write-Host "  removido: $t"
  }
}
$app = Join-Path $HOME 'DataModeling/data-modeling.html'
if ($All -and (Test-Path $app)) {
  Remove-Item -Path $app -Force
  $demo = Join-Path (Split-Path $app -Parent) 'loja-aurora.json'
  if (Test-Path $demo) { Remove-Item -Path $demo -Force }
  $dir = Split-Path $app -Parent
  if (-not (Get-ChildItem -Path $dir -Force)) { Remove-Item -Path $dir -Force }
  Write-Host "  removido: $app"
} elseif (Test-Path $app) {
  Write-Host "  mantido: $app (use -All para remover)"
}
Write-Host '  Data Modeling desinstalado.'
