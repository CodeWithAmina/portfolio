# Hosting on Render

I have prepared your project for deployment on [Render](https://render.com/).

## Prerequisites
1.  **GitHub Account**: Ensure you have a GitHub account.
2.  **Render Account**: Sign up at dashboard.render.com using your GitHub account.

## Steps

### 1. Push Code to GitHub
Open your terminal in this project folder and run:
```bash
git push origin main
```
*(If you haven't set up the remote origin yet, you need to create a repository on GitHub and follow the instructions to push an existing repository)*.

### 2. Deploy on Render
1.  Log in to your **Render Dashboard**.
2.  Click **New +** and select **Blueprint**.
3.  Connect your GitHub repository.
4.  Render will automatically detect the `render.yaml` file I created.
5.  Click **Apply** or **Create Service**.

That's it! Render will:
- Install dependencies from `requirements.txt`.
- Install your local `ai_helper_lib`.
- Start the app using `gunicorn`.

Your website will be live at a URL like `https://portfolio-amina.onrender.com`.
