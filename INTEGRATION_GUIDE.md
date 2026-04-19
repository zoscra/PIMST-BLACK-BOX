# Guía de Integración — pimst-black-box → Proyecto Unificado PIMST

## Rol de este repositorio

pimst-black-box aporta el **módulo de reporting** al proyecto unificado.
Su contenido va íntegramente a `reporting/` del proyecto integrado.

---

## Archivos que migran al proyecto unificado

### Núcleo de reporting → `reporting/`

| Archivo origen | Destino unificado | Prioridad |
|---------------|-------------------|-----------|
| `src/report_generator.py` | `reporting/report_generator.py` | 🔴 ALTA |
| `generate_report.py` | `reporting/cli.py` | 🔴 ALTA |
| `src/__init__.py` | `reporting/__init__.py` | 🟡 MEDIA |

### Datos y ejemplos

| Archivo origen | Destino unificado |
|---------------|-------------------|
| `benchmarks/data/` | `benchmarks/data/atsp_lkh3/` |
| `examples/` | `examples/reporting/` |

### Documentación → `docs/user_guide/`

| Archivo origen | Destino unificado |
|---------------|-------------------|
| `docs/getting_started.md` | `docs/user_guide/reporting_quickstart.md` |
| `docs/user_guide.md` | `docs/user_guide/reporting_guide.md` |
| `QUICK_START.md` | Merge con `docs/user_guide/reporting_quickstart.md` |

---

## Interfaz pública esperada

```python
# reporting/__init__.py
from .report_generator import ReportGenerator

def generate_report(benchmark_data: dict, output_path: str = "report.html") -> str:
    """
    Genera reporte HTML interactivo desde datos de benchmark ATSP.

    Args:
        benchmark_data: Dict con formato:
            {
                "benchmark_info": {"name": ..., "date": ..., "instances_tested": ...},
                "results": [{"instance": ..., "pimst_solution": ..., ...}]
            }
        output_path: Ruta del archivo HTML generado

    Returns:
        Ruta absoluta del reporte generado
    """
    generator = ReportGenerator()
    return generator.generate(benchmark_data, output_path)
```

### Uso desde CLI

```bash
# Generar reporte con datos de ejemplo
python -m reporting.cli

# Generar reporte desde datos propios
python -m reporting.cli --input benchmarks/data/my_results.json --output my_report.html
```

---

## Dependencias

Ligeras — sin NumPy ni dependencias científicas pesadas:

```
jinja2        # Templates HTML (si se usa)
plotly        # Gráficos interactivos (alternativa a Chart.js inline)
```

Ver `requirements.txt` para la lista completa actualizada.

---

## Pasos de integración (orden)

1. Copiar `src/report_generator.py` → `reporting/report_generator.py`
2. Adaptar `generate_report.py` como `reporting/cli.py` (mantener argparse)
3. Crear `reporting/__init__.py` exponiendo `generate_report()`
4. Copiar datos de ejemplo → `benchmarks/data/atsp_lkh3/`
5. Añadir tests básicos en `tests/reporting/test_report_generator.py`
6. Verificar con `python -m reporting.cli` → debe generar `report.html`

---

## Nota sobre el diseño "black box"

El diseño de este repo es intencionalmente opaco: los reportes muestran resultados sin revelar el código del algoritmo — ideal para presentaciones a inversores o clientes.

En el proyecto unificado, este comportamiento se mantiene **opcionalmente**: el código del solver estará disponible internamente, pero los reportes HTML generados no lo exponen.
