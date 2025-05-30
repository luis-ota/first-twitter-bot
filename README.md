# first-twitter-bot

Este projeto é um bot simples para o Twitter desenvolvido em Python, utilizando a biblioteca Tweepy. O bot responde automaticamente a tweets que contenham uma hashtag específica.

## Funcionalidades

* Monitoramento de tweets com uma hashtag definida.
* Resposta automática a esses tweets com uma mensagem predefinida.

## Resultados

Este bot foi utilizado no perfil [@MusicaFoxBot](https://x.com/MusicaFoxBot), onde alcançou quase 5.000 seguidores de forma 100% orgânica, apenas interagindo com tweets relacionados a uma hashtag de meme.

## Pré-requisitos

* Python 3.6 ou superior.
* Conta de desenvolvedor no Twitter com as seguintes credenciais:

  * API Key
  * API Secret Key
  * Access Token
  * Access Token Secret

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/luis-ota/first-twitter-bot.git
   cd first-twitter-bot
   ```

2. Instale as dependências necessárias:

   ```bash
   pip install tweepy
   ```

3. Configure suas credenciais do Twitter no arquivo `reply_hashtag.py`:

   ```python
   consumer_key = 'SUA_API_KEY'
   consumer_secret = 'SUA_API_SECRET_KEY'
   access_token = 'SEU_ACCESS_TOKEN'
   access_token_secret = 'SEU_ACCESS_TOKEN_SECRET'
   ```

## Uso

Execute o script principal para iniciar o bot:

```bash
python reply_hashtag.py
```

O bot começará a monitorar o Twitter em busca da hashtag especificada e responderá automaticamente aos tweets encontrados.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

