from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Review, Rate
from .forms import ProductForm, ReviewForm

import joblib
import re
import os

# Load the trained model
# model = joblib.load('./model/fake_review_detection_model.pkl')
model = joblib.load(os.path.join(os.path.dirname(__file__), 'model/fake_review_detection_model.pkl'))

# Preprocess the review text
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

# Product Views
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = Review.objects.filter(product=product)

    for review in reviews:
        # Preprocess the review text
        processed_review = preprocess_text(review.text)
        # Use the trained model to predict
        prediction = model.predict([processed_review])
        # Calculate the percentage
        percentage_fake = model.predict_proba([processed_review])[0][0] * 100
        percentage_genuine = 100 - percentage_fake
        # Add percentage to review object
        review.percentage_fake = round(percentage_fake, 2)
        review.percentage_genuine = round(percentage_genuine, 2)

    return render(request, 'product_detail.html', {'product': product, 'reviews': reviews})

# Category Views
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

# Review Views
@login_required
def review_create(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', pk=pk)
    else:
        form = ReviewForm()
    return render(request, 'review_form.html', {'form': form, 'product': product})

# Rate Views
@login_required
def rate_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        rating = int(request.POST.get('rating'))
        rate, created = Rate.objects.get_or_create(product=product)
        rate.update_rating(rating)
        return redirect('product_detail', pk=pk)
    return redirect('product_detail', pk=pk)
