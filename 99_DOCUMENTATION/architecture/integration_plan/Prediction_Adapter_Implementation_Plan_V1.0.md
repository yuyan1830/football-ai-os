# Football AI OS Ω+ V3.2.1

# Prediction Adapter Implementation Plan V1.0


====================================
一、目标
====================================


建立统一预测调用接口。


连接:


AI_RUNTIME



Prediction Adapter



06_PREDICTION_INTELLIGENCE_ENGINE



Model Connector



Model Pool



====================================
二、复用模块
====================================


已有:

EloConnector

DixonColesConnector

PoissonConnector

XGBoostConnector



不重复创建。



====================================
三、Adapter职责
====================================


PredictionAdapter:


负责:

1. 接收比赛输入


2. 调用四模型Connector


3. 获取模型输出


4. 统一概率格式



====================================
四、输入
====================================


match:

home_team

away_team

league

features



====================================
五、输出
====================================


返回:


{

elo:{},

dixon_coles:{},

poisson:{},

xgboost:{}

}



====================================
六、开发原则
====================================


禁止:

修改模型代码


禁止:

复制模型逻辑


采用:

Connector调用



====================================
七、下一步
====================================


Implement:

prediction_adapter.py


然后:

单元测试

Runtime接入

Checkpoint



====================================
