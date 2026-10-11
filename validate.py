#!/usr/bin/env python3
"""Banco de validacion y metrologia.

Capacidad 5 - Validacion, QA y metrologia.

Ejecuta un equipo bajo prueba (DUT) contra sus especificaciones, calcula el
error medio, la repetibilidad (desviacion tipica de las muestras) y la
incertidumbre expandida (k=2), decide conformidad por punto de calibracion y
emite un informe de validacion mas una plantilla de certificado.

Uso:
    python validate.py --demo
    python validate.py --specs specs/dut_specs.json --report validation_report.md

Solo biblioteca estandar de Python 3.
"""

from __future__ import annotations

import argparse
import json
import math
import random
from dataclasses import dataclass
from datetime import date
from pathlib import Path

SPECS = Path(__file__).parent / "specs" / "dut_specs.json"


@dataclass
class PointResult:
    name: str
    nominal: float
    tolerance: float
    unit: str
    mean: float
    error: float
    stdev: float
    uncertainty: float
    verdict: str


def measure(spec: dict, seed: int = 5) -> PointResult:
    """Simula `samples` lecturas del DUT con un sesgo y ruido deterministas."""
    rng = random.Random(seed + int(spec["nominal"] * 100))
    bias = spec["nominal"] * 0.004 + 0.01        # error sistematico del equipo
    noise = 0.006 * (1 + spec["nominal"] / 10)   # dispersion de las lecturas
    samples = [spec["nominal"] + bias + rng.gauss(0, noise) for _ in range(spec["samples"])]
    mean = sum(samples) / len(samples)
    stdev = math.sqrt(sum((x - mean) ** 2 for x in samples) / (len(samples) - 1))
    error = mean - spec["nominal"]
    # Incertidumbre estandar tipo A + resolucion, expandida con k.
    u_a = stdev / math.sqrt(len(samples))
    u_res = spec["tolerance"] / 100.0
    uncertainty = math.sqrt(u_a ** 2 + u_res ** 2)
    return PointResult(
        name=spec["name"], nominal=spec["nominal"], tolerance=spec["tolerance"],
        unit=spec["unit"], mean=round(mean, 4), error=round(error, 4),
        stdev=round(stdev, 5), uncertainty=round(uncertainty, 5),
        verdict="CONFORME" if abs(error) <= spec["tolerance"] else "NO CONFORME",
    )


def validate(specs: dict, seed: int = 5) -> list[PointResult]:
    return [measure(s, seed) for s in specs["parameters"]]


def render_report(specs: dict, results: list[PointResult]) -> str:
    passed = sum(1 for r in results if r.verdict == "CONFORME")
    k = specs["k_factor"]
    lines = [
        "# Informe de validacion metrologica",
        "",
        f"- Equipo bajo prueba: **{specs['device']}**",
        f"- Magnitud: **{specs['unit_under_test']}**",
        f"- Factor de cobertura: **k = {k}**",
        f"- Puntos conformes: **{passed}/{len(results)}**",
        f"- Fecha: {date.today().isoformat()}",
        "",
        "| Punto | Nominal | Media | Error | Desv. tipica | Incertidumbre (k=2) | Tolerancia | Veredicto |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for r in results:
        lines.append(
            f"| {r.name} | {r.nominal} {r.unit} | {r.mean} | {r.error} | {r.stdev} | "
            f"{round(r.uncertainty * k, 5)} | ±{r.tolerance} | {r.verdict} |"
        )
    lines += [
        "",
        "## Lectura de resultados",
        "",
        "- **Error**: desviacion de la media respecto al valor nominal.",
        "- **Repetibilidad**: desviacion tipica de las muestras en condiciones constantes.",
        f"- **Incertidumbre expandida**: incertidumbre estandar combinada x k={k}.",
        "- Un punto es conforme si el error medio cae dentro de la tolerancia.",
        "",
        "> Evidencia reproducible: `python validate.py --demo`.",
    ]
    return "\n".join(lines) + "\n"


def render_certificate(specs: dict, results: list[PointResult]) -> str:
    rows = "\n".join(
        f"| {r.name} | {r.nominal} {r.unit} | {r.mean} | ±{round(r.uncertainty * specs['k_factor'], 5)} | {r.verdict} |"
        for r in results
    )
    return (
        "# Plantilla de certificado de calibracion\n\n"
        f"**Equipo:** {specs['device']}\n\n"
        f"**Fecha:** {date.today().isoformat()}\n\n"
        "| Punto | Nominal | Valor medido | Incertidumbre (k=2) | Veredicto |\n"
        "| --- | --- | --- | --- | --- |\n"
        f"{rows}\n\n"
        "_Plantilla de demostracion: sustituir por el certificado acreditado del laboratorio._\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Banco de validacion metrologica")
    parser.add_argument("--specs", type=Path, default=SPECS)
    parser.add_argument("--report", type=Path, default=Path("validation_report.md"))
    parser.add_argument("--certificate", type=Path, default=Path("certificate.md"))
    parser.add_argument("--demo", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    specs = json.loads(args.specs.read_text(encoding="utf-8"))
    results = validate(specs)

    if args.json:
        print(json.dumps([r.__dict__ for r in results], ensure_ascii=False, indent=2))
        return 0

    args.report.write_text(render_report(specs, results), encoding="utf-8")
    args.certificate.write_text(render_certificate(specs, results), encoding="utf-8")
    passed = sum(1 for r in results if r.verdict == "CONFORME")
    print(f"[ok] {passed}/{len(results)} puntos conformes -> {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
