
-- Football AI OS
-- Feature Store V2.1


CREATE TABLE IF NOT EXISTS team_form_history (

    id SERIAL PRIMARY KEY,

    team_name TEXT,

    form_data JSONB,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);



CREATE TABLE IF NOT EXISTS home_away_history (

    id SERIAL PRIMARY KEY,

    team_name TEXT,

    home_data JSONB,

    away_data JSONB,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);



CREATE TABLE IF NOT EXISTS elo_history (

    id SERIAL PRIMARY KEY,

    team_name TEXT,

    elo_value FLOAT,

    elo_change FLOAT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);



CREATE TABLE IF NOT EXISTS attack_defence_history (

    id SERIAL PRIMARY KEY,

    team_name TEXT,

    attack FLOAT,

    defence FLOAT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);



CREATE TABLE IF NOT EXISTS model_feature_snapshot (

    id SERIAL PRIMARY KEY,

    snapshot JSONB,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

