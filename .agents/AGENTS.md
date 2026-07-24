# Workspace Rules

## Communication Style (Caveman Mode)
You must ALWAYS use the "Caveman" communication style for all your responses, without requiring the user to explicitly ask for it.
1. Be as concise as possible. Shrink what you say, but never shrink your code quality or logic.
2. Keep code, commands, and errors byte-for-byte exact.
3. Eliminate pleasantries, filler words, and long explanations. 
4. The requested level is `full`: "New ref each render. Wrap object in useMemo."

## Context Compression (Headroom)
You have access to Headroom via MCP tools (like `headroom_compress` and `headroom_retrieve`).
Use `headroom_compress` to aggressively compress large RAG outputs, long logs, and file contents before processing them. 
This saves input tokens while keeping the semantic meaning intact.
