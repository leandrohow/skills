---
name: automation-radar
description: >-
  Audita a rotina de trabalho do usuário, encontra tarefas de baixo valor que
  consomem tempo e recomenda o que automatizar, delegar ou eliminar — com um ROI
  realista calculado. / Audits the user's work routine, finds low-value time
  sinks, and recommends what to automate, delegate, or eliminate with a
  realistic ROI estimate. Use sempre que o usuário disser "o que eu automatizo",
  "onde estou perdendo tempo", "o que dá pra delegar", "auditoria de rotina",
  "estou virando gargalo", "não dou conta", "vale a pena automatizar X",
  "como ganho tempo de volta", "tô gastando X horas com Y" — even when phrased
  as "what should I automate", "routine audit", "I'm overloaded", or "ROI of
  automating this". Use this even if the user does not say "automation"
  explicitly.
---

# Automation Radar

Mapeia a rotina de alguém, separa o que dá valor do que só consome tempo, e
recomenda **automatizar, delegar ou eliminar** cada peça — sempre com um ROI
realista, não com entusiasmo. O objetivo é devolver horas, não impressionar com
tecnologia.

Princípio: **a pergunta não é "isso dá pra automatizar?", e sim "vale a pena
automatizar isso?".** Quase tudo é automatizável; pouca coisa compensa o custo
de montar e manter a automação. Esta skill existe pra evitar que você gaste 10
horas automatizando uma tarefa de 5 minutos por mês.

## Fluxo

### 1. Levante a rotina

Peça ao usuário (ou extraia da conversa) a lista de tarefas recorrentes. Para
cada tarefa, você precisa de três números:

- **Tempo por ocorrência** (em minutos)
- **Frequência** (quantas vezes por semana/mês)
- **Quão repetível/previsível é** (sempre igual vs. exige julgamento)

Se o usuário não souber os números exatos, peça uma estimativa — aproximado
serve. Não trave a análise esperando precisão.

### 2. Classifique cada tarefa

Coloque cada tarefa em um balde: **eliminar**, **delegar**, **automatizar** ou
**manter**. A decisão depende de valor da tarefa, repetibilidade e quanto
julgamento ela exige. Para os critérios de classificação e as armadilhas
comuns (ex.: automatizar algo que deveria simplesmente deixar de existir),
consulte `reference/classification.md`.

### 3. Calcule o ROI das candidatas a automação

Para as tarefas marcadas como "automatizar", estime o retorno. Use o script
`scripts/roi.py`, que calcula horas economizadas por ano e o tempo de payback
da automação:

```bash
python scripts/roi.py --minutes 15 --per-week 5 --setup-hours 8
```

O script devolve horas/ano economizadas, o payback em semanas e um veredito
(vale, marginal, não vale). Rode-o por tarefa em vez de estimar de cabeça —
cálculo determinístico evita o viés otimista de quem está empolgado pra
automatizar. Para o método por trás da conta, veja o cabeçalho do próprio
script.

### 4. Escolha o "como"

Para cada tarefa que vale automatizar, recomende o caminho mais barato que
resolve — nem sempre é o mais sofisticado. As opções vão de template e atalho
até skill do Claude, script ou no-code. Consulte
`reference/automation-menu.md` para o menu de opções e quando usar cada uma.

### 5. Priorize

Ordene as recomendações por retorno sobre esforço. O que dá mais horas de volta
com menos esforço de montagem vem primeiro. Eliminar costuma ganhar de tudo —
custo zero de manutenção.

## Formato de saída

SEMPRE entregue neste formato:

```markdown
# Radar de Automação — [pessoa/contexto]

**Tempo recuperável estimado:** ~[X] horas/semana

## Quadro
| Tarefa | Tempo/sem | Balde | Recomendação | ROI |
|---|---|---|---|---|
| [tarefa] | [h] | automatizar/delegar/eliminar/manter | [como] | payback [X] sem |

## Top 3 movimentos (por retorno sobre esforço)
1. **[tarefa]** — [o que fazer], [ganho], [esforço de montagem]. Por que primeiro: [...]
2. ...
3. ...

## Eliminar primeiro
[tarefas que deveriam simplesmente deixar de existir — ganho imediato, custo zero]

## Cuidado
[1-2 tarefas que parecem boas candidatas mas NÃO valem automatizar, e por quê]
```

A seção "Cuidado" é obrigatória: a credibilidade da análise vem de você dizer
*não* automatizar algo, não de recomendar automação pra tudo.

## Exemplo

**Input:** "Toda segunda eu monto um relatório de status copiando dados de 3
planilhas e colando num doc. Leva uns 40 minutos."

**Output:** tarefa classificada como automatizar (repetível, sem julgamento);
ROI calculado (40 min × 1/sem ≈ 35 h/ano; com ~6h de montagem, payback em ~9
semanas → vale); recomendação de caminho (script Python ou skill que consolida
as 3 fontes), com a ressalva de validar que as planilhas têm formato estável
antes de investir na automação.

Veja um exemplo completo em `examples/example-weekly-audit.md`.
