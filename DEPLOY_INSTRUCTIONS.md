# Deploying on Render

The repository includes a Render Blueprint in `render.yaml`. It builds the Flask app, starts Gunicorn on Render's assigned port, and checks `/` for service health.

## First deployment

1. Push the project to the `main` branch on GitHub:

   ```powershell
   git add app.py requirements.txt render.yaml README.md DEPLOY_INSTRUCTIONS.md static templates build
   git commit -m "Prepare portfolio for Render deployment"
   git push origin main
   ```

   Do not add local credentials or `.env` files.

2. Sign in at [Render](https://dashboard.render.com/), choose **New → Blueprint**, and connect `CodeWithAmina/portfolio`.
3. Review the `portfolio-amina` web service from `render.yaml` and choose **Apply**.
4. Wait for the first deployment to finish, then open the service's `onrender.com` URL.

Render can automatically redeploy from `main` after the Blueprint service is created.

## Contact email

For contact form email delivery, add these environment variables in the Render service's **Environment** settings:

- `MAIL_SERVER`
- `MAIL_PORT` (`587` for STARTTLS, or `465` for implicit TLS)
- `MAIL_USERNAME`
- `MAIL_PASSWORD`
- `FROM_EMAIL`
- `TO_EMAIL`

Save changes to trigger a redeploy. Without SMTP configuration, the live contact form does not log submitted message contents; it asks visitors to email directly. SMTP credentials belong only in Render's environment settings, never in the repository.
