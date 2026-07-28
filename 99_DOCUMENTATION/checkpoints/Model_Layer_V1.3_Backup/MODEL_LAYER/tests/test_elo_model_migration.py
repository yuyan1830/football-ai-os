import sqlite3
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from models.elo_model import EloModel


def test_elo_model_trains_from_matches_and_persists_results(tmp_path):
    db_path = tmp_path / "football.db"
    conn = sqlite3.connect(db_path)
    conn.execute(
        """
        CREATE TABLE matches_clean (
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
        CREATE TABLE elo_history (
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
        CREATE TABLE team_rating (
            team TEXT PRIMARY KEY,
            elo REAL
        )
        """
    )
    conn.executemany(
        """
        INSERT INTO matches_clean (match_date, home_team, away_team, home_score, away_score)
        VALUES (?, ?, ?, ?, ?)
        """,
        [
            ("2024-01-01", "Team A", "Team B", 2, 1),
            ("2024-01-08", "Team B", "Team C", 1, 0),
        ],
    )
    conn.commit()
    conn.close()

    model = EloModel()
    result = model.train({"db_path": str(db_path)})

    assert result["status"] == "TRAINED"
    assert result["matches_processed"] == 2

    conn = sqlite3.connect(db_path)
    history_count = conn.execute("SELECT COUNT(*) FROM elo_history").fetchone()[0]
    team_count = conn.execute("SELECT COUNT(*) FROM team_rating").fetchone()[0]
    conn.close()

    assert history_count >= 4
    assert team_count >= 3

    prediction = model.predict({"home_team": "Team A", "away_team": "Team B"})

    assert set(prediction.keys()) == {"home_win", "draw", "away_win"}
    assert round(prediction["home_win"] + prediction["draw"] + prediction["away_win"], 6) == 1.0

    saved_path = tmp_path / "elo_model.json"
    assert model.save(str(saved_path)) is True

    reloaded = EloModel()
    assert reloaded.load(str(saved_path)) is True
    assert reloaded.name == "Elo"
