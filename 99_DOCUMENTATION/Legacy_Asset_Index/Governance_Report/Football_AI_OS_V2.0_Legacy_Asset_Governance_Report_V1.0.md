Football AI OS V2.0 Legacy Asset Governance Report V1.0
文档信息

项目名称：

Football AI OS

版本：

V1.0

文档类型：

Legacy Asset Governance Report

资产来源：

E:\football_v

生成日期：

2026-07-25

1. 报告目的

本报告用于记录 Football AI OS Legacy 系统资产治理结果。

目标：

建立 E:\football_v 当前完整资产认知。
明确现有代码、数据、数据库、模型、Feature资产价值。
判断资产保留、重构、合并、归档方向。
为 Football AI OS V2.0 架构迁移提供依据。
避免未来重复开发和架构失控。
2. Legacy资产治理范围

本次资产治理按照以下维度进行。

2.1 文件资产

分析内容：

Python文件
配置文件
数据文件
数据库文件
模型文件
文档文件

目标：

建立完整文件资产地图。

2.2 功能资产

分析内容：

文件功能
模块职责
系统能力

形成关系：

文件

↓

功能

↓

系统能力

2.3 Class资产

分析内容：

类定义
类职责
核心业务对象
类之间关系

目标：

识别系统核心对象。

2.4 Function资产

分析内容：

函数
方法
核心计算逻辑
执行入口

目标：

掌握系统代码能力。

2.5 调用关系资产

分析内容：

模块调用
函数调用
数据调用
Runtime执行流程

形成：

入口

↓

Runtime

↓

Engine

↓

Model

↓

Output

2.6 数据库资产

分析内容：

数据库文件
数据表
字段结构
数据用途

主要包括：

比赛数据
球队数据
赔率数据
历史数据
2.7 模型资产

核心模型：

Elo Engine

用途：

球队实力动态评分。

Dixon-Coles Engine

用途：

足球低比分概率修正。

Poisson Engine

用途：

进球概率预测。

XGBoost Engine

用途：

机器学习融合预测。

2.8 Feature资产

核心Feature：

Team Form
Match History
Rating
Fatigue
Momentum
Home Away
H2H

目标：

建立统一 Feature Store。

2.9 Runtime资产

分析：

Prediction入口
Decision入口
Engine流程
Pipeline流程
输出流程

目标：

建立完整运行链。

3. 当前Legacy系统架构

当前 E:\football_v 已形成足球AI分析系统基础架构。

Runtime Layer

        |

        |

Prediction / Decision Layer

        |

        |

Model Intelligence Layer


--------------------------------

Elo

Dixon-Coles

Poisson

XGBoost

--------------------------------


        |

        |

Feature Intelligence Layer


--------------------------------

Form

History

Rating

Fatigue

Momentum

--------------------------------


        |

        |

Data Layer


--------------------------------

Match Data

Odds Data

Database

--------------------------------
4. 核心保留资产（Core Assets）
4.1 Data Layer

保留：

matches
fixtures
teams
competitions
seasons
match_stats
odds

原因：

数据层是所有模型、Feature和预测系统共同基础。

处理方式：

保留

统一接口

迁移到 V2 Data Layer

4.2 Feature Layer

保留：

team_form_history
home_away_history
fatigue_history
rating_history
h2h_history

未来统一：

Feature Store

目标：

减少重复计算。

统一历史特征管理。

4.3 Model Layer

核心保留：

Elo Engine
Dixon-Coles Engine
Poisson Engine
XGBoost Engine

迁移目标：

03_MODEL_LAYER
5. 重构资产（Rebuild Assets）
5.1 Prediction系统

当前状态：

Legacy系统中存在多个预测相关入口。

可能包含：

predict
prediction
fusion
engine
runtime

当前问题：

预测入口分散。
模型调用关系不统一。
输出格式不统一。
后续维护成本增加。

未来统一为：

Prediction Engine


        |

        |


Model Fusion


        |

        |


Probability Output


目标：

建立统一预测服务。

负责：

接收比赛输入。
调用模型。
融合概率。
输出预测结果。
5.2 Decision系统

当前状态：

部分决策逻辑分散在预测代码中。

未来建立独立：

Decision Layer

负责：

胜平负判断。
盘口分析。
SP分析。
市场风险判断。
推荐等级。
投注策略输出。

目标：

实现：

模型预测

↓

决策分析

↓

用户输出

6. 合并资产（Merge Assets）
6.1 Rating Service

当前相关资产：

team_rating
elo_rating
strength_rating
rating_history

问题：

多个评分体系可能存在重复。

未来统一：

Rating Service

负责：

球队实力评分。
动态排名。
历史变化。
模型输入。
6.2 History Service

当前历史相关资产：

team_form_history
home_away_history
h2h_history
performance_history

问题：

历史数据分散。

未来统一：

History Service

管理：

最近状态。
主客场表现。
对战历史。
长期趋势。
6.3 Market Intelligence Layer

当前相关资产：

odds
handicap
SP
market movement

未来统一：

Market Intelligence Layer

负责：

市场赔率分析。
盘口变化。
市场情绪。
资金方向。
风险识别。
7. 归档资产（Archive Assets）

以下资产不进入核心运行系统。

统一进入：

99_ARCHIVE

包括：

历史版本
old_versions

用途：

保存旧版本代码。

临时代码
temporary_scripts

用途：

保存测试脚本和一次性工具。

测试文件
test_files

用途：

保存验证过程文件。

部署记录
deployment_history

用途：

保存历史部署过程。

实验模型
experimental_models

用途：

保存未正式上线模型。

8. Football AI OS V2.0目标架构

目标架构：

01_SYSTEM_LAYER


02_DATA_LAYER


03_FEATURE_LAYER


04_MODEL_LAYER


05_PREDICTION_LAYER


06_MARKET_LAYER


07_DECISION_LAYER


08_RUNTIME_LAYER


09_REPORT_LAYER


99_ARCHIVE

9. 架构治理规则

未来新增任何模块之前，必须执行资产检查。

数据检查

确认：

是否已有：

数据表。
数据接口。
数据处理流程。
功能检查

确认：

是否已有：

相同功能。
类似模块。
可扩展组件。
模型检查

确认：

是否已有：

同类型模型。
已训练模型。
可复用算法。
Feature检查

确认：

是否已有：

相同特征。
历史计算结果。
Feature Store资产。
Runtime检查

确认：

是否已有：

执行入口。
Pipeline。
服务接口。
10. 禁止事项（Governance Restrictions）

Football AI OS V2.0 架构治理过程中，禁止以下行为：

10.1 禁止重复创建模型

禁止：

创建重复预测模型。
创建相同算法不同名称版本。
未评估旧模型价值直接废弃。

要求：

新增模型前必须确认：

是否已有类似模型。
是否可以升级已有模型。
是否可以作为已有模型子模块。
10.2 禁止重复创建Feature

禁止：

重复计算已有特征。
创建功能相同Feature表。
多处保存同一种历史指标。

要求：

所有Feature最终进入：

Feature Store

统一管理。

10.3 禁止重复创建数据库

禁止：

创建多个相同用途数据库。
创建重复历史表。
分散保存同类数据。

要求：

数据库必须经过：

数据资产登记

↓

字段确认

↓

用途确认

↓

架构归属确认

10.4 禁止重复创建预测入口

禁止：

多个predict入口。
多个比赛分析入口。
多套输出格式。

要求：

统一：

Prediction Engine

↓

Decision Layer

↓

Report Layer
10.5 禁止未经资产分析直接开发

任何新增模块必须经过：

需求提出

↓

资产检查

↓

功能确认

↓

架构评估

↓

开发批准

↓

代码实现
11. 资产状态分类标准（A/B/C/D）

未来所有资产统一评级。

A级资产（核心资产）

定义：

直接支撑 Football AI OS 核心能力。

包括：

核心数据库。
核心模型。
核心Feature。
核心Engine。
核心Runtime。

处理：

保留。

迁移。

优化。

B级资产（可复用资产）

定义：

具有价值，可以经过调整后继续使用。

包括：

辅助模块。
工具代码。
分析脚本。
部分历史模块。

处理：

评估。

重构。

合并。

C级资产（历史资产）

定义：

有参考价值，但不进入主系统。

包括：

实验代码。
旧版本模型。
测试程序。
临时代码。

处理：

归档。

D级资产（废弃资产）

定义：

无实际价值或重复资产。

包括：

重复代码。
无效测试文件。
空模块。
废弃脚本。

处理：

删除或备份。

12. Migration治理原则

迁移不是简单复制代码。

必须按照：

Legacy Asset

↓

Asset Evaluation

↓

Architecture Mapping

↓

Migration Decision

↓

V2 Implementation
13. Migration判断标准

每个文件、模块、数据库、模型需要判断：

保留（KEEP）

条件：

当前仍有业务价值。
属于核心能力。
可直接迁移。
重构（REBUILD）

条件：

功能有价值。
架构不符合V2要求。
需要重新设计。
合并（MERGE）

条件：

功能重复。
数据重复。
责任边界不清。
删除（REMOVE）

条件：

无使用记录。
无业务价值。
被新模块替代。
14. Football AI OS V2.0迁移目标

最终目标：

将：

E:\football_v

迁移为：

Football AI OS V2.0

形成稳定企业级架构。

15. V2.0目标运行流程

完整流程：

Raw Data


↓

Data Layer


↓

Feature Store


↓

Model Layer


↓

Prediction Engine


