# Generic AI and Neural-Network Templates

Use these templates when the user asks for a common AI architecture, neural-network family, agent workflow, or custom system without case-library terminology.

## Common conventions

- Inputs: name data type and shape if known.
- Feature blocks: operation + role.
- Repeated blocks: use `×N` unless full expansion is requested.
- Skip/residual paths: show bypass arrows explicitly.
- Fusion: label the exact mechanism.
- State, memory, retrieval, and tool-use loops: show them as explicit side paths or feedback edges.
- Outputs: distinguish logits, probabilities, maps, masks, embeddings, class scores, generated text, actions, or API calls.

## MLP

Canonical flow:

```text
Input vector → Dense/Linear → Activation/Norm/Dropout → repeated hidden blocks → Output head
```

Use for tabular features, compact encoders, projection heads, gating MLPs, adapters, and small decision heads. If the user specifies dimensions, label nodes like `Linear d_in→128`.

## CNN

Canonical flow:

```text
Image/Grid input → Conv block ×N → Downsample/Pooling → Feature map → Head → Output
```

Use separate blocks for:
- convolution stack
- normalization/activation
- pooling or stride downsampling
- classifier/regression/segmentation head

## ResNet

Canonical block:

```text
Input → Conv/BN/ReLU → Conv/BN → Add with identity/projection skip → ReLU → Output
```

Full-network flow:

```text
Input → Stem → Residual Stage 1 → Residual Stage 2 → Residual Stage 3 → Global Pool → Head
```

Always show the skip/residual add node when drawing block detail.

## U-Net

Canonical flow:

```text
Input → Encoder Level 1 → Encoder Level 2 → Bottleneck → Decoder Level 2 → Decoder Level 1 → Output mask/map
```

Rules:
- Show encoder and decoder as separate subgraphs when possible.
- Show skip connections from matching encoder levels to decoder levels.
- Label downsample and upsample transitions.

## Transformer

Canonical encoder flow:

```text
Tokens/Patches → Embedding → Positional Encoding → Transformer Encoder Block ×N → Pool/Readout → Head
```

Transformer encoder block detail:

```text
Input → Multi-Head Self-Attention → Add & Norm → Feed-Forward Network → Add & Norm → Output
```

Rules:
- Show positional encoding as an additive or side input.
- If temporal and spatial encoding are both present, show both explicitly.
- For patch-based spatial models, label patch size or token count if known.
- For decoder-only LLMs, show tokenization, embedding, causal self-attention blocks, KV cache when relevant, and next-token head.

## GNN

Canonical flow:

```text
Graph nodes/features + adjacency → Graph convolution/message passing ×N → Temporal/recurrent block if any → Readout/Upsample → Output
```

Rules:
- Separate graph construction from graph processing.
- Show adjacency, edge features, or learned graph structure as side inputs.
- For spatiotemporal GNNs, keep spatial and temporal processing distinct.

## ConvLSTM

Canonical flow:

```text
Temporal grid sequence → ConvLSTM Cell/Stack → Hidden state sequence → Prediction head → Risk/probability map
```

ConvLSTM cell detail:

```text
X_t + H_{t-1} → Convolutional gates → i_t, f_t, o_t, candidate → C_t/H_t update
```

Rules:
- Show recurrent state flow when drawing cell detail.
- For stacked ConvLSTM, use `Stacked ConvLSTM ×L`.
- If context modulates hidden states, label it as hidden-layer modulation, not output fusion.

## Attention fusion

Use when combining one stream as Query with another stream or context as Key/Value:

```text
Query features + Context Key/Value → Cross-Attention → Attended features → Fusion/Head
```

Rules:
- Label Query and Key/Value roles.
- Show whether output is concatenated, multiplied, added, or gated.

## Multi-stream fusion

Use subgraphs or clusters for each stream:

```text
Stream A → representation A
Stream B → representation B
Stream C → representation C
representations → fusion mechanism → output
```

Fusion node names should be precise:
- `Concat + MLP`
- `Residual Add`
- `FiLM Modulation`
- `Cross-Attention Fusion`
- `Softmax-Gated Weighted Sum`
- `Router / Mixture-of-Experts Gate`
- `Late Ensemble Average`

## RAG system

Canonical flow:

```text
User query → query rewrite/embedding → retriever → ranked documents → context builder → LLM → answer + citations
```

Rules:
- Separate offline indexing from online retrieval when both are relevant.
- Show vector store, keyword index, reranker, and context window as distinct nodes if mentioned.
- Do not imply citations, tools, or grounding checks unless the user provided them.

## Agent workflow

Canonical flow:

```text
User goal → planner/controller → tool selection → tool call/API → observation → memory/state update → final response/action
```

Rules:
- Show loops explicitly: plan → act → observe → revise.
- Distinguish model reasoning/state from external systems.
- Label human approval gates, sandbox boundaries, or policy checks when supplied.

## Training and evaluation pipeline

Canonical flow:

```text
Raw data → preprocessing → split → model training → validation/tuning → test evaluation → reporting/deployment artifact
```

Rules:
- Use top-down layout for staged workflows.
- Keep metrics/evaluation nodes factual; do not invent metric values.
- Show feedback from validation/tuning back into training only when iterative tuning is requested.

## Multimodal architecture

Canonical flow:

```text
Modality A encoder + Modality B encoder + optional text/metadata encoder → alignment/fusion → shared representation → task heads
```

Rules:
- Keep each modality in its own stream until the stated fusion point.
- Label alignment mechanisms: contrastive loss, cross-attention, concat, gated fusion, late fusion.
- If training and inference differ, show them as separate branches or phases.
