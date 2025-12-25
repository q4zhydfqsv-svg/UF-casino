<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <title>UF Casino | O'yin</title>

  <!-- Telegram Mini App SDK -->
  <script src="https://telegram.org/js/telegram-web-app.js"></script>

  <style>
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
      color: white;
      text-align: center;
    }

    .container {
      padding: 30px 20px;
    }

    h1 {
      margin-top: 20px;
    }

    button {
      margin-top: 30px;
      padding: 18px 30px;
      font-size: 18px;
      border: none;
      border-radius: 12px;
      background: #00c853;
      color: #fff;
      cursor: pointer;
    }

    button:active {
      transform: scale(0.97);
    }

    .info {
      margin-top: 20px;
      opacity: 0.8;
    }
  </style>
</head>
<body>

<div class="container">
  <h1>🎰 UF CASINO</h1>
  <p>O‘yinga xush kelibsiz!</p>

  <button onclick="startGame()">🎮 O‘yinni boshlash</button>

  <div class="info">
    <p>ID: <span id="uid">...</span></p>
  </div>
</div>

<script>
  const tg = window.Telegram.WebApp;
  tg.ready();

  document.getElementById("uid").innerText =
    tg.initDataUnsafe?.user?.id || "nomaʼlum";

  function startGame() {
    alert("O‘yin keyingi bosqichda ulanadi!");
    // Bu yerga keyin o‘yin logikasini qo‘shamiz
  }
</script>

</body>
</html>