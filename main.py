import streamlit as st
import os
import json
# Importação absoluta: o Python procurará 'scripts' a partir da raiz
from scripts.gerador_memorial import gerar_memorial

def main():
    st.set_page_config(page_title="Gestão de Laudos - KM", layout="wide")
    st.title("Sistema de Gestão de Laudos - KM")

    with st.form("form_laudo"):
        col1, col2 = st.columns(2)
        with col1:
            projeto = st.text_input("Nome do Projeto")
            area_terreno = st.number_input("Área do Terreno (m²)", min_value=0.0)
            valor_m2_terreno = st.number_input("Valor m² Terreno (R$)", min_value=0.0)
            recuo_f = st.number_input("Recuo Frontal (m)", min_value=0.0)
        with col2:
            area_construida = st.number_input("Área Construída (m²)", min_value=0.0)
            cub_m2 = st.number_input("CUB atual (R$/m²)", min_value=0.0)
            idade = st.number_input("Idade aparente (anos)", min_value=0.0)
            estado_cons = st.number_input("Fator de conservação", min_value=0.0, value=1.0)
            
        submitted = st.form_submit_button("Gerar Laudo")

    if submitted:
        dados = {
            "projeto": projeto,
            "engenheiro": "MARCIO RODRIGUES DE OLIVEIRA",
            "crea": "1522223070",
            "num_art": "A PREENCHER",
            "recuo_frontal": recuo_f,
            "terreno": {"area_m2": area_terreno, "valor_unitario_m2": valor_m2_terreno},
            "edificacao": {
                "area_m2": area_construida,
                "cub_atual_m2": cub_m2,
                "idade_aparente_anos": idade,
                "vida_util_total_anos": 50,
                "estado_conservacao": estado_cons
            }
        }
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        pasta_saida = os.path.join(base_dir, 'output')
        
        try:
            gerar_memorial(dados, pasta_saida)
            st.success("Laudo gerado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao gerar laudo: {e}")

if __name__ == "__main__":
    main()