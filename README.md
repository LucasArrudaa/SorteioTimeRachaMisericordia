# Racha da Misericórdia

<<<<<<< HEAD
Aplicação web para montar cinco times de futebol a partir dos capitães, dos jogadores e dos níveis de cada participante.
=======
https://sorteiodetimerachamisericordia.netlify.app/

Aplicação web local para organizar uma rodada de futebol entre cinco times. O sistema permite cadastrar capitães e jogadores, definir o nível de cada participante e escolher entre uma montagem manual ou uma distribuição automática equilibrada.
>>>>>>> 56ab56508514275abbf6bbe6f5dd07de2ce43eef

O sistema oferece duas formas de montagem:

- **Manual:** você escolhe para qual time cada jogador vai.
- **Automática:** o sistema distribui os jogadores tentando equilibrar a pontuação total dos times.

## O que o projeto faz

- Cadastra 5 capitães e exatamente 25 jogadores.
- Atribui um nível de 1 a 5 estrelas para cada pessoa.
- Mostra os jogadores disponíveis agrupados por nível.
- Mantém os capitães fixos em seus times.
- Permite trocar jogadores depois do sorteio automático.
- Funciona no computador e no celular.
- Não exige banco de dados, Node.js ou instalação de pacotes Python.

## Como executar

### Opção 1: servidor Python

Pré-requisito: Python 3.8 ou superior.

Abra o terminal na pasta do projeto e execute:

```bash
python main.py
```

Depois, abra no navegador:

```text
http://127.0.0.1:8000
```

Para parar o servidor, pressione `Ctrl + C` no terminal.

### Opção 2: Live Server

Com a extensão **Live Server** do VS Code:

1. Abra `static/index.html`.
2. Clique em **Go Live**.
3. Acesse o endereço exibido pelo VS Code, normalmente `http://127.0.0.1:5500/static/index.html`.

O servidor Python é mais fiel à estrutura final do projeto, mas as duas opções funcionam para testar a interface.

## Como usar

1. Informe os nomes dos cinco capitães.
2. Informe os nomes dos 25 jogadores.
3. Escolha o nível de cada participante clicando nas estrelas.
4. Escolha uma das opções de montagem:
   - **Ir para montagem manual:** selecione um jogador disponível e clique em **Adicionar jogador aqui** no time desejado.
   - **Sortear times automaticamente:** gere uma sugestão equilibrada com base nos níveis cadastrados.
5. Na montagem manual, use o botão `x` de um jogador para devolvê-lo à lista de disponíveis.
6. No resultado automático, clique em dois jogadores de times diferentes para trocar os dois.

O botão **Preencher exemplo** cria um elenco completo para testar rapidamente a aplicação.

### Regras da rodada

- São 5 times.
- Cada time possui 1 capitão e até 5 jogadores.
- Os capitães não podem ser trocados no resultado automático.
- É obrigatório preencher os 5 capitães.
- É obrigatório preencher exatamente 25 jogadores.
- Os dados são apagados quando a página é atualizada.

## Como o código funciona

O projeto separa a aplicação em três partes clássicas:

```text
HTML       estrutura da página
CSS        aparência e responsividade
JavaScript comportamento e regras da montagem
```

Não é usado nenhum framework frontend. A interface usa JavaScript puro e as APIs nativas do navegador.

### Estado da aplicação

Em `static/app.js`, o objeto `state` guarda os dados digitados:

```javascript
const state = {
  captains: [],
  players: []
};
```

Cada capitão ou jogador possui um nome e um rating. Outras variáveis guardam os times gerados, o jogador selecionado e a montagem manual atual.

Esse estado existe apenas na memória do navegador. Não há `localStorage`, API ou banco de dados.

### Renderização da interface

As funções `renderCaptains`, `renderPlayers`, `renderManual` e `renderTeams` transformam o estado em HTML usando template strings e `innerHTML`.

O fluxo é:

1. O usuário altera um campo ou clica em uma estrela.
2. Um evento atualiza o estado.
3. A função de renderização desenha novamente a parte afetada da interface.

As classes CSS, como `active-section`, `selected-available` e `selected-player`, representam os estados visuais da aplicação.

### Validação

