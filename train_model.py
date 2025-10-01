"""
Train & evaluate LogisticRegression.
"""

from dataclasses import dataclass
from typing import Dict, Any
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from pipeline import main as pipe_main


"""
This class design - 

This class is designed to be a container for the results of training a machine learning model. It's like a package that holds:

How well the model performed (metrics)
The model itself that can make predictions
The frozen=True makes it safe because:

You can't accidentally change the metrics after they're recorded
You can't modify the trained model
It ensures the results stay consistent
This is particularly useful when you need to:

Save training results
Pass results between different parts of your program
Keep track of multiple training runs
Ensure results aren't accidentally modified
"""


@dataclass(frozen=True)  # Immutable decorator
class TrainResult:
    """
        Dict[str, Any] means it's a dictionary where:
    Keys are strings (like "accuracy", "precision", "recall")
    Values can be any type (numbers, lists, etc.)
    """

    metrics: Dict[str, Any]

    """
    The model attribute is like storing the actual trained teacher:

It holds a LogisticRegression object
This is the trained model that can make predictions
It's like keeping the trained teacher in the envelope so you can use them later
    """
    model: LogisticRegression

    """
    The Function Definition (def train):
Like creating a training program for teachers
Takes two inputs:
X_train: The training materials (features)
y_train: The correct answers (labels)
Returns a trained teacher (LogisticRegression)
Creating the Teacher (model = LogisticRegression(max_iter=500)):
Makes a new teacher with a specific rule
max_iter=500 means "try to learn for 500 attempts"
Like hiring a teacher with a specific teaching style
The Learning Process (model.fit(X_train, y_train)):
Shows the teacher all the training materials
The teacher studies the materials and correct answers
Like having the teacher grade practice quizzes and learn from them
Returning the Result (return model):
Gives back the now-trained teacher
The teacher can now make predictions on new materials
    """


def train(X_train, y_train) -> LogisticRegression:
    model = LogisticRegression(max_iter=500)
    model.fit(X_train, y_train)
    return model


"""
What the Method Does
Let's break down each line:

preds = model.predict(X_test):
Like giving the teacher a test with new questions
The teacher makes predictions for each question
Returns a list of answers the teacher thinks are correct
acc = accuracy_score(y_test, preds):
Compares the teacher's answers with the correct answers
Calculates what percentage they got right
Like grading a test and getting a final score
report = classification_report(y_test, preds, output_dict=True):
Creates a detailed report card
Shows how well the teacher did for each type of question
Like a breakdown of strengths and weaknesses
return {"accuracy": acc, "report": report}:
Packages the results into a neat summary
Returns both the overall score and detailed report
Like sending home a report card with detailed feedback

----This method is crucial because it helps you understand---- 
- how well your model will perform on new, unseen data - 
just like how a student's performance on a test they've 
never seen before is a better measure of their knowledge 
than their performance on practice problems they've studied.
"""


def evaluate(model: LogisticRegression, X_test, y_test) -> Dict[str, Any]:
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    report = classification_report(y_test, preds, output_dict=True)
    return {"accuracy": acc, "report": report}


def run_training() -> TrainResult:
    X_train, X_test, y_train, y_test = pipe_main()
    model = train(X_train, y_train)
    metrics = evaluate(model, X_test, y_test)
    return TrainResult(metrics=metrics, model=model)


if __name__ == "__main__":
    result = run_training()
    print("Accuracy:", result.metrics["accuracy"])
