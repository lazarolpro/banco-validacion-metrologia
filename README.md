# Capa 5 — Validación y metrología

[`lazarolpro/banco-validacion-metrologia`](https://github.com/lazarolpro/banco-validacion-metrologia) · parte del [portafolio de 9 capacidades](https://github.com/lazarolpro/portafolio)

**Capacidad demostrada:** validar un equipo contra su especificación con
**conformidad** e **incertidumbre de medida** declarada.

> © 2026 Ronny L. Díaz López. **Todos los derechos reservados.** El código fuente,
> los datos de detalle y los informes completos son propiedad del autor y no se
> publican. Prohibida su venta o uso comercial sin autorización escrita. Ver
> [`LICENSE`](LICENSE).

## Problema real

"Parece que funciona" no es una validación. Un equipo es conforme solo si el error
cae dentro de la tolerancia **con su incertidumbre declarada**. Sin ese cálculo, la
decisión de aceptar o rechazar un instrumento no es defendible.

## Qué hace

- Compara las lecturas del equipo con los valores nominales.
- Calcula error medio, repetibilidad e **incertidumbre expandida** (k = 2).
- Emite un veredicto de conformidad por punto y una plantilla de certificado.

## Evidencia que produce

- [`assets/muestra_validacion.pdf`](assets/muestra_validacion.pdf) — muestra
  resumida del informe de validación (con marca de agua).
- [`specs/dut_specs.json`](specs/dut_specs.json) — especificación del equipo bajo
  prueba (nominales y tolerancias).

## Alcance de este repositorio

Este repositorio es una **vitrina del resultado**: muestra el informe de
conformidad y la incertidumbre. El **código fuente**, el certificado completo y los
**informes completos** son propiedad del autor y se mantienen fuera del repositorio
público.

## Stack

Python 3 (solo biblioteca estándar: `statistics`, `json`). Sin dependencias.
*(El código no se publica; ver `LICENSE`.)*

## Por qué le importa a la empresa

Cubre **validación, QA y metrología**: la diferencia entre "parece funcionar" y
"está demostrado dentro de tolerancia con incertidumbre declarada".

**En mantenimiento:** verificar que un instrumento mide bien antes de confiar en
su lectura.
