import streamlit as st
import requests
import pandas as pd
import os

st.set_page_config(page_title="Artificial Analysis Dashboard", layout="wide")
st.title("Dashboard de Artificial Analysis API")

# Obtener API Key
def get_api_key():
    key = st.sidebar.text_input("API Key", value=os.environ.get("AA_API_KEY", ""), type="password")
    return key

api_key = get_api_key()
if not api_key:
    st.warning("Introduce tu API Key en la barra lateral para continuar.")
    st.stop()

# Cachear datos
@st.cache_data
def load_models(key):
    url = "https://artificialanalysis.ai/api/v2/data/llms/models"
    headers = {"x-api-key": key, "Accept": "application/json"}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    data = resp.json().get("data", [])
    return pd.json_normalize(data)

# Cargar datos
df = load_models(api_key)

# Mostrar tabla completa con columnas seleccionadas
st.subheader("Modelos disponibles")
cols = ["name", "release_date", "model_creator.name", 
        "evaluations.artificial_analysis_intelligence_index",
        "evaluations.artificial_analysis_coding_index",
        "evaluations.artificial_analysis_math_index",
        "median_output_tokens_per_second",
        "pricing.price_1m_blended_3_to_1"]
st.dataframe(df[cols].rename(columns={
    "model_creator.name": "Creador",
    "evaluations.artificial_analysis_intelligence_index": "IA Index",
    "evaluations.artificial_analysis_coding_index": "Coding Index",
    "evaluations.artificial_analysis_math_index": "Math Index",
    "median_output_tokens_per_second": "Tokens/s",
    "pricing.price_1m_blended_3_to_1": "Precio ($/1M)"
}))

# Filtros en la barra lateral
st.sidebar.subheader("Filtrar modelos")
min_ia = st.sidebar.slider("IA Index mínimo", 0.0, 100.0, 50.0)
max_price = st.sidebar.slider("Precio máximo ($/1M tokens)", 0.0, float(df["pricing.price_1m_blended_3_to_1"].max()), float(df["pricing.price_1m_blended_3_to_1"].max()))

df_filtered = df[(df["evaluations.artificial_analysis_intelligence_index"] >= min_ia) & 
                (df["pricing.price_1m_blended_3_to_1"] <= max_price)]

st.subheader(f"Modelos filtrados ({len(df_filtered)})")
st.dataframe(df_filtered[cols])

# Gráficos
st.subheader("Distribución de IA Index")
st.bar_chart(df_filtered.set_index("name")["evaluations.artificial_analysis_intelligence_index"])

st.subheader("Tiempo medio de respuesta (Tokens/s)")
st.line_chart(df_filtered.set_index("name")["median_output_tokens_per_second"])

# Métricas globales
st.subheader("Métricas globales")
col_avg1, col_avg2 = st.columns(2)
avg_ia_total = df["evaluations.artificial_analysis_intelligence_index"].mean()
avg_code_total = df["evaluations.artificial_analysis_coding_index"].mean()
col_avg1.metric("Media IA Index", f"{avg_ia_total:.2f}")
col_avg2.metric("Media Coding Index", f"{avg_code_total:.2f}")

# Ranking de modelos por razonamiento y programación
st.subheader("Ranking de modelos")
col1, col2 = st.columns(2)
with col1:
    st.markdown("#### Top 5 modelos por IA Index")
    df_top_ia = df.nlargest(5, "evaluations.artificial_analysis_intelligence_index")[["name","evaluations.artificial_analysis_intelligence_index"]]
    df_top_ia = df_top_ia.rename(columns={"name":"Modelo","evaluations.artificial_analysis_intelligence_index":"IA Index"})
    st.table(df_top_ia)
with col2:
    st.markdown("#### Top 5 modelos por Coding Index")
    df_top_code = df.nlargest(5, "evaluations.artificial_analysis_coding_index")[["name","evaluations.artificial_analysis_coding_index"]]
    df_top_code = df_top_code.rename(columns={"name":"Modelo","evaluations.artificial_analysis_coding_index":"Coding Index"})
    st.table(df_top_code)

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Desarrollado con Streamlit y Artificial Analysis API") 