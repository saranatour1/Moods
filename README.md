## Table of Contents
- [Introduction](#Introduction)
- [Setup](#setup)
- [Backstory](#Backstory)
- [Contributers](#Contributers)
- [Tools used ](#Tools-used)
- [Functionality](#Functionality)
  - [Sign in and Sign Up pages](#Sign-in-and-Sign-Up-pages)
    - [Demo](#Demo)
  - [dashboard ](#dashboard)
    - [Demo](#Demo)
  - [Logged in profile pages](#Logged-in-profile-pages) 
    - [Demo](#Demo)
  - [other's profiles](#other's-profiles)
    - [Demo](#Demo)
  - [messages](#messages)
    - [Demo](#Demo)
  - [other functions](#other-functions)
    - [Search](#Search)
      - [Demo](#Demo)
    - [Custom error pages](#Custom-error-pages) 
      - [Demo](#Demo)
    - [issues](#issues)
 - [Conclusion](#Conclusion) 
    



## Introduction - Moods "Connect Across Time Zones with Ease"

**Welcome to Moods!** a full stack application made with Django framework version 2.2.4, as one of the stack ending project with the coding Dojo and Axsos Academy. 

### Setup:
In order to use this website, you have to have Python installed, specifically Python 3. To install Python, please visit [python docs](https://www.python.org/downloads/) 

After that, you need to install a virtual environment by running the following command in Windows:
```bash
  python -m venv py3Env 
```
Then, activate the virtual environment by running this command in the command prompt:
```bash
  call py3Env\Scripts\activate 
```
After activation, install the project dependencies to the virtual environment using this command:
```bash
  pip install -r requirements.txt 
```
Then, go to the folder directory where the manage.py file is located and use this command to start the app:
```bash
  python manage.py runserver
```
The program will run on localhost:8000 and you should be good to go!  

_______________________

### Backstory:

As we were looking for a project idea, creating a minified version of Facebook was on the table. We were struggling to figure out what to do and how to do it. Then, we came up with the idea of connecting people in different time zones. We got to work and created a simple app that replicates most of Facebook's functionality. Users can create their own profile with a random avatar, post on the main dashboard, comment, message other users, and view the time for users in different time zones.

## Contributers

* <a href="https://github.com/saranatour1">Sara  Nat</a>
* <a href="https://github.com/hamzafarsakh">Hamza Farsakh </a>
* <a href="https://github.com/KhalidHassouna">Khalid Hassounah </a>

## Tools used 
 ![Visual Studio Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
 ![Django Frame Work ](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
 ![BootStrap 5](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
 ![JQuery](https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)
 ![SQLLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

## Languages Used 
 ![Python 3](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
 ![ JavaScript  ](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
 ![CSS3 ](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
 ![HTML5  ](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
 

## Functionality
### Sign In and Sign Up Pages:

On these pages, we have used **Ajax** to implement the non-refreshing page method for a better user experience. Once the user registers for the app, they are redirected to the main dashboard to let them know that their registration process went smoothly. Once they sign up, a random avatar is generated for them based on their first name. You can find out more about how to use this avatar here -->> [Random Avatar](https://www.stefanjudis.com/blog/apis-to-generate-random-user-avatars/#multiavatar-api).
<!-- How to center this -->
#### Demo:
![Regestration page](https://user-images.githubusercontent.com/77834808/233746123-ff6d8970-0013-44a2-ae8e-f86508a591a0.png)


### dashboard 
in the dashboard, You are met on the left with your user information, and on the right you have the abilty to see people's posts and comment them, you can have your own posts, you have the ability to delete your own comments and posts. Ajax was implemented here on the comments, posts, likes. 

We have used alot of crud operations here, such as Creating a post object, creating a like on the post and updating the count, and many more, you can feel free to check our models file with the views. 

#### Demo 
![dashboard](https://user-images.githubusercontent.com/77834808/233746267-7f9f5cef-5b9f-4550-a3c4-eb71388d4550.png)

### Logged In Profile Pages:
When we go to our profile in the navigation bar or click on our name, we are redirected to our main profile. Here, we can see our posts, our friends, our requests, and we can post on our profiles, which will also be displayed on the main dashboard.
#### Demo 
![Logged in user profile](https://user-images.githubusercontent.com/77834808/233746399-3d51a16b-b9e4-417b-a153-4f3356645bcc.png)


### Other Users' Profiles:
This is very similar to the user profile page. Here, we can see the other user's information and posts, with an additional feature to see their local time and the time difference between both of you. We can also add them as a friend, and check if they have sent us a friend request.
#### Demo 
![other profile](https://user-images.githubusercontent.com/77834808/233746610-762a3217-35ab-49d0-bea7-d37810f36ce5.png)


### Messages:

When you go to the messages section, you will see the users you have sent messages to, the users you have not sent messages to, and other users' information.

#### Demo

![messages](https://user-images.githubusercontent.com/77834808/233746747-183e9b39-3750-406d-9129-f31e03eb87a6.png)


### Other Functions:

#### Search:
We have added a search feature where you can look up people by their first name, last name, and email.
  #### Demo

![search](https://user-images.githubusercontent.com/77834808/233746904-79135a08-86bb-43e9-ade1-2558ca386a61.png)

 #### Custom error pages
 we have added a custom error page for errors  :404 and 500, and in the future we are planning to add more
  #### Demo
![error message](https://user-images.githubusercontent.com/77834808/233746956-2edb4807-3b8c-42f4-ba58-16eb8c4c02b1.png)
 

and that's it for now, we have some functionality additions in the future!

### issues
Some of the issues we faced during the project were related to the problem of static files rendering. Here are a few resources that can make your life easier:
- [Stack overflow, running on the local host](https://stackoverflow.com/questions/62555499/django-react-the-resource-was-blocked-due-to-mime-type-text-html-mismatch)
- [Stack overflow, settings.py fix](https://stackoverflow.com/questions/25913849/django-static-file-not-loading)
- [whitenoise](https://whitenoise.readthedocs.io/en/latest/)

# Conclusion:

This was a fun project, and we enjoyed working together as a team to ensure its success. We demonstrated time management and soft skills by listening to each other and utilizing our strengths to complete tasks efficiently. We were amazed at how differently each of us approached problem-solving and delighted to work in a respectful team environment.

As a team, we believe this project has a future, and there are still some functionalities we did not have time to implement. We plan to revisit the repository, clean up the code, and add more features to make it even more presentable.

We would love to hear your feedback and criticism if you end up using our code. Please don't hesitate to reach out to us. And if you find our project useful, please consider giving us a star on the repository.

Finally, we learned a lot during this project in a limited period of time. We were all eager to learn and help each other, which made the experience even more enjoyable.

Thank you for taking the time to read about our project!

- Creators of Moods 

  ![image](https://user-images.githubusercontent.com/77834808/230228434-15fbe2c1-dc37-4518-9f00-9affb391acb0.png)
