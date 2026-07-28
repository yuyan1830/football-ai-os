# Football AI OS ��+ V3.2
# Legacy Model Migration Report V1.0

**Date:** 2026-07-25
**Status:** COMPLETED (Phase 1 - Code Migration)
**System:** Football AI OS Betting Intelligence System ��+ V3.2

---

## 1. Executive Summary

### 1.1 Migration Scope

从 `E:\football\Football_AI_System\03_Model_Engine` 迁移模型代码到 `E:\football_v\LEGACY_IMPORT`。

| Metric | Count |
|--------|-------|
| Total files migrated | 26 |
| Prediction Models | 8 |
| Data Engine | 11 |
| Supporting | 7 |
| Stub modules (需改造) | 3 |
| Data leakage risk (需重构) | 3 |
| Duplicate variants (待废弃) | 3 |

### 1.2 Classification Summary

| Class | Definition | Count | Files |
|-------|-----------|-------|-------|
| **CLASS_A** | 直接迁移 - 符合Omega架构 | 16 | Elo, Dixon-Coles, Poisson, XGBoost engines + history + support |
| **CLASS_B** | 需改造 - 功能存在但需调整 | 4 | match_loader, odds_loader, team_loader, competition_loader |
| **CLASS_C** | 需重构为时间序列 - 数据泄露风险 | 3 | form_engine, fatigue_engine_v2, home_away_engine |
| **CLASS_D** | 待废弃 - 重复模块 | 3 | elo_engine_data, dixon_coles_data, poisson_engine_data |

---

## 2. Governance Reference Files (已验证)

| # | File | Path | Status |
|---|------|------|--------|
| 1 | CLAUDE.md | E:\football_v\CLAUDE.md | VERIFIED - AI行为约束/架构冻结 |
| 2 | Architecture Baseline V3.2 | E:\football_v\03_Data_Governance\Architecture_Baseline\... | VERIFIED - 10层架构定义 |
| 3 | Legacy Asset Index V1.0 | E:\football_v\10_GOVERNANCE_LAYER\registry\... | VERIFIED - 7个模型资产注册 |
| 4 | Project Control Baseline V1.0 | E:\football_v\03_Data_Governance\Project_Control\... | VERIFIED - 迁移策略指引 |

---

## 3. File Inventory by Architecture Layer

### 3.1 Layer 3 - Prediction Intelligence Layer (8 files)

| # | File | Model | Source Path (authoritative) |
|---|------|-------|----------------------------|
| 1 | elo_engine.py | Elo Rating | 03_Model_Engine\02_Probability_Model\Elo\ |
| 2 | dixon_coles.py | Dixon-Coles | 03_Model_Engine\02_Probability_Model\Dixon_Coles\ |
| 3 | dixon_coles_history_engine.py | Dixon-Coles History | 03_Model_Engine\02_Probability_Model\Dixon_Coles\ |
| 4 | poisson_engine.py | Poisson | 03_Model_Engine\02_Probability_Model\Poisson\ |
| 5 | poisson_history_engine.py | Poisson History | 03_Model_Engine\02_Probability_Model\Poisson\ |
| 6 | xgboost_engine.py | XGBoost Base | 03_Model_Engine\03_Machine_Learning\XGBoost\ |
| 7 | xgboost_fusion_engine.py | XGBoost Fusion V1 | 03_Model_Engine\03_Machine_Learning\XGBoost\ |
| 8 | xgboost_fusion_v2_engine.py | XGBoost Fusion V2 | 03_Model_Engine\03_Machine_Learning\XGBoost\ |

### 3.2 Layer 1 - Data Intelligence Layer (11 files)

| # | File | Type | Source Path |
|---|------|------|-------------|
| 9 | match_loader.py | STUB | 03_Model_Engine\01_Data_Engine\data_engine\ |
| 10 | odds_loader.py | STUB | 03_Model_Engine\01_Data_Engine\data_engine\ |
| 11 | team_loader.py | STUB | 03_Model_Engine\01_Data_Engine\data_engine\ |
| 12 | competition_loader.py | Active | 03_Model_Engine\01_Data_Engine\data_engine\ |
| 13 | form_engine.py | DATA_LEAK | 03_Model_Engine\01_Data_Engine\data_engine\ |
| 14 | fatigue_engine_v2.py | DATA_LEAK | 03_Model_Engine\01_Data_Engine\data_engine\ |
| 15 | home_away_engine.py | DATA_LEAK | 03_Model_Engine\01_Data_Engine\data_engine\ |
| 16 | clean_matches.py | Active | 03_Model_Engine\01_Data_Engine\data_engine\ |
| 17 | team_form_history_engine.py | History | 03_Model_Engine\01_Data_Engine\data_engine\ |
| 18 | home_away_history_engine.py | History | 03_Model_Engine\01_Data_Engine\data_engine\ |
| 19 | fatigue_history_engine.py | History | 03_Model_Engine\01_Data_Engine\data_engine\ |

### 3.3 Layer 0 / Supporting (7 files)

| # | File | Type | Source Path |
|---|------|------|-------------|
| 20 | data_audit_engine.py | Audit | 03_Model_Engine\01_Data_Engine\data_engine\ |
| 21 | model_data_registry_engine.py | Registry | 03_Model_Engine\01_Data_Engine\data_engine\ |
| 22 | import_local_data.py | Import | 03_Model_Engine\01_Data_Engine\data_engine\ |
| 23 | import_full_data.py | Import | 03_Model_Engine\01_Data_Engine\data_engine\ |
| 24 | elo_engine_data.py | DUPLICATE | 03_Model_Engine\01_Data_Engine\data_engine\elo_engine.py |
| 25 | dixon_coles_data.py | DUPLICATE | 03_Model_Engine\01_Data_Engine\data_engine\dixon_coles.py |
| 26 | poisson_engine_data.py | DUPLICATE | 03_Model_Engine\01_Data_Engine\data_engine\poisson_engine.py |

---

## 4. Key Findings

### 4.1 Critical: Data Leakage Risk (3 engines)

以下引擎使用全量数据计算特征，存在**未来数据泄露**，已被 `model_data_registry` 标记为 `deprecated`：

| Engine | Risk | Impact |
|--------|------|--------|
| form_engine.py | HIGH | 使用所有比赛后的 last5/last10 统计 |
| fatigue_engine_v2.py | HIGH | 使用 `max(all_dates)` 作为当前日期 |
| home_away_engine.py | HIGH | 全量统计主客场胜率 |

**已有时间序列版本可用：**
- `team_form_history_engine.py`
- `fatigue_history_engine.py`
- `home_away_history_engine.py`

**建议：** V3.2 融合模型（xgboost_fusion_v2_engine.py）已经直接 JOIN 这些历史表，应优先使用时间序列版本。

### 4.2 Warning: XGBoost Fusion V1 使用已废弃数据

`xgboost_fusion_engine.py` 从 `dixon_coles_rating` 和 `poisson_rating` 读取数据，这两个表已被 `model_data_registry` 标记为 `deprecated`（原因：future_data_leakage_risk）。

**建议：** 将 Fusion V1 升级为使用 `dixon_coles_history` 和 `poisson_history` 时间序列表。

### 4.3 Info: Stub Modules

`match_loader.py`, `odds_loader.py`, `team_loader.py` 目前仅为存根（仅打印占位信息）。需要实现实际功能后方可用于生产。

### 4.4 Info: Duplicate Files

`data_engine/` 目录下的 `elo_engine.py`, `dixon_coles.py`, `poisson_engine.py` 与 `02_Probability_Model/` 和 `03_Machine_Learning/` 下的权威版本重复。已复制到 `03_SUPPORTING/` 并重命名以作区分。

---

## 5. LEGACY_IMPORT Directory Structure

