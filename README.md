# Rule

个人维护的 Loon 分流规则。

安卓 Clash Meta 使用的远程规则集合见 [ClashMeta](./ClashMeta/README.md)。该目录仅包含公共规则，私人节点配置保存在设备本地。

## AI

`AI.lsr` 合并通用 AI 服务与 Apple Intelligence、Siri、Apple Relay 规则，并完成格式统一和去重。

Loon 远程规则：

```text
https://raw.githubusercontent.com/riddikuluswen/Rule/refs/heads/main/AI.lsr, policy=AI, tag=AI, enabled=true
```

规则文件：[`AI.lsr`](./AI.lsr)

上游来源：

- AI 规则历史快照：<https://raw.githubusercontent.com/axtyet/Luminous/refs/heads/main/sooyaabo/Rule/AI.lsr>
- Apple Intelligence：[`Apple-AI.list`](./Apple-AI.list)
- Apple Intelligence 补充：<https://raw.githubusercontent.com/ddgksf2013/Filter/refs/heads/master/AppleIntelligence.list>

原 AI 订阅 `https://loon.103516.xyz/Rule/AI.lsr` 已跳转到 Telegram，本仓库使用其公开镜像快照恢复规则。
