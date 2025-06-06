# Artificial Analysis CLI & Dashboard

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/) [![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Un proyecto completo para interactuar con la **Artificial Analysis API**, que proporciona:

- Un **CLI** elegante con Rich para explorar, filtrar y ordenar modelos de IA según índices de razonamiento y programación.
- Un **dashboard interactivo** con Streamlit para analizar gráficas, rankings y métricas en tiempo real.

---

## Tabla de Contenidos

1. [Características](#caracter%C3%ADsticas)
2. [Requisitos](#requisitos)
3. [Instalación](#instalaci%C3%B3n)
4. [Uso](#uso)
   - [CLI](#cli)
   - [Dashboard](#dashboard)
5. [Estructura del Proyecto](#estructura-del-proyecto)
6. [Contribuir](#contribuir)
7. [Licencia](#licencia)

---

## Características

- Extracción y visualización de datos de modelos de IA (ID, nombre, puntuaciones, coste, rendimiento).
- Filtrado interactivo y ranking de modelos por **IA Index** y **Coding Index**.
- Métricas agregadas (media, distribuciones) y gráficos dinámicos.
- CLI configurable: número de modelos a mostrar, uso de datos de ejemplo, personalización de la clave API.
- Dashboard web con Streamlit: tablas, filtros, métricas y gráficos.

---

## Requisitos

- Python 3.8 o superior
- Clave de API de Artificial Analysis (regístrate en https://artificialanalysis.ai)

---

## Instalación

```bash
# Clona este repositorio
git clone https://github.com/falopp/artificial_analysis.git
cd artificial_analysis

# Instala dependencias
pip install -r requirements.txt
```

---

## Uso

### CLI

El script `aa_cli.py` permite listar y ordenar modelos directamente en la terminal.

```bash
python aa_cli.py -k YOUR_API_KEY [--top N] [--sample]
```

Opciones:

- `-k`, `--api-key`: tu clave API (puede venir de la variable `AA_API_KEY`).
- `-n`, `--top`: número de modelos a mostrar (por defecto: 5).
- `--sample`: usar datos de ejemplo si no dispones de clave API.

**Ejemplo**:
```bash
python aa_cli.py -k aa_LHFnZfWzXmOe... -n 10
```

### Dashboard

Lanza la aplicación web para explorar datos con Streamlit:

```bash
streamlit run streamlit_app.py
```

- Introduce tu API Key en la barra lateral.
- Ajusta filtros de **IA Index** y **Precio**.
- Visualiza tablas, gráficos y rankings.

---

## Estructura del Proyecto

```
artificial_analysis/
├── aa_cli.py             # CLI con Rich
├── streamlit_app.py      # Dashboard interactivo con Streamlit
├── requirements.txt      # Dependencias del proyecto
├── README.md             # Documentación principal
└── LICENSE               # Licencia MIT
```

---

## Contribuir

Todas las contribuciones son bienvenidas:

1. Haz un _fork_ del repositorio.
2. Crea una rama (`git checkout -b feature/mi-mejora`).
3. Realiza tus cambios y _commits_ (`git commit -m "feat: descripción de mi mejora"`).
4. Abre un _pull request_.

Por favor, respeta las buenas prácticas de codificación y añade tests cuando sea posible.

---

## Licencia

Este proyecto está bajo la licencia [MIT](LICENSE). ¡Disfruta y aporta! 🚀 