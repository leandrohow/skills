# skills

Skills abertas para o Claude — construídas e documentadas por
**[Leandro Henrique de Souza](https://github.com/leandrohow)**.

> Coleção de Agent Skills genéricas, bem documentadas e feitas para serem
> estendidas. A ideia não é só te dar a skill pronta — é te mostrar *como ela é
> construída*, pra você conseguir fazer a sua.

**English summary:** A small, curated collection of open Agent Skills for Claude
— generic, well-documented, and built to be forked. Each skill ships with design
notes explaining *why* it's built the way it is, so you can build your own. The
skills' instructions are in Portuguese (one operates specifically on Portuguese
text); they work across Claude.ai, Claude Code, and Claude Cowork. Install
instructions below.

---

## O que é uma skill?

Uma skill é uma pasta com um arquivo `SKILL.md` — instruções estruturadas que
dão ao Claude uma capacidade nova e repetível, sem escrever código. Quando a
tarefa bate com a descrição da skill, o Claude a usa automaticamente. As skills
aqui seguem o padrão aberto [Agent Skills](https://agentskills.io), então
funcionam em qualquer ferramenta que adote o padrão.

## As skills

| Skill | O que faz |
|---|---|
| **[meeting-war-room](meeting-war-room/)** | Prepara você para uma reunião importante: gera um Mapa da Reunião com leitura de participantes, objeções prováveis, riscos e a jogada de condução. |
| **[automation-radar](automation-radar/)** | Audita sua rotina e diz o que automatizar, delegar ou eliminar — com ROI realista calculado por um script em Python. |
| **[humanizador](humanizador/)** | Tira a cara de IA de um texto em português, deixando-o natural — sem perder o sentido nem inventar. |

Cada pasta tem um `README.md` próprio com instruções de uso, notas de design e
pontos de extensão.

## Como instalar

As skills funcionam nas três superfícies do Claude. O mesmo `SKILL.md` roda em
todas — o que muda é como você instala. (Os passos abaixo refletem a interface
atual; para o procedimento sempre atualizado, veja a
[ajuda oficial](https://support.claude.com/en/articles/12512180-use-skills-in-claude).)

### Claude.ai (Chat)

1. Em **Configurações → Recursos (Capabilities)**, ative **Code Execution and
   File Creation**.
2. Compacte a pasta da skill em um `.zip` — a pasta da skill precisa ser a
   **raiz** do zip (ex.: o zip contém `meeting-war-room/SKILL.md`, não
   `skills/meeting-war-room/SKILL.md`).
3. Ainda em Recursos, faça upload do `.zip` na seção de Skills.

Os `.zip` prontos para upload estão nas
[Releases](https://github.com/leandrohow/skills/releases) deste repositório.

### Claude Cowork

1. Clique em **Customize** na barra lateral e abra o diretório.
2. Na aba **Skills**, instale a skill. Skills habilitadas também ficam
   disponíveis nos add-ins de Excel, PowerPoint, Word e Outlook.

### Claude Code

As skills são baseadas em arquivos — sem upload. Copie a pasta da skill para o
seu projeto:

```bash
mkdir -p .claude/skills
cp -r meeting-war-room .claude/skills/
```

O Claude Code carrega a skill automaticamente quando ela é relevante. Também dá
para usar `/nome-da-skill` para invocar manualmente.

## Filosofia

A maioria das skills públicas só diz o que faz. Estas tentam fazer melhor: cada
skill separa **o que o Claude lê em runtime** (o `SKILL.md`, operacional) da
**explicação para humanos** (o `README.md`, com notas de design e como
estender). Isso não é detalhe de organização — é o que permite que você pegue
qualquer skill aqui, entenda as decisões por trás dela e construa a sua versão.

Três princípios guiam todas:

- **Divulgação progressiva.** O `SKILL.md` fica enxuto; o conteúdo pesado vai
  para `reference/` e só entra no contexto quando é necessário.
- **Prosa para julgamento, script para o que precisa ser exato.** Cálculo vira
  código (ver `automation-radar/scripts/roi.py`), não texto.
- **A descrição é o gatilho.** É a `description` que faz a skill disparar — então
  ela é escrita concreta, específica e bilíngue.

## Uso responsável

Skills podem rodar ferramentas, ler arquivos e executar código. Revise qualquer
skill — daqui ou de qualquer lugar — antes de habilitar, e só use skills de
fontes em que você confia. Nenhuma skill deste repositório contém credenciais,
segredos ou código malicioso.

## Licença

[MIT](LICENSE) — use, modifique, distribua e construa em cima. Contribuições são
bem-vindas; veja [CONTRIBUTING.md](CONTRIBUTING.md).

---

Feito por Leandro Henrique de Souza · [github.com/leandrohow](https://github.com/leandrohow)
