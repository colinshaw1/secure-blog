# secure-blog

Description
--
The purpose is to provide a platform for individuals to share their ideas, experiences and knowledge with other members in a secure environment. The blog will incorporate user registration, authentication and a dashboard for managing posts and comments. 
Overall the Secure Blog provides a simple flexible way for individuals to create and publish their content which will allow healthy engagement between members. 

Setup
Prerequisites
pip install -r requirements.txt





Branches


Secure
--
git branch -m main secure

git fetch origin

git branch -u origin/secure secure

git remote set-head origin -a

The secure branch is the code implemented in a secure manner with authentication, csrf tokens and form control to stop XXS.

Insecure
--
git branch -m main insecure

git fetch origin

git branch -u origin/insecure insecure

git remote set-head origin -a

The insecure branch is the code developed in an insecure manner. There is no csrf tokens, no authentiction for the application so anyone can end blog posts etc.  

