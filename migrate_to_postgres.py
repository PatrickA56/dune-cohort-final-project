#!/usr/bin/env python
"""
Migration script to load data from SQLite backup into PostgreSQL on Render.

This script should be run AFTER:
1. Setting up PostgreSQL database on Render
2. Running migrations on the new database
3. Setting the DATABASE_URL environment variable

Usage:
    python migrate_to_postgres.py
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'patakinsmart.settings')
django.setup()

from django.core.management import call_command
from django.db import connection

def check_database_connection():
    """Verify database connection"""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        print("✓ Database connection successful")
        return True
    except Exception as e:
        print(f"✗ Database connection failed: {e}")
        return False

def get_database_info():
    """Display current database configuration"""
    db_settings = connection.settings_dict
    print("\n" + "="*60)
    print("DATABASE CONFIGURATION")
    print("="*60)
    print(f"Engine: {db_settings['ENGINE']}")
    print(f"Name: {db_settings['NAME']}")
    print(f"Host: {db_settings.get('HOST', 'N/A')}")
    print(f"Port: {db_settings.get('PORT', 'N/A')}")
    print("="*60 + "\n")

def migrate_data():
    """Load data from backup JSON file into PostgreSQL"""
    print("\n" + "="*60)
    print("STARTING DATA MIGRATION")
    print("="*60 + "\n")
    
    # Check if backup file exists
    backup_file = 'data_backup.json'
    if not os.path.exists(backup_file):
        print(f"✗ Error: {backup_file} not found!")
        print("Please ensure data_backup.json is in the project root directory.")
        return False
    
    print(f"✓ Found backup file: {backup_file}")
    
    try:
        # Load the data
        print("\nLoading data into PostgreSQL database...")
        call_command('loaddata', backup_file, verbosity=2)
        print("\n✓ Data migration completed successfully!")
        return True
    except Exception as e:
        print(f"\n✗ Error during data migration: {e}")
        return False

def verify_data():
    """Verify that data was loaded correctly"""
    from django.contrib.auth.models import User
    from products.models import Category, Product
    
    print("\n" + "="*60)
    print("VERIFYING DATA")
    print("="*60)
    
    user_count = User.objects.count()
    category_count = Category.objects.count()
    product_count = Product.objects.count()
    
    print(f"Users: {user_count}")
    print(f"Categories: {category_count}")
    print(f"Products: {product_count}")
    print("="*60 + "\n")
    
    return user_count > 0 or category_count > 0 or product_count > 0

def main():
    """Main migration process"""
    print("\n" + "="*60)
    print("POSTGRESQL MIGRATION SCRIPT")
    print("="*60)
    
    # Display database info
    get_database_info()
    
    # Check database connection
    if not check_database_connection():
        print("\nPlease check your DATABASE_URL environment variable.")
        sys.exit(1)
    
    # Confirm before proceeding
    response = input("\nDo you want to proceed with data migration? (yes/no): ")
    if response.lower() not in ['yes', 'y']:
        print("Migration cancelled.")
        sys.exit(0)
    
    # Migrate data
    if migrate_data():
        # Verify data
        if verify_data():
            print("✓ Migration completed and verified successfully!")
            print("\nYour data has been successfully migrated to PostgreSQL.")
        else:
            print("⚠ Warning: Migration completed but no data found in database.")
    else:
        print("\n✗ Migration failed. Please check the errors above.")
        sys.exit(1)

if __name__ == '__main__':
    main()
