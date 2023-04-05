# Moods - "connect across time zones with ease"
  Moods is a project that has been created using the django 2.2.4 version, the puspose of this project is to bring people together regarless of their time zones differences.

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

# Functionality

* responsive design across all pages Using BootStrap 5 

On Desktop devices:
![image](https://user-images.githubusercontent.com/77834808/230219214-593c6acb-9c33-4c08-bc0b-0240b6947338.png)

On Mobile phones: <br>
![Screen Shot 2023-04-05 at 23 47 22](https://user-images.githubusercontent.com/77834808/230219354-b80f6db5-5b4c-41c4-9106-fdf1d2596b20.png)

  * we used an offCanvas element provided by bootstrap in cases where the space is limited:

![Screen Shot 2023-04-05 at 23 51 11](https://user-images.githubusercontent.com/77834808/230220077-250d334e-d246-42ce-9123-cb23f7aab28f.png)

![Screen Shot 2023-04-05 at 23 52 25](https://user-images.githubusercontent.com/77834808/230220255-a09cff92-d9ac-412d-8003-02fadd153fd0.png)

* the main Functionality, this can be divided into a few categories: 

1. Login and Regestration: in the lognin and regestration, we have used the implementation of ajax to redirect to the dashboard without problems, and to not refresh the page if there was an error: 

Example: <br>
![Screen Shot 2023-04-05 at 23 48 42](https://user-images.githubusercontent.com/77834808/230220817-b0a7db40-92ca-4a00-a652-978f6a5debd3.png)
![image](https://user-images.githubusercontent.com/77834808/230221122-d25c6c21-94f9-40e7-bed8-b547fa6360ae.png)

We have added a Users table that has all the required fields, where the validation has been done: 

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
once the user signs up, they get redirected to the dashboard. 

* the main dashboard : after being redirected to the main dashboard the user gets greeted with their name, their current local time based on the time zone stored in the databse 

