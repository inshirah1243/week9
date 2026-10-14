pipeline
{
    agent any
    stages{
        stage('Build Docker Image'){
            steps{
                echo "Build Docker Image"
                bat "docker build -t kubedemoapp:v1 ."
            }
        }
        stage('Docker Login'){
            steps{
                bat 'docker login -u inshirah1243 -p Inshirah@1122' 
            }
        }
        stage('push Docker Image to Docker Hub'){
            steps{
                echo "push Docker Image to Docker Hub"
                bat "docker tag kubedemoapp:v1 inshirah1243/sample:kubeimage1"
                bat "docker push inshirah1243/sample:kubeimage1"
            }
        }
        stage('Deploy to Kubernets')
        {
            steps{
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }
    post{
        success{
            echo 'Piplime completed successfully!'

        }
        failure{
            echo 'Pipeline failed, Please check the logs.'
        }
    }
}