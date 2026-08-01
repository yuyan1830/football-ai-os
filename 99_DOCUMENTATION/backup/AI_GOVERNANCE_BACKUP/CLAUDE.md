# Football AI OS Ω+
# CLAUDE Development Governance Rules
# Version: V3.2 Production Baseline Final Edition


==================================================
# 1. 项目身份
==================================================


项目名称:

Football AI OS Ω+


系统定位:

足球智能决策操作系统。


当前生产基线:

Football AI OS Ω+ V3.2


当前状态:

Architecture Frozen

Production Stabilization Mode



当前目标:

在 V3.2 稳定基础上，

逐步升级为:

Football AI OS Ω+

Intelligence Trading System



升级路线:


V3.2 Production Baseline

↓

V3.3 Data Intelligence Edition

↓

V3.5 Market Intelligence Edition

↓

V4.0 Intelligence Trading System



禁止:

未经审核推翻已有架构。



==================================================
# 2. 最高治理原则 Prime Directive
==================================================


系统治理最高原则:


稳定优先于扩展。

收敛优先于新增。

验证优先于上线。



任何开发必须遵循:


第一优先:

复用已有能力


第二优先:

迁移已有能力


第三优先:

优化已有模块


最后:

创建新模块



禁止:

为了增加复杂度而增加模块。



==================================================
# 3. 最高参考文件
==================================================


所有AI助手必须优先读取:


E:\football_v\99_DOCUMENTATION\Architecture_Audit\



核心文件:


01_PROJECT_ASSET_AUDIT_REPORT_V1.0.md


04_REAL_ARCHITECTURE_REPORT_V1.0.md


06_MODULE_FREEZE_REGISTRY_V1.0.md


07_DEVELOPMENT_BASELINE_V1.0.md



这些文件定义:


- 当前真实架构
- 已完成资产
- 冻结模块
- 模块职责
- 开发方向



==================================================
# 4. Single Decision Authority 架构原则
==================================================


Football AI OS 必须保持:


ONE Runtime


ONE Decision Authority


ONE Production Output Pipeline



含义:


允许:

多个分析模块

多个预测模型

多个市场模型



但是:

最终决策必须经过唯一 Decision Layer。



当前核心链路:


DATA_LAYER

↓

MODEL_LAYER

↓

MODEL_FUSION

↓

AI_RUNTIME

↓

08_DECISION_LAYER

↓

12_API_LAYER

↓

13_OUTPUT_SERVICE_LAYER



禁止:


- 创建第二Runtime
- 创建第二Decision系统
- 创建第二Output链路
- 绕过Decision Layer输出结果



==================================================
# 5. 冻结模块规则
==================================================


以下模块冻结:


02_FEATURE_LAYER


03_MODEL_LAYER


05_MODEL_AI


06_PREDICTION_INTELLIGENCE_ENGINE



核心模型:


Elo


Dixon-Coles


Poisson


XGBoost


Fusion



允许:


- 参数优化
- 性能优化
- 接口优化



禁止:


- 重建同类模型
- 改变模块职责
- 创建平行模型系统



==================================================
# 6. 模块发现、迁移与创建规则
==================================================


任何新增功能开发前:

必须先搜索整个项目。



流程:


Step 1:

搜索已有模块。



检查:


- ACTIVE模块
- DEPRECATED模块
- ARCHIVE模块
- 历史资产
- 相似功能实现



Step 2:

如果存在已有能力:


禁止新建重复模块。



必须:


分析

↓

复用

↓

迁移

↓

升级



Step 3:

迁移完成后:


检查旧模块。



如果确认:

无生产依赖


进入:


DEPRECATED


或:


ARCHIVE



Step 4:

清理重复生产路径。



最终要求:


ONE Capability


ONE Responsibility


ONE Production Implementation



==================================================
# 7. 新模块创建审批
==================================================


创建新模块是最后选择。



只有满足:


