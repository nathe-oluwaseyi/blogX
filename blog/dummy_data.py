from django.utils.text import slugify
from .models import Post, Tag, Category
from datetime import datetime, timedelta
import random


# List of sample categories for network engineering
category_names = [
    'Networking Basics',
    'Routing and Switching',
    'Network Security',
    'Wireless Networking',
    'Cloud Networking',
    'Data Center Networking',
    'SDN (Software-Defined Networking)'
]


# Insert categories into the database
for name in category_names:
    category, created = Category.objects.get_or_create(name=name, slug=slugify(name))
    if created:
        print(f"Category '{name}' created successfully.")
    else:
        print(f"Category '{name}' already exists.")
print('Dummy category added successfully')



# List of samples tags related to network engineering
tag_names = [
    'TCP/IP',
    'Cisco',
    'BGP',
    'Firewall',
    'VLAN',
    'Network Security',
    'Wireless',
    'SDN',
    'Cloud Computing',
    'IPv6',
    'Network Automation',
    'Routing Protocols',
    'Load Balancing',
    'Packet Sniffing',
    'Cybersecurity'
]

# Insert tags into the database
for name in tag_names:
    tag, created = Tag.objects.get_or_create(name=name, slug=slugify(name))
    if created:
        print(f"Tag '{name}' created successfully.")
    else:
        print(f"Tag '{name}' already exists.")
print("Dummy tags added successfully ")



# Dummy categories
categories = list(Category.objects.all()) # change QuerySet list to python list
tags = list(Tag.objects.all()) # change QuerySet list to python list

# Dummy data for network engineering posts
dummy_posts = [
    {
        'title': 'Understanding TCP/IP Networking',
        'content': 'TCP/IP is the backbone of modern networking, consisting of four key layers...',
        'description': 'A deep dive into TCP/IP model and how it powers the internet',
        'category': random.choice(categories) if categories else None,
        'tags': random.sample(tags, min(len(tags), 3)) if tags else [],
        'featured_image': None,
        'views': random.randint(100, 1000),
        'read_time': random.randint(5, 15),
    },
    
    {
        "title": "Configuring VLANs on Cisco Switches",
        "content": "VLANs allow segmentation of networks to improve security and efficiency...",
        "description": "A practical guide to setting up VLANs on Cisco switches.",
        "category": random.choice(categories) if categories else None,
        "tags": random.sample(tags, min(len(tags), 3)) if tags else [],
        "featured_image": None,
        "views": random.randint(100, 1000),
        "read_time": random.randint(5, 15),
        
    },
    
    {
        "title": "How to Secure Your Network with Firewalls",
        "content": "Firewalls act as the first line of defense in network security...",
        "description": "Best practices for configuring firewalls to protect your network.",
        "category": random.choice(categories) if categories else None,
        "tags": random.sample(tags, min(len(tags), 3)) if tags else [],
        "featured_image": None,
        "views": random.randint(100, 1000),
        "read_time": random.randint(5, 15),
    }
]


# Insert data into the database
for data in dummy_posts:
    post = Post.objects.create(
        title=data['title'],
        content=data['content'],
        description=data['description'],
        category=data['category'],
        featured_image=data['featured_image'],
        views=data['views'],
        read_time=data['read_time'],
        
    )
    post.tags.set(data['tags']) # Add ManyToMany tags
    post.save()

print("Dummy network engineering posts created successfully.")