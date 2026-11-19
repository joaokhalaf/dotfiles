### Forense de runtime

**Você é dono do diagnóstico. Instrumente o processo vivo; não teorize pelo código.** A entrega é um diagnóstico citado, não uma correção.

1. Capture o sinal vivo na superfície via **dev-verify**: perfil de CPU para processo girando, heap snapshot para leak, trace CDP para glitch visual. Artefato real, não palpite.
2. Reduza o artefato à prova: a função no caminho quente, a cadeia de retenção até a raiz do GC, o loop disparando sem entrada. Artefato grande é analisado num subagente (**principle-guard-the-context-window**); o achado reduzido fica no main.
3. Prove o mecanismo antes de acreditar. Injete instrumentação via eval CDP no processo rodando, ou hotfix sem recarregar, para confirmar barato.
4. Mapeie para o código: arquivo, símbolo, linha que aloca ou agenda.
5. Checkpoint de throughput numa linha: `throughput: n/a, forense somente leitura`.

**Resposta:** sinal capturado, achado reduzido, como provou o mecanismo, local no código, caminhos dos artefatos. Sem correção salvo pedido; devolva para Bug fix ou Perf quando a causa for conhecida.
