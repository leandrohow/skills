# Menu de Automação

Referência carregada sob demanda pela skill `automation-radar`. Lista os
caminhos de automação do mais barato ao mais robusto. **Regra geral: escolha o
caminho mais simples que resolve.** Sofisticação é custo, não virtude.

## Do mais barato ao mais robusto

### Eliminar / simplificar (custo ~zero)

Antes de qualquer ferramenta: a tarefa pode acabar, encolher ou virar menos
frequente? Relatório semanal que vira mensal. Aprovação que vira notificação.
Sempre o primeiro a considerar.

### Template / checklist / atalho de texto

Para tarefas que você refaz do zero mas que são quase iguais. Um modelo de
documento, um snippet de texto, um atalho de teclado. Setup de minutos, sem
manutenção. Resolve mais coisa do que parece.

### Skill do Claude

Para tarefas de raciocínio repetível: gerar um tipo de documento, processar um
formato de entrada, seguir um fluxo de análise. A skill empacota a instrução
uma vez e o Claude a aplica de novo de forma consistente. Bom quando a tarefa
envolve linguagem/julgamento estruturado, não só mover dados.

### Automação no-code (Zapier, Make, n8n e afins)

Para conectar apps e disparar ações em eventos ("quando chega e-mail X, salva
anexo em Y"). Sem código, mas exige manutenção quando os apps mudam. Bom para
fluxos entre ferramentas que têm integração pronta.

### Script (Python, Bash)

Para transformação de dados, consolidação de planilhas, geração de arquivos —
qualquer coisa determinística e repetível. Mais esforço inicial, mas controle
total e custo de execução baixo. Ideal quando a lógica é clara e o input é
estável. Um script bem escrito é a automação mais durável da lista.

### Sistema sob medida / integração

Para volume alto e processo central do negócio. Maior custo de montagem e
manutenção — só se justifica quando o ROI é grande e recorrente. Raramente o
primeiro passo; normalmente o destino de algo que começou como script.

## Como escolher

Pergunte, nesta ordem:

1. **Dá pra eliminar ou encolher?** Faça isso primeiro.
2. **É só formatação/repetição de texto?** Template ou atalho.
3. **Envolve linguagem ou julgamento estruturado?** Skill do Claude.
4. **É mover dados entre apps com integração pronta?** No-code.
5. **É transformar dados com lógica clara?** Script.
6. **É volume alto e central, com ROI grande?** Aí sim, sistema sob medida.

## Delegação não é automação (mas resolve o mesmo problema)

Se a tarefa precisa de humano mas não de você, a "automação" certa é uma
instrução boa entregue uma vez. Documente o passo a passo, defina o critério de
pronto, e delegue. O custo é escrever bem uma vez; o retorno é nunca mais fazer.
