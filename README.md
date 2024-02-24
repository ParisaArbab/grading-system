# grading-system
calculate the total score of answers
This Python code defines a function called totalScore that calculates a student's total score for an assignment based on several criteria. Here's a step-by-step explanation of what the code does:

Initialize Total Score: It starts by setting the total_score variable to 0, which will accumulate the student's score based on their answers to the subsequent questions.

Submission Format Check: The function asks if the assignment was submitted as a single uncompressed .py file. If the answer is not "yes," it immediately returns a score of 0.

Authorship Information Check: Next, it verifies whether the assignment includes the author's name and date. If this information is missing, the function returns a score of 0.

Honor Statement Confirmation: It checks if the student confirms not having given or received unauthorized assistance by agreeing to an honor statement. If the answer is not "yes," the score returned is 0.

Video Link Requirement: The function asks if there's a link to an unlisted 3-minute YouTube video explaining the code and answering questions. If absent, the function returns 0.

Evaluation of Code Correctness: If all previous conditions are met, the function proceeds to ask for an evaluation of the code's correctness on a scale of 0 to 10, and this score is added to the total_score.

Evaluation of Code Elegance: It then asks for an evaluation of the code's elegance (considering data structure selection, algorithm efficiency, function implementation, etc.) on a scale of 0 to 10, which is also added to the total_score.

Code Hygiene Evaluation: The function requests a score for code hygiene (including whitespace use, docstrings, etc.) on a scale of 0 to 10, adding this to the total_score.

Quality of Video Discussion: It asks for a score evaluating the quality of the discussion in the YouTube video, with this score (0 to 10) also contributing to the total_score.

Late Submission Penalty: Finally, it checks if the assignment was submitted late. If so, it calculates a penalty based on how many hours late the assignment was submitted, applying a maximum penalty of 100%. This penalty is deducted from the total_score.

Return Total Score: After all evaluations are done, and any applicable penalty is applied, the function returns the total_score.

The main part of the code (if __name__ == "__main__":) demonstrates how the totalScore function can be used in a real scenario. It prompts the user (presumably the grader) to enter the student's name, date, and YouTube video link upfront. After that, it walks the user through the grading process by asking the series of questions defined in the totalScore function. Finally, it prints the total score calculated for the assignment.

This grading system ensures that submissions adhere to specific requirements and standards before evaluating the technical and educational quality of the student's work.
