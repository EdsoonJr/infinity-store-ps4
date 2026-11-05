# Infinity Store • Instalador Direto PS4

Instalador web autônomo para o PlayStation 4 com GoldHEN. Permite que qualquer usuário faça o download e instalação da loja **Infinity Store** diretamente pelo console, sem necessidade de pendrive, computador ou celular.

---

## 🚀 Como funciona

1. O usuário acessa este site pelo **Navegador de Internet do PS4** com o GoldHEN ativo.
2. Ao clicar no botão **"Instalar Diretamente no PS4"**, o site envia um instalador binário leve para a porta local `9090` (BinLoader do GoldHEN).
3. O GoldHEN aciona o serviço nativo de download em segundo plano (**BGFT**) do PS4.
4. O console baixa e instala o arquivo `.pkg` oficial automaticamente com notificação na tela.

---

## 🛠️ Deploy no Render (Passo a Passo)

1. Crie um novo repositório no seu GitHub (ex: `infinity-store-ps4`).
2. Suba todos os arquivos desta pasta:
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Infinity Store PS4 Installer"
   git branch -M main
   git remote add origin https://github.com/SEU_USUARIO/infinity-store-ps4.git
   git push -u origin main
   ```
3. No painel do [Render](https://dashboard.render.com/):
   - Clique em **New +** > **Web Service**.
   - Conecte o repositório `infinity-store-ps4`.
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Clique em **Deploy Web Service**.

Assim que o deploy finalizar, basta abrir o link gerado pelo Render no navegador do PS4!

