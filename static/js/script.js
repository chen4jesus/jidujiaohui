// ======== CHURCH WEBSITE JAVASCRIPT ========

document.addEventListener('DOMContentLoaded', function() {
    initializeAnimations();
    initializeScrollEffects();
    initializeNavigationEffects();
    initializeFormValidation();
    initializeParallaxEffects();
});

// ======== ANIMATION INITIALIZATION ========
function initializeAnimations() {
    // Animate elements on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');

                // Add stagger effect for multiple elements
                const siblings = entry.target.parentElement.children;
                Array.from(siblings).forEach((sibling, index) => {
                    if (sibling !== entry.target && sibling.classList.contains('animate-stagger')) {
                        setTimeout(() => {
                            sibling.classList.add('animate-in');
                        }, index * 100);
                    }
                });
            }
        });
    }, observerOptions);

    // Observe elements with animation classes
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    animatedElements.forEach(el => observer.observe(el));
}

// ======== SCROLL EFFECTS ========
function initializeScrollEffects() {
    let lastScroll = 0;
    const navbar = document.querySelector('.navbar');

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        // Navbar hide/show on scroll
        if (currentScroll > lastScroll && currentScroll > 100) {
            navbar.style.transform = 'translateY(-100%)';
        } else {
            navbar.style.transform = 'translateY(0)';
        }

        lastScroll = currentScroll;

        // Add scrolled class for styling changes
        if (currentScroll > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        // Parallax effect for hero section
        updateParallax();
    });
}

// ======== NAVIGATION EFFECTS ========
function initializeNavigationEffects() {
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');

    navLinks.forEach(link => {
        link.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });

        link.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Active link highlighting
    const currentPath = window.location.pathname;
    navLinks.forEach(link => {
        const linkPath = new URL(link.href).pathname;
        if (currentPath === linkPath || (currentPath === '/' && linkPath === '/')) {
            link.classList.add('active');
        }
    });
}

// ======== FORM VALIDATION ========
function initializeFormValidation() {
    const forms = document.querySelectorAll('form');

    forms.forEach(form => {
        const inputs = form.querySelectorAll('input, textarea, select');

        inputs.forEach(input => {
            // Add focus effects
            input.addEventListener('focus', function() {
                this.parentElement.classList.add('focused');
            });

            input.addEventListener('blur', function() {
                this.parentElement.classList.remove('focused');
                validateField(this);
            });

            // Real-time validation
            input.addEventListener('input', function() {
                if (this.classList.contains('is-invalid')) {
                    validateField(this);
                }
            });
        });

        // Form submission
        form.addEventListener('submit', function(e) {
            let isValid = true;
            inputs.forEach(input => {
                if (!validateField(input)) {
                    isValid = false;
                }
            });

            if (!isValid) {
                e.preventDefault();
                showNotification('请正确填写所有必填字段', 'error');
            }
        });
    });
}

function validateField(field) {
    const value = field.value.trim();
    const isRequired = field.hasAttribute('required');
    const type = field.type;
    let isValid = true;
    let message = '';

    // Check if required and empty
    if (isRequired && !value) {
        isValid = false;
        message = '此字段为必填项';
    }

    // Email validation
    if (type === 'email' && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            isValid = false;
            message = '请输入有效的邮箱地址';
        }
    }

    // Phone validation
    if (type === 'tel' && value) {
        const phoneRegex = /^[\d\s\-\+\(\)]+$/;
        if (!phoneRegex.test(value)) {
            isValid = false;
            message = '请输入有效的电话号码';
        }
    }

    // Update field styling
    if (isValid) {
        field.classList.remove('is-invalid');
        field.classList.add('is-valid');
        removeFieldError(field);
    } else {
        field.classList.remove('is-valid');
        field.classList.add('is-invalid');
        showFieldError(field, message);
    }

    return isValid;
}

function showFieldError(field, message) {
    removeFieldError(field);

    const errorDiv = document.createElement('div');
    errorDiv.className = 'invalid-feedback';
    errorDiv.textContent = message;
    field.parentElement.appendChild(errorDiv);
}

function removeFieldError(field) {
    const errorDiv = field.parentElement.querySelector('.invalid-feedback');
    if (errorDiv) {
        errorDiv.remove();
    }
}

// ======== PARALLAX EFFECTS ========
function initializeParallaxEffects() {
    const parallaxElements = document.querySelectorAll('.parallax');

    window.addEventListener('scroll', updateParallax);

    function updateParallax() {
        const scrolled = window.pageYOffset;

        parallaxElements.forEach(element => {
            const speed = element.dataset.speed || 0.5;
            const yPos = -(scrolled * speed);
            element.style.transform = `translateY(${yPos}px)`;
        });
    }
}

