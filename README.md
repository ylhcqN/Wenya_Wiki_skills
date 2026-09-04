# Wenya Wiki Skills

> Ai agent技能包：基于李文亚宇宙 Wiki 镜像的世界观设定、角色扮演与 Wiki 编辑指导。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## 项目简介

本项目是通用 agent 框架的2个技能包，用于：

- **世界观创作**：基于双轨叙事的小说/剧本设定
- **Wiki 编辑**：生成符合文亚宇宙 Wiki 规范的 MediaWiki 页面
---

## 技能模块

| 模块 | 路径 | 用途 | 触发词 |
|------|------|------|--------|
| **liwenya-universe** | `liwenya-universe/` | AI 小说创作世界观技能包（双轨叙事、角色卡、理论体系、时间线） | `李文亚宇宙`、`文亚宇宙世界观`、`世界观设定` |
| **liwenya-wiki-template** | `liwenya-wiki-template/` | 文亚宇宙 Wiki 模板使用指导（5 种信息框 + 编辑规则） | `写 wiki 条目`、`文亚宇宙 Wiki`、`Wiki 模板` |

### liwenya-universe

基于文亚宇宙 Wiki 的完整世界观设定包：

- **双轨叙事机制**：A 轨（文亚内在真实 / 悲壮史诗）vs B 轨（灰色现实 / 黑色幽默）
- **核心角色卡库**：李文亚（主角）、清醒人格（2026 年觉醒）、孙笑川教授 / 114514 研究所（反派阵营）、支持者阵营
- **理论体系**：星球三重引力范围、太阳直径理论、黑体生物理论、文亚四定律、长生之道
- **完整时间线**：现实时间线（B 轨锚点）+ 宇宙虚构时间线（A 轨锚点）
- **场景模板**：8 个典型创作场景（讲课发作、评论区互动、金坤奖颁奖……）

### liwenya-wiki-template

文亚宇宙 Wiki 编辑指导：

- **5 种信息框模板**：Character（人物）、Institutions（机构）、Theory（理论）、Concept（概念）、Event（事件）
- **辅助模板**：维护提示、Stub、引言块、来函块、导航模板
- **页面推荐结构**：人物 / 机构 / 理论 / 事件条目骨架
- **编辑规则与写作规范**：命名规则、分类规则、索引列表、CC-BY-SA 许可
- **AI Agent 工作流程**：类型判断 → 读镜像 → 生成信息框 + 正文 → 检查 → 输出

---

## 安装

### 前置条件

- 已经安装任意agent 框架
- 文亚宇宙 Wiki 镜像（需另行获取，130 篇条目 + 模板，可选）

### 步骤

```bash
# 1. 克隆本仓库
git clone https://github.com/<your-org>/Wenya_Wiki_skills.git

# 2. 将技能目录链接或复制到 agent 技能目录
#    （具体路径取决于 agent 的技能加载配置）
cp -r liwenya-perspective/ <SKILLS_DIR>/
cp -r liwenya-universe/ <SKILLS_DIR>/
cp -r liwenya-wiki-template/ <SKILLS_DIR>/

```

---

## 使用示例

### Wiki 条目生成

激活 `liwenya-wiki-template` 技能后，描述需要创建的条目类型：

> **用户**：帮我写一个孙笑川教授的 wiki 条目
>
> **AI**：先读取 `wiki_dump/articles/孙笑川教授.wiki` 和 Character 模板，生成信息框 + 符合中立语气的正文，输出完整 MediaWiki 页面代码。

### 世界观创作

激活 `liwenya-universe` 技能后，可获得世界观咨询或直接进行创作：

> **用户**：写一段 A 轨风格的文亚讲课场景
>
> **AI**：基于双轨叙事规则，以李文亚第一人称限制全知视角，生成爆裂鼓手发作式讲课场景。

---

## 项目结构

```
Wenya_Wiki_skills/
├── README.md
├── LICENSE                     # MIT License
├── liwenya-universe/
│   └── SKILL.md               # 世界观技能定义（335 行）
└── liwenya-wiki-template/
    └── SKILL.md               # Wiki 模板技能定义（380 行）
```

---

## 数据来源

| 类型 | 内容 | 规模 |
|------|------|------|
| 一手语料 | 李文亚教授主题分类语料库（T01-T09） | 1218 篇 |
| 一手语料 | 李文亚全集 srt 字幕（图片转文本 OCR） | 1170 集 |
| 二手来源 | 社会对李文亚评价（B 站视频字幕） | 3 个视频 |
| Wiki 镜像 | `lwy_wiki/wiki_dump/`（articles + templates + categories） | 130 篇条目 |

---

## 写作规范

创作时遵循以下原则：

1. **双轨分离**：单章节单轨道，严禁单章混轨
2. **尊重李文亚本人**：严禁骚扰、辱骂、诽谤；创作属于戏仿叙事
3. **中立语气**：Wiki 条目采用百科式中立叙述外壳
4. **图片 AI 生成**：推荐 GPT-Image2 等，不得使用真人照片
5. **CC-BY-SA 许可**：Wiki 内容遵循 CC-BY-SA 协议
6. **避开敏感内容**：政治敏感、社会议题、涉黄涉恐等

---

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v2.1.0 | 2026-08 | 同步 2026-08 快照：新增二向箔的投放者、张雪峰教授、枪毙概念专条、诺奖与民科研究交流协会内乱事件、江南大学等 |
| v2.0.0 | — | 依据 wiki 镜像全面对齐设定；新增清醒人格、文亚四定律、太阳直径 42 亿千米、泰姆瑞尔帝国等 |
| v1.0.0 | — | 初始版本：完整世界观、角色卡、理论体系、时间线、双轨叙事引擎、写作模板 |

---

## 许可证

本项目采用 [MIT License](LICENSE) 许可证。
---

## 致谢

- 李文亚本人的公开视频与语料，为本项目提供了基础素材
- 文亚宇宙 Wiki 社区的条目贡献者
