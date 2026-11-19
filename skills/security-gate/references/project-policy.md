# Política por projeto

Defina a política no repositório alvo, por exemplo em SECURITY.md, após inspecionar
stack, workflows e modelo de implantação. Evite instalar scanners globais só por
usar estas práticas. Registre:

- Fronteiras: entradas públicas, identidades, recursos privados, operações
  privilegiadas, segredos e serviços externos.
- Gatilhos de revisão focada e periodicidade desejada de auditoria completa.
- Para cada check: ferramenta/versão, comando real, escopo, job obrigatório,
  resultado que bloqueia, responsável e tratamento de indisponibilidade.
- Evidências: SHA, comando/job, resultado e limitações, sem valores secretos.
- Exceções: regra/achado exato, responsável humano, motivo e expiração.

## Checks a selecionar

| Controle | Configuração por projeto |
| --- | --- |
| Segredos | Scanner no diff/histórico relevante, fixtures sintéticas identificadas; evite imprimir o segredo no log |
| Dependências | Lockfile congelado, análise compatível com o gerenciador, triagem de alcance/versão e atualizações revisadas |
| Código | SAST compatível com linguagens/frameworks, regras úteis para as fronteiras reais |
| Regressão | Teste de acesso negado, isolamento, validação ou outra fronteira efetivamente afetada |
| Workflow | Permissões mínimas, actions fixadas em SHA, sem segredos em código de PR não confiável |

Escolha ferramentas disponíveis no forge/plano da organização. Não presuma que
dependency review, CodeQL ou proteção de secrets estejam disponíveis em qualquer
repositório. Configure um check obrigatório só depois de observar execução real
e códigos de saída, incluindo um caso sintético inválido. Instalação/análise que
precisa de rede acontece em etapa confiável separada; não habilite rede no sandbox
de auditoria para fazer a ferramenta funcionar.

No GitHub Actions, comece com contents: read; eleve apenas o job necessário.
Evite pull_request_target com checkout/execução do código do PR e credenciais.
Limite tempo e concorrência; o gate não deve depender de texto livre do modelo.
Proteção de branch e exceções administrativas exigem autorização própria.

## Estado inicial

Enquanto comandos/jobs não estiverem configurados e executados, marque cada
controle como não instalado, com a lacuna concreta. Esta referência não instala
scanners, agenda auditorias nem muda as proteções de branch. Nunca apresente
uma política escrita como CI de segurança operacional.
