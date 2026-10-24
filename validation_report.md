# Informe de validacion metrologica

- Equipo bajo prueba: **TRANSMISOR-P-01**
- Magnitud: **presion**
- Factor de cobertura: **k = 2**
- Puntos conformes: **3/3**
- Fecha: 2026-10-24

| Punto | Nominal | Media | Error | Desv. tipica | Incertidumbre (k=2) | Tolerancia | Veredicto |
| --- | --- | --- | --- | --- | --- | --- | --- |
| presion_0bar | 0.0 bar | 0.0075 | 0.0075 | 0.00778 | 0.00502 | ±0.05 | CONFORME |
| presion_5bar | 5.0 bar | 5.0354 | 0.0354 | 0.00925 | 0.00618 | ±0.1 | CONFORME |
| presion_10bar | 10.0 bar | 10.0384 | 0.0384 | 0.01483 | 0.00984 | ±0.15 | CONFORME |

## Lectura de resultados

- **Error**: desviacion de la media respecto al valor nominal.
- **Repetibilidad**: desviacion tipica de las muestras en condiciones constantes.
- **Incertidumbre expandida**: incertidumbre estandar combinada x k=2.
- Un punto es conforme si el error medio cae dentro de la tolerancia.

> Evidencia reproducible: `python validate.py --demo`.
