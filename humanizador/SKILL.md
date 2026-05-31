---
name: humanizador
description: >-
  Remove sinais de escrita gerada por IA de um texto em português, deixando-o
  natural e humano sem perder o sentido nem inventar informação. / Removes
  AI-writing tells from Brazilian Portuguese text, making it natural and human
  while preserving meaning and never inventing facts. Use sempre que o usuário
  pedir para "humanizar", "tirar cara de IA", "tirar jeitão de ChatGPT", "deixar
  mais natural", "deixar menos robótico", "remover o slop", "reescrever de forma
  humana", "tirar os padrões de IA", "melhorar a escrita", ou colar um texto em
  português que claramente tem padrões de IA (linguagem inflada, listas com
  emoji, jargão vazio, travessão como aparte, "não apenas X, mas também Y") e
  pedir para "arrumar", "editar" ou "melhorar". Use this even without the word
  "humanizar".
---

# Humanizador

Reescreve um texto em português para que soe como uma pessoa escreveu, removendo
os sinais típicos de escrita gerada por IA, sem perder o sentido, sem mudar os
fatos e sem inflar o tamanho.

Princípio: **humanizar é cortar, não enfeitar.** Texto de IA quase sempre tem
gordura: rodeios, ênfases vazias, simetrias forçadas. O trabalho é remover essa
gordura e devolver o ritmo irregular e a economia que a escrita humana tem
naturalmente. O resultado é quase sempre mais curto que o original.

## Regras inegociáveis

- **Preserve o sentido.** Não mude o que o texto afirma. Humanizar é mexer na
  forma, não no conteúdo.
- **Nunca invente.** Não acrescente fatos, números, exemplos ou afirmações que
  não estavam no original.
- **Não infle.** Se a reescrita ficou maior que o original, você provavelmente
  errou. Corte.
- **Respeite o registro.** Se o original é técnico, mantenha técnico. Se é
  casual, mantenha casual. Não rebaixe nem empole.
- **Nada de travessão (—).** O travessão usado como pausa ou aparte é um dos
  sinais mais reconhecíveis de texto de IA. Não use travessão na saída: troque
  por vírgula, ponto, dois-pontos ou parênteses, ou quebre a frase em duas. Vale
  para o travessão longo (—) e o médio (–). Única exceção: diálogo/fala de
  verdade, onde o travessão é a pontuação correta.

## Fluxo

### 1. Detecte os sinais de IA

Leia o texto procurando os padrões que denunciam IA. Os principais estão abaixo;
o catálogo completo, com exemplos de antes/depois, está em
`reference/sinais-de-ia.md`. Consulte quando precisar dos detalhes.

Sinais mais comuns em português:

- **Travessão como aparte ou pausa de efeito:** "a IA — que muda tudo — chegou".
  Um dos tells mais fortes hoje.
- **Linguagem inflada:** "revolucionário", "transformador", "no mundo de hoje",
  "cada vez mais", "de suma importância".
- **Simetria forçada:** "não apenas X, mas também Y", "não se trata de X, e sim
  de Y", regra de três artificial.
- **Ênfase vazia:** "é importante ressaltar que", "vale destacar", "é
  fundamental notar".
- **Jargão corporativo oco:** "alavancar", "potencializar", "sinergia",
  "robusto", "solução".
- **Verbos clichê de IA:** "mergulhar", "navegar (por um cenário)",
  "desbloquear", "elevar", "impulsionar".
- **Ritmo uniforme:** todas as frases com o mesmo tamanho e a mesma cadência.
- **Conclusão vazia:** parágrafo final que começa com "Em resumo" e só repete o
  que já foi dito.
- **Formatação excessiva:** listas com emoji, negrito espalhado, bullet para
  tudo, quando prosa resolveria.

### 2. Reescreva cortando

Aplique, na ordem:

1. **Corte a gordura:** remova ênfases vazias, transições mecânicas ("Além
   disso", "Ademais", "Por outro lado") e adjetivos genéricos empilhados.
2. **Desfaça as simetrias:** troque "não apenas X, mas também Y" por uma frase
   direta. Quebre a regra de três artificial.
3. **Troque o inflado pelo concreto:** "revolucionário" vira o que a coisa de
   fato faz. Palavra grande vira palavra exata.
4. **Tire os travessões:** troque por vírgula, ponto, dois-pontos ou parênteses,
   conforme o caso, ou divida em duas frases.
5. **Varie o ritmo:** misture frases curtas e longas. Uma frase curta depois de
   uma longa cria respiração. Texto humano não é métrico.
6. **Prefira prosa a lista:** se a informação flui como parágrafo, deixe
   parágrafo. Lista só quando a estrutura é de fato uma lista.

### 3. Confira

Antes de entregar, verifique:

- O sentido continua o mesmo? (Compare com o original.)
- Você inventou alguma coisa? (Se sim, remova.)
- Sobrou algum travessão? (Se sim, troque.)
- Ficou mais curto ou igual? (Se ficou maior, corte mais.)
- Você leria isso em voz alta sem tropeçar no artificial?

## Formato de saída

Por padrão, entregue **apenas o texto reescrito**, pronto para usar. Sem
preâmbulo, sem "aqui está a versão humanizada".

Se o usuário pedir para ver o que mudou, acrescente depois do texto uma seção
curta **"O que mudei"** com 3 a 5 pontos objetivos (ex.: "cortei 4 ênfases
vazias", "removi 2 travessões", "transformei a lista de 6 itens em um parágrafo").

## Exemplo

**Input:**
> É importante ressaltar que a inteligência artificial, essa força
> transformadora — que está mudando tudo —, não é apenas uma ferramenta
> revolucionária, mas também um divisor de águas que está mudando radicalmente a
> forma como navegamos pelo cenário corporativo atual. 🚀

**Output:**
> A inteligência artificial está mudando como as empresas trabalham. O potencial
> é grande, mas ainda estamos aprendendo a usá-lo.

(Repare: saíram os dois travessões, a abertura "é importante ressaltar", o par
"não apenas... mas também", o jargão e o emoji. E ficou mais curto.)

Veja mais em `examples/exemplo-antes-depois.md`.
