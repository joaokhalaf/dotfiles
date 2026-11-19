---
name: principle-boundary-discipline
description: "Aplique ao ligar validação, tratamento de erros ou adapters de framework. Guardas nas fronteiras do sistema (CLI, config, rede, APIs externas); confie nos tipos internos e mantenha a lógica de negócio em funções puras."
disable-model-invocation: true
---

# Boundary Discipline

Valide, estreite tipos e trate erros onde os dados cruzam uma fronteira do sistema (args de CLI, arquivos de config, APIs externas, rede). Dentro, confie nos tipos: sem revalidação e sem checagens de nulo redundantes. Converta dados brutos em tipos de domínio na fronteira e mantenha tipos de transporte e framework fora da superfície pública. Lógica de negócio vive em funções puras sem dependência de framework. A casca que as chama é fina.

Dois testes. Este dado está cruzando uma fronteira agora? Se não, a validação é redundante. Isto pode ser uma função pura que a casca só chama? Se sim, extraia.
