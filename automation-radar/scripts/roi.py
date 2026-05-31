#!/usr/bin/env python3
"""
roi.py — Calculadora de ROI de automação para a skill `automation-radar`.

Método
------
A conta é deliberadamente simples e conservadora. A ideia não é precisão
contábil, e sim uma decisão honesta: vale o esforço de montar e manter esta
automação?

    horas_por_ano   = (minutos_por_ocorrencia / 60) * ocorrencias_por_ano
    payback_semanas = setup_horas / horas_economizadas_por_semana

Por padrão descontamos uma manutenção anual (15% do tempo de setup), porque
automação não é "monte e esqueça" — ela quebra, muda, precisa de ajuste. Ignorar
isso é o erro otimista mais comum.

Veredito (heurística, ajuste à vontade):
    - payback <= 12 semanas  -> "vale"
    - payback <= 52 semanas  -> "marginal"
    - payback  > 52 semanas  -> "não vale"

Uso (linha de comando)
----------------------
    python roi.py --minutes 15 --per-week 5 --setup-hours 8
    python roi.py --minutes 40 --per-month 4 --setup-hours 6 --hourly 120

Uso (importado)
---------------
    from roi import roi
    r = roi(minutes=15, per_week=5, setup_hours=8)
    print(r["payback_weeks"], r["verdict"])
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, asdict


WEEKS_PER_YEAR = 52
MAINTENANCE_FRACTION = 0.15  # manutenção anual como fração do setup


@dataclass
class ROIResult:
    hours_saved_per_week: float
    hours_saved_per_year: float
    setup_hours: float
    maintenance_hours_per_year: float
    net_hours_year_1: float          # economia ano 1 menos setup e manutenção
    payback_weeks: float | None      # None se não economiza tempo
    verdict: str
    money_saved_per_year: float | None  # só se hourly for informado


def roi(
    minutes: float,
    setup_hours: float,
    per_week: float | None = None,
    per_month: float | None = None,
    hourly: float | None = None,
    maintenance_fraction: float = MAINTENANCE_FRACTION,
) -> dict:
    """Calcula o ROI de automatizar uma tarefa recorrente.

    Informe a frequência por --per-week OU --per-month (não os dois).
    """
    if per_week is None and per_month is None:
        raise ValueError("Informe per_week ou per_month.")
    if per_week is not None and per_month is not None:
        raise ValueError("Informe apenas um: per_week ou per_month.")

    occurrences_per_week = per_week if per_week is not None else (per_month * 12) / WEEKS_PER_YEAR

    hours_per_occurrence = minutes / 60.0
    hours_saved_per_week = hours_per_occurrence * occurrences_per_week
    hours_saved_per_year = hours_saved_per_week * WEEKS_PER_YEAR
    maintenance_hours_per_year = setup_hours * maintenance_fraction

    net_hours_year_1 = hours_saved_per_year - setup_hours - maintenance_hours_per_year

    if hours_saved_per_week <= 0:
        payback_weeks = None
        verdict = "não vale"
    else:
        payback_weeks = setup_hours / hours_saved_per_week
        if payback_weeks <= 12:
            verdict = "vale"
        elif payback_weeks <= WEEKS_PER_YEAR:
            verdict = "marginal"
        else:
            verdict = "não vale"

    money = (hours_saved_per_year * hourly) if hourly is not None else None

    result = ROIResult(
        hours_saved_per_week=round(hours_saved_per_week, 2),
        hours_saved_per_year=round(hours_saved_per_year, 1),
        setup_hours=setup_hours,
        maintenance_hours_per_year=round(maintenance_hours_per_year, 1),
        net_hours_year_1=round(net_hours_year_1, 1),
        payback_weeks=(round(payback_weeks, 1) if payback_weeks is not None else None),
        verdict=verdict,
        money_saved_per_year=(round(money, 2) if money is not None else None),
    )
    return asdict(result)


def _format(r: dict) -> str:
    lines = [
        f"Horas economizadas/semana : {r['hours_saved_per_week']}",
        f"Horas economizadas/ano    : {r['hours_saved_per_year']}",
        f"Setup (uma vez)           : {r['setup_hours']} h",
        f"Manutenção/ano            : {r['maintenance_hours_per_year']} h",
        f"Saldo líquido no ano 1    : {r['net_hours_year_1']} h",
        f"Payback                   : "
        + (f"{r['payback_weeks']} semanas" if r["payback_weeks"] is not None else "nunca"),
        f"Veredito                  : {r['verdict'].upper()}",
    ]
    if r["money_saved_per_year"] is not None:
        lines.append(f"Economia financeira/ano   : {r['money_saved_per_year']}")
    return "\n".join(lines)


def main() -> None:
    p = argparse.ArgumentParser(description="Calculadora de ROI de automação.")
    p.add_argument("--minutes", type=float, required=True, help="Minutos por ocorrência.")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--per-week", type=float, help="Ocorrências por semana.")
    g.add_argument("--per-month", type=float, help="Ocorrências por mês.")
    p.add_argument("--setup-hours", type=float, required=True, help="Horas para montar a automação.")
    p.add_argument("--hourly", type=float, default=None, help="(Opcional) Valor da sua hora, para economia em R$.")
    args = p.parse_args()

    r = roi(
        minutes=args.minutes,
        setup_hours=args.setup_hours,
        per_week=args.per_week,
        per_month=args.per_month,
        hourly=args.hourly,
    )
    print(_format(r))


if __name__ == "__main__":
    main()