// ======== NOTIFICATION SYSTEM ========
function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existingNotifications = document.querySelectorAll('.notification');
    existingNotifications.forEach(notification => notification.remove());

    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <div class="notification-content">
            <i class="fas fa-${getNotificationIcon(type)}"></i>
            <span>${message}</span>
            <button class="notification-close" onclick="this.parentElement.parentElement.remove()">
                <i class="fas fa-times"></i>
            </button>
        </div>
    `;

    // Add styles
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 9999;
        padding: 15px 20px;
        border-radius: 8px;
        background: ${getNotificationColor(type)};
        color: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        transform: translateX(400px);
        transition: transform 0.3s ease;
        max-width: 350px;
    `;

    document.body.appendChild(notification);

    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);

    // Auto remove
    setTimeout(() => {
        notification.style.transform = 'translateX(400px)';
        setTimeout(() => {
            if (notification.parentElement) {
                notification.remove();
            }
        }, 300);
    }, 5000);
}

function getNotificationIcon(type) {
    const icons = {
        success: 'check-circle',
        error: 'exclamation-circle',
        warning: 'exclamation-triangle',
        info: 'info-circle'
    };
    return icons[type] || 'info-circle';
}

function getNotificationColor(type) {
    const colors = {
        success: '#28a745',
        error: '#dc3545',
        warning: '#ffc107',
        info: '#5E9BD6'
    };
    return colors[type] || '#5E9BD6';
}

// ======== UTILITY FUNCTIONS ========
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// ======== LAZY LOADING ========
function initializeLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');

    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });

    images.forEach(img => {
        img.classList.add('lazy');
        imageObserver.observe(img);
    });
}

// ======== SMOOTH SCROLLING ========
function initializeSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');

    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();

            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                const offsetTop = targetElement.offsetTop - 80;
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// ======== MODAL ENHANCEMENTS ========
function initializeModals() {
    const modals = document.querySelectorAll('.modal');

    modals.forEach(modal => {
        modal.addEventListener('show.bs.modal', function() {
            document.body.style.overflow = 'hidden';
        });

        modal.addEventListener('hidden.bs.modal', function() {
            document.body.style.overflow = '';
        });
    });
}

// ======== CAROUSEL ENHANCEMENTS ========
function initializeCarousels() {
    const carousels = document.querySelectorAll('.carousel');

    carousels.forEach(carousel => {
        // Add swipe support for touch devices
        let startX = 0;
        let endX = 0;

        carousel.addEventListener('touchstart', (e) => {
            startX = e.changedTouches[0].screenX;
        });

        carousel.addEventListener('touchend', (e) => {
            endX = e.changedTouches[0].screenX;
            handleSwipe();
        });

        function handleSwipe() {
            const threshold = 50;
            const diff = startX - endX;

            if (Math.abs(diff) > threshold) {
                if (diff > 0) {
                    // Swipe left - next slide
                    bootstrap.Carousel.getInstance(carousel).next();
                } else {
                    // Swipe right - previous slide
                    bootstrap.Carousel.getInstance(carousel).prev();
                }
            }
        }
    });
}

// ======== ACCESSIBILITY ENHANCEMENTS ========
function initializeAccessibility() {
    // Skip to main content link
    const skipLink = document.createElement('a');
    skipLink.href = '#main-content';
    skipLink.textContent = '跳转到主要内容';
    skipLink.className = 'skip-link';
    skipLink.style.cssText = `
        position: absolute;
        top: -40px;
        left: 6px;
        background: var(--primary-color);
        color: white;
        padding: 8px;
        text-decoration: none;
        z-index: 10000;
        border-radius: 4px;
    `;

    skipLink.addEventListener('focus', function() {
        this.style.top = '6px';
    });

    skipLink.addEventListener('blur', function() {
        this.style.top = '-40px';
    });

    document.body.insertBefore(skipLink, document.body.firstChild);

    // Add aria labels for dynamically loaded content
    const dynamicContent = document.querySelectorAll('[data-dynamic]');
    dynamicContent.forEach(element => {
        element.setAttribute('aria-live', 'polite');
    });
}

// Initialize additional features
document.addEventListener('DOMContentLoaded', function() {
    initializeLazyLoading();
    initializeSmoothScrolling();
    initializeModals();
    initializeCarousels();
    initializeAccessibility();
});

// ======== ERROR HANDLING ========
window.addEventListener('error', function(e) {
    console.error('JavaScript Error:', e.error);
    // In production, you might want to send this to an error tracking service
});

// ======== PERFORMANCE MONITORING ========
function logPerformance() {
    if ('performance' in window) {
        window.addEventListener('load', function() {
            setTimeout(function() {
                const perfData = performance.getEntriesByType('navigation')[0];
                const loadTime = perfData.loadEventEnd - perfData.loadEventStart;
                console.log(`Page load time: ${loadTime}ms`);

                if (loadTime > 3000) {
                    console.warn('Slow page load detected. Consider optimizing.');
                }
            }, 0);
        });
    }
}

logPerformance();