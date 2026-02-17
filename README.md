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
