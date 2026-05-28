# 🛒 PatakinsMart - Online Supermarket

![Django](https://img.shields.io/badge/Django-6.0.5-green.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![DRF](https://img.shields.io/badge/Django%20REST%20Framework-3.x-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A modern, full-featured online supermarket web application built with Django. PatakinsMart provides a seamless shopping experience for customers to browse and purchase quality food stuffs and groceries online.

## ✨ Features

### 🎨 Modern UI/UX
- **Responsive Design**: Fully responsive layout that works on desktop, tablet, and mobile devices
- **Beautiful Gradients**: Modern color schemes with smooth gradient backgrounds
- **Smooth Animations**: Hover effects, transitions, and animations for enhanced user experience
- **Intuitive Navigation**: Easy-to-use navigation with sticky header and clear menu structure

### 📦 Product Management
- **Product Catalog**: Browse all available products with detailed information
- **Product Details**: View comprehensive product information including price, stock, and category
- **CRUD Operations**: Full Create, Read, Update, Delete functionality for products (staff only)
- **Category Organization**: Products organized by categories for easy browsing
- **Stock Management**: Real-time stock tracking and availability status
- **Search & Filter**: Advanced filtering and search capabilities

### 🔐 User Management
- **Authentication**: Secure user login and registration system
- **Role-Based Access**: Different permissions for regular users and staff members
- **Admin Panel**: Comprehensive Django admin interface for site management

### 🚀 API Integration
- **RESTful API**: Full REST API for product management
- **Token Authentication**: Secure API access with token-based authentication
- **JWT Support**: JSON Web Token authentication for enhanced security
- **Pagination**: Efficient data loading with pagination support
- **Filtering & Search**: API endpoints with advanced filtering capabilities

## 🛠️ Technology Stack

### Backend
- **Django 6.0.5**: High-level Python web framework
- **Django REST Framework**: Powerful toolkit for building Web APIs
- **PostgreSQL/SQLite**: Database support (configurable)
- **Python 3.x**: Programming language

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with custom properties and animations
- **Vanilla JavaScript**: For dynamic interactions
- **Responsive Design**: Mobile-first approach

### Additional Tools
- **django-cors-headers**: Cross-Origin Resource Sharing support
- **django-filter**: Advanced filtering for querysets
- **python-decouple**: Environment variable management
- **dj-database-url**: Database configuration from URLs
- **whitenoise**: Static file serving for production

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment tool (venv)
- Git (for version control)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/PatrickA56/dune-cohort-final-project.git
cd final_project_patakinsmart
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the `patakinsmart` directory:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOST=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### 7. Create Categories (via Django Shell)
```bash
python manage.py shell
```
```python
from products.models import Category

# Create sample categories
Category.objects.create(name="Fruits & Vegetables", description="Fresh produce")
Category.objects.create(name="Dairy Products", description="Milk, cheese, yogurt")
Category.objects.create(name="Beverages", description="Drinks and juices")
Category.objects.create(name="Grains & Cereals", description="Rice, pasta, bread")
Category.objects.create(name="Meat & Poultry", description="Fresh meat products")
exit()
```

### 8. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## 📁 Project Structure

```
final_project_patakinsmart/
├── accounts/                 # User authentication app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── products/                 # Product management app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py             # Product and category forms
│   ├── models.py            # Product and Category models
│   ├── pagination.py        # Custom pagination
│   ├── serializers.py       # DRF serializers
│   ├── tests.py
│   ├── urls.py              # App URL configuration
│   └── views.py             # Views and API endpoints
├── patakinsmart/            # Project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py
│   └── .env                 # Environment variables
├── templates/               # HTML templates
│   ├── base.html           # Base template
│   ├── home.html           # Home page
│   ├── about.html          # About page
│   └── products/           # Product templates
│       ├── product_list.html
│       ├── product_detail.html
│       ├── product_form.html
│       └── product_confirm_delete.html
├── static/                  # Static files (CSS, JS, images)
├── staticfiles/            # Collected static files
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
├── Procfile               # Heroku deployment config
├── .gitignore             # Git ignore file
└── README.md              # This file
```

## 🎯 Usage

### For Customers
1. **Browse Products**: Visit the home page to see featured products
2. **View All Products**: Navigate to the Products page to see the complete catalog
3. **Product Details**: Click on any product to view detailed information
4. **About Us**: Learn more about PatakinsMart on the About page

### For Staff/Admin
1. **Login**: Access the admin panel at `/admin/`
2. **Add Products**: Use the "Add Product" button or admin panel
3. **Manage Products**: Edit or delete products from the product list or detail pages
4. **Manage Categories**: Create and manage product categories via admin panel

## 🔌 API Endpoints

### Products API
```
GET    /api/products/              # List all products (with pagination, filtering, search)
POST   /api/products/              # Create new product (authenticated)
GET    /api/products/{id}/         # Retrieve product details
PUT    /api/products/{id}/         # Update product (authenticated)
DELETE /api/products/{id}/         # Delete product (authenticated)
```

### Authentication
```
POST   /api/token/                 # Obtain auth token
POST   /api/token/jwt/             # Obtain JWT token
POST   /api/token/refresh/         # Refresh JWT token
```

### Query Parameters
- `?page=1` - Pagination
- `?page_size=10` - Items per page
- `?search=rice` - Search products
- `?category=1` - Filter by category
- `?is_available=true` - Filter by availability
- `?ordering=-created_at` - Sort results

### Example API Usage
```bash
# Get all products
curl http://127.0.0.1:8000/api/products/

# Search for products
curl http://127.0.0.1:8000/api/products/?search=rice

# Get product by ID
curl http://127.0.0.1:8000/api/products/1/

# Create product (requires authentication)
curl -X POST http://127.0.0.1:8000/api/products/ \
  -H "Authorization: Token your-token-here" \
  -H "Content-Type: application/json" \
  -d '{"name":"Rice","price":5000,"stock":100,"category":1}'
```

## 🎨 Features Showcase

### Home Page
- Hero section with call-to-action buttons
- Feature cards highlighting key benefits
- Category badges for easy navigation
- Statistics display
- Recently added products grid
- Responsive layout

### Product List
- Grid layout with product cards
- Product images with gradient backgrounds
- Availability badges
- Stock information
- Quick action buttons
- Empty state handling

### Product Detail
- Split-screen design
- Large product display
- Comprehensive product information
- Staff action buttons (Edit/Delete)
- Responsive layout

### Product Management
- Intuitive forms with validation
- Real-time feedback
- Success/error messages
- Confirmation dialogs for destructive actions

## 🔒 Security Features

- CSRF protection enabled
- Secure password hashing
- Token-based API authentication
- Role-based access control
- Environment variable configuration
- SQL injection protection (Django ORM)

## 🚀 Deployment

### Heroku Deployment
The project includes a `Procfile` for Heroku deployment:

```bash
# Login to Heroku
heroku login

# Create Heroku app
heroku create your-app-name

# Set environment variables
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOST=your-app-name.herokuapp.com

# Push to Heroku
git push heroku main

# Run migrations
heroku run python manage.py migrate

# Create superuser
heroku run python manage.py createsuperuser
```

## 🧪 Testing

Run tests with:
```bash
python manage.py test
```

## 📝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Known Issues

- Static files directory warning (resolved by creating static folder)
- Ensure categories are created before adding products

## 📞 Support

For support, email: support@patakinsmart.com

## 👥 Authors

- **Patrick A** - *Initial work* - [PatrickA56](https://github.com/PatrickA56)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Django Documentation
- Django REST Framework
- Bootstrap inspiration for UI components
- The open-source community

## 🔮 Future Enhancements

- [ ] Shopping cart functionality
- [ ] Payment gateway integration
- [ ] Order management system
- [ ] Email notifications
- [ ] Product reviews and ratings
- [ ] Wishlist feature
- [ ] Advanced search with filters
- [ ] Product images upload
- [ ] Inventory alerts
- [ ] Sales analytics dashboard
- [ ] Multi-language support
- [ ] Mobile app (React Native/Flutter)

## 📊 Project Status

**Status**: Active Development ✅

**Version**: 1.0.0

**Last Updated**: May 28, 2026

---

Made with ❤️ by Patrick A | © 2026 PatakinsMart. All rights reserved.
