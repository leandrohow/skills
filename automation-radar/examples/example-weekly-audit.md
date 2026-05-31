# Exemplo — Radar de Automação (rotina semanal)

Exemplo completo de saída da skill `automation-radar`, a partir de um contexto
fictício.

---

**Contexto dado pelo usuário:**

> Minha semana tem essas tarefas fixas:
> - Relatório de status toda segunda: copio dados de 3 planilhas e colo num doc (~40 min).
> - Respondo e-mails de agendamento de reunião, uns 10 por dia (~3 min cada).
> - Reunião de "alinhamento" toda quarta, 1h, com 6 pessoas — raramente sai decisão.
> - Reviso propostas comerciais antes de enviar (~30 min cada, ~3 por semana).
> - Atualizo uma planilha de controle de horas, todo fim de dia (~5 min).

---

# Radar de Automação — rotina semanal

**Tempo recuperável estimado:** ~4,5 horas/semana

## Quadro

| Tarefa | Tempo/sem | Balde | Recomendação | ROI |
|---|---|---|---|---|
| Relatório de status (segunda) | ~0,7 h | automatizar | script que consolida as 3 planilhas | payback ~9 sem |
| E-mails de agendamento | ~2,5 h | automatizar | ferramenta de autoagendamento (link de calendário) | payback ~2 sem |
| Reunião de alinhamento (quarta) | 1,0 h | eliminar | substituir por update assíncrono escrito | imediato |
| Revisão de propostas | ~1,5 h | manter | julgamento seu — automatize só a checagem de formato | — |
| Planilha de horas (diária) | ~0,4 h | automatizar/eliminar | avaliar se o controle ainda é necessário | baixo |

## Top 3 movimentos (por retorno sobre esforço)

1. **E-mails de agendamento** — adotar link de autoagendamento elimina quase
   toda a troca de mensagens. Ganho: ~2,5 h/semana. Esforço: ~2 h de setup.
   Por que primeiro: maior ganho, menor esforço, e o input já é padronizado.
2. **Reunião de alinhamento** — trocar por um update escrito assíncrono. Ganho:
   1 h/semana sua + o tempo das outras 5 pessoas. Esforço: ~zero, é uma decisão.
   Por que segundo: eliminar é o melhor tipo de ROI — custo de manutenção zero.
3. **Relatório de status** — script em Python que lê as 3 planilhas e gera o
   doc. Ganho: ~0,7 h/semana. Esforço: ~6 h. Por que terceiro: vale, mas só
   depois de confirmar que as planilhas têm formato estável.

## Eliminar primeiro

A reunião de quarta. Uma hora recorrente que "raramente gera decisão" é o
candidato número um a deixar de existir. Vira um texto assíncrono; quem precisar
decidir algo, marca pontual.

## Cuidado

- **Revisão de propostas — não automatize.** Parece repetível, mas é onde seu
  julgamento comercial entra. Automatize só a checagem mecânica (formato, dados,
  typos); o conteúdo continua seu.
- **Planilha de horas — investigue antes de automatizar.** Antes de montar
  qualquer coisa, pergunte se esse controle ainda serve a alguém. Pode ser caso
  de eliminar, não de automatizar.
