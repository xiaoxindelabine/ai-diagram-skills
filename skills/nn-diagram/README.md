# `nn-diagram` Skill / 神经网络与 AI 架构图 Skill

`nn-diagram` turns neural-network, AI-system, agent, RAG, multimodal, and experiment-pipeline descriptions into editable diagram source.

`nn-diagram` 可以把神经网络、AI 系统、Agent、RAG、多模态模型和实验流程描述转换成可编辑图源码。

## Use it for / 适用场景

- Model architecture diagrams: MLP, CNN, ResNet, U-Net, Transformer, GNN, ConvLSTM, multimodal models.
- AI system diagrams: RAG pipelines, agent loops, tool-use workflows, training/evaluation pipelines.
- Comparison diagrams: model families, baselines, ablations, fusion strategies, retrieval strategies.
- Module-detail diagrams: residual blocks, ConvLSTM gates, attention, routers, adapters, fusion modules.
- Optional case-library diagrams: OutputFusion, FiLM, DualStreamV2, STGCN, DCRNN, Graph WaveNet.

## Default output / 默认输出

- Mermaid for most requests.
- Graphviz DOT for large or cluster-heavy graphs.
- SVG only when explicitly requested.

## Install / 安装

Copy this folder into your Claude skills directory:

```text
skills/nn-diagram/
```

Then invoke it by name in Claude Code or any compatible Claude skill environment:

```text
使用 nn-diagram 画一个 Transformer encoder 架构图。
```

## Example requests / 示例请求

```text
使用 nn-diagram 画一个 U-Net segmentation architecture，用 Mermaid。
```

```text
Use nn-diagram to compare a RAG pipeline and a tool-using agent workflow.
```

```text
使用 nn-diagram 画 ConvLSTM cell 的门控结构。
```

```text
Use nn-diagram to generate an editable SVG for a multimodal fusion model.
```

```text
使用 nn-diagram 画 OutputFusionPredictor 架构图。
```

## Files / 文件说明

- `SKILL.md` — skill router, behavior, input/output contract.
- `templates.md` — generic AI and neural-network templates.
- `case-library.md` — optional case studies and project-derived examples.
- `output-formats.md` — Mermaid, DOT, and SVG emission rules.
- `examples.md` — response examples and coverage cases.

## Extending / 扩展

Add new reusable model families to `templates.md`. Add project-specific or paper-specific examples to `case-library.md` so they remain opt-in rather than default assumptions.

建议把通用模型族放进 `templates.md`，把论文或项目专属结构放进 `case-library.md`，避免影响普通用户的默认输出。
