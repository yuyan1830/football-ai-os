# Football AI OS Database Architecture V2.1 Frozen Baseline

Version:
V2.1

Status:
FROZEN

Date:
2026-07-23


## 1. Architecture Principle

Football AI OS adopts:

Multi Database Isolation Architecture

+
football_ai_os.db Central Management Database


Goals:

- Stable runtime
- Easy migration
- Easy upgrade
- Production ready
- Future expansion


## 2. Final Database Structure


Football_AI_OS

databases

 core
     football_ai_os.db

 data
     match_data.db

 feature
     feature_store.db

 model
     model_store.db

 prediction
     prediction.db

 market
     market.db

 runtime
     runtime_log.db

 archive


## 3. Database Responsibilities


## football_ai_os.db

Role:

System Control Center


Contains:

- database_registry
- schema_version
- migration_history
- system_status


Responsible for:

- database registration
- version control
- migration management
- system configuration



## match_data.db

Role:

Raw Match Data Layer


Contains:

- matches
- teams
- competitions
- seasons


Does not contain:

- prediction results
- model outputs



## feature_store.db

Role:

Feature Management Layer


Contains:

- ELO features
- Dixon-Coles features
- Poisson features
- Team form
- Home/Away features
- Fatigue features
- Market features



## model_store.db

Role:

Model Asset Management


Contains:

- model versions
- model parameters
- model weights
- model accuracy
- evaluation records


Note:

model_cache.db is NOT separated currently.

Future expansion only.



## prediction.db

Role:

Prediction Storage


Contains:

- predictions
- probability outputs
- model fusion results
- backtest results



## market.db

Role:

Market Intelligence Database


Contains:

- European odds
- Asian handicap
- SP data
- odds movement
- market sentiment



## runtime_log.db

Role:

System Runtime Monitoring


Contains:

- system_log
- model_call_log
- prediction_log
- error_log
- user_action_log



## 4. Development Database Rule


Development environment:

Contains:

- complete historical data
- training data
- trained models
- backtest results
- runtime logs



## 5. Production Database Rule


Production structure must match development structure.


Production initially provides:

- database schema
- trained base models
- model parameters
- system framework


User data:

Imported by user.


Production database does NOT contain private user data.


## 6. Development Rules


All future development must follow:


1. Determine database ownership before creating tables

2. No random cross-database storage

3. New tables must register in football_ai_os.db

4. Schema changes require migration_history

5. Development and production schema must remain consistent



## Frozen Baseline

This document is the official:

Football AI OS Database Architecture V2.1 Frozen Baseline


All future database development must reference this version.

