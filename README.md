# Python API test for Get team member(s) API

## Before run the tests:
1. Install Python 3.6+
2. Install dependencies: pip install -r requirements.txt

## To run tests locally:
1. Run the `pytest tests` command


## To use this project with a CI system like Jenkins, you can create a Jenkinsfile with the following contents:
```
pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest test_api.py'
            }
        }
    }
}
```
