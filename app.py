# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'church_website_secret_key_2024'
app.config.from_object(Config)
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

# Route handlers
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/ministries')
def ministries():
    return render_template('ministries.html')

@app.route('/sermons')
def sermons():
    return render_template('sermons.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# API Routes
@app.route('/api/sermons')
def api_sermons():
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

@app.route('/api/ministries')
def api_ministries():
    return jsonify({
        'ministries': sample_ministries,
        'total': len(sample_ministries)
    })

@app.route('/api/events')
def api_events():
    return jsonify({
        'events': sample_events,
        'total': len(sample_events)
    })

@app.route('/api/contact', methods=['POST'])
def api_contact():
    data = request.get_json()
    return jsonify({
        'message': 'Contact form submitted successfully',
        'received_at': datetime.now().isoformat()
    })

@app.route('/api/newsletter', methods=['POST'])
def api_newsletter():
    data = request.get_json()
    return jsonify({
        'message': 'Successfully subscribed to newsletter',
        'email': data.get('email', ''),
        'subscribed_at': datetime.now().isoformat()
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
