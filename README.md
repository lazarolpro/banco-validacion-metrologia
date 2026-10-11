# Capa 5 — Validación, QA y metrología

[![CI](https://github.com/lazarolpro/banco-validacion-metrologia/actions/workflows/ci.yml/badge.svg)](https://github.com/lazarolpro/banco-validacion-metrologia/actions/workflows/ci.yml)
[`lazarolpro/banco-validacion-metrologia`](https://github.com/lazarolpro/banco-validacion-metrologia) · parte del [portafolio de 6 capacidades](https://github.com/lazarolpro/portafolio)

**Capacidad demostrada:** validar un equipo contra su especificación con
criterio metrológico: error, repetibilidad e incertidumbre expandida.

## Problema real

"Funciona" no basta. Un equipo debe demostrarse **conforme** a una tolerancia, con
su incertidumbre declarada. Sin esto, las decisiones de calidad no son defendibles.

## Qué hace

- Lee las especificaciones del equipo bajo prueba (nominal, tolerancia, muestras).
- Simula las lecturas (reemplazable por el banco real) con sesgo y ruido.
- Calcula media, error, desviación típica y **incertidumbre expandida (k=2)**.
- Decide conformidad por punto y emite informe + plantilla de certificado.

## Cómo ejecutar

```bash
python validate.py --demo
python validate.py --specs specs/dut_specs.json --report validation_report.md
python validate.py --json
python -m pytest -q
```

## Evidencia que produce

- `validation_report.md` — informe por punto de calibración.
- `certificate.md` — plantilla de certificado.
- Pruebas en verde.

## Stack

Python 3 (biblioteca estándar). Sin dependencias externas.

## Por qué le importa a la empresa

Cubre **validación, QA y metrología**: la diferencia entre "parece funcionar" y
"está demostrado dentro de tolerancia con incertidumbre declarada".
