pipeline {
    agent any

    stages {
        stage('1. Checkout') {
            steps {
                echo 'Fetching the latest code from GitHub...'
                // Since we connected Git in Jenkins, this happens automatically
            }
        }

        stage('2. Build') {
            steps {
                echo 'Software build process has started...'
                echo 'Checking application version:'
                bat 'type sample.txt'
            }
        }

        stage('3. Test') {
            steps {
                echo 'Running automated testing...'
                bat 'type test.txt'
                
                echo 'Verifying test results...'
                // This command searches for "STATUS=PASS" in test.txt. It will fail if not found.
                bat 'findstr "STATUS=PASS" test.txt'
            }
        }

        stage('4. Deploy') {
            steps {
                echo 'Testing successful! Deploying code to the production server...'
                echo 'Congratulations! Your app is now live.'
            }
        }
    }
}