# humanizador

> Reescreve um texto em português para soar humano, removendo os sinais típicos
> de escrita gerada por IA — sem perder o sentido, sem inventar e sem inflar.

**English summary:** A Claude skill that rewrites Brazilian Portuguese text to
remove AI-writing tells (inflated language, forced "not only X but also Y"
symmetry, empty emphasis, corporate jargon, emoji-laden formatting) while
preserving meaning and never adding facts. Operates on Portuguese text; useful
for the Brazilian market specifically. Triggers on "humanizar / tirar cara de
IA" and variations.

---

## O que faz

Pega um texto com cara de ChatGPT e devolve uma versão que soa como pessoa.
A filosofia é simples: **humanizar é cortar, não enfeitar.** Texto de IA tem
gordura — rodeios, ênfases vazias, simetrias forçadas. A skill remove isso e
devolve o ritmo irregular da escrita humana. O resultado é quase sempre mais
curto que o original.

## Quando dispara

"Humaniza isso", "tira o jeitão de IA", "deixa mais natural", "remove o slop",
"reescreve como humano" — ou quando você cola um texto em português com padrões
óbvios de IA e pede para "arrumar" ou "melhorar".

## Como usar

1. Instale a skill (veja o [README do repositório](../README.md)).
2. Cole o texto e peça para humanizar.
3. Receba o texto reescrito, pronto pra usar. Peça "mostra o que mudou" se quiser
   ver os cortes.

Exemplos de antes/depois em [`examples/exemplo-antes-depois.md`](examples/exemplo-antes-depois.md).

## Anatomia

```
humanizador/
├─ SKILL.md                     ← o que o Claude lê em runtime (regras + fluxo)
├─ reference/
│  └─ sinais-de-ia.md           ← catálogo completo de padrões de IA + conserto
└─ examples/
   └─ exemplo-antes-depois.md   ← pares antes/depois em 3 registros
```

## Notas de design

- **Regras inegociáveis no topo do `SKILL.md`.** Preservar sentido, nunca
  inventar, não inflar, respeitar o registro. Elas vêm antes do fluxo de
  propósito: o maior risco de uma skill de reescrita é "melhorar" o texto
  inventando coisas ou trocando o tom. As regras prendem isso.
- **O catálogo de sinais fica em `reference/`, não no corpo.** Divulgação
  progressiva: o `SKILL.md` lista os sinais mais comuns; o catálogo detalhado
  com exemplos só entra no contexto quando é preciso. Mantém a skill leve.
- **A saída é o texto, sem preâmbulo.** Por padrão a skill entrega só o texto
  reescrito — porque é isso que você vai colar em algum lugar. O "o que mudei" é
  opcional, sob pedido.
- **É deliberadamente PT-BR.** Os sinais de IA em português têm marcas próprias
  ("não apenas X, mas também Y", "de suma importância", "alavancar"). Uma skill
  genérica em inglês não pega esses padrões com a mesma precisão. A
  especificidade de idioma é a força dela, não uma limitação.

## Como estender

- **Sua lista de palavras-mortas.** Adicione ao catálogo os clichês que *você*
  mais detesta — a skill fica com a sua sensibilidade editorial.
- **Seu registro padrão.** Se você sempre escreve no mesmo tom (formal, casual,
  técnico), fixe isso nas regras pra não precisar pedir toda vez.
- **Suporte a inglês.** Duplique o catálogo de sinais para EN e amplie a
  `description` — vira um humanizador bilíngue.
- **Modo "diff".** Faça o "o que mudei" virar padrão, com antes/depois lado a
  lado, se você quiser aprender com os cortes em vez de só aplicá-los.

## Nota de uso responsável

Esta skill melhora a *qualidade* da escrita; ela não foi feita para enganar
detectores de IA nem para fazer passar por humano um texto que precisa ser
declarado como gerado por IA. Use para escrever melhor, não para burlar regras
de transparência de onde você publica.

## Licença

MIT — veja [LICENSE](../LICENSE). Use, modifique e construa em cima.
