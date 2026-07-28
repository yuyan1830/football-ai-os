# -*- coding: utf-8 -*-

import json
import sqlite3
from collections import defaultdict
from pathlib import Path

from model_interface import BaseModelInterface


class EloModel(BaseModelInterface):

    def __init__(self):
        self.name = "Elo"
        self.k_factor = 30
        self.home_advantage = 60
        self.team_ratings = {}
        self.training_summary = {}
        self.model_path = None

    def _resolve_db_path(self, data):
        if isinstance(data, dict):
            db_path = data.get("db_path")
        else:
            db_path = data

        if not db_path:
            raise ValueError("db_path is required for EloModel training")

        return str(db_path)

    def _ensure_tables(self, conn):
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS matches_clean (
                match_date TEXT,
                home_team TEXT,
                away_team TEXT,
                home_score INTEGER,
                away_score INTEGER
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS elo_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                team TEXT,
                elo_before REAL,
                elo_after REAL,
                opponent TEXT
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS team_rating (
                team TEXT PRIMARY KEY,
                elo REAL
            )
            """
        )
        conn.commit()

    def _persist_results(self, conn, history_rows, ratings):
        conn.execute("DELETE FROM elo_history")
        conn.execute("DELETE FROM team_rating")

        for row in history_rows:
            conn.execute(
                """
                INSERT INTO elo_history (date, team, elo_before, elo_after, opponent)
                VALUES (?, ?, ?, ?, ?)
                """,
                row,
            )

        for team, rating in sorted(ratings.items()):
            conn.execute(
                "INSERT INTO team_rating (team, elo) VALUES (?, ?)",
                (team, rating),
            )

        conn.commit()

    def train(self, data):
        db_path = self._resolve_db_path(data)
        conn = sqlite3.connect(db_path)
        self._ensure_tables(conn)

        rows = conn.execute(
            """
            SELECT match_date, home_team, away_team, home_score, away_score
            FROM matches_clean
            ORDER BY match_date
            """
        ).fetchall()

        ratings = defaultdict(lambda: 1500)
        history_rows = []

        for match_date, home_team, away_team, home_score, away_score in rows:
            home_before = ratings[home_team]
            away_before = ratings[away_team]
            home_rating = home_before + self.home_advantage

            expected_home = 1 / (
                1 + 10 ** ((away_before - home_rating) / 400)
            )
            expected_away = 1 - expected_home

            if home_score > away_score:
                result_home = 1
                result_away = 0
            elif home_score == away_score:
                result_home = 0.5
                result_away = 0.5
            else:
                result_home = 0
                result_away = 1

            ratings[home_team] += self.k_factor * (result_home - expected_home)
            ratings[away_team] += self.k_factor * (result_away - expected_away)

            history_rows.append(
                (
                    match_date,
                    home_team,
                    home_before,
                    ratings[home_team],
                    away_team,
                )
            )
            history_rows.append(
                (
                    match_date,
                    away_team,
                    away_before,
                    ratings[away_team],
                    home_team,
                )
            )

        self._persist_results(conn, history_rows, dict(ratings))
        conn.close()

        self.team_ratings = dict(ratings)
        self.training_summary = {
            "model": self.name,
            "status": "TRAINED",
            "matches_processed": len(rows),
            "db_path": db_path,
        }
        return self.training_summary

    def predict(self, features):
        home_team = features.get("home_team") if isinstance(features, dict) else None
        away_team = features.get("away_team") if isinstance(features, dict) else None

        if not home_team or not away_team:
            raise ValueError("home_team and away_team are required")

        home_before = self.team_ratings.get(home_team, 1500)
        away_before = self.team_ratings.get(away_team, 1500)
        home_rating = home_before + self.home_advantage

        expected_home = 1 / (
            1 + 10 ** ((away_before - home_rating) / 400)
        )
        expected_away = 1 - expected_home

        return {
            "home_win": round(expected_home, 6),
            "draw": round(max(0.0, 1 - expected_home - expected_away), 6),
            "away_win": round(expected_away, 6),
        }

    def evaluate(self, result):
        return {
            "model": self.name,
            "status": "EVALUATED",
            "result": result,
        }

    def save(self, path):
        payload = {
            "name": self.name,
            "k_factor": self.k_factor,
            "home_advantage": self.home_advantage,
            "team_ratings": self.team_ratings,
            "training_summary": self.training_summary,
        }
        save_path = Path(path)
        save_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        self.model_path = str(save_path)
        return True

    def load(self, path):
        load_path = Path(path)
        if not load_path.exists():
            return False

        payload = json.loads(load_path.read_text(encoding="utf-8"))
        self.name = payload.get("name", self.name)
        self.k_factor = payload.get("k_factor", self.k_factor)
        self.home_advantage = payload.get("home_advantage", self.home_advantage)
        self.team_ratings = payload.get("team_ratings", {})
        self.training_summary = payload.get("training_summary", {})
        self.model_path = str(load_path)
        return True



