---
tipo: registro-de-decisoes
tags: [produto, decisoes]
---
# Decisões

## D001 — Público inicial
Status: aceito pelo fundador.
Startups B2B de software com venda consultiva, múltiplos stakeholders e CS pequeno ou liderado pelos fundadores. A demanda comercial ainda precisa ser validada.

## D002 — Proposta de valor
Status: aceita pelo fundador.
Preservar contexto da venda, acompanhar resultados e indicar contas que precisam de ação com evidências.

## D003 — Unidade do Kanban
Status: solicitado pelo fundador.
Cada cartão é empresa × módulo. Módulos da mesma empresa podem estar em etapas diferentes. Clicar abre a visão geral da empresa com o módulo selecionado destacado.

## D004 — Etapas
Status: padrão inicial proposto, sujeito à validação.
Captação → Qualificação → Proposta → Negociação → Onboarding → Adoção → Renovação → Expansão.
Situação contratual é independente da etapa. Mover um cartão não assina um contrato. Retornos de etapa são permitidos e registrados no diário.

## D005 — Interface
Status: solicitado pelo fundador.
Aplicação web em localhost, visual inspirado no Notion: tipografia de sistema, espaços em branco, tons neutros, cartões e colunas discretas.
Nome Elo é provisório, escolhido para o protótipo.

## D006 — Saúde e satisfação
Status: aceito.
Adiar fórmula de health score. Cada etapa terá critérios próprios. Registrar sinais qualitativos promotores/detratores sem tratá-los como NPS ou previsão de churn.

## D007 — Atividades e reuniões
Status: solicitado pelo fundador.
Atividades com responsável, prazo e conclusão. Registros de reuniões, decisões e tópicos abertos/resolvidos, vinculados a empresa e módulo. Gestão mais detalhada de tópicos/projetos ficará no backlog.

## D008 — Memória Obsidian
Status: solicitado pelo fundador; implementação inicial definida.
Decisões de produto e pendências em Markdown com frontmatter e wikilinks. Dados operacionais exportados automaticamente para Contas. Sincronização unidirecional do CRM para Markdown; JSON é a fonte de verdade.

## D009 — Escopo técnico
Status: escolha reversível de implementação.
Python padrão + HTML/CSS/JavaScript sem build. Servidor vinculado apenas a 127.0.0.1. Persistência em disco e sem dependências externas. Sem integração de canais ou modelo de IA nesta versão.
