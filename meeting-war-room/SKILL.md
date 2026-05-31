---
name: meeting-war-room
description: >-
  Prepara o usuário para uma reunião importante gerando um Mapa da Reunião:
  objetivo real, leitura dos participantes, objeções prováveis com respostas,
  riscos e uma estratégia de condução. / Prepares the user for a high-stakes
  meeting by producing a Meeting Map (objective, stakeholder read, likely
  objections with responses, risks, and a play). Use sempre que o usuário
  mencionar "preparar reunião", "me preparar para apresentar", "reunião de
  venda", "negociação", "como conduzir essa reunião", "quem vai estar na sala",
  "objeções possíveis", "war room", "game plan", "briefing de reunião", ou
  compartilhar lista de participantes, pauta ou contexto de cliente com a
  intenção de entrar preparado — even when the user says "meeting prep",
  "stakeholder prep", "QBR", "kickoff", or "how do I handle this conversation".
  Use this even if the user does not say "war room" explicitly.
---

# Meeting War Room

Gera o **Mapa da Reunião**: um documento curto de preparação que transforma uma
reunião importante de improviso em jogada pensada. O mapa é munição mental para
quem vai conduzir — não um roteiro pra ler em voz alta. Quem entra com mapa
escuta melhor, antecipa, e não é pego de surpresa.

Princípio: **a reunião é ganha antes de começar.** O valor não está em prever
cada frase, e sim em chegar com hipóteses sobre quem está na sala, o que cada um
quer, o que pode dar errado e como você reage.

## Fluxo

Siga esta sequência. Não pule a coleta de contexto — um mapa genérico não serve
pra nada.

### 1. Colete o contexto (pergunte só o que faltar)

Antes de gerar qualquer coisa, você precisa saber:

- **Objetivo da reunião** — o que conta como sucesso ao sair da sala? (avançar
  proposta, fechar, alinhar escopo, destravar decisão, etc.)
- **Quem participa** — nomes, cargos, e o que se sabe de cada um. Se houver
  links de LinkedIn, transcrições anteriores ou e-mails, use.
- **Histórico** — o que já aconteceu antes desta reunião?
- **Restrições** — prazo, orçamento, concorrência, política interna.

Se o usuário já deu parte disso na conversa, **não pergunte de novo** — extraia.
Pergunte apenas as lacunas que mudam o mapa. Faça no máximo uma rodada de
perguntas; com o essencial em mãos, gere.

### 2. Leia os participantes

Para cada pessoa relevante, identifique: o que ela quer de verdade, o que ela
teme, qual o poder dela na decisão, e como ela provavelmente vai se posicionar.
Para o método de leitura e os arquétipos comuns (decisor, influenciador,
cético, bloqueador, patrocinador), consulte `reference/stakeholder-mapping.md`.

### 3. Antecipe objeções

Liste as objeções mais prováveis e prepare uma resposta para cada. A resposta
não é um contra-ataque — é um reconhecimento seguido de reenquadramento. Para os
padrões de objeção e a estrutura de resposta, consulte
`reference/objection-patterns.md`.

### 4. Mapeie riscos

Pense no que pode descarrilar a reunião e classifique cada risco por
probabilidade e impacto. Tipos comuns:

- **Ausência de poder** — a pessoa que decide não está na sala.
- **Agenda oculta** — alguém quer algo que não está na pauta.
- **Sequestro de pauta** — a conversa escapa para um tema secundário.
- **Silêncio** — ninguém se compromete e a reunião "morre" sem decisão.
- **Comparação** — surge um concorrente ou alternativa não prevista.

Para cada risco de probabilidade média/alta, defina um movimento de mitigação.

### 5. Monte a jogada

Defina três coisas, sempre conectadas ao objetivo:

- **Abertura** — como você ancora a reunião nos primeiros 2 minutos.
- **Condução** — a sequência que leva ao objetivo, e onde você dá espaço pra
  escuta.
- **Fechamento** — qual é o próximo passo concreto que você quer arrancar antes
  de todos saírem da sala.

## Formato de saída

SEMPRE entregue o mapa neste template, em prosa enxuta (sem encher):

```markdown
# Mapa da Reunião — [contexto]

**Objetivo:** [o que conta como sucesso, em uma frase]

## Quem está na sala
- **[Nome — cargo]:** quer [X] · teme [Y] · poder [alto/médio/baixo] · provável postura: [...]
- (repita por participante relevante)

## Objeções prováveis
1. **"[objeção]"** → [reconhecimento + reenquadramento, 1-2 frases]
2. ...

## Riscos
- **[risco]** (prob. [alta/média/baixa], impacto [alto/médio/baixo]) → mitigação: [...]

## A jogada
- **Abertura:** [...]
- **Condução:** [...]
- **Fechamento (próximo passo a arrancar):** [...]

## Um lembrete
[uma única frase de foco — o que NÃO esquecer no calor da reunião]
```

Mantenha o mapa curto o suficiente para ser relido em 2 minutos antes da
reunião. Se ficar longo, corte — densidade vale mais que completude aqui.

## Exemplo

**Input:** "Reunião amanhã com o time de TI de um cliente pra renovar um
contrato de software. Vai o gerente de TI (gosta da gente) e o novo CFO (entrou
há 1 mês, está cortando custos). Objetivo: renovar sem desconto agressivo."

**Output:** um Mapa da Reunião onde o CFO aparece como cético-de-custo (quer
provar valor da posição dele, teme estar pagando caro), com objeção provável
"está caro demais" respondida por reenquadramento em custo-de-troca e risco
operacional; risco principal = o CFO ancorar a conversa em preço antes de ver
valor, mitigado por abrir com resultado entregue no último ciclo; fechamento =
arrancar uma data para a decisão, não a decisão na hora.

Veja um exemplo completo em `examples/example-saas-renewal.md`.
