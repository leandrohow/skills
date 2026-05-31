# automation-radar

> Audita sua rotina, encontra as tarefas que só consomem tempo e recomenda o que
> **automatizar, delegar ou eliminar** — com ROI realista calculado, não com
> entusiasmo.

**English summary:** A Claude skill that audits your work routine, finds
low-value time sinks, and recommends what to automate, delegate, or eliminate —
each with a realistic ROI estimate computed by a bundled Python script. The
skill's instructions are in Portuguese; it works in any language. Triggers on
overload / time-waste intent even without the word "automation".

---

## O que faz

Em vez de "isso dá pra automatizar?" (quase tudo dá), a skill pergunta "isso
**vale** automatizar?". Ela mapeia suas tarefas recorrentes, classifica cada uma
(eliminar / delegar / automatizar / manter), calcula o payback das candidatas a
automação e prioriza por retorno sobre esforço. A seção mais valiosa da saída é a
que diz o que **não** automatizar.

## Quando dispara

"O que eu automatizo", "onde estou perdendo tempo", "tô virando gargalo", "não
dou conta", "vale a pena automatizar X", "tô gastando 3 horas com Y" — ou
qualquer reclamação de sobrecarga. Não precisa dizer "automação".

## Como usar

1. Instale a skill (veja o [README do repositório](../README.md)). Para o
   cálculo de ROI rodar, você precisa de execução de código ligada (Chat/Cowork)
   ou estar no Claude Code.
2. Liste suas tarefas recorrentes com tempo e frequência aproximados.
3. Receba o Radar de Automação com quadro, top 3 movimentos e os alertas de
   "não automatize isso".

Exemplo completo em [`examples/example-weekly-audit.md`](examples/example-weekly-audit.md).

## Anatomia

```
automation-radar/
├─ SKILL.md                      ← o que o Claude lê em runtime (fluxo + template)
├─ scripts/
│  └─ roi.py                     ← calculadora de payback (determinística, em Python)
├─ reference/
│  ├─ classification.md          ← critérios dos 4 baldes + armadilhas
│  └─ automation-menu.md         ← menu de caminhos, do mais barato ao mais robusto
└─ examples/
   └─ example-weekly-audit.md    ← exemplo trabalhado completo
```

## Notas de design

- **Um script faz o cálculo, não o modelo.** O ROI vive em `scripts/roi.py`, não
  em prosa. Por quê: cálculo é exatamente o tipo de coisa que deve ser
  determinística — um script sempre dá o mesmo resultado e remove o viés
  otimista de quem está empolgado pra automatizar. Esse é um padrão central de
  skills: **prosa para julgamento, script para o que precisa ser exato.**
- **O custo de manutenção entra na conta.** O script desconta 15% do setup como
  manutenção anual, porque "automação que monta e esquece" não existe. Ignorar
  manutenção é o erro de ROI mais comum.
- **"Eliminar" antes de "automatizar".** O fluxo força a pergunta "isso precisa
  existir?" antes de qualquer ferramenta. Automatizar tarefa inútil é o
  anti-padrão que a skill foi feita pra evitar.
- **A `description` é o gatilho** e está em PT + EN, levemente "puxada", com
  frases de sobrecarga reais — porque o usuário raramente pede "automação"; ele
  diz que está afogado.

## Como estender

- **Calibre o veredito.** Os cortes de payback (12 e 52 semanas) e o fator de
  manutenção (15%) estão no topo de `roi.py`. Ajuste à sua realidade.
- **Custo monetário.** Passe `--hourly` pro script pra ver economia em R$, não só
  em horas — útil pra justificar investimento.
- **Conecte sua agenda.** Adicione uma etapa que lê seu calendário (via um MCP)
  e detecta reuniões recorrentes candidatas a eliminação, em vez de depender do
  que você lista.
- **Seu próprio menu de ferramentas.** Troque `automation-menu.md` pelas
  ferramentas que você de fato usa e domina.

## Licença

MIT — veja [LICENSE](../LICENSE). Use, modifique e construa em cima.
