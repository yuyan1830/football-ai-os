# Football AI OS Ω+ V3.2
# Elo Model Migration Design V1.0

版本：
V1.0

状态：
DESIGN COMPLETE / WAITING APPROVAL

---

# 1. 文档目的

本文档定义 Football AI OS Betting Intelligence System Ω+ V3.2 中：

Legacy Elo Engine

向

Omega V3.2 Model Layer EloModel

迁移的设计方案。

本迁移遵循：

Legacy资产保护原则

不重新设计架构。

目标：

将已有成熟Elo算法能力接入Omega V3.2统一模型体系。

---

# 2. 项目基线

必须遵守：

1. CLAUDE.md
2. Football_AI_OS_Betting_Intelligence_System_Omega_V3.2_Baseline.md
3. Football_AI_OS_Legacy_Asset_Index_V1.0.csv

以上文件为最高优先级治理文件。

---

# 3. 当前状态

## Legacy Elo

路径：

03_MODEL_LAYER/
legacy_import/
01_Data_Engine/
data_engine/
elo_engine.py


能力：

- Elo评分计算
- 比赛数据读取
- 主场优势调整
- K值更新
- 历史评分保存


输入：

matches_clean


输出：

elo_history

team_rating


---

## Omega Elo

路径：

05_MODEL_AI/
MODEL_LAYER/
models/
elo_model.py


当前状态：

接口框架。

已有：

- BaseModelInterface
- ModelRegistry


缺少：

- Elo算法
- 数据读取
- 训练流程
- 预测逻辑

---

# 4. 迁移目标

完成后：

数据层

↓

EloModel

↓

Fusion Engine

↓

Prediction Intelligence

↓

Decision Engine


---

# 5. 迁移范围

必须迁移：

## 算法

- Elo Expected Score
- Rating Update
- Home Advantage
- K Factor


## 数据

- matches_clean读取
- team_rating维护
- elo_history记录


## 接口

适配：

BaseModelInterface

实现：

train()

predict()

evaluate()

save()

load()

---

# 6. 保留策略


禁止删除：

Legacy Elo文件


原因：

- 历史参考
- 回归测试
- 回滚依据


保留：

03_MODEL_LAYER

football.db

elo_history

team_rating


---

# 7. 新模型设计


class:

EloModel


继承：

BaseModelInterface


## train()

功能：

根据历史比赛训练球队评分。


输入：

比赛数据


输出：

训练状态。


---

## predict()

输入：

home_team

away_team


输出：

home_win

draw

away_win


要求：

禁止硬编码概率。


---

## evaluate()

用于：

模型效果评估。


指标：

Accuracy

Brier Score

Calibration


---

# 8. 数据库规则


禁止：

直接覆盖历史数据。


迁移前：

必须备份数据库。


新增版本记录：

ELO_LEGACY_V1

ELO_OMEGA_V3.2_V1


---

# 9. 测试要求


必须完成：


## 单元测试

验证：

- Elo公式
- K值
- 主场优势


## 回归测试

Legacy vs Omega


要求：

预测结果误差 < 2%


## 集成测试

验证：

EloModel

↓

Fusion Engine


---

# 10. 执行顺序


阶段1：

设计确认


阶段2：

数据库备份


阶段3：

实现EloModel


阶段4：

测试


阶段5：

接入ModelRegistry


阶段6：

更新治理文件


---

# 11. 修改规则


任何代码修改前：

必须：

1. 更新任务状态
2. 确认影响范围
3. 保留旧资产
4. 完成测试
5. 更新版本记录


---

# 12. 当前状态


Migration Design:

COMPLETE


Code Migration:

NOT STARTED


Waiting:

Human Approval
