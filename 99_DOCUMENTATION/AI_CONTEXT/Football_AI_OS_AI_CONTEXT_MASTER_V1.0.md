# Football AI OS Ω+ V3.2

# AI Context Master

Version: V1.0



## 项目身份


项目：

Football AI OS Betting Intelligence System Ω+


路径：

E:\football_v


架构基准：

Football AI OS Betting Intelligence System Ω+ V3.2



最高优先级文件：

1. CLAUDE.md

2. Football_AI_OS_Betting_Intelligence_System_Omega_V3.2_Baseline.md

3. Football_AI_OS_Legacy_Asset_Index_V1.0



---

# 当前系统状态


## Legacy Asset


位置：

03_MODEL_LAYER


已有：

- Elo Engine

- Dixon-Coles Engine

- Poisson Engine

- XGBoost Engine



这些属于有效历史资产。



---

# Current Architecture


位置：

05_MODEL_AI



已有：

- ModelRegistry

- ModelLoader

- ModelRuntime

- ModelInterface



模型：

- EloModel

- DixonColesModel

- PoissonModel

- XGBoostModel



当前状态：

框架完成。

算法迁移未完成。



---

# Legacy  Ω+ V3.2


|能力|旧资产|当前架构|状态|
|-|-|-|-|
|Elo|elo_engine|elo_model|待迁移|
|Dixon-Coles|dixon_coles|dixon_coles_model|待迁移|
|Poisson|poisson_engine|poisson_model|待迁移|
|XGBoost|xgboost_engine|xgboost_model|待迁移|
|Model Registry|旧Model Pool|Model Registry|框架完成|
|Fusion|fusion_engine|fusion_engine|部分完成|
|Backtest|旧回测|Backtest Engine|部分完成|



---

# 当前问题


1.

Legacy 与 Current 双体系存在。


目标：

Legacy Asset



Ω+ Architecture



2.

模型接口存在。

真实算法需要迁移。



3.

Feature Store 尚未完成。



---

# 开发路线


## Phase 1

Legacy Algorithm Migration


迁移：

- Elo

- Dixon-Coles

- Poisson

- XGBoost



## Phase 2

Feature Store


建立：

统一特征入口。



## Phase 3

Model Engine


形成：

Feature



Models



Fusion



## Phase 4

Decision Engine


实现：

- 胜平负

- 盘口分析

- 风险评分

- 价值判断



## Phase 5

Self Learning


实现：

预测



结果



误差分析



模型优化



---

# AI 行为规范


每次打开项目：

必须读取：

1. CLAUDE.md

2. AI Context Master

3. Omega Baseline

4. Legacy Asset Index



重大修改：

必须升级版本。

必须更新文档。



禁止：

- 创建重复模块

- 删除旧资产

- 根据文件名判断重复

- 改变冻结架构



判断依据：

类

函数

调用关系

数据流

测试



---

# 最终目标


建设：

Football AI OS Ω+ V3.2


成为：

Football Intelligence Operating System



能力：

数据智能

特征工程

多模型预测

市场分析

风险控制

决策推荐

自动学习



END

