"""
Author: Parisa Arbab
Date: Jan 17 2024
Statement:“I have not given or received any unauthorized assistance on this assignment.”


Questions:
• How does the function stop asking questions when the user failed an early condition (like including their name) and return 0?
• How did you deal with the fact that input() returns a string when you needed ints to compute the total score?
• Why should you return the score as an int rather than print it?
"""
def totalScore():
    total_score = 0

    # submit only .py file
    pyfile = input(
        "Did the student submit the assignment as a single uncompressed .py file? (yes/no): ").lower()
    if pyfile != "yes":
        return 0  # If not, return 0

    # Provide the author name and date
    NameDate = input("Did the assignment include the author's name and date? (yes/no): ").lower()
    if NameDate != "yes":
        return 0  # If not, return 0

    # Do you agree with the statement?
    statement = input("Are you confirm to not given help or recommendation in this course? (yes/no): ").lower()
    if statement != "yes":
        return 0  # If not, return 0

    # 3minutes video on Youtube is recorded. The link is provided
    link = input(
        "Did the assignment include a link to an unlisted 3-minute YouTube video? (yes/no): ").lower()
    if link != "yes":
        return 0  # If not, return 0

     #inputs are string and for getting a total score should convert them to int
    convertScoretoInt = int(input("how would you evaluate the correctness of the code? (0-10): "))
    total_score += convertScoretoInt

  #elegance code: data structure selection, algorithm efficiency, function implementation, etc
    elegance_score = int(input("how would you evaluate the elegance of the code? (0-10): "))
    total_score += elegance_score

    # hygine_score: white space, docstrings, etc.)
    hygiene_score = int(input("how would you evaluate the code hygiene? (0-10): "))
    total_score += hygiene_score

    # Evaluate quality of video
    video_score = int(
        input("Out of 10 points, how would you evaluate the quality of the discussion in the YouTube video? (0-10): "))
    total_score += video_score

    # not late submit
    is_late = input("Is the assignment late? (yes/no): ").lower()
    if is_late == "yes":
        hours_late = int(input("How many hours late is the assignment?: "))
        late_penalty = min(100, hours_late)  # Maximum penalty is 100%
        total_score -= (late_penalty / 100) * total_score

    return total_score


# Example usage
if __name__ == "__main__":
    name = input("Enter your name: ")
    date = input("Enter the date: ")
    video_link = input("Enter the YouTube video link: ")

    honor_statement = "I have not given or received any unauthorized assistance on this assignment."

    print("Please answer the following questions:")

    total_score = totalScore()

    print("Total Score:", total_score)
