# 基督教会网站

一个使用 Flask 3 和 Python 3.x 构建的现代化教会网站，具有完整的前端界面和后端API。

## 功能特性

### 🌐 网站板块
- **首页** - 欢迎页面，展示教会简介、近期活动和讲道预告
- **关于我们** - 教会历史、信仰宣言、使命愿景、牧养团队介绍
- **事工** - 各项事工介绍，包括主日学、青年团契、妇女事工、敬拜赞美等
- **讲道信息** - 讲道视频、音频资源，支持筛选和搜索
- **联系我们** - 教会地址、联系方式、在线联系表单、祷告请求

### 🎨 设计特点
- **金属亮蓝主题** - 采用现代化的金属亮蓝色调
- **响应式设计** - 完美支持各种尺寸的设备
- **动态特效** - 平滑的动画效果和交互体验
- **简约流畅** - 清晰的界面布局和用户体验

### 🔧 技术特性
- **Flask 3** - 现代化的 Python Web 框架
- **RESTful API** - 完整的 API 接口，便于未来扩展
- **Bootstrap 5** - 现代化的前端框架
- **Font Awesome** - 丰富的图标库
- **动态 JavaScript** - 增强用户交互体验

## 项目结构

```
project/
├── app.py                    # Flask 主应用文件
├── requirements.txt          # Python 依赖包
├── static/                   # 静态文件目录
│   ├── css/
│   │   └── style.css        # 自定义样式文件
│   ├── js/
│   │   └── script.js        # JavaScript 功能文件
│   └── images/              # 图片资源目录
└── templates/               # HTML 模板目录
    ├── base.html            # 基础模板
    ├── index.html           # 首页模板
    ├── about.html           # 关于我们页面
    ├── ministries.html      # 事工页面
    ├── sermons.html         # 讲道信息页面
    └── contact.html         # 联系我们页面
```

## 🚀 快速开始

### 1. 环境准备
确保已安装 Python 3.8+：

```bash
python --version
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 运行应用
```bash
python app.py
```

应用将在 `http://localhost:5000` 启动。

## 📱 API 接口

### 当前可用接口：
- `GET /api/sermons` - 获取讲道列表
- `GET /api/ministries` - 获取事工信息
- `GET /api/events` - 获取活动信息
- `POST /api/contact` - 提交联系表单
- `POST /api/newsletter` - 订阅通讯

### 预留扩展接口：
- `GET /api/gallery` - 图片画廊（待实现）
- `GET /api/blog` - 博客文章（待实现）
- `POST /api/donations` - 捐赠功能（待实现）
- `GET /api/live-stream` - 直播功能（待实现）

## 🎨 自定义主题

### 主要颜色变量：
- `--primary-color: #5E9BD6` - 金属亮蓝色
- `--primary-dark: #4A7CBB` - 深蓝色
- `--primary-light: #8AB4E8` - 浅蓝色
- `--accent-color: #FFC107` - 金色点缀

### 修改主题：
编辑 `static/css/style.css` 文件中的 CSS 变量即可自定义颜色主题。

## 🔧 部署说明

### 生产环境部署：
1. 设置环境变量 `FLASK_ENV=production`
2. 使用 WSGI 服务器（如 Gunicorn）：
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Docker 部署：
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 📝 开发说明

### 添加新页面：
1. 在 `templates/` 目录创建新的 HTML 文件
2. 在 `app.py` 中添加对应的路由
3. 继承 `base.html` 模板保持一致性

### 扩展 API：
1. 在 `app.py` 中添加新的 API 路由
2. 更新相应的 JavaScript 代码
3. 添加错误处理和数据验证

### 样式修改：
- 主要样式在 `static/css/style.css`
- 使用 CSS 变量便于主题定制
- 遵循移动优先的响应式设计原则

## 🤝 贡献指南

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- [Flask](https://flask.palletsprojects.com/) - Web 框架
- [Bootstrap](https://getbootstrap.com/) - 前端框架
- [Font Awesome](https://fontawesome.com/) - 图标库
- [Unsplash](https://unsplash.com/) - 示例图片

---

**基督教会网站** - 用科技传扬福音，用网络连接心灵 🙏
