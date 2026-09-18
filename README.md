# Elo

Elo é um protótipo de CRM local para startups B2B de software que precisam preservar o contexto da venda e acompanhar toda a jornada do cliente — da captação à expansão — sem espalhar decisões, compromissos e sinais importantes entre várias ferramentas.

O projeto nasceu da ideia de que uma empresa pode estar em momentos diferentes da jornada para cada módulo contratado. Por isso, a unidade principal do quadro não é apenas a empresa: cada cartão representa uma combinação **empresa × módulo**. Assim, um cliente pode estar em onboarding em um produto e, ao mesmo tempo, negociando outro.

> **Status:** primeira versão funcional para validação local. O nome Elo é provisório e os dados criados no primeiro acesso são demonstrativos.

## O que já foi feito

- Kanban com as etapas de Captação, Qualificação, Proposta, Negociação, Onboarding, Adoção, Renovação e Expansão.
- Cartões independentes por empresa e módulo, movidos por arraste ou por seletor.
- Cadastro e edição de empresas e módulos.
- Página de contexto da empresa com objetivo, responsável e módulos da jornada.
- Cadastro de stakeholders e seus papéis na conta.
- Atividades com responsável, prazo, vínculo a módulo e controle de conclusão.
- Diário para reuniões, decisões, tópicos abertos ou resolvidos e sinais promotores ou detratores.
- Registro automático no diário quando um módulo muda de etapa.
- Busca por empresa ou módulo e filtro por situação comercial.
- Visões consolidadas de empresas, atividades e decisões.
- Persistência local em JSON, com gravação atômica e fila de salvamento no navegador.
- Projeção automática dos dados de cada conta em Markdown para consulta no Obsidian.
- Interface responsiva inspirada na simplicidade visual do Notion.
- Servidor restrito a `127.0.0.1`, sem exposição automática à rede.

## A ideia por trás

Em vendas consultivas, a passagem de contexto entre comercial e Customer Success costuma ser frágil. Objetivos do cliente, pessoas envolvidas, decisões tomadas e próximos passos ficam fragmentados, dificultando a implantação e a demonstração de valor na renovação.

O Elo propõe uma memória compartilhada e operacional do relacionamento:

1. cadastrar a empresa e os módulos relevantes;
2. acompanhar cada módulo na sua etapa real;
3. abrir a conta para recuperar rapidamente o contexto;
4. registrar conversas, decisões, evidências e compromissos;
5. revisar atividades e manter próximos passos claros;
6. consultar a memória das contas também em Markdown.

A primeira validação é voltada a startups B2B com venda consultiva, múltiplos stakeholders e uma operação de CS pequena ou ainda conduzida pelos fundadores. A hipótese central é que reunir contexto e ação em um mesmo workspace melhora a continuidade do relacionamento e reduz o tempo necessário para entender o estado de cada cliente.

O produto evita, nesta fase, transformar sinais qualitativos em métricas artificiais. Pontos promotores e detratores são registrados com evidências, enquanto fórmulas de health score, previsão de churn e automações com IA permanecem fora do protótipo até que existam dados reais e critérios definidos para cada etapa.

## Como executar

Pré-requisito: Python 3. Não é necessário instalar pacotes.

```bash
cd crm
python server.py
```

Depois, acesse [http://localhost:8765](http://localhost:8765).

No primeiro acesso, a aplicação cria dados demonstrativos. As alterações são salvas em `crm/data/state.json`.

## Integração com Obsidian

A pasta `crm/Obsidian` pode ser aberta como um cofre do Obsidian. A cada salvamento, o servidor gera uma nota em `crm/Obsidian/Contas` para cada empresa.

Essa sincronização é unidirecional:

- `crm/data/state.json` é a fonte operacional de verdade;
- as notas de contas são uma projeção para leitura e podem ser sobrescritas;
- anotações manuais devem ser mantidas em outras notas do cofre;
- recomenda-se fazer backup do JSON e do cofre.

## Arquitetura

```text
crm/
├── server.py           # servidor HTTP, API de persistência e exportação Markdown
├── web/
│   ├── index.html      # estrutura da aplicação
│   ├── app.js          # estado, regras e interações da interface
│   ├── style.css       # layout e componentes
│   └── notion.css      # ajustes visuais
└── Obsidian/           # decisões, backlog e memória do produto
```

A implementação usa apenas a biblioteca padrão do Python e HTML, CSS e JavaScript nativos. Não há etapa de build nem dependências externas.

## Limites atuais

- Uso local e individual, sem autenticação ou isolamento entre organizações.
- Sem integrações externas, importação/exportação pela interface ou sincronização bidirecional com o Obsidian.
- Sem edição e exclusão completa de todos os tipos de registro.
- Sem casos formalizados de perda, cancelamento, arquivamento e reabertura.
- Sem health score, pesquisa de satisfação, previsão de churn ou IA em execução.
- Dados demonstrativos ainda não podem ser removidos pela interface com um único comando.
- Não deve ser publicado na internet sem revisão de segurança e uma camada adequada de autenticação.

## Próximos passos

- Validar etapas e critérios de entrada e saída do funil.
- Definir o catálogo de módulos e o tratamento de múltiplas contratações.
- Selecionar startups-piloto e medir tempo de recuperação de contexto e conclusão de atividades.
- Estruturar tópicos de reuniões com responsáveis, status e histórico.
- Definir critérios de saúde específicos por etapa usando dados observáveis.
- Adicionar backup, importação e exportação pela interface.
- Avaliar integrações e extração de compromissos com IA somente a partir de casos reais.

As decisões de produto, pendências e verificações da primeira versão estão documentadas em [`crm/Obsidian`](crm/Obsidian).
