# Phase5 Self Learning Core Batch01


Project:

Football AI OS


Architecture:

Omega V3.2


Task:

Implement Self Learning Core Extension


Target:

07_BACKTEST_AI


Do NOT create:

09_SELF_LEARNING


Objective:

Create learning capability inside existing Backtest layer.



Required Components:



1.

Learning Decision Engine


Path:

07_BACKTEST_AI\learning_core\learning_decision.py



Function:

Determine whether model learning is required.



Input:

- accuracy degradation
- ROI degradation
- prediction errors



Output:

learning_required



---



2.

Feature Feedback Engine


Path:

07_BACKTEST_AI\learning_core\feature_feedback_engine.py



Function:

Analyze feature errors.



Output:

- feature importance review
- weight adjustment suggestion



---



3.

Learning Validation Test


Path:

07_BACKTEST_AI\learning_core\tests



Required:

pytest PASS



---



Rules:



1. Do not modify production models.

2. Do not modify Elo/Dixon-Coles/Poisson/XGBoost directly.

3. Generate candidate feedback only.

4. Follow DEVELOPMENT_WORKFLOW.md.

5. Create report.

6. Create checkpoint.



Validation:

PASS required before next phase.


