# DevOps2 Team 2 


## Introduction 

This application is a software able to recognise the real digits on an image containing written digits. 
The user only has to upload one of his own image directly to his web page and wait few seconds before getting the results 
of our machine learning algorithm on his image.

This project is part of a course at ESIEE Paris where we had to develop the whole infrastructure of an application and manage its 
distributed deployment.

## Structure

So first, we need an environment where our application could be run in real time for anyone.
For that, we had to use different technologies, in our case GitHub, BuddyWorks and AWS.

### Deployment Part

GitHub is our repository where all our scripts used by the software are stocked. 

BuddyWorks creates a link between our Github repository and AWS. When some modifications are pushed on the master branch on Github, 
BuddyWorks makes sure to validate them by testing if it doesn't raise any error before allowing them to go through. 

AWS (Amazon Web Services) is our cloud provider, the platform that handle our software application so that it is available for everyone.

We also use Docker which allows us to create containers in order to deploy our software application inside them.
It allows an easy installation of the requirements needed to run our application, such as Django, Numpy, Pandas, ...

As AWS's cost is time dependant, we decided not to maintain it all the time. 

### Backend

The backend is coded using Python 3.8.
At the moment, to predict the digits, we are using a model found here (https://github.com/pavitrakumar78/Python-Custom-Digit-Recognition)
which either uses a SVM or a KNN. For now, the KNN part is activated for our application.  
We couldn't take it as it is and had to modify it to match with Django (updated libraries mainly).  
We also first tried to use a keras/tensorflow model for the recognition but we encountered problems with Docker using it.

### Frontend

We had multiple choices for our web framework and decided to go with Django as some team members already had some experience with it.  
Different usual languages are used to code it (Javascript, CSS, HTML).

## Instructions

Here are the instructions to recreate what we have done :  

First of all, you will need to create an AWS account (free) in order to get your own AWS instance (as ours isn't reacheable when not in use or simply if you want to use your own). Check the Amazon AWS website and make sure to create an EC2 instance as it is the kind we used.  
After that, the access from outside should be allowed. By going into the security groups settings, you should be able to modify it (security group for the instance -> actions -> modify entering rules -> add new -> HTTP & from everywhere).  
Pay attention to the fact that the AWS instance is free until a certain amount of time consumed : don't forget to shut it down when you are not using it.   

You will have to come back to AWS but for now, create a BuddyWorks account.  
You will be asked to link your github repository (use ours for now).  
Create your first pipeline, then add the various actions that we used by looking at our own BuddyWorks application.
There is some tweaking involved so I encourage you to follow the link to ours and copy what we did.  
If you want to get more information on how it is designed, read this link (https://buddy.works/guides/how-build-and-deploy-frontend-applications).  

In our case, BuddyWorks does the following steps on every push to master :

- Validate Dockerfile with lint.  
- Upload files to [host](http://15.188.193.88/)
- Run docker-compose command to restart container.

*Note: the major part of server conf is on [front](https://github.com/AugPro/DevOps-DigitML-front) repository*

Now, come back on AWS and follow the BuddyWorks instructions in order to link both in ssh (https://buddy.works/docs/deployments/aws/ec2).
Also, don't forget to open port 80 for the webserver.

Now use the public IP/DNS given on AWS for your instance on your favorite browser and let's test it !


### If an AWS or BuddyWorks problem arises and you can't debug it

In case you encounter some difficulties and can't run AWS or Buddy Works, you can follow those steps to atleast see our application :

Requirements :
(If Buddy Works problem only)
- AWS free or premium account with EC2 instance (check Amazon AWS website)
- Access from the outside using public IP/DNS allowed for this instance on AWS

OR 

Any linux based machine

[N.B. : Grant the 30Gb of storage to your instance for free users.]

[N.B. :
To grant access from outside :
security group for the instance -> actions -> modify entering rules -> add new -> HTTP & from everywhere
]

Installation Steps - Tested For Ubuntu 18.04LTS : 

#init
sudo apt-get update
sudo apt-get upgrade

#docker
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt update
apt-cache policy docker-ce
sudo apt install docker-ce

[optional]
*check if docker installed*
sudo systemctl status docker

#docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

[optional]
*check if docker-compose installed*
docker-compose --version

#pip/pip3 
sudo apt install python3-pip (for python3 ie pip3)
(if python2 ie pip : sudo apt install python3-pip)

[optional]
*check if pip/pip3 installed*
pip3 --version (for python3)
(pip --version (for python2))

#create folder for projet
sudo mkdir devops
cd devops

#git clone front & back end
git clone https://github.com/AugPro/DevOps-DigitML
git clone https://github.com/AugPro/DevOps-DigitML-front

#prepare environment back end
cd DevOps-DigitML

#run server back-end
sudo docker-compose build
sudo docker-compose up -d

N.B. : 	The -d parameter will start the server and give you the control back
	For test purposes you can simply execute : sudo docker-compose up

#Go back to previous repertory (../devops)
cd ..

#prepare environment front-end
cd DevOps-DigitML-front
sudo docker-compose build
sudo docker-compose up -d

*Check on your favorite browser that you have access to the webpage/app using IP or DNS*


## All links needed

GitHub Frontend : https://github.com/AugPro/DevOps-DigitML-front  
GitHub Backend : https://github.com/AugPro/DevOps-DigitML-back  
BuddyWorks : https://app.buddy.works/augustinpro/devops-digitml  