A função `validate()` usa `trim()`, `some()` e `filter()` para verificar:

- se algum capitão está sem nome;
- quantos jogadores foram preenchidos;
- se a quantidade é exatamente 25.

Se houver erro, a montagem não começa e uma mensagem é exibida na tela.

### Montagem manual

Na função `setupManual()`, cada capitão recebe um time vazio. A função `renderManual()` cria:

- a lista de jogadores disponíveis;
- os grupos por nível;
- os cinco times;
- os botões para adicionar e remover jogadores.

O campo `sourceIndex` preserva a posição original de cada jogador. Um `Set`, criado em `assignedPlayerIndexes()`, impede que um jogador já distribuído apareça novamente entre os disponíveis.

### Montagem automática

A função usada pelo botão de sorteio é `makeBalancedTeams()`:

1. Cria cinco times e coloca um capitão em cada um.
2. Ordena os jogadores do maior para o menor nível.
3. Procura o time com menor pontuação que ainda tenha espaço.
4. Adiciona o jogador nesse time.
5. Atualiza a pontuação e repete o processo.

Esse é um algoritmo guloso: a melhor escolha disponível é feita a cada passo. Ele é simples e rápido, mas não garante a combinação matematicamente perfeita em todos os casos.

O equilíbrio considera somente a soma dos níveis. Não considera posição, estilo de jogo, entrosamento ou preferências dos jogadores.

### Troca de jogadores

A função `selectOrSwapPlayer()` controla as trocas no resultado automático:

- o primeiro clique seleciona um jogador;
- o segundo clique em outro time troca os dois jogadores;
- clicar novamente no mesmo jogador cancela a seleção.

Depois da troca, `updateTeamScores()` recalcula a pontuação de cada equipe com `reduce()`.

### Segurança nos nomes

Como os cartões são montados com `innerHTML`, a função `escapeHtml()` transforma caracteres especiais em entidades HTML. Isso impede que um nome digitado seja interpretado como código HTML.

## Estrutura dos arquivos

```text
RoboSorteioTimes/
├── main.py
├── netlify.toml
├── README.md
└── static/
    ├── index.html
    ├── app.js
    ├── styles.css
    └── assets/
        └── racha-da-misericordia.png
```

### `main.py`

Servidor HTTP local feito com `http.server`, módulo incluído na biblioteca padrão do Python. Ele entrega os arquivos estáticos e abre `static/index.html` quando a raiz do site é acessada.

### `static/index.html`

Define a estrutura da página, os campos, os botões, a navegação e as áreas onde o JavaScript insere os cartões.

### `static/app.js`

Controla o estado, os eventos, a validação, as estrelas, a montagem manual e o algoritmo automático.

### `static/styles.css`

Define o tema visual, o layout com Flexbox e CSS Grid, os estados dos componentes e os ajustes para telas menores com media queries.

### `static/assets/`

Guarda a imagem usada na identidade visual da aplicação.

### `netlify.toml`

Indica que a pasta publicada em uma hospedagem estática é `static`:

```toml
[build]
publish = "static"
```

## Tecnologias e bibliotecas

<<<<<<< HEAD
- **HTML5:** estrutura semântica da página.
- **CSS3:** layout, cores, tipografia e responsividade.
- **JavaScript ES6+:** lógica, eventos, arrays, template strings e manipulação do DOM.
- **Python 3:** servidor local.
- **`http.server`:** servidor HTTP da biblioteca padrão do Python.
- **Google Fonts:** fontes Manrope e DM Mono.
- **Netlify:** configuração opcional para publicar os arquivos estáticos.

Não é necessário executar `pip install`, `npm install` ou configurar um banco de dados.

## Limitações atuais

- Os dados não são salvos permanentemente.
- Atualizar ou fechar a página apaga o cadastro.
- O equilíbrio automático usa somente os ratings.
- Não há login ou múltiplos usuários.
- O servidor Python é apenas para desenvolvimento local.
- O projeto não possui uma licença definida.
=======
Este projeto ainda não possui uma licença definida. Para distribuí-lo formalmente, adicione um arquivo `LICENSE` com a licença escolhida.
>>>>>>> 56ab56508514275abbf6bbe6f5dd07de2ce43eef
