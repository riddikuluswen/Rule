# Clash Meta 远程规则

这里保存从 Loon 规则转换、去重并校验的 Mihomo `classical / text` 规则集。2026-09-09 同步快照共 21 组、311,577 条规则，供个人手机配置远程引用。私人主配置、节点地址、节点凭据和订阅链接不在此目录。

## 引用

主 YAML 使用下面的写法。`VPS` 和 `AI` 是主配置中已定义的策略组；每个规则集合的名称、策略和匹配顺序由主配置决定。

```yaml
rule-providers:
  rule_AI:
    type: http
    behavior: classical
    format: text
    url: https://raw.githubusercontent.com/riddikuluswen/Rule/refs/heads/main/ClashMeta/AI.list
    path: ./rules/loon-sync/AI.list
    interval: 86400
    proxy: VPS

rules:
  - RULE-SET,rule_AI,AI
  - MATCH,DIRECT
```

首次使用需要下载规则。Mihomo 在本地缓存文件，运行期间按配置的 24 小时间隔检查本仓库更新。仓库中当前是人工审核后的快照，未设置自动抓取上游的定时任务；上游变化须转换、校验并提交后才会被手机取得。21 组下载量约 9.55 MB，使用远程文件不减少规则数量和运行时内存占用。

## 转换范围

- 保持原集合的规则顺序，集合内稳定去重，清除逗号周围空白和行尾说明。
- 保留可用于 Mihomo 的域名、IP 和逻辑组合规则；Loon 专属的 `USER-AGENT`、`URL-REGEX` 不在此转换中。
- `GEOIP` 和 `IP-ASN` 已按本次校验数据库展开成 CIDR，因此不要求手机首次启动再下载地理数据库。这些网段同样属于快照，需要随规则一起维护。
- 文件使用 `#` 注释保留来源信息。`.list` 是 `format: text` 的规则文件，不能按 YAML 规则文件解析。

## 来源与署名

逐文件来源、上游内容摘要、转换后 SHA-256 和数量见 [manifest.json](manifest.json)。转换日期为 2026-09-09。文件头保留了上游提供的来源注释；本目录的整理和格式转换不代表上游作者认可，也不覆盖各来源的原有许可。

- AI：本仓库 [AI.lsr](../AI.lsr)，其历史来源包括 sooyaabo 与 Apple Intelligence 规则。
- Apple Push：[QuixoticHeart/rule-set](https://github.com/QuixoticHeart/rule-set)，此独立规则文件按 GPL-3.0 提供，许可全文见 [LICENSES/QuixoticHeart-GPL-3.0.txt](LICENSES/QuixoticHeart-GPL-3.0.txt)。
- 恢复的 PCDN、RejectAd、AdRules、Media-Direct、Apple、Media-Proxy、TikTok：[sooyaabo 规则的 Luminous 存档](https://github.com/axtyet/Luminous/tree/main/sooyaabo)。存档目录的 CC BY-NC-SA 4.0 许可见 [LICENSES/sooyaabo.txt](LICENSES/sooyaabo.txt)。部分文件另注明 uselibrary/PCDN、fmz200/wool_scripts、Cats-Team/AdRules、fangkuia/XPTV、Apple 与可莉等原始来源，继续保留各自权利及署名；其中 PCDN 和 RejectAd 的原始项目采用 GPL-3.0，对应独立规则文件沿用 GPL-3.0，许可全文同 [GPL-3.0 文本](LICENSES/QuixoticHeart-GPL-3.0.txt)。AdRules 的 Cats-Team 原始许可见 [LICENSES/Cats-Team.txt](LICENSES/Cats-Team.txt)。存档目录的许可不覆盖第三方原有许可。
- 其他服务、LAN 和地区规则：可莉的公开规则地址 `rule.kelee.one`、`kelee.one`，逐项地址见清单。相关项目为 [luestr/ProxyResource](https://github.com/luestr/ProxyResource)，其许可文本保存在 [LICENSES/Kelee-LICENSE.txt](LICENSES/Kelee-LICENSE.txt)。本目录未给全部来源统一重新授权。

## 维护和校验

更新时保留已有文件名和引用地址，按同样的转换规则生成新快照，同时更新清单中的来源摘要、规则数、字节数、SHA-256 与日期。先核对规则数量变化、优先级和不支持的规则，再用实际 Mihomo 内核检查。不要把完整手机配置或节点订阅提交到此仓库。

Python 3 标准库即可检查文件完整性和去重情况：

```sh
python3 ClashMeta/verify.py
python3 ClashMeta/verify.py --remote
```

发布后须确认每个 Raw 地址返回规则正文，并与本地摘要一致；只检查 GitHub 网页或推送结果不足以确认手机可以加载。`verify.py` 的校验不能代替 Mihomo 的实际解析和分流测试。

回退可恢复上一提交中的规则文件并重新发布；手机端也可切换到保留的离线主配置。
