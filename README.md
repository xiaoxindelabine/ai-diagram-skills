# ai-diagram-skills

Bilingual Claude skills for generating precise, editable AI architecture diagrams.

用于生成精准、可编辑 AI 架构图的中英双语 Claude Skills 集合。

## Included skills / 当前包含

### `nn-diagram`

Generate AI system and neural-network diagrams as Mermaid, Graphviz DOT, or SVG.

将神经网络、AI 系统、Agent、RAG、多模态模型和实验流程转换为 Mermaid、Graphviz DOT 或 SVG 图源码。

Use it for:

- Neural-network architectures: MLP, CNN, ResNet, U-Net, Transformer, GNN, ConvLSTM.
- AI workflows: RAG, agent loops, tool-use systems, training/evaluation pipelines.
- Comparisons: baselines, ablations, fusion mechanisms, retrieval strategies.
- Module details: attention, gates, residual blocks, routers, adapters, fusion blocks.
- Optional case-library examples: OutputFusion, FiLM, DualStreamV2, STGCN, DCRNN, Graph WaveNet.

## Quick start / 快速开始

Copy the skill folder into your Claude skills directory:

```text
skills/nn-diagram/
```

Then invoke it by name:

```text
使用 nn-diagram 画一个 Transformer encoder 架构图，用 Mermaid。
```

```text
Use nn-diagram to draw a RAG pipeline with retriever, reranker, context builder, and LLM.
```

## Repository layout / 仓库结构

```text
.
├── skills/
│   └── nn-diagram/
│       ├── SKILL.md
│       ├── templates.md
│       ├── case-library.md
│       ├── output-formats.md
│       ├── examples.md
│       └── README.md
├── scripts/
│   └── validate.py
├── README.md
├── LICENSE
└── CHANGELOG.md
```

## Design principles / 设计原则

- Editable source first: Mermaid by default, DOT for clustered graphs, SVG when explicitly requested.
- Structural fidelity: preserve streams, layers, tensor flow, fusion points, skip paths, state loops, retrieval/tool boundaries, and output heads.
- Generic core, optional cases: reusable templates stay in `templates.md`; project or paper-specific material stays in `case-library.md`.
- Minimal assumptions: do not invent layers, metrics, datasets, tools, or performance claims.

## Development / 开发

Run the lightweight validation script:

```bash
python scripts/validate.py
```

The script checks skill frontmatter, referenced local Markdown files, removed legacy references, and obvious absolute-path leakage.

## Extending / 扩展

- Add reusable model/system families to `skills/nn-diagram/templates.md`.
- Add paper-specific or project-specific diagrams to `skills/nn-diagram/case-library.md`.
- Add response examples to `skills/nn-diagram/examples.md`.
- Keep new cases opt-in; they should not change generic default behavior.

## License / 许可证

MIT License. See `LICENSE`.
