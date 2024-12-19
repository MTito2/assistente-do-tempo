## Assistente do Tempo

Um sistema que gera um relatório sobre as condições climáticas com sugestões de atividades, roupas adequadas, cuidados pessoais, curiosidades e dicas extras.

## Técnicas Utilizadas
Foi utilizada a API do **GPT**, **Gmail**, **Weather API** e a linguagem **Python**.

## Como Funciona
Primeiramente, o script chama a **API de Clima** e recebe dados sobre o clima de acordo com a cidade escolhida pelo usuário. Em seguida essas informações são repassadas para a **API do GPT**, junto com um prompt que faz ele analisar os dados e gerar um relatório completo para o usuário. Por fim, se a opção de enviar o relatório por **e-mail** for escolhida, o sistema usa o **Gmail** para realizar o envio automaticamente.
