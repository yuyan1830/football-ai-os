# Football AI OS Ω+
# Checkpoint-077
# Model Probability Layer Design V1.0


## 目标

建立统一模型概率输出层。


---

## 当前问题

四模型输出形式不同：

Elo:

Rating


Dixon-Coles:

Attack / Defense


Poisson:

Lambda / Score Probability


XGBoost:

Classification


无法直接比较。


---

## V3.3解决方案


建立：

Model Probability Contract


所有模型统一输出：


{
model_name,

home_win_probability,

draw_probability,

away_win_probability,

confidence,

score_probability

}


---

## 接入模型


1. Elo Probability Adapter

2. Dixon-Coles Probability Adapter

3. Poisson Probability Adapter

4. XGBoost Probability Adapter


---

## 后续能力


支持：

- Probability Fusion
- Probability Calibration
- Historical Evaluation
- ROI Validation


---

状态：

Design Frozen

下一阶段：

Implementation

