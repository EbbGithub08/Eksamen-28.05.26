import json
from urllib import request


#Brukt veiledning av cursor copilot
# Kilde: https://cursor.com/
class HighscoreDatabase:

    def __init__(self):
        self.api_base_url = "http://172.20.128.37:5000"

    def init_db(self) -> None:
        req = request.Request(f"{self.api_base_url}/health", method="GET")
        with request.urlopen(req):
            pass

    def save_highscore(self, username, world, time_seconds, coins, perfect_run):
        username = "".join(char for char in username if char.isalpha()).upper()[:9]
        if not username:
            return

        payload = {
            "username": username,
            "world_id": int(world),
            "time_seconds": float(time_seconds),
            "perfect_run": bool(perfect_run),
            "coins": int(coins),
        }
        data = json.dumps(payload).encode("utf-8")
        req = request.Request(
            f"{self.api_base_url}/highscores",
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with request.urlopen(req):
            pass

    def _get_scores_by_world(self):
        scores = {1: [], 2: [], 3: [], 4: [], 5: []}
        for w in range(1, 6):
            endpoint = f"{self.api_base_url}/highscores?world_id={w}"

            req = request.Request(endpoint, method="GET")
            with request.urlopen(req) as response:
                rows = json.loads(response.read().decode("utf-8"))

            cleaned_rows = []
            for row in rows:
                cleaned_rows.append(
                    (
                        row["username"],
                        row["world_id"],
                        float(row["time_seconds"]),
                        row["coins"],
                        1 if row["perfect_run"] else 0,
                    )
                )
            scores[w] = cleaned_rows
        return scores

    def get_top_scores(self):
        return self._get_scores_by_world()

    def get_all_scores(self):
        return self._get_scores_by_world()
