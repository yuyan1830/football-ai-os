# FOOTBALL_AI_OS_DATABASE_ARCHITECTURE_V2.2_FROZEN

Version: V2.2  
Status: FROZEN  
Date: 2026-07-23  

---

# 1. Database Architecture Overview

Football AI OS adopts a multi-database architecture.

The system separates:

- System Control Layer
- Match Data Layer
- Feature Engineering Layer
- Model Layer

Design objective:

- improve stability
- isolate responsibilities
- support user self-data import
- support independent model upgrade
- prevent database coupling


Final Architecture:


E:\football_v

00_SYSTEM_OS

01_DATA_LAYER
   
   database
       
       football_ai_os.db
       match_data.db

02_FEATURE_LAYER
   
   database
       
       feature_store.db

03_MODEL_LAYER
    
    database
        
        model_store.db


---

# 2. Database Responsibility Definition


## 2.1 football_ai_os.db

Role:

System Management Database


Location:

00_SYSTEM_OS/01_DATA_LAYER/database/


Responsibilities:

- system version management
- database registration
- model registration
- runtime status
- task management


Tables:

system_registry

database_registry

model_registry

runtime_registry

task_registry


Restrictions:

DO NOT store:

- match history
- user data
- raw data
- training samples


---

# 2.2 match_data.db

Role:

Football Match Data Database


Responsibilities:

Store:

- historical matches
- teams
- competitions
- seasons
- odds history
- xG data
- cleaned match data


Current Data:


matches_full:

96337


matches_clean:

96305


odds_history:

139501


odds_history_clean:

139454


xg_shot_history:

515218


xg_shot_history_clean:

515217


This database is the only source for feature generation.


---

# 2.3 feature_store.db

Role:

AI Feature Database


Location:

00_SYSTEM_OS/02_FEATURE_LAYER/database/


Responsibilities:

Store generated model features:


Tables:

elo_history

dixon_coles_history

poisson_history

team_form_history

home_away_history

fatigue_rating

feature_vector


Data Flow:


match_data.db

        |

        v

Feature Engine

        |

        v

feature_store.db



---

# 2.4 model_store.db

Role:

AI Model Database


Location:

00_SYSTEM_OS/03_MODEL_LAYER/database/


Responsibilities:

Store:


elo_model

dixon_coles_model

poisson_model

xgboost_model

fusion_model

model_weight

model_version


Data Flow:


feature_store.db

        |

        v

Training Engine

        |

        v

model_store.db



---

# 3. Development Database and Production Database


## Development Environment


Purpose:

System development and training.


Contains:

- full historical data
- feature generation
- model training
- experiments



## Production Environment


Purpose:

User prediction system.


Production database rules:


football_ai_os.db

contains:

- system configuration
- model registry


match_data.db

provided by user.


feature_store.db

generated from user data.


model_store.db

contains released models.



---

# 4. User Deployment Design


User installation process:


Install Football AI OS

        |

        v

Download own football data

        |

        v

Import match_data.db

        |

        v

Generate feature_store.db

        |

        v

Load model_store.db

        |

        v

Prediction System Ready



---

# 5. Model Delivery Policy


Football AI OS provides:


YES:

- trained model parameters
- model weights
- model versions
- prediction engine


NO:

- developer private database
- raw development data
- internal experiments



---

# 6. Backup Policy


Before migration:


Create backup:


archive_match_data_before_v22.db


Location:


99_Documentation/checkpoints/


Backup must remain until:


- Feature Layer completed
- Model migration completed
- Release validation completed



---

# 7. Database Migration Rules


Rules:


1. Never directly modify production database structure.


2. All schema changes require version upgrade.


3. Migration must create backup.


4. Migration must generate report.


5. Validation must pass before deleting old database.



---

# 8. Current Validation Status


DATABASE_SYSTEM_VALIDATION_V2.2.4:


football_ai_os.db       PASS

match_data.db           PASS

feature_store.db        PASS

model_store.db          PASS



---

# 9. Future Development Rules


All new modules must follow:


Data Module:

01_DATA_LAYER


Feature Module:

02_FEATURE_LAYER


Model Module:

03_MODEL_LAYER


System Module:

football_ai_os.db



No independent uncontrolled databases allowed.



---

# 10. Freeze Statement


This document defines:

FOOTBALL AI OS DATABASE ARCHITECTURE V2.2


All future development must follow this architecture.

Any database architecture modification requires:

- architecture review
- version upgrade
- migration plan
- validation report



END OF DOCUMENT
