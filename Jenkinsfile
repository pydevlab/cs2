pipeline {
  environment {
      registry = "pydevlab/caesar_cipher"
      registry2 = "pydevlab/caesar_cipher_decode"
      registryCredential = 'dockerhub-cred'
      dockerImage = ''
      dockerImage2 = ''
  }
  agent any
  stages {
      stage('Cloning git repository') {
          steps {
              git branch: 'main', url: 'https://github.com/pydevlab/cs2.git'
          }
      }
      stage('Building encode image') {
          steps{
              script {
                  dockerImage = docker.build registry + ":$BUILD_NUMBER"
              }
         }
      }
      stage('Building decode image') {
          steps{
	      sh "cd $WORKSPACE/decode"
              script {
                  dockerImage2 = docker.build registry2 + ":$BUILD_NUMBER"
	      }
	      sh "cd $WORKSPACE"
         }
      }
      stage('Push encode image to DockerHub') {
          steps{
              script {
                  docker.withRegistry( '', registryCredential ) {
                      dockerImage.push()
		      dockerImage.push('latest') 
                  }
              }
          }
      }
      stage('Push decode image to DockerHub') {
          steps{
	      sh "cd $WORKSPACE/decode"
              script {
                  docker.withRegistry( '', registryCredential ) {
	              dockerImage2.push()
		      dockerImage2.push('latest')
		  }
              }
	      sh "cd $WORKSPACE"	  
          }
      }
      stage('Deploy to staging') {
          steps {
	      sh "docker-compose down"
	      sh "docker-compose up -d"
        }
     }
	  
  }
}
