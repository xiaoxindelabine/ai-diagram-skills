# Case Library: OutputFusion and Spatiotemporal Risk Models

This optional case library contains diagram-ready examples from a spatiotemporal risk-modeling project. Use it only when the user explicitly asks for a bundled case study or names one of the architectures below.

These examples are provided as reusable architecture patterns, not as default assumptions for unrelated projects.

## Case vocabulary

Model names and aliases:

- `OutputFusion`, `OutputFusionPredictor`, `OutputFusion (+W+R)`
- `ConvLSTMFusionPredictor`, `ConvLSTM baseline`, `FiLM hidden-layer fusion`
- `SpatioTemporalTransformer`, `TransformerPredictor`, `STAEformer-style Transformer`, `Transformer+W+R`
- `DualStreamV2`, `StructuredContextEncoderModel`, `CrossAttentionFusion`
- `STGCN`, `STGCNPredictor`
- `DCRNN`, `DCRNNPredictor`
- `GWNet`, `GWNetPredictor`, `Graph WaveNet`
- `CNNGridPredictor`, `LSTMGridPredictor`, `BiLSTMGridPredictor`, `KNN`, `Persistence`

Key phrases to preserve when this case is explicitly requested:

- `output-layer fusion`
- `Softmax gating`
- `weighted output fusion`
- `energy-conserving normalization`
- `hidden-layer fusion`
- `FiLM modulation`
- `cross-attention fusion`
- `structured semantic context`
- `extremely sparse accident prediction`
- `cross-jurisdiction validation`

## OutputFusionPredictor flagship template

Use this as the default template only for OutputFusion architecture requests.

### Concept

OutputFusion decouples spatiotemporal accident modeling from weather/road feature correction. ConvLSTM learns the historical accident pattern. Weather and road encoders produce independent correction logits. The three output maps are fused at the output layer through softmax-gated weighted sum.

### Mermaid skeleton

```mermaid
flowchart LR
  subgraph S1[Base Spatiotemporal Stream]
    A[Historical Accident Sequence<br/>T×1×H×W] --> N[Energy-Conserving<br/>Normalization]
    N --> C[Stacked ConvLSTM ×2]
    C --> B[Base Logits / Risk Map]
  end

  subgraph S2[Weather Correction Stream]
    W[Weather Sequence<br/>T×4] --> WA[Temporal Aggregation<br/>mean + last]
    WA --> WF[8D Weather Feature]
    WF --> WM[Weather MLP]
    WM --> WL[Weather Correction Logits]
  end

  subgraph S3[Road Correction Stream]
    R[Road Feature Map<br/>C×H×W] --> RC[Conv 3×3 + ReLU]
    RC --> RC2[Conv 3×3]
    RC2 --> RL[Road Correction Logits]
  end

  B --> G[Softmax Gating<br/>3×H×W]
  WL --> G
  RL --> G
  G --> F[Weighted Output Fusion]
  F --> Y[Final Accident Risk<br/>Probability Map H×W]
```

### Required fidelity checks

- Must show exactly three streams unless the user requests an ablation.
- Must show fusion at the output/logits level, not inside ConvLSTM hidden states.
- Must label the fusion as `Softmax Gating` or `Softmax-Gated Weighted Sum`.
- Weather stream should include aggregation into mean + last-step features when medium/high detail.
- Road stream should be a 2-layer convolution encoder when medium/high detail.

## OutputFusion vs FiLM comparison

Use for ablation or “fusion position” diagrams.

Essential contrast:

- FiLM: external features generate `γ, β`; hidden state is modulated as `H' = γ ⊙ H + β`; this is hidden-layer fusion.
- OutputFusion: external features produce output correction logits; three logits streams are fused by softmax gating; this is output-layer fusion.

Suggested visual structure:

```text
Left cluster: FiLM hidden-layer fusion
Right cluster: OutputFusion output-layer fusion
Center/bottom annotation: fusion position determines whether external features disturb spatiotemporal hidden states
```

## ConvLSTMFusionPredictor template

Use for ConvLSTM baseline or FiLM weather modulation requests.

```mermaid
flowchart LR
  X[Historical Accident Sequence] --> CL[Stacked ConvLSTM ×2]
  W[Weather / Context Features] --> MLP[FiLM MLP]
  MLP --> GB[gamma, beta]
  GB --> FM[Hidden-State FiLM<br/>H' = gamma ⊙ H + beta]
  CL --> FM
  FM --> Head[Prediction Head]
  Head --> Y[Risk Probability Map]
```

