pipeline {
    agent any

    stages {
        stage('First Step - Initialization') {
            steps {
                echo 'Jenkins pipeline has just started...'
            }
        }

        stage('Second Step - Read File') {
            steps {
                echo 'Now checking the created sample.txt file...'
                // Using 'bat' command to view file contents in Windows
                bat 'type sample.txt'
            }
        }

        stage('Third Step - Build & Execute') {
            steps {
                echo 'Awesome! Your build completed successfully.'
                echo 'Software delivery process success!'
            }
        }
    }
}