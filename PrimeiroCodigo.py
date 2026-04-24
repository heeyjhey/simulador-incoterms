import streamlit as st

# 1. Configuração da Página (Para aspeto de Dashboard)
st.set_page_config(page_title="Simulador Incoterms 2020", layout="wide", page_icon="🚢")

# 2. Dados e Regras
categorias = [
    "Embalagem e Carga", "Despacho Exportação", "Frete Internacional", 
    "Seguro Internacional", "Despacho Importação", "Descarga Destino"
]

dados = {
    "EXW": {
        "custos": ["Vendedor", "Comprador", "Comprador", "Comprador", "Comprador", "Comprador"],
        "riscos": ["Vendedor", "Comprador", "Comprador", "Comprador", "Comprador", "Comprador"],
        "alerta": "Risco máximo para o Comprador. O Vendedor apenas disponibiliza a mercadoria nas suas instalações."
    },
    "FCA": {
        "custos": ["Vendedor", "Vendedor", "Comprador", "Comprador", "Comprador", "Comprador"],
        "riscos": ["Vendedor", "Vendedor", "Comprador", "Comprador", "Comprador", "Comprador"],
        "alerta": "O risco transfere-se para o Comprador aquando da entrega da mercadoria ao transportador nomeado."
    },
    "FOB": {
        "custos": ["Vendedor", "Vendedor", "Comprador", "Comprador", "Comprador", "Comprador"],
        "riscos": ["Vendedor", "Vendedor", "Comprador", "Comprador", "Comprador", "Comprador"],
        "alerta": "Exclusivo para vias navegáveis. O risco transfere-se apenas quando a mercadoria está a bordo do navio na origem."
    },
    "CFR": {
        "custos": ["Vendedor", "Vendedor", "Vendedor", "Comprador", "Comprador", "Comprador"],
        "riscos": ["Vendedor", "Vendedor", "Comprador", "Comprador", "Comprador", "Comprador"],
        "alerta": "Ponto Crítico! O Vendedor paga o Frete Internacional, mas o Risco transfere-se na origem (a bordo do navio)."
    },
    "CIF": {
        "custos": ["Vendedor", "Vendedor", "Vendedor", "Vendedor", "Comprador", "Comprador"],
        "riscos": ["Vendedor", "Vendedor", "Comprador", "Comprador", "Comprador", "Comprador"],
        "alerta": "Ponto Crítico! O Vendedor paga frete e seguro, mas o Risco transfere-se na origem (a bordo do navio)."
    },
    "DAP": {
        "custos": ["Vendedor", "Vendedor", "Vendedor", "Vendedor", "Comprador", "Comprador"],
        "riscos": ["Vendedor", "Vendedor", "Vendedor", "Vendedor", "Comprador", "Comprador"],
        "alerta": "O Vendedor assume os riscos até ao local de destino acordado, mas a Descarga é da responsabilidade do Comprador."
    },
    "DPU": {
        "custos": ["Vendedor", "Vendedor", "Vendedor", "Vendedor", "Comprador", "Vendedor"],
        "riscos": ["Vendedor", "Vendedor", "Vendedor", "Vendedor", "Comprador", "Vendedor"],
        "alerta": "Atenção! Este é o único Incoterm em que o Vendedor é responsável pela Descarga no Destino final."
    },
    "DDP": {
        "custos": ["Vendedor", "Vendedor", "Vendedor", "Vendedor", "Vendedor", "Comprador"],
        "riscos": ["Vendedor", "Vendedor", "Vendedor", "Vendedor", "Vendedor", "Comprador"],
        "alerta": "Risco máximo para o Vendedor. Impossibilidade legal ou grande dificuldade no Brasil, dado que exige que o Exportador atue como Importador formal."
    }
}

# 3. Interface Visual (UI)
st.title("📦 Simulador de Responsabilidades - Incoterms 2020")
st.markdown("Explora a divisão de custos e riscos entre Exportador e Importador de forma interativa.")
st.markdown("---")

# Controlos Superiores
col1, col2 = st.columns([1, 1])

with col1:
    incoterm_selecionado = st.selectbox("Selecione o Incoterm:", list(dados.keys()))

with col2:
    perspetiva = st.radio("Perspetiva de Análise:", ["Custo", "Risco"], horizontal=True)

# Lógica de seleção de dados
chave_perspetiva = "custos" if perspetiva == "Custo" else "riscos"
info_atual = dados[incoterm_selecionado]
responsaveis = info_atual[chave_perspetiva]

st.markdown("<br>", unsafe_allow_html=True) # Espaçamento
st.subheader(f"Análise de {perspetiva} para {incoterm_selecionado}")

# Criação da Linha do Tempo (6 colunas)
colunas_timeline = st.columns(6)

for i in range(6):
    responsavel = responsaveis[i]
    categoria = categorias[i]
    
    # Define a cor baseada em quem é o responsável (Azul para Vendedor, Laranja para Comprador)
    cor = "#60a5fa" if responsavel == "Vendedor" else "#fb923c"
    
    with colunas_timeline[i]:
        # Criamos um pequeno "cartão" usando HTML dentro do Markdown do Streamlit
        st.markdown(
            f"""
            <div style="background-color: #262730; padding: 15px; border-radius: 8px; text-align: center; border-top: 4px solid {cor}; height: 120px;">
                <p style="font-size: 0.85rem; color: #aaa; margin-bottom: 10px; line-height: 1.2;">{categoria}</p>
                <h4 style="color: {cor}; margin: 0; text-transform: uppercase;">{responsavel}</h4>
            </div>
            """, 
            unsafe_allow_html=True
        )

st.markdown("<br>", unsafe_allow_html=True)

# Caixa de Alerta
st.warning(f"**ALERTA DE RISCO:** {info_atual['alerta']}", icon="⚠️")

#teste