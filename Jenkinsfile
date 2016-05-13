node {

    stage 'Checkout'
    git url: 'https://github.com/whelmed/devops_ci_demo.git'

    stage 'Build'
    workspace = pwd()
    sh "ls -asl"
    sh "chmod 755 ./build.sh && ./build.sh"


    stage 'Test'
    // Test stage
    workspace = pwd()
    sh "chmod 755 ./test.sh && ./test.sh"

    stage 'Create OS Installer'
    def buildNumber = env.BUILD_NUMBER
    def buildOSPackage = "fpm -s dir -t deb -n faceit -v 0.${env.BUILD_NUMBER} -d \"python,python-dev,apache2\" ./faceit=/var/sites/"
    sh buildOSPackage

    stage 'Copy Artifact to Repo'
    // A fake repo in this case, but you get the idea
    def copyCommand = "cp faceit_0.${env.BUILD_NUMBER}_amd64.deb /var/app"
    sh copyCommand
}
