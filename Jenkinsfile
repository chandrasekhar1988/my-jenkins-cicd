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

    // Post-execution block starts here
    post {
        success {
            echo 'Build succeeded! Sending success email to the manager...'
            mail to: 'chandrasekhar.maroju@gmail.com',
                 subject: "SUCCESS: Job '${env.JOB_NAME}' [Build #${env.BUILD_NUMBER}]",
                 body: "Hello Manager,\n\nOur project build completed successfully (PASSED).\n\nTo view the build details, please click here: ${env.BUILD_URL}\n\nRegards,\nJenkins Automation Robot"
        }
        
        failure {
            echo 'Build failed! Sending alert email to the manager...'
            mail to: 'chandrasekhar.maroju@gmail.com',
                 subject: "FAILURE: Job '${env.JOB_NAME}' [Build #${env.BUILD_NUMBER}]",
                 body: "Hello Manager,\n\nOur project build has failed (FAILED). Please investigate immediately.\n\nTo view the error details, check the console output here: ${env.BUILD_URL}console\n\nRegards,\nJenkins Automation Robot"
        }
    }
}