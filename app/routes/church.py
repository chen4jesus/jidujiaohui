# -*- coding: utf-8 -*-
"""
Church website routes blueprint
Contains all routes for the church website pages and API endpoints
"""
from flask import Blueprint, render_template, request, jsonify
from datetime import datetime

church_bp = Blueprint('church', __name__)

# Sample data for demonstration
sample_sermons = [
    {
        "id": 1,
        "title": "信心的力量",
        "speaker": "王牧师",
        "date": "2024-12-15",
        "description": "探讨信心在基督徒生活中的重要性和实践",
        "audio_url": "/api/sermons/1/audio",
        "video_url": "/api/sermons/1/video"
    },
    {
        "id": 2,
        "title": "爱与饶恕",
        "speaker": "李牧师",
        "date": "2024-12-08",
        "description": "从圣经的角度理解爱与饶恕的真谛",
        "audio_url": "/api/sermons/2/audio",
        "video_url": "/api/sermons/2/video"
    }
]

sample_ministries = [
    {
        "id": 1,
        "name": "主日学",
        "description": "为各个年龄段的弟兄姊妹提供圣经教导",
        "schedule": "每周日 9:00-10:00",
        "leader": "陈老师",
        "contact": "sunday@church.com"
    },
    {
        "id": 2,
        "name": "青年团契",
        "description": "为青年弟兄姊妹提供团契交流和成长平台",
        "schedule": "每周五 19:00-21:00",
        "leader": "刘弟兄",
        "contact": "youth@church.com"
    }
]

sample_events = [
    {
        "id": 1,
        "title": "圣诞赞美会",
        "date": "2024-12-24",
        "time": "19:00",
        "location": "主堂",
        "description": "庆祝耶稣诞生的特别赞美会"
    }
]


# Page Routes
@church_bp.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@church_bp.route('/about')
def about():
    """About us page"""
    return render_template('about.html')


@church_bp.route('/ministries')
def ministries():
    """Ministries page"""
    return render_template('ministries.html')


@church_bp.route('/sermons')
def sermons():
    """Sermons page"""
    return render_template('sermons.html')


@church_bp.route('/contact')
def contact():
    """Contact page"""
    return render_template('contact.html')


# API Routes
@church_bp.route('/api/sermons')
def api_sermons():
    """Get sermons API endpoint with pagination"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    start = (page - 1) * per_page
    end = start + per_page

    return jsonify({
        'sermons': sample_sermons[start:end],
        'total': len(sample_sermons),
        'page': page,
        'per_page': per_page,
        'total_pages': (len(sample_sermons) + per_page - 1) // per_page
    })


@church_bp.route('/api/ministries')
def api_ministries():
    """Get ministries API endpoint"""
    return jsonify({
        'ministries': sample_ministries,
        'total': len(sample_ministries)
    })


@church_bp.route('/api/events')
def api_events():
    """Get events API endpoint"""
    return jsonify({
        'events': sample_events,
        'total': len(sample_events)
    })


@church_bp.route('/api/contact', methods=['POST'])
def api_contact():
    """Contact form submission endpoint"""
    data = request.get_json()
    return jsonify({
        'message': 'Contact form submitted successfully',
        'received_at': datetime.now().isoformat()
    })


@church_bp.route('/api/newsletter', methods=['POST'])
def api_newsletter():
    """Newsletter subscription endpoint"""
    data = request.get_json()
    return jsonify({
        'message': 'Successfully subscribed to newsletter',
        'email': data.get('email', ''),
        'subscribed_at': datetime.now().isoformat()
    })
