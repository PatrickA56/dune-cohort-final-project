# PostgreSQL Migration and Render Deployment Guide

## Overview
This guide will help you migrate your data from SQLite to PostgreSQL and deploy your Django application on Render.

## Data Export Summary
- **Total Records Exported**: 63
- **Users**: 1 (superuser: Olalekan)
- **Categories**: 8
- **Products**: 22
- **Admin Log Entries**: 31
- **Sessions**: 1

## Prerequisites
- Render account (https://render.com)
- Git repository with your code
- `data_backup.json` file (already created)

## Step-by-Step Deployment Process

### 1. Prepare Your Repository

Ensure these files are in your repository:
- ✓ `requirements.txt` - Python dependencies
- ✓ `Procfile` - Render startup commands
- ✓ `data_backup.json` - Your exported data
- ✓ `migrate_to_postgres.py` - Migration script
- ✓ `.gitignore` - Excludes db.sqlite3, venv, etc.

**Important**: Make sure `data_backup.json` is committed to your repository:
```bash
git add data_backup.json migrate_to_postgres.py RENDER_DEPLOYMENT_GUIDE.md
git commit -m "Add data backup and migration scripts for PostgreSQL"
git push origin main
```

### 2. Create PostgreSQL Database on Render

1. Log in to Render Dashboard (https://dashboard.render.com)
2. Click **"New +"** → **"PostgreSQL"**
3. Configure your database:
   - **Name**: `patakinsmart-db` (or your preferred name)
   - **Database**: `patakinsmart`
   - **User**: (auto-generated)
   - **Region**: Choose closest to your users
   - **Plan**: Free or paid plan
4. Click **"Create Database"**
5. Wait for database to be provisioned (1-2 minutes)
6. **Copy the Internal Database URL** (starts with `postgresql://`)

### 3. Create Web Service on Render

1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub/GitLab repository
3. Configure your web service:
   - **Name**: `patakinsmart`
   - **Region**: Same as database
   - **Branch**: `main` (or your default branch)
   - **Root Directory**: (leave blank)
   - **Runtime**: `Python 3`
   - **Build Command**: 
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command**: 
     ```bash
     gunicorn patakinsmart.wsgi:application
     ```

### 4. Configure Environment Variables

In your Render Web Service, go to **"Environment"** tab and add these variables:

| Key | Value | Notes |
|-----|-------|-------|
| `DATABASE_URL` | `<Internal Database URL from Step 2>` | PostgreSQL connection string |
| `SECRET_KEY` | `<your-secret-key>` | Django secret key |
| `DEBUG` | `False` | Production setting |
| `ALLOWED_HOST` | `patakinsmart.onrender.com,localhost` | Your Render URL |
| `PYTHON_VERSION` | `3.11.0` | Or your Python version |

**To generate a new SECRET_KEY**:
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Deploy and Run Migrations

1. Click **"Create Web Service"**
2. Render will automatically deploy your application
3. Once deployed, open the **Shell** tab in your web service
4. Run migrations:
   ```bash
   python manage.py migrate
   ```

### 6. Load Your Data into PostgreSQL

In the Render Shell, run the migration script:
```bash
python migrate_to_postgres.py
```

The script will:
- ✓ Check database connection
- ✓ Display database configuration
- ✓ Load all data from `data_backup.json`
- ✓ Verify data was loaded correctly

**Expected Output**:
```
Users: 1
Categories: 8
Products: 22
✓ Migration completed and verified successfully!
```

### 7. Create Superuser (Optional)

If you need to create a new superuser or the migration didn't preserve passwords:
```bash
python manage.py createsuperuser
```

### 8. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 9. Verify Deployment

1. Visit your Render URL: `https://patakinsmart.onrender.com`
2. Test the admin panel: `https://patakinsmart.onrender.com/admin`
3. Login with your credentials
4. Verify all products and categories are present

## Alternative: Manual Data Loading

If the migration script doesn't work, you can manually load data:

```bash
python manage.py loaddata data_backup.json
```

## Troubleshooting

### Issue: Database Connection Error
**Solution**: Verify DATABASE_URL is correctly set in environment variables

### Issue: Migration Fails
**Solution**: 
1. Check that migrations were run first: `python manage.py migrate`
2. Ensure data_backup.json is in the project root
3. Check Render logs for specific errors

### Issue: Static Files Not Loading
**Solution**: 
1. Run `python manage.py collectstatic --noinput`
2. Verify `whitenoise` is in requirements.txt
3. Check STATIC_ROOT and STATICFILES_STORAGE in settings.py

### Issue: 502 Bad Gateway
**Solution**: 
1. Check Render logs for errors
2. Verify Procfile has correct command
3. Ensure gunicorn is in requirements.txt

## Post-Deployment Checklist

- [ ] Database is created and accessible
- [ ] Web service is deployed successfully
- [ ] Migrations are applied
- [ ] Data is loaded (63 records)
- [ ] Static files are collected
- [ ] Admin panel is accessible
- [ ] Products are visible on the site
- [ ] Can login with superuser credentials

## Important Notes

1. **Backup Data**: The `data_backup.json` file contains your complete database including:
   - User accounts (with hashed passwords)
   - All products and categories
   - Admin activity logs

2. **Security**: 
   - Never commit `.env` files with real credentials
   - Use environment variables on Render
   - Keep DEBUG=False in production

3. **Database**: 
   - Render's free PostgreSQL tier has limitations
   - Consider upgrading for production use
   - Regular backups are recommended

4. **Updates**: 
   - Push code changes to Git
   - Render auto-deploys on push (if enabled)
   - Run migrations after model changes

## Useful Commands

### Check Database Connection
```bash
python manage.py dbshell
```

### Create Database Backup on Render
```bash
python manage.py dumpdata --indent 2 --natural-foreign --natural-primary -e contenttypes -e auth.Permission -o backup_$(date +%Y%m%d).json
```

### View Logs
```bash
# In Render Dashboard → Logs tab
```

## Support Resources

- Render Documentation: https://render.com/docs
- Django Deployment: https://docs.djangoproject.com/en/stable/howto/deployment/
- PostgreSQL on Render: https://render.com/docs/databases

## Summary

Your SQLite data has been successfully exported and is ready for PostgreSQL migration. Follow the steps above to deploy your application on Render with all your existing data intact.

**Files Created**:
- `data_backup.json` - Complete database export (63 records)
- `migrate_to_postgres.py` - Automated migration script
- `RENDER_DEPLOYMENT_GUIDE.md` - This deployment guide

Good luck with your deployment! 🚀
