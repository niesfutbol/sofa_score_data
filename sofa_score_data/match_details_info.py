def get_attendance(match_details) -> int:
    return match_details["content"]["matchFacts"]["infoBox"]["Attendance"]