For pure ConvLSTM baseline, omit weather/FiLM branch:

```text
Historical sequence → Stacked ConvLSTM ×2 → Prediction head → Risk map
```

## SpatioTemporalTransformer template

Use for STAEformer-style baseline or Transformer comparison requests.

```mermaid
flowchart LR
  X[Grid Sequence] --> P[Patch Embedding]
  P --> SPE[2D Spatial Positional Encoding]
  P --> TPE[Temporal Positional Encoding]
  SPE --> ENC[Transformer Encoder Blocks ×2]
  TPE --> ENC
  ENC --> TA[Temporal Attention]
  TA --> Head[MLP / Patch Prediction Head]
  Head --> Y[Risk Map]
```

Important notes:
- Include patching when the request concerns large-grid sparse accident prediction.
- If comparing with ConvLSTM, label patching as a possible spatial-resolution bottleneck only if the user asks for explanatory notes.

## DualStreamV2 template

Use for structured context / cross-attention requests.

```mermaid
flowchart LR
  subgraph S1[Spatiotemporal Stream]
    X[Historical Accident Sequence] --> CL[ConvLSTM Backbone]
    CL --> H[Spatial Feature Map H]
  end

  subgraph S2[Structured Semantic Context]
    T[Time Features] --> TE[Time Encoder]
    W[Weather Sequence] --> WE[Weather Context Encoder]
    A[Accident History Stats] --> AE[Accident History Encoder]
    TE --> C[Concat Context Vector]
    WE --> C
    AE --> C
  end

  H --> Q[Query: Spatial Features]
  C --> KV[Key/Value: Context]
  Q --> CA[Cross-Attention Fusion]
  KV --> CA
  CA --> Head[Prediction Head]
  Head --> Y[Risk Map]
```

Required fidelity:
- Show structured context encoders separately.
- Show cross-attention as feature-space fusion, not output-layer softmax gating.

## GNN baseline templates

### STGCN

```text
Grid/node features + adjacency → Chebyshev Graph Conv → Temporal Conv → STConv Block ×N → Readout/Upsample → Risk map
```

### DCRNN

```text
Node features + diffusion adjacency → Diffusion Convolution → DCGRU recurrent update → Node predictions → Grid risk map
```

### Graph WaveNet / GWNet

```text
Node features + adaptive adjacency → Dilated Causal Conv → Graph Convolution → GWNet Block ×N → Prediction head
```

### Generic graph pipeline pattern

```text
Grid accident maps → grid_to_node_features / aggregate_grid → GNN blocks → node_to_grid / upsample_grid → risk map
```

## Experiment pipeline template

Use only when the user asks for this case-study workflow or supplies matching stage names.

Compact stage flow:

```mermaid
flowchart TD
  D[Data Bundle] --> S1[Stage 1<br/>Exploratory baselines]
  S1 --> S2[Stage 2<br/>Full experiment system]
  S2 --> S3[Stage 3<br/>Capacity / multi-step checks]
  S3 --> S4[Stage 4<br/>OutputFusion finalized]
  S4 --> S5[Stage 5<br/>Main 5-model experiments]
  S5 --> S6[Stage 6<br/>Resolution + multi-step]
  S6 --> S7[Stage 7<br/>10-seed stability + extreme weather]
  S7 --> S8[Stage 8<br/>Ablation + 5-fold CV]
  S8 --> S9[Stage 9<br/>Statistics + gamma robustness]
  S9 --> S10[Stage 10<br/>GNN baselines + ensemble]
  S10 --> S11[Stage 11<br/>Cross-jurisdiction validation]
  S11 --> T[Transformer comparison]
```

## Data cleaning pipeline template

```text
Raw accident records → timestamp parsing / invalid removal → numeric coercion → coordinate validation + projection → spatial clipping → deduplication → grid/time-window construction → train/val/test split
```

## Cross-jurisdiction validation template

```text
Yinzhou training/evaluation → OutputFusion learned mechanism → Jiangbei independent dataset → 10-seed paired comparison → AUPRC/F1 statistical tests → cross-jurisdiction conclusion
```
