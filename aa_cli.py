#!/usr/bin/env python3
"""
CLI de Artificial Analysis API con Rich
"""

import os
import sys
import requests
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

# Endpoint principal
aPI_MODELS_URL = "https://artificialanalysis.ai/api/v2/data/llms/models"

# Datos de ejemplo para demostración
SAMPLE_DATA = [
    {
        "id": "sample-1",
        "name": "model-alpha",
        "model_creator": {"id": "creator-1", "name": "TestCo", "slug": "testco"},
        "evaluations": {"artificial_analysis_intelligence_index": 85.2, "artificial_analysis_coding_index": 78.4},
        "pricing": {"price_1m_blended_3_to_1": 1.5},
        "median_output_tokens_per_second": 120,
        "median_time_to_first_token_seconds": 10.5
    },
    {
        "id": "sample-2",
        "name": "model-beta",
        "model_creator": {"id": "creator-2", "name": "DevCorp", "slug": "devcorp"},
        "evaluations": {"artificial_analysis_intelligence_index": 75.5, "artificial_analysis_coding_index": 88.7},
        "pricing": {"price_1m_blended_3_to_1": 2.1},
        "median_output_tokens_per_second": 95,
        "median_time_to_first_token_seconds": 8.2
    }
]


def fetch_models(api_key):
    headers = {"x-api-key": api_key, "Accept": "application/json"}
    resp = requests.get(aPI_MODELS_URL, headers=headers)
    resp.raise_for_status()
    return resp.json().get("data", [])


def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description="CLI de Artificial Analysis con Rich")
    parser.add_argument("-k", "--api-key", help="Clave API", default=os.environ.get("AA_API_KEY"))
    parser.add_argument("-n", "--top", type=int, default=5, help="Top N modelos a mostrar")
    parser.add_argument("--sample", action="store_true", help="Usar datos de ejemplo en lugar de la API")
    return parser.parse_args()


def main():
    console = Console()
    args = parse_args()

    if args.sample or not args.api_key:
        console.print("[yellow]Usando datos de ejemplo (sample)[/yellow]")
        models = SAMPLE_DATA
    else:
        console.print("Obteniendo datos desde la API...")
        try:
            models = fetch_models(args.api_key)
        except Exception as e:
            console.print(f"[red]Error al obtener datos: {e}[/red]")
            sys.exit(1)
    
    # Top IA Index
    sorted_ia = sorted(models, key=lambda m: m.get("evaluations", {}).get("artificial_analysis_intelligence_index") or 0, reverse=True)
    table_ia = Table(title=f"Top {args.top} Modelos por IA Index")
    table_ia.add_column("Rank", justify="right")
    table_ia.add_column("Modelo", style="cyan")
    table_ia.add_column("IA Index", justify="right")
    for i, m in enumerate(sorted_ia[:args.top], start=1):
        ia = m.get("evaluations", {}).get("artificial_analysis_intelligence_index", 0)
        table_ia.add_row(str(i), m.get("name", "-"), f"{ia:.1f}")
    console.print(table_ia)

    # Top Coding Index
    sorted_code = sorted(models, key=lambda m: m.get("evaluations", {}).get("artificial_analysis_coding_index") or 0, reverse=True)
    table_code = Table(title=f"Top {args.top} Modelos por Coding Index")
    table_code.add_column("Rank", justify="right")
    table_code.add_column("Modelo", style="magenta")
    table_code.add_column("Coding Index", justify="right")
    for i, m in enumerate(sorted_code[:args.top], start=1):
        code = m.get("evaluations", {}).get("artificial_analysis_coding_index", 0)
        table_code.add_row(str(i), m.get("name", "-"), f"{code:.1f}")
    console.print(table_code)

    # Estadísticas simples
    ia_vals = [(m.get("evaluations") or {}).get("artificial_analysis_intelligence_index") or 0 for m in models]
    code_vals = [(m.get("evaluations") or {}).get("artificial_analysis_coding_index") or 0 for m in models]
    avg_ia = sum(ia_vals) / len(ia_vals) if ia_vals else 0
    avg_code = sum(code_vals) / len(code_vals) if code_vals else 0
    console.print(f"\n[bold]Media IA Index:[/bold] {avg_ia:.2f}   [bold]Media Coding Index:[/bold] {avg_code:.2f}")

if __name__ == '__main__':
    main() 