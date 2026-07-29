# Football AI OS Ω+ V3.2
# Architecture Governance Rules V4.0


# 1. 项目身份

本项目：

Football AI OS Betting Intelligence System Ω+ V3.2


当前状态：

Architecture Frozen

Production Development Mode


禁止推翻已有架构。


--------------------------------------------------


# 2. 最高优先级参考文件


所有AI助手必须优先读取：


E:\football_v\99_DOCUMENTATION\Architecture_Audit\


核心文件：


01_PROJECT_ASSET_AUDIT_REPORT_V1.0.md

04_REAL_ARCHITECTURE_REPORT_V1.0.md

06_MODULE_FREEZE_REGISTRY_V1.0.md

07_DEVELOPMENT_BASELINE_V1.0.md



这些文件定义：

- 当前真实架构
- 已完成资产
- 冻结模块
- 后续开发方向



--------------------------------------------------


# 3. 已冻结模块


以下模块禁止重构：


02_FEATURE_LAYER


03_MODEL_LAYER


05_MODEL_AI


06_PREDICTION_INTELLIGENCE_ENGINE



包括：

Elo

Dixon-Coles

Poisson

XGBoost

Fusion



允许：

参数优化

性能优化

接口优化



禁止：

重新创建同类模块。



--------------------------------------------------


# 4. 当前开发方向


只允许进入：


Market Intelligence



Decision Engine



Output Service



当前重点：

101_REAL_MARKET_INTELLIGENCE_ENGINE


104_MARKET_SENTIMENT_FUSION_ENGINE


105_HANDICAP_VALUE_DECISION_ENGINE


107_MARKET_PATTERN_RECOGNITION_ENGINE


110_FINAL_MARKET_DECISION_ENGINE


144_MATCH_ANALYSIS_EXECUTOR



--------------------------------------------------


# 5. 禁止行为


AI不得：

1. 创建新的Prediction Engine

2. 创建新的Model Layer

3. 删除历史资产

4. 自动重构架构

5. 修改冻结模块职责

6. 绕过测试直接提交代码



--------------------------------------------------


# 6. 开发流程


任何代码修改必须：

Step 1

读取Architecture_Audit


Step 2

确认模块职责


Step 3

提出修改方案


Step 4

执行代码


Step 5

测试


Step 6

保存Checkpoint



--------------------------------------------------


# 7. Git规则


所有重要修改必须：

commit


提交信息必须说明：

- 修改模块
- 修改目的
- 测试结果



--------------------------------------------------


# 8. 最终目标


将系统完善为：


Prediction



Market Intelligence



Decision



Report


完整智能决策系统。


