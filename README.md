# Racha da Misericórdia

https://sorteiodetimerachamisericordia.netlify.app/

Aplicação web local para organizar uma rodada de futebol entre cinco times. O sistema permite cadastrar capitães e jogadores, definir o nível de cada participante e escolher entre uma montagem manual ou uma distribuição automática equilibrada.

## Funcionalidades

- Cadastro de cinco capitães e exatamente 25 jogadores.
- Avaliação de capitães e jogadores em uma escala de 1 a 5 estrelas.
- Preenchimento de exemplo para testar a interface rapidamente.
- Montagem manual dos cinco times, com capitães fixos.
- Organização dos jogadores disponíveis por nível.
- Sorteio automático priorizando o equilíbrio da pontuação total das equipes.
- Troca de jogadores entre times no resultado automático.
- Layout responsivo para computador e celular.
- Funcionamento local sem banco de dados, framework ou dependências externas.

## Tecnologias

- HTML5
- CSS3
- JavaScript puro
- Python 3, usando `http.server` da biblioteca padrão

## Como acessar

### Pelo Live Server

Com a extensão **Live Server** do VS Code instalada, abra `static/index.html` e clique em **Go Live**. O endereço normalmente será:

[http://127.0.0.1:5500/static/index.html](http://127.0.0.1:5500/static/index.html)

### Pelo servidor Python

O projeto também inclui um servidor local simples. No terminal, dentro da pasta do projeto, execute:

```bash
python main.py
```

Depois, acesse:

[http://127.0.0.1:8000](http://127.0.0.1:8000)

Para encerrar o servidor, pressione `Ctrl + C` no terminal.

## Como usar

1. Preencha os nomes dos cinco capitães.
2. Adicione os 25 jogadores e defina o nível de cada um pelas estrelas.
3. Escolha uma das opções:
   - **Montagem manual:** selecione um jogador disponível e adicione-o ao time desejado. Cada equipe aceita até cinco jogadores além do capitão.
   - **Sorteio automático:** gere cinco equipes com os capitães fixos e jogadores distribuídos por pontuação.
4. Na tela do resultado automático, clique em dois jogadores de equipes diferentes para trocar os dois. Capitães não podem ser trocados.

O botão **Preencher exemplo** insere um elenco completo para demonstração. O sistema exige todos os cinco capitães e exatamente 25 jogadores antes de montar as equipes.

## Como funciona o equilíbrio automático

Os capitães começam fixos em seus respectivos times. Em seguida, os jogadores são ordenados do maior para o menor nível e enviados, um por vez, para a equipe com menor pontuação que ainda tenha espaço. O resultado é uma sugestão baseada somente nos níveis cadastrados; posição em campo, entrosamento e características individuais não são considerados.

## Regras e limitações

- A rodada é formada por cinco times de seis pessoas: um capitão e cinco jogadores.
- Os dados ficam apenas na memória do navegador enquanto a página está aberta.
- Atualizar a página apaga o cadastro e os times montados.
- Não há login, persistência, banco de dados ou backend de aplicação.
- O projeto foi pensado para uso local e não inclui publicação automática em hospedagem.

## Estrutura do projeto

```text
RoboSorteioTimes/
├── main.py                       # Servidor HTTP local opcional
├── README.md                     # Documentação do projeto
└── static/
    ├── index.html                # Estrutura da interface
    ├── styles.css                # Estilos e responsividade
    ├── app.js                    # Estado, validações e regras dos times
    └── assets/
        └── racha-da-misericordia.png
```

## Requisitos

- Navegador moderno.
- Python 3.8 ou superior, apenas se optar por usar `main.py`.
- Não é necessário instalar pacotes com `pip` ou usar Node.js.

## Publicar no GitHub

Crie um repositório no GitHub e execute os comandos abaixo na pasta do projeto, substituindo a URL pelo endereço do seu repositório:

```bash
git init
git add .
git commit -m "feat: cria organizador de times"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
git push -u origin main
```

## Licença

Este projeto ainda não possui uma licença definida. Para distribuí-lo formalmente, adicione um arquivo `LICENSE` com a licença escolhida.
