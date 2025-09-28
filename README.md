# 📝 Django Blog

**Django Blog** is a full-stack web application built with **Django** that allows users to create, read, update, and delete blog posts.  
It includes a secure authentication system, commenting features, an "About Me" section with Cloudinary integration for profile images, and a collaboration request form.  
The project is fully deployed on **Heroku** with static and media file management via **WhiteNoise** and **Cloudinary**.

---

## 📌 Project Overview

The application includes:

- **User Authentication**  
  Signup, login, and logout using **Django Allauth**.

- **Blog Posts**  
  - Create, view, and paginate blog posts.  
  - Rich-text editor via **Django Summernote**.  
  - Featured images stored in **Cloudinary**.

- **Comments**  
  - Authenticated users can add, edit, and delete their comments.  
  - Comments require approval before being published.  
  - Comment count is displayed per post.

- **Profile Page**  
  Each user has a profile page showing their own comments.

- **About Section**  
  - Displays personal description text.  
  - Supports a profile image via **Cloudinary**, with fallback to a default static image.

- **Collaboration Requests**  
  Visitors can submit a request form (name, email, message).  
  Requests are saved in the database and visible via the Django Admin panel.

- **Responsive Design**  
  Templates styled with **Bootstrap 5** for mobile-first UI.

---

## 🛠️ Technologies Used

- **Python 3.13**  
- **Django 5.2** (main framework)  
- **PostgreSQL** (database, hosted on Neon DB)  
- **Cloudinary** (media storage for images)  
- **WhiteNoise** (static file handling on Heroku)  
- **Django Allauth** (user authentication)  
- **Crispy Forms + Bootstrap 5** (form rendering and styling)  
- **Django Summernote** (rich-text editor for blog posts)  
- **Heroku** (deployment)

---

## 📚 What I Learned

- Setting up and structuring a Django project with multiple apps (`blog`, `about`).  
- Managing static and media files with **WhiteNoise** and **Cloudinary**.  
- Creating models, forms, and views that interact seamlessly.  
- Using **class-based views** (ListView) and **function-based views**.  
- Implementing secure user authentication and authorization.  
- Writing clean, documented code following **PEP8** standards (validated with **Pylint**).  
- Handling migrations and database schema updates.  
- Deploying a Django app to **Heroku** with environment variables.  

---

## 📊 Example Features

### 📰 Blog Post List
- Displays paginated published posts with featured images.  
- Links to detail pages via slugs.

### 📝 Post Detail Page
- Shows post content, featured image, and comments.  
- Authenticated users can submit, edit, or delete comments.  

### 👤 About Page
- Displays profile text and image (Cloudinary).  
- Fallback static image if no custom upload is provided.  
- Includes collaboration form for visitor requests.

---

## 🚀 Deployment

The project is deployed on **Heroku**.  

1. Clone this repository:
   ```bash
   git clone https://github.com/Drake-Designer/Django-Blog.git
   cd Django-Blog
