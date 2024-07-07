import json, os

import data, func


def create_json_db(*args) -> None:

    with open("db.json", "w", encoding="utf-8") as f:
        json.dump(args, f, ensure_ascii=False, indent=4, separators=(",", ": "))


if __name__ == "__main__":
    if not os.path.exists("db.json"):
        create_json_db(
            data.goals, data.teachers, data.days_of_week, data.time_for_practice
        )
        print("\nDatabase - db.json is successfully created\n")
    for tutor_id in [8, 9, 10, 11]:
        func.add_goal_to_tutor("programming", tutor_id)
