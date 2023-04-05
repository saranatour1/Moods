# Moods - "Connect Across Time Zones with Ease"
Moods is a project created using Django 2.2.4. The purpose of this project is to bring people together regardless of their time zone differences.


## Contributers

* <a href="https://github.com/saranatour1">Sara  Nat</a>
* <a href="https://github.com/hamzafarsakh">Hamza Farsakh </a>
* <a href="https://github.com/KhalidHassouna">Khalid Hassounah </a>

## Tools used 
<p> <span>Visual Studio code</span> <br> <img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" /> </p>


<p> <span>Django Frame Work </span> <br> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green" /> </p>

<p> <span>BootStrap 5</span> <br> <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" /> </p>

<p> <span>JQuery</span> <br> <img src="https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white" /> </p>

<p> <span>SQLLite</span> <br> <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" /> </p>


## Languages Used 
* Python 3   <br> <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />

* JavaScript   <br> <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" />

* CSS3 <br> <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />

* HTML5 <br> <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />

## Functionality

- Responsive design across all pages using Bootstrap 5.


On Desktop devices:
![image](https://user-images.githubusercontent.com/77834808/230219214-593c6acb-9c33-4c08-bc0b-0240b6947338.png)

On Mobile phones: <br>
![Screen Shot 2023-04-05 at 23 47 22](https://user-images.githubusercontent.com/77834808/230219354-b80f6db5-5b4c-41c4-9106-fdf1d2596b20.png)

- Used Bootstrap's off-canvas element in cases where space is limited.


![Screen Shot 2023-04-05 at 23 51 11](https://user-images.githubusercontent.com/77834808/230220077-250d334e-d246-42ce-9123-cb23f7aab28f.png)

![Screen Shot 2023-04-05 at 23 52 25](https://user-images.githubusercontent.com/77834808/230220255-a09cff92-d9ac-412d-8003-02fadd153fd0.png)

- Main Functionality: This can be divided into a few categories:
  - Login and registration: We used AJAX implementation to redirect to the dashboard without refreshing the page in case of errors.


Example: <br>
![Screen Shot 2023-04-05 at 23 48 42](https://user-images.githubusercontent.com/77834808/230220817-b0a7db40-92ca-4a00-a652-978f6a5debd3.png)
![image](https://user-images.githubusercontent.com/77834808/230221122-d25c6c21-94f9-40e7-bed8-b547fa6360ae.png)

- Users table: We have added a table that includes all the required fields with appropriate validation.


```python
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=255) # the bcrypt password hash only.
    birthday=models.DateField()
    gender = models.CharField(max_length=50)
    time_zone = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManeger()

```
- Dashboard: Once the user signs up, they are redirected to their dashboard.


- Main dashboard: After being redirected to the dashboard, the user is greeted with their name, current local time based on their time zone stored in the database, and a clock that is being populated from their registered time zone.

![image](https://user-images.githubusercontent.com/77834808/230222916-6de301a7-001c-42b4-8551-98e4fa3f62ef.png)

- User interaction: Logged-in users can perform the following actions:
  - Add new posts
  - Comment on other users' posts
  - Like and unlike posts and comments
  - Delete their own posts and comments only


![Screen Shot 2023-04-06 at 00 12 26](https://user-images.githubusercontent.com/77834808/230223353-b26ecb06-2e1a-46dc-8487-e235ab7383f4.png)

- Ajax implementation: Ajax was also implemented on likes.
- Logged-in user profile: When a user opens their profile page, they are greeted with their information.


![Screen Shot 2023-04-06 at 00 17 37](https://user-images.githubusercontent.com/77834808/230224094-5c3ccf39-e18e-4b9b-9011-8b63e3c2bad9.png)

- Logged-in user profile: Users can view their recent posts and make new posts on their profile, which will also be displayed on the dashboard.


![Screen Shot 2023-04-06 at 00 19 22](https://user-images.githubusercontent.com/77834808/230224345-bb883350-f2fb-4f32-8722-10518e6f1cd4.png)


- Messages page: Users can visit their messages page by navigating to the navbar and clicking on "Messages."

![Screen Shot 2023-04-06 at 00 21 07](https://user-images.githubusercontent.com/77834808/230224645-fe9e7774-c671-4dfc-8003-f4d1a6675926.png)


- Messages page: When a user visits their messages page, they can see the last person they interacted with, along with that person's local time and the time difference between the two users from the logged-in user's perspective.

![Screen Shot 2023-04-06 at 00 22 59](https://user-images.githubusercontent.com/77834808/230224900-c886ff85-7e60-4c85-a804-dea8da612080.png)

- Messages page: Users can navigate to see their latest messages and the people they have not yet interacted with through messages.


![Screen Shot 2023-04-06 at 00 26 54](https://user-images.githubusercontent.com/77834808/230225375-04a5eee4-7139-4922-9190-f273b167fa42.png)
- Messaging feature: Users can message other users on the platform using a normal messenger.

![Screen Shot 2023-04-06 at 00 29 33](https://user-images.githubusercontent.com/77834808/230225747-b89fe946-9812-4ee0-a99d-b0e51ebe96e3.png)

- Friend requests: Users can view incoming and outgoing friend requests, and choose to accept or ignore requests. Users can also view their current list of friends and add new friends.

![Screen Shot 2023-04-06 at 00 30 40](https://user-images.githubusercontent.com/77834808/230226411-64d9fad5-7682-4839-906d-126aa253160a.png)

![Screen Shot 2023-04-06 at 00 32 25](https://user-images.githubusercontent.com/77834808/230226463-8f00b0c2-bfa8-4ec0-bc5c-69c027a11b72.png)


- Search feature: Users can use the functional search bar to search for other users by their first name, last name, or email.



![Screen Shot 2023-04-06 at 00 36 02](https://user-images.githubusercontent.com/77834808/230226740-7519edce-c355-44de-9826-63d81e2ec2ef.png)


# Conclusion 

This was a very fun project to do, and we enjoyed working together as a team to ensure that the project was successful. Throughout the project, we demonstrated time management and soft skills by listening to each other and utilizing our individual strengths to complete tasks efficiently. We were amazed at how differently each of us approached problem-solving and delighted to work in a respectful team environment.

As a team, we believe that this project has a future and there are still some functionalities that we did not have time to implement. We plan to revisit the repository, clean up the code, and add more features to make it even more presentable. 

We would love to hear your feedback and criticism if you end up using our code. Please don't hesitate to reach out to us. And, if you find our project useful, please consider giving us a star on the repository. 

Finally, we were amazed at how much we learned during this project in such a limited period of time. We were all eager to learn and help each other, which made the experience even more enjoyable.

Thank you for taking the time to read about our project!

- Creators of Moods 



  ![image](https://user-images.githubusercontent.com/77834808/230228434-15fbe2c1-dc37-4518-9f00-9affb391acb0.png)