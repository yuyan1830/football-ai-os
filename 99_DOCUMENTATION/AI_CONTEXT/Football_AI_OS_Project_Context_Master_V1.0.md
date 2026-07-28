# Football AI OS Project Context Master V1.0


## 项目身份

项目：
Football AI OS


最终目标：

Football AI OS Betting Intelligence System Ω+ V3.2


本文件用途：

任何 AI 接手项目时，
必须首先阅读。

目的：

快速理解：

- 项目目标
- 当前状态
- 已有能力
- 未完成能力
- 下一阶段方向


==================================================

## 核心治理文件

最高优先级：

1. CLAUDE.md

2. Football_AI_OS_Betting_Intelligence_System_Omega_V3.2_Baseline.md

3. Football_AI_OS_Legacy_Asset_Index_V1.0


任何代码修改前必须检查。


==================================================

## 当前阶段

当前阶段：

Legacy Asset  Ω+ V3.2 Architecture 迁移阶段。


不是：

重新设计系统。


目标：

把已有旧能力迁移进入统一架构。


==================================================

## 已存在能力


### 模型框架

位置：

05_MODEL_AI


已有：

- ModelRegistry
- ModelLoader
- ModelRuntime
- ModelInterface


### 基础模型

已有：

- EloModel
- DixonColesModel
- PoissonModel
- XGBoostModel


注意：

当前主要为架构框架。

真实算法需要从 Legacy 迁移。


### 融合

已有：

FusionEngine


### 回测

已有：

BacktestEngine

ROI Analyzer

Accuracy Report


==================================================

## Legacy资产


主要位置：

03_MODEL_LAYER


包含：

- Elo真实算法
- Dixon-Coles真实算法
- Poisson真实算法
- XGBoost训练逻辑


旧资产不能简单删除。


必须先判断：

能力是否迁移。


==================================================

## 当前核心问题


1.

旧算法没有完整迁移。


2.

新架构存在接口，但缺少真实数据流。


3.

存在功能重复表现。


判断重复：

必须依据：

- 类
- 函数
- 调用关系
- 数据流

不能依据文件名。


==================================================

## AI执行原则


禁止：

- 重构整个架构
- 新建重复模块
- 删除Legacy资产
- 绕过治理文件


必须：

先审计。

再迁移。

最后优化。


==================================================

## 最终系统目标


实现：

数据层



Feature Store



模型层



融合层



市场分析



风险分析



决策层



反馈学习


形成自学习足球智能系统。