项目不存在相关能力


才允许创建。



创建前必须说明:


- 搜索结果
- 为什么不能复用
- 新模块职责
- 输入数据
- 输出结果
- 预期提升



==================================================
# 8. 模块生命周期管理
==================================================


所有文件和模块必须属于:


ACTIVE


生产使用。



DEPRECATED


历史版本。

禁止新开发依赖。



ARCHIVE


历史归档。



DELETE_PENDING


等待审核删除。



规则:


Deprecated != Delete



禁止:

AI自动删除历史资产。



==================================================
# 9. 清理与删除规则
==================================================


允许清理:


- 重复模块
- 空壳模块
- 无效Demo
- 已完全替代模块



删除流程:


Step 1:

扫描引用关系。



Step 2:

确认无生产依赖。



Step 3:

创建Git Checkpoint。



Step 4:

执行删除。



Step 5:

系统测试。



Step 6:

生成Cleanup Report。



==================================================
# 10. 数据治理规则
==================================================


数据属于核心资产。



禁止:


- 删除历史数据
- 覆盖训练数据
- 混合开发数据和生产数据



环境:


DEV


↓

VALIDATION


↓

PRODUCTION



==================================================
# 11. 模型治理规则
==================================================


当前核心模型:


Elo


Dixon-Coles


Poisson


XGBoost



新增模型必须提供:


- 模型目的
- 输入数据
- 输出结果
- 与已有模型区别
- 回测结果
- 实际提升



禁止:

仅因为增加复杂度而增加模型。



==================================================
# 12. AI助手权限规则
==================================================


Claude Code 可以:


- 分析代码
- 检查架构
- 搜索模块
- 提出方案
- 编写代码
- 创建测试
- 生成文档



Claude Code 禁止:


- 自动改变架构
- 自动删除资产
- 创建重复系统
- 修改冻结模块职责
- 绕过测试上线



重大修改必须:


设计

↓

审核

↓

实现

↓

测试

↓

Checkpoint

↓

Git Commit



==================================================
# 13. 开发流程
==================================================


所有修改必须:


Step 1:

读取 Architecture Audit


Step 2:

确认模块职责


Step 3:

搜索已有实现


Step 4:

制定方案


Step 5:

执行修改


Step 6:

运行测试


Step 7:

保存Checkpoint


Step 8:

Git提交



==================================================
# 14. Git规则
==================================================


重要修改必须:


git commit



提交信息格式:


Feature:

新增功能



Upgrade:

升级模块



Fix:

修复问题



Cleanup:

清理重复资产



重大版本:

必须创建Tag。



==================================================
# 15. 当前升级路线
==================================================


## V3.2 Production Baseline


目标:


稳定系统。


重点:


- Runtime稳定
- Decision稳定
- Output稳定
- Backtest完善
- 复盘闭环建立



--------------------------------------------------


## V3.3 Data Intelligence Edition


目标:


建立数据智能基础。



包括:


- Feature Store
- Data Pipeline
- Historical Validation
- Backtest System



--------------------------------------------------


## V3.5 Market Intelligence Edition


目标:


建立市场理解能力。



包括:


- Odds Intelligence
- Fair Price Engine
- Handicap Intelligence
- Market Sentiment
- No Bet Engine



--------------------------------------------------


## V4.0 Intelligence Trading System


目标:


足球市场智能决策系统。



包括:


- Alpha Discovery
- Capital Behavior
- Portfolio Risk
- Strategy Management
- Controlled Evolution



==================================================
# 16. 最终系统目标
==================================================


Football AI OS Ω+


不是简单预测程序。



最终目标:


Football AI OS Ω+

Intelligence Trading System



核心能力:


Football Intelligence


+

Market Intelligence


+

Price Discovery


+

Risk Management


+

Decision Intelligence


+

Continuous Evolution



==================================================

END OF CLAUDE GOVERNANCE RULES
==================================================