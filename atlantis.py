import streamlit as st
import pandas as pd

# 1. Configuração visual do App
st.set_page_config(page_title="Atlantis - Simulador de Economia", page_icon="💰", layout="centered")

st.title("🔋 Simulador Atlantis: Economia de Energia")
st.markdown("### Pare de pagar taxas extras para a distribuidora!")

# 2. Entrada de Dados do Cliente
with st.container():
    nome_cliente = st.text_input("Nome do Cliente (Opcional):", placeholder="Ex: João Silva")
    valor_conta = st.number_input("Quanto o cliente paga por mês (R$):", min_value=100.0, value=2500.0, step=100.0)
    desconto_percentual = st.slider("% de Desconto Garantido (ACL):", 10, 35, 20) / 100

# 3. Cálculos de Impacto Financeiro
economia_mensal = valor_conta * desconto_percentual
economia_anual = economia_mensal * 12
economia_5anos = economia_anual * 5

st.divider()

# 4. Painel de Métricas (Visual Impactante)
col1, col2 = st.columns(2)
col1.metric("Economia Mensal", f"R$ {economia_mensal:,.2f}")
with col2:
    st.success(f"**Economia em 5 anos**\n\n### R$ {economia_5anos:,.2f}")

# 5. Argumentos de Venda (Texto Informativo)
st.info(f"✨ **Vantagens para {nome_cliente if nome_cliente else 'o cliente'}:**\n"
        "- Sem obras ou placas solares (Portabilidade Pura)\n"
        "- Energia 100% limpa e sustentável (ESG)\n"
        "- Adesão com custo zero e zero investimento")

# 6. GRÁFICO DE ÁREA (O "Efeito Visual" que você quer)
st.subheader("📈 Projeção de Lucro Acumulado")
df_projecao = pd.DataFrame({
    "Economia Acumulada (R$)": [economia_anual * i for i in range(1, 6)]
}, index=["Ano 1", "Ano 2", "Ano 3", "Ano 4", "Ano 5"])

# Este comando cria a área azul preenchida mostrando o dinheiro subindo
st.area_chart(df_projecao)

# 7. Ferramenta de Fechamento (WhatsApp)
st.divider()
texto_venda = (
    f"Olá {nome_cliente}! Boas notícias da Atlantis. 🚀\n\n"
    f"Fiz sua simulação e você pode economizar *R$ {economia_mensal:,.2f} todos os meses*.\n"
    f"💰 **Em 5 anos, são R$ {economia_5anos:,.2f} de lucro no seu bolso.**\n\n"
    f"Tudo isso sem investimento e com energia 100% limpa. Podemos conversar?"
)

if st.button("📱 Gerar Proposta para WhatsApp"):
    st.code(texto_venda)
    # Link formatado corretamente para abrir o WhatsApp Web ou App
    link_wa = f"https://wa.me{texto_venda.replace(' ', '%20').replace('\n', '%0A')}"
    st.link_button("Ir para o WhatsApp", link_wa)
