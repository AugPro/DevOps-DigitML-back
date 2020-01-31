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
which uses a SVM / KNN.  
We couldn't take it as it is and had to modify it to match with Django (updated libraries mainly).  
We also first tried to use a keras/tensorflow model for the recognition but we encountered problems with Docker using it.

### Frontend

We had multiple choices for our web framework and decided to go with Django as some team members already had some experience with it.  
Different usual languages are used to code it (Javascript, CSS, HTML).


## Instructions

For AWS, you need to follow some instructions :

(Deprecated ?)

- First of all, you will need to create your own AWS instance (as ours isn't reacheable when not in use).  
For that, you only need to follow the tutorial here ().  
- After that, the access from outside should be allowed. By going into the security groups settings, you should be able to modify it.  
- Execute the script deploy.sh.  
- When asked, you will need to enter your github account which has access to the repository you want to use. In our case, we had
to do it two times as we divided the parts for the backend and the frontend.  
- add 'predict(input.files[0]);' in master.js
In readURL(), just after 'reader.readAsDataURL(input.files[0]);'
[In DevOps-DigitML-front/site/js/master.js]
- Now, you need to check your instance IP on your browser.  

For deployment, you shouldn't have to do anything as BuddyWorks already does the following steps on every push to master :

- Validate Dockerfile with lint.  
- Upload files to [host](http://15.188.193.88/)
- run docker-compose command to restart container.

*Note: the major part of server conf is on [front](https://github.com/AugPro/DevOps-DigitML-front) repository*

## All links needed

GitHub Frontend : https://github.com/AugPro/DevOps-DigitML-front  
GitHub Backend : https://github.com/AugPro/DevOps-DigitML-back  
BuddyWorks : https://app.buddy.works/augustinpro/devops-digitml  

