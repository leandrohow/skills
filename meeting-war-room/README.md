# meeting-war-room

> Prepara você para uma reunião importante gerando um **Mapa da Reunião**:
> objetivo, leitura dos participantes, objeções prováveis com respostas, riscos
> e uma jogada de condução.

**English summary:** A Claude skill that prepares you for a high-stakes meeting
(sales, negotiation, stakeholder alignment, kickoff, QBR) by producing a concise
*Meeting Map* — objective, stakeholder read, likely objections with responses,
risk register, and an opening/closing play. The skill's instructions are in
Portuguese; it works in any language. Triggers on meeting-prep intent even
without the words "war room".

---

## O que faz

Transforma uma reunião de improviso em jogada pensada. Em vez de você entrar na
sala torcendo, a skill produz um documento curto que responde: quem está na
sala, o que cada um quer, o que pode dar errado e como você reage. O mapa é pra
ser relido em 2 minutos antes da reunião — munição mental, não roteiro.

## Quando dispara

Pedidos como "me prepara pra essa reunião", "reunião de venda amanhã",
"quem vai estar na sala", "quais objeções podem aparecer", "game plan da
reunião" — ou quando você cola uma pauta, lista de participantes ou contexto de
cliente. Não precisa dizer "war room".

## Como usar

1. Instale a skill (veja o [README do repositório](../README.md)).
2. Descreva a reunião: objetivo, quem participa, histórico, restrições.
3. Responda às perguntas de lacuna (no máximo uma rodada).
4. Receba o Mapa da Reunião. Releia antes de entrar.

Exemplo completo de saída em [`examples/example-saas-renewal.md`](examples/example-saas-renewal.md).

## Anatomia

```
meeting-war-room/
├─ SKILL.md                         ← o que o Claude lê em runtime (fluxo + template)
├─ reference/
│  ├─ stakeholder-mapping.md        ← método de leitura de pessoas + arquétipos
│  └─ objection-patterns.md         ← objeções clássicas + estrutura de resposta
└─ examples/
   └─ example-saas-renewal.md       ← exemplo trabalhado completo
```

## Notas de design

Por que a skill está estruturada assim — útil se você quiser construir a sua
versão:

- **A `description` carrega todo o gatilho.** No padrão de skills, é a
  `description` (não o corpo) que decide se a skill é acionada. Ela é escrita em
  PT **e** EN e levemente "puxada" porque o Claude tende a *subdisparar* skills —
  ou seja, não usá-las quando seriam úteis. Frases de gatilho concretas resolvem
  isso melhor que uma descrição abstrata.
- **Coleta de contexto antes de gerar.** A maior falha de uma skill de
  preparação é cuspir um mapa genérico. Por isso o fluxo força a coleta do
  essencial primeiro — e instrui a *não* reperguntar o que já está na conversa.
- **Divulgação progressiva (progressive disclosure).** O método detalhado de
  leitura de stakeholders e o catálogo de objeções ficam em `reference/`, fora
  do `SKILL.md`. Eles só entram no contexto quando são necessários, o que mantém
  a skill leve em toda ativação. Esse é o padrão que separa uma skill enxuta de
  um prompt gigante.
- **Template fixo de saída.** O formato do mapa é fixo de propósito: consistência
  na saída é o que torna a skill confiável de usar repetidamente.

## Como estender

Pontos de extensão pensados para você adaptar:

- **Sua biblioteca de objeções.** `reference/objection-patterns.md` traz padrões
  genéricos. Troque pelas objeções reais do seu mercado e suas respostas
  testadas — é aqui que a skill vira *sua*.
- **Seus arquétipos de stakeholder.** Se você vende sempre pro mesmo tipo de
  comprador, substitua os arquétipos genéricos pelos personas do seu funil.
- **Um passo de pesquisa.** Se você tiver as ferramentas, adicione uma etapa que
  busca os participantes no LinkedIn antes da leitura.
- **Conexão com CRM.** Plugue uma etapa que puxa o histórico da conta de um MCP
  do seu CRM, em vez de depender do que você digita.
- **Rubrica de pontuação.** Adicione um score de "prontidão da reunião" (0-10)
  ao final do mapa, com critérios.

## Licença

MIT — veja [LICENSE](../LICENSE). Use, modifique e construa em cima.