↓

Decision Layer


↓

Risk Analysis


↓

Report Layer


↓

User Output
16. 下一阶段任务

进入：

Phase 12
Football AI OS V2.0 Migration Map V1.0

输出内容：

16.1 文件迁移表

包含：

原路径。
文件名称。
功能。
状态。
目标路径。
迁移动作。
16.2 模块迁移表

包含：

当前模块。
当前职责。
V2归属。
是否合并。
是否重构。
16.3 数据迁移表

包含：

数据库。
数据表。
字段。
使用模块。
迁移方案。
16.4 模型迁移表

包含：

模型名称。
算法。
输入Feature。
输出结果。
V2位置。
16.5 删除清单

包含：

重复文件。
废弃代码。
无效数据库。
临时文件。
17. Migration执行顺序

Football AI OS V2.0迁移按照以下顺序执行：

Phase 1：资产冻结

目标：

冻结当前 Legacy 状态。

操作：

保存当前资产清单。
保存数据库状态。
保存模型状态。
保存运行环境。

输出：

Legacy Asset Snapshot。

Phase 2：核心数据迁移

目标：

建立 V2 数据基础。

迁移：

Legacy Database

↓

V2 Data Layer

内容：

比赛数据。
球队数据。
赔率数据。
历史数据。
Phase 3：Feature迁移

目标：

建立统一 Feature Store。

迁移：

History Feature

↓

Feature Store

内容：

Form。
Rating。
Fatigue。
Home Away。
H2H。
Phase 4：模型迁移

目标：

建立统一 Model Layer。

迁移：

Legacy Model

↓

V2 Model Layer

包括：

Elo。
Dixon-Coles。
Poisson。
XGBoost。
Phase 5：Prediction重构

目标：

建立统一预测入口。

结构：

Input

↓

Prediction Engine

↓

Model Fusion

↓

Probability Output
Phase 6：Decision建设

目标：

建立决策系统。

包括：

推荐。
风险。
盘口。
市场判断。
Phase 7：Runtime迁移

目标：

统一执行流程。

包括：

自动运行。
模型调用。
数据更新。
输出生成。
Phase 8：旧系统归档

目标：

保存历史价值。

结构：

99_ARCHIVE

|

|-- old_versions

|-- experiments

|-- old_scripts

|-- deployment_history

18. V2.0目录规划

目标目录：

Football_AI_OS_V2


│

├── 01_SYSTEM_LAYER

│

├── 02_DATA_LAYER

│

├── 03_FEATURE_LAYER

│

├── 04_MODEL_LAYER

│

├── 05_PREDICTION_LAYER

│

├── 06_MARKET_LAYER

│

├── 07_DECISION_LAYER

│

├── 08_RUNTIME_LAYER

│

├── 09_REPORT_LAYER

│

└── 99_ARCHIVE

19. 文档治理体系

Football AI OS 后续维护必须建立以下文档：

19.1 Architecture Document

记录：

系统架构。
Layer职责。
模块关系。
19.2 Asset Registry

记录：

文件。
模块。
数据。
模型。
19.3 Migration Record

记录：

迁移时间。
迁移内容。
迁移结果。
19.4 Model Registry

记录：

模型版本。
训练数据。
参数。
效果。
19.5 Feature Registry

记录：

Feature名称。
计算方式。
使用模型。
更新周期。
20. 长期架构治理原则

Football AI OS 后续开发遵循：

原则1：先治理，后开发

任何新功能：

必须先检查已有资产。

原则2：能力复用优先

优先：

扩展已有模块。

禁止：

重新创建类似模块。

原则3：数据统一管理

所有数据：

进入 Data Layer。

所有Feature：

进入 Feature Store。

原则4：模型独立管理

所有模型：

进入 Model Layer。

每个模型必须有：

输入。
输出。
版本。
评价。
原则5：模块职责单一

每个模块：

必须只有一个主要职责。

避免：

一个文件承担：

数据 + 模型 + 输出。

21. 当前治理结论

经过 Legacy Asset Governance 分析：

Football_v 已经具备：

完整比赛数据基础。
多模型预测体系。
历史Feature体系。
市场分析基础。
预测Runtime基础。

当前主要问题：

模块分散。
部分功能重复。
入口不统一。
数据职责需要整理。
模型和Feature需要服务化。
22. 最终治理方向

Football AI OS V2.0 不进行简单复制迁移。

采用：

Legacy资产

↓

治理分析

↓

架构映射

↓

模块重构

↓

统一部署

↓

企业级Football AI OS
23. 下一阶段输出文件

Phase 12完成后生成：

Football_AI_OS_V2.0_Migration_Map_V1.0.md

内容：

文件级迁移方案。
模块级迁移方案。
数据迁移方案。
模型迁移方案。
删除清单。
执行顺序。