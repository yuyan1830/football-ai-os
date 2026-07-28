# Football AI OS Product Database Architecture V1.0

Framework: Football AI OS Ultimate Fusion Framework V1.5

Status: APPROVED

Purpose: 用户免训练发布版本数据库架构设计。

------------------------------------------------------------------------

## 1. 核心原则

开发环境 ≠ 产品环境

开发阶段完成：

-   历史数据积累
-   数据清洗
-   特征工程
-   模型训练
-   参数优化
-   回测验证

最终发布时：

用户安装即可使用，不需要重新训练模型。

------------------------------------------------------------------------

## 2. 开发环境

研发阶段使用：

-   development
-   sandbox
-   staging
-   warehouse

用途：

-   数据开发
-   模型实验
-   训练
-   验证
-   版本迭代

------------------------------------------------------------------------

## 3. 产品发布数据库

用户安装版本只保留：

    database

    ├── match_data.db

    ├── feature_store.db

    └── model_store.db

------------------------------------------------------------------------

## 4. match_data.db

作用：

保存比赛事实数据。

包含：

-   teams
-   competitions
-   seasons
-   matches
-   match_stats
-   odds
-   xG
-   injuries
-   updates

不保存：

-   模型结果
-   模型权重
-   实验数据

------------------------------------------------------------------------

## 5. feature_store.db

作用：

保存模型输入特征。

包含：

-   Elo features
-   Dixon-Coles features
-   Poisson features
-   XGBoost features
-   Team form
-   Fatigue
-   Home/Away features
-   Market features
-   Sentiment features

------------------------------------------------------------------------

## 6. model_store.db

作用：

保存成熟模型。

包含：

-   model_registry
-   model_version
-   model_parameter
-   model_metrics
-   model_artifact

发布模型：

-   Elo Model
-   Dixon-Coles Model
-   Poisson Model
-   XGBoost Model
-   V38.8.1 Handicap Model
-   Market Risk Model 2.0

------------------------------------------------------------------------

## 7. 用户安装流程

    安装

    ↓

    加载数据库

    ↓

    加载预训练模型

    ↓

    同步最新数据

    ↓

    更新特征

    ↓

    比赛预测

    ↓

    生成报告

用户无需：

-   重新训练模型
-   导入全部历史数据
-   配置开发环境

------------------------------------------------------------------------

## 8. 模型更新机制

采用增量更新：

    新比赛数据

    ↓

    match_data.db

    ↓

    feature更新

    ↓

    模型评估

    ↓

    模型小幅调整

    ↓

    发布新版本

------------------------------------------------------------------------

## 9. 最终产品形态

Football AI OS Product V1.0

包含：

-   四模型融合预测
-   V38.8.1盘口模型
-   Market Risk Model 2.0
-   自动赔率分析
-   自动报告
-   Dashboard
-   历史复盘

------------------------------------------------------------------------

## 10. DATABASE GOVERNANCE目标

16_DATABASE_GOVERNANCE_LAYER

目标：

将研发数据库体系

转换为：

Football AI OS Product Database Package V1.0

------------------------------------------------------------------------

Version: V1.0

Date: 2026-07-22
