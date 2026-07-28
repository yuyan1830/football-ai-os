# Football AI OS Project Context

## 项目目标

建立 Football AI OS Ω+ 智能足球预测系统。


## 当前架构基线

Football AI OS Betting Intelligence System Ω+ V3.2


## 已存在能力

- Elo模型
- Dixon-Coles模型
- Poisson模型
- XGBoost模型
- Fusion Engine
- Model Registry
- Model Runtime
- Backtest框架
- 数据治理体系


## 当前迁移状态

Legacy Asset 已发现：

03_MODEL_LAYER

包含：

- 真实模型算法
- 数据计算逻辑
- 历史训练代码


当前新架构：

05_MODEL_AI

包含：

- 模型接口
- 注册
- 加载
- 运行框架


状态：

框架迁移完成

算法迁移未完成


## 未完成核心任务

1. Legacy算法迁移到新模型层

2. Feature Store建设

3. Runtime执行链建设

4. Decision Engine建设

5. 市场/风险/价值模型接入


## 唯一推荐运行路径

Data



Feature Store



Model Registry



Model Runtime



Elo/Dixon-Coles/Poisson/XGBoost



Fusion Engine



Backtest



Decision Engine


## AI工作原则

不要创建新模块。

先寻找已有能力。

优先迁移已有资产。

所有重大修改必须更新：

- 架构版本
- 迁移矩阵
- 项目状态文档
