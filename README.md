## Table of Contents
- [Introduction](#Introduction)
- [Backstory](#Backstory)
- [Contributers](#Contributers)
- [Tools used ](#Tools-used)
- [Functionality](#Functionality)
  - [Sign in and Sign Up pages](#Sign-in-and-Sign-Up-pages)
    - [Demo](#Demo)
  - [dashboard ](#dashboard)
    - [Demo](#Demo)
  -[Logged in profile pages](#Logged-in-profile-pages) 
    - [Demo](#Demo)
  - [other's profiles](#other's-profiles)
    - [Demo](#Demo)
  - [messages](#messages)
    -[Demo](#Demo)
  -[other functions](#other functions)
    - [Search](#Search)
      - [Demo](#Demo)
    -[Custom error pages](#Custom-error-pages) 
      - [Demo](#Demo)
 -[Conclusion](#Conclusion) 
    



## Introduction - Moods "Connect Across Time Zones with Ease"

**Welcome to Moods!** a full stack application made with Django framework version 2.2.4, as one of the stack ending project with the coding Dojo and Axsos Academy. 

### Backstory

As we were looking for a Project Idea, making a minified Facebook was on the table. We were trying hard to figure out what to do and how to do it. Then we came up with the idea of connecting people on different time zones. We got to work and created a simple app that mimics most of Facebook's functionality. Users can have their own profile with a random avatar, post on the main dashboard, comment, message people, and view the time for users in different time zones.

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

### Sign in and Sign Up pages
in these pages, we have used **ajax** to implement the non-refreshing page method for a better user experience, once the user Regesters to the app they are me with the main dashboard to let them know that their Regestration proccess went smoothly, Once they sign up they have a random avatar generated for them based on thir first name, you can find out more about how to use this avatar here -->> [Random avatar](https://www.stefanjudis.com/blog/apis-to-generate-random-user-avatars/#multiavatar-api)
<!-- How to center this -->
#### Demo:
![Regestration Page](https://user-images.githubusercontent.com/77834808/231585866-c7c0793b-d8e5-457c-a6f8-243a2aea0075.gif)


### dashboard 
in the dashboard, You are met on the left with your user information, and on the right you have the abilty to see people's posts and comment them, you can have your own posts, you have the ability to delete your own comments and posts. Ajax was implemented here on the comments, posts, likes. 

We have used alot of crud operations here, such as Creating a post object, creating a like on the post and updating the count, and many more, you can feel free to check our models file with the views. 

#### Demo 
![Dashboard](https://user-images.githubusercontent.com/77834808/231593112-271b2856-4ba5-4a75-af2d-0384657e16cf.gif)

### Logged in profile pages 
For this, we when we go to our profile in the nav bar, or click on our name, we will be redirected to our main profile, where we can see our posts, we can see our posts, our friends , our requests, we can post on our profiles and it will be posted on the dashboard as well.

#### Demo 

![Main User Profile](https://user-images.githubusercontent.com/77834808/231595981-89f2fb21-0068-441e-8af5-11c43a5260ac.gif)


### other's profiles
this is very similar to the user profile,  we can see the other users information and posts, with an additional feature to see their own local time and how much time difference is between both of you, you can add them as a friend, see if they have sen't you a friend request. 
#### Demo 
![other user's profile](https://user-images.githubusercontent.com/77834808/231597104-aa878bc1-c3ea-42a5-8b78-29e760f2ba00.gif)


### messages
here, When you go to the messages section, You'll be met with the users you have sent messages to, user's who you have not sent messages to, and the other users information. 

#### Demo
![Messages](https://user-images.githubusercontent.com/77834808/231600109-0be0c29b-0265-4f82-9c14-7ca3aeae718f.gif)


<!-- ![Sign in and Sign up](https://user-images.githubusercontent.com/77834808/231596142-a0aef97c-275c-413b-8217-9c9b6a4700f4.gif) -->

### other functions
 #### Search 
 We have added a search feature where you can look up people by their first name and last name and email
  #### Demo

   ![Search](https://user-images.githubusercontent.com/77834808/231600176-36f5bd83-881f-48df-9e62-2227bf4e3740.gif)

 #### Custom error pages
 we have added a custom error page for errors  :404 and 500, and in the future we are planning to add more
  #### Demo
  
   ![Custom error messages](https://user-images.githubusercontent.com/77834808/231601414-abccb8af-2c22-4160-b0ea-97ce47d30056.gif)

    
 

and that's it for now, we have some functionality additions in the future!
# Conclusion 

This was a very fun project to do, and we enjoyed working together as a team to ensure that the project was successful. Throughout the project, we demonstrated time management and soft skills by listening to each other and utilizing our individual strengths to complete tasks efficiently. We were amazed at how differently each of us approached problem-solving and delighted to work in a respectful team environment.

As a team, we believe that this project has a future and there are still some functionalities that we did not have time to implement. We plan to revisit the repository, clean up the code, and add more features to make it even more presentable. 

We would love to hear your feedback and criticism if you end up using our code. Please don't hesitate to reach out to us. And, if you find our project useful, please consider giving us a star on the repository. 

Finally, we were amazed at how much we learned during this project in such a limited period of time. We were all eager to learn and help each other, which made the experience even more enjoyable.

Thank you for taking the time to read about our project!

- Creators of Moods 

  ![image](https://user-images.githubusercontent.com/77834808/230228434-15fbe2c1-dc37-4518-9f00-9affb391acb0.png)