```
LEGACY_IMPORT/
├── 01_PREDICTION_MODELS/
│   ├── Elo/
│   │   └── elo_engine.py
│   ├── Dixon_Coles/
│   │   ├── dixon_coles.py
│   │   └── dixon_coles_history_engine.py
│   ├── Poisson/
│   │   ├── poisson_engine.py
│   │   └── poisson_history_engine.py
│   └── XGBoost/
│       ├── xgboost_engine.py
│       ├── xgboost_fusion_engine.py
│       └── xgboost_fusion_v2_engine.py
├── 02_DATA_ENGINE/
│   ├── match_loader.py
│   ├── odds_loader.py
│   ├── team_loader.py
│   ├── competition_loader.py
│   ├── form_engine.py
│   ├── fatigue_engine_v2.py
│   ├── home_away_engine.py
│   ├── clean_matches.py
│   ├── team_form_history_engine.py
│   ├── home_away_history_engine.py
│   └── fatigue_history_engine.py
├── 03_SUPPORTING/
│   ├── data_audit_engine.py
│   ├── model_data_registry_engine.py
│   ├── import_local_data.py
│   ├── import_full_data.py
│   ├── elo_engine_data.py
│   ├── dixon_coles_data.py
│   └── poisson_engine_data.py
└── 04_MANIFEST/
    ├── migration_manifest.csv
    └── migration_report_V1.0.md
```

---

## 6. Verification Checklist

| # | Item | Status |
|---|------|--------|
| 1 | CLAUDE.md 已读取 | ✓ |
| 2 | Architecture Baseline 已读取 | ✓ |
| 3 | Legacy Asset Index 已读取 | ✓ |
| 4 | Project Control Baseline 已读取 | ✓ |
| 5 | LEGACY_IMPORT 目录结构已创建 | ✓ |
| 6 | 26个文件已从权威路径复制 | ✓ |
| 7 | 零修改（只复制不修改） | ✓ |
| 8 | migration_manifest.csv 已生成 | ✓ |
| 9 | 文件完整性已验证 | ✓ |

---

## 7. Next Steps (per Project Control Baseline)

| Phase | Action | Priority |
|-------|--------|----------|
| Phase 2 | 生成 Architecture Mapping V1.0（映射到Omega V3.2 Layer） | HIGH |
| Phase 3 | 解决数据泄露问题：form/fatigue/home_away 引擎的时间序列改造 | CRITICAL |
| Phase 3 | 解决 XGBoost Fusion V1 使用 deprecated 数据源问题 | HIGH |
| Phase 3 | Stub 模块实现（match/odds/team loader） | MEDIUM |
| Phase 4 | 重复模块清理（CLASS_D 文件） | LOW |
| Phase 5 | 模型验证：回测 + ROI验证 | HIGH |
| Phase 6 | 集成测试：Prediction Model Pool 端到端 | MEDIUM |
| Phase 7 | 系统认证 | FINAL |

---

## 8. Governance Compliance

本次迁移遵循以下治理原则：

- **Rule 4 (目标驱动执行):** 计划 → 修改 → 测试 → 验证 ✓
- **Rule 5 (AI辅助判断):** 分类/分析/判断/总结 由AI执行 ✓
- **Rule 8 (修改前阅读):** 所有源文件已读取确认 ✓
- **Rule 11 (项目规范优先):** 遵循 Architecture Baseline V3.2 层级结构 ✓
- **Architecture Rule 3 (质量优先):** 已识别并标记数据泄露风险 ✓
- **Architecture Rule 4 (不重复造轮子):** 已识别并标记重复模块 ✓
- **Part 5 (核心资产保护):** 仅复制，零修改 ✓

---

**Report Generated:** 2026-07-25
**Next Review:** After Phase 2 Architecture Mapping completion
**System:** Football AI OS ��+ V3.2 - ARCHITECTURE_FROZEN - FINAL_RELEASE
