# Versiones Óptimas — pimst-black-box

## Resumen

pimst-black-box es una herramienta de **visualización y reporting** para benchmarks ATSP. Es un proyecto estable con una sola versión funcional, por lo que no requiere selección entre versiones alternativas.

---

## Versión actual: 1.0 (rama `claude/add-pimst-readme`)

### Estado: PRODUCCIÓN ✅

| Característica | Detalle |
|---------------|----------|
| Función principal | Genera reportes HTML interactivos desde datos JSON |
| Input | JSON con resultados PIMST vs LKH-3 |
| Output | HTML standalone con gráficos interactivos (Chart.js) |
| Tiempo de generación | Segundos |
| Dependencias | Ver `requirements.txt` |

### Archivos clave

| Archivo | Función |
|---------|----------|
| `generate_report.py` | CLI principal — punto de entrada del usuario |
| `src/report_generator.py` | Motor de generación de reportes (14,673 bytes) |
| `benchmarks/data/` | Datos de benchmark de ejemplo (JSON) |
| `src/__init__.py` | Módulo Python |

### Resultados validados con los datos de ejemplo

- **10/15 instancias ATSP**: PIMST supera a LKH-3 en calidad
- **+0.43%** mejora promedio en calidad de solución
- **+41.2%** speedup promedio de ejecución
- **Hasta 53% más rápido** en instancias grandes (N > 150 nodos)

---

## No hay versiones anteriores para comparar

Este repositorio nació directamente como herramienta de presentación. No requiere selección de versiones algorítmicas.

---

## Próximas versiones planeadas (roadmap)

| Versión | Feature | Estado |
|---------|---------|--------|
| v1.0 | HTML reports + ATSP vs LKH-3 + CLI | ✅ Completo |
| v1.1 | Export a PDF | 🔲 Planeado |
| v1.2 | Más tipos de gráficos y visualizaciones | 🔲 Planeado |
| v1.3 | Batch processing para múltiples datasets | 🔲 Planeado |
| v1.4 | Custom styling y temas | 🔲 Planeado |

---

## Relación con el proyecto unificado

Ver `INTEGRATION_GUIDE.md` para cómo este repositorio se incorpora como módulo `reporting/` del proyecto principal PIMST.
