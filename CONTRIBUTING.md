# Contribuindo / Contributing

🇧🇷 **Português**

Estas skills foram feitas para serem forkadas, melhoradas e adaptadas. Se você
construiu uma versão melhor, ótimo — esse é o objetivo.

**Como propor melhorias:**

1. Faça um fork do repositório.
2. Crie um branch para sua mudança (`git checkout -b minha-melhoria`).
3. Edite a skill. Se mudar comportamento, atualize também o `README.md` da skill
   e os exemplos.
4. Abra um Pull Request descrevendo o que mudou e por quê.

**Padrão das skills deste repo:**

- Cada skill é uma pasta com `SKILL.md` (obrigatório), `README.md`, e opcionais
  `reference/`, `scripts/`, `examples/`.
- O `SKILL.md` segue o padrão aberto de Agent Skills ([agentskills.io](https://agentskills.io)):
  frontmatter YAML com `name` e `description`, corpo em Markdown.
- A `description` é o gatilho — escreva-a concreta e específica.
- Coloque o que o Claude lê em runtime no `SKILL.md`; a explicação para humanos
  (notas de design, como estender) vai no `README.md`.
- Nada de credenciais, segredos ou código malicioso. Skills podem rodar
  ferramentas e código — mantenha tudo transparente.

---

🇬🇧 **English**

These skills are meant to be forked, improved, and adapted. If you built a
better version, great — that's the point.

**To propose changes:**

1. Fork the repo.
2. Create a branch (`git checkout -b my-improvement`).
3. Edit the skill. If you change behavior, update the skill's `README.md` and
   examples too.
4. Open a Pull Request describing what changed and why.

**Repo conventions:**

- Each skill is a folder with `SKILL.md` (required), `README.md`, and optional
  `reference/`, `scripts/`, `examples/`.
- `SKILL.md` follows the open Agent Skills standard
  ([agentskills.io](https://agentskills.io)): YAML frontmatter with `name` and
  `description`, Markdown body.
- The `description` is the trigger — make it concrete and specific.
- Put what Claude reads at runtime in `SKILL.md`; human-facing explanation goes
  in `README.md`.
- No credentials, secrets, or malicious code. Skills can run tools and code —
  keep everything transparent.
