import os

def gerar():
    with open("payload_render_hex.js", "r", encoding="utf-8") as f:
        hex_js = f.read()

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>Infinity Store • Instalador PS4</title>
  <style>
    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      -webkit-user-select: none;
      user-select: none;
    }}

    body {{
      background: radial-gradient(circle at 50% 20%, #101c38 0%, #060913 80%);
      color: #ffffff;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 24px;
      overflow-x: hidden;
    }}

    .card {{
      background: rgba(14, 22, 43, 0.85);
      border: 1px solid rgba(0, 112, 209, 0.4);
      border-radius: 20px;
      max-width: 520px;
      width: 100%;
      padding: 36px 28px;
      text-align: center;
      box-shadow: 0 15px 40px rgba(0, 0, 0, 0.7), 0 0 30px rgba(0, 112, 209, 0.2);
      backdrop-filter: blur(10px);
      animation: fadeIn 0.8s ease-out;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(15px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .icon-wrapper {{
      position: relative;
      width: 130px;
      height: 130px;
      margin: 0 auto 20px;
      border-radius: 26px;
      padding: 4px;
      background: linear-gradient(135deg, #0070d1, #00d2ff);
      box-shadow: 0 0 25px rgba(0, 112, 209, 0.5);
    }}

    .icon-wrapper img {{
      width: 100%;
      height: 100%;
      border-radius: 22px;
      object-fit: cover;
      display: block;
      background: #090f1d;
    }}

    h1 {{
      font-size: 26px;
      font-weight: 800;
      letter-spacing: 0.5px;
      margin-bottom: 6px;
      background: linear-gradient(90deg, #ffffff, #8bc7ff);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .badge {{
      display: inline-block;
      background: rgba(0, 112, 209, 0.2);
      border: 1px solid #0070d1;
      color: #38a9ff;
      font-size: 11px;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 50px;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 18px;
    }}

    .desc {{
      font-size: 14px;
      color: #a4b3cf;
      line-height: 1.5;
      margin-bottom: 24px;
    }}

    .btn-install {{
      background: linear-gradient(135deg, #0070d1 0%, #00439c 100%);
      color: #ffffff;
      border: 2px solid #00a2ff;
      border-radius: 14px;
      font-size: 16px;
      font-weight: 700;
      padding: 16px 24px;
      width: 100%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      transition: all 0.2s ease;
      box-shadow: 0 6px 20px rgba(0, 112, 209, 0.4);
      outline: none;
    }}

    .btn-install:hover, .btn-install:focus {{
      background: linear-gradient(135deg, #0084f7 0%, #0056c7 100%);
      transform: scale(1.02);
      box-shadow: 0 8px 30px rgba(0, 112, 209, 0.7);
      border-color: #ffffff;
    }}

    .btn-install:active {{
      transform: scale(0.98);
    }}

    #statusBox {{
      margin-top: 20px;
      padding: 14px 16px;
      border-radius: 12px;
      font-size: 13px;
      display: none;
      line-height: 1.5;
      text-align: left;
    }}

    .status-loading {{
      background: rgba(0, 112, 209, 0.15);
      border: 1px solid #0070d1;
      color: #7cc3ff;
      display: block !important;
    }}

    .status-success {{
      background: rgba(0, 200, 83, 0.15);
      border: 1px solid #00c853;
      color: #69f0ae;
      display: block !important;
    }}

    .status-error {{
      background: rgba(255, 61, 0, 0.15);
      border: 1px solid #ff3d00;
      color: #ff8a80;
      display: block !important;
    }}

    .proto-warning {{
      background: rgba(255, 171, 0, 0.15);
      border: 1px solid #ffab00;
      color: #ffd740;
      padding: 12px 14px;
      border-radius: 10px;
      font-size: 12px;
      margin-bottom: 18px;
      text-align: left;
      line-height: 1.4;
      display: none;
    }}

    .footer-info {{
      margin-top: 24px;
      font-size: 11px;
      color: #55698b;
    }}
  </style>
</head>
<body>

  <div class="card">
    <div class="icon-wrapper">
      <img src="https://infinityps4.onrender.com/download/ICON0.png" alt="Infinity Store Logo">
    </div>

    <h1>Infinity Store</h1>
    <div class="badge">PS4 Beta v0.0.12</div>

    <p class="desc">
      Instale a loja oficial diretamente no seu PlayStation 4 com apenas um clique, sem necessidade de pendrive USB.
    </p>

    <!-- Alerta caso a pagina seja aberta em HTTPS -->
    <div id="protoWarning" class="proto-warning">
      ⚠️ <b>Aviso de Protocolo (HTTPS detectado):</b><br>
      O navegador do PS4 bloqueia o envio de comandos locais caso o site esteja em HTTPS (bloqueio de segurança Mixed Content). Se der erro, certifique-se de acessar por HTTP comum.
    </div>

    <button id="btnAction" class="btn-install" onclick="executarInstalacao()">
      <span id="btnIcon">🚀</span>
      <span id="btnText">INSTALAR NO MEU PS4</span>
    </button>

    <div id="statusBox"></div>

    <div class="footer-info">
      Compatível com GoldHEN (Firmwares 5.05 até 11.00+)<br>
      Porta do Payload Server: 9090
    </div>
  </div>

  <script>
    const isPS4 = navigator.userAgent.indexOf("PlayStation 4") !== -1 || navigator.userAgent.indexOf("PlayStation") !== -1;
    const PKG_URL = "https://infinityps4.onrender.com/download/Infinitykkj-STORE.pkg";

    // Alerta se for HTTPS
    if (window.location.protocol === "https:") {{
      const pw = document.getElementById("protoWarning");
      if (pw) pw.style.display = "block";
    }}

    window.addEventListener("DOMContentLoaded", () => {{
      const btnText = document.getElementById("btnText");
      const btnIcon = document.getElementById("btnIcon");
      if (!isPS4) {{
        btnIcon.textContent = "💾";
        btnText.textContent = "Baixar Arquivo PKG (PC / Celular)";
      }}
    }});

    // 🔒 Payload HEX pré-compilado (exatamente igual Sandro Store, apontando para o PKG na nuvem)
    {hex_js}

    async function executarInstalacao() {{
      // 1. Se NAO for PS4 (PC ou Celular), faz o download direto do .pkg
      if (!isPS4) {{
        window.location.href = PKG_URL;
        return;
      }}

      const status = document.getElementById("statusBox");
      const btn = document.getElementById("btnAction");

      status.style.display = "block";
      status.className = "status-loading";
      status.innerHTML = "⏳ <b>Preparando instalador...</b><br>Injetando payload no Payload Server (porta 9090) do GoldHEN.";
      btn.style.opacity = "0.7";
      btn.disabled = true;

      try {{
        // Converte HEX string para Uint8Array
        const payloadBytes = new Uint8Array(
          payloadHex.map(h => parseInt(h, 16))
        );
        const data = payloadBytes.buffer;

        // Dispara para o GoldHEN local (porta 9090)
        let erroEncontrado = null;
        let enviadoSucesso = false;

        // Tenta porta padrao 9090 e alternativa 9020
        const alvos = ["http://127.0.0.1:9090", "http://127.0.0.1:9020"];
        for (let i = 0; i < alvos.length; i++) {{
          try {{
            const send = await fetch(alvos[i], {{
              method: "POST",
              body: data
            }});
            if (send.ok || send.status === 200) {{
              enviadoSucesso = true;
              break;
            }}
          }} catch (e) {{
            erroEncontrado = e;
          }}
        }}

        // Se deu erro e estamos em HTTPS, explica a razao com precisao
        if (!enviadoSucesso && window.location.protocol === "https:") {{
          throw new Error("O navegador do PS4 bloqueou a conexão local porque esta página está em HTTPS (Mixed Content). Detalhe: " + (erroEncontrado ? erroEncontrado.message : "TypeError"));
        }}

        if (!enviadoSucesso && erroEncontrado) {{
          throw erroEncontrado;
        }}

        status.className = "status-success";
        status.innerHTML = "🚀 <b>Instalador carregado com sucesso!</b><br>Verifique a notificação de download no canto superior da sua TV.";
        alert("Instalador carregado com sucesso 🚀\\n\\nVerifique as notificações de download no console!");
      }} catch (err) {{
        console.error(err);
        status.className = "status-error";
        status.innerHTML = "❌ <b>Erro ao enviar payload:</b><br>" + err.message + "<br><br>👉 Verifique se o <b>Payload Server</b> está ativo no GoldHEN.";
        alert("Erro ao enviar payload ❌\\n\\n" + err.message);
      }} finally {{
        btn.style.opacity = "1";
        btn.disabled = false;
      }}
    }}
  </script>
</body>
</html>
"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("index.html gerado com sucesso! Tamanho:", len(html))

if __name__ == "__main__":
    gerar()
