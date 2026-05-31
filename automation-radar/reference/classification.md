# Classificação de Tarefas

Referência carregada sob demanda pela skill `automation-radar` para decidir o
balde de cada tarefa: **eliminar, delegar, automatizar ou manter**.

## A ordem importa

Sempre pergunte nesta ordem. Pular a primeira pergunta é o erro mais caro.

### 1. Isso precisa existir? → ELIMINAR

Antes de automatizar ou delegar, pergunte se a tarefa deveria simplesmente
deixar de existir. Relatório que ninguém lê, reunião recorrente sem decisão,
aprovação que não muda nada. **Automatizar uma tarefa inútil só a torna inútil
mais rápido.** Eliminar tem custo zero de manutenção e é quase sempre o melhor
movimento. Procure por: tarefas que existem "porque sempre foi assim", entregas
que ninguém usa, etapas de controle que nunca pegam erro.

### 2. Exige o seu julgamento único? → MANTER (ou automatizar partes)

Se a tarefa depende de critério, relacionamento ou contexto que só você tem,
mantenha. Mas quase toda tarefa "de julgamento" tem partes mecânicas em volta
(coletar dados, formatar, agendar). Automatize a casca, mantenha o miolo.

### 3. É repetível e previsível? → AUTOMATIZAR

Se a tarefa é sempre igual, segue regras claras e não exige decisão a cada vez,
é candidata a automação. Quanto mais previsível o input e o output, melhor a
candidata. Passe para o cálculo de ROI antes de decidir de fato (uma tarefa
automatizável de baixíssima frequência pode não compensar).

### 4. Precisa de uma pessoa, mas não de você? → DELEGAR

Tarefa que exige humano mas não exige *você* — vai para delegação. O critério
não é "é chato", e sim "alguém com menos contexto faria isso bem com uma
instrução clara?". Se sim, delegue. Delegar bem é escrever a instrução uma vez e
nunca mais fazer a tarefa.

## Armadilhas comuns

- **Automatizar o que deveria sumir.** Coberto acima — a mais cara.
- **Sobre-engenharia.** Montar um sistema robusto pra uma tarefa rara. O ROI
  pega isso, mas o impulso de "fazer direito" é forte. Resista.
- **Confundir frequência com importância.** Algo que você faz toda hora pode ter
  baixo valor (e merecer eliminação), não automação.
- **Automatizar input instável.** Se o formato da entrada muda toda vez (uma
  planilha que cada pessoa preenche diferente), a automação vive quebrando. Ou
  você estabiliza o input primeiro, ou não automatiza.
- **Ignorar a manutenção.** Toda automação custa atenção contínua. Some isso ao
  custo antes de decidir (o `scripts/roi.py` já desconta).

## Resumo de bolso

| Pergunta | Se sim |
|---|---|
| Ninguém perde se isso parar de existir? | **Eliminar** |
| Só você consegue fazer (julgamento/relação)? | **Manter** (automatize a casca) |
| É sempre igual e segue regras? | **Automatizar** (rode o ROI) |
| Precisa de humano, mas não de você? | **Delegar** |
