# Telegram Promo Bot

Um bot para Telegram que envia automaticamente links de promoções em horários pré-definidos (9h às 18h) e também responde manualmente ao comando `/promo`.  
O projeto integra banco de dados MongoDB Atlas, agendamento de tarefas e envio de mensagens com botões interativos.

---

## 🚀 Funcionalidades
- Envio automático de promoções em horários configurados (job queue).
- Comando `/promo` para listar todas as promoções disponíveis.
- Mensagens com botões interativos que levam direto ao link da promoção.
- Integração com banco de dados MongoDB Atlas para armazenar e atualizar os links.
- Configuração de fuso horário para garantir que os envios ocorram no horário de Brasília.

---

## 🛠️ Bibliotecas utilizadas
- **[python-telegram-bot](https://python-telegram-bot.org/)**  
  Biblioteca principal para criação do bot, envio de mensagens e botões inline.

- **pymongo**  
  Conexão com o banco de dados MongoDB Atlas, leitura e atualização dos links de promoções.

- **pytz**  
  Manipulação de fusos horários, garantindo que os agendamentos sigam o horário de Brasília.

- **datetime**  
  Definição dos horários de execução dos jobs (`datetime.time`).

- **os / python-dotenv**  
  Carregamento de variáveis de ambiente (TOKEN do bot e CHAT_ID do grupo), mantendo informações sensíveis fora do código.

---

## 📂 Estrutura do projeto
- `bot.py` → código principal do bot (funções, handlers e agendamento).
- `load_promotions()` → função que lê os links direto do MongoDB Atlas.
- `promo()` → comando manual que lista todas as promoções.
- `send_scheduled_message()` → função que envia automaticamente a promoção correspondente ao horário.
- `.env` → arquivo com variáveis de ambiente (TOKEN e CHAT_ID).

---

## ⚙️ Como funciona
1. O bot conecta ao MongoDB Atlas e carrega os links de promoções.
2. O `job_queue` agenda mensagens automáticas de acordo com os horários definidos.
3. O comando `/promo` pode ser usado a qualquer momento para listar todas as promoções.
4. As mensagens enviadas possuem botões interativos que levam direto ao link.

---

## ▶️ Execução
1. Configure o arquivo `.env` com:
   ```env
   TOKEN=seu_token_do_bot
   CHAT_ID=-123456789





# Telegram Promo Bot

A Telegram bot that automatically sends promotional links at scheduled times (9 AM to 6 PM) and also responds manually to the `/promo` command.  
The project integrates MongoDB Atlas, scheduling tasks, and interactive messages with inline buttons.

---

## 🚀 Features
- Automatic sending of promotions at predefined times using the job queue.
- `/promo` command to list all available promotions.
- Messages with interactive buttons that redirect users to the promotion link.
- Integration with MongoDB Atlas to store and update links.
- Timezone configuration to ensure messages are sent according to Brasília time.

---

## 🛠️ Libraries Used
- **[python-telegram-bot](https://python-telegram-bot.org/)**  
  Core library for building the bot, sending messages, and creating inline buttons.

- **pymongo**  
  Connects to MongoDB Atlas, enabling reading and updating of promotion links.

- **pytz**  
  Handles timezone management, ensuring scheduling follows Brasília time.

- **datetime**  
  Defines job execution times (`datetime.time`).

- **os / python-dotenv**  
  Loads environment variables (bot TOKEN and group CHAT_ID), keeping sensitive data outside the code.

---

## 📂 Project Structure
- `bot.py` → main bot code (functions, handlers, and scheduling).
- `load_promotions()` → reads links directly from MongoDB Atlas.
- `promo()` → manual command that lists all promotions.
- `send_scheduled_message()` → automatically sends the promotion corresponding to the scheduled time.
- `.env` → environment file containing variables (TOKEN and CHAT_ID).

---

## ⚙️ How It Works
1. The bot connects to MongoDB Atlas and loads promotion links.
2. The `job_queue` schedules automatic messages based on defined times.
3. The `/promo` command can be used anytime to list all promotions.
4. Messages include inline buttons that redirect users to the promotion link.

---

## ▶️ Running the Bot
1. Configure the `.env` file:
   ```env
   TOKEN=your_bot_token
   CHAT_ID=-123456789

