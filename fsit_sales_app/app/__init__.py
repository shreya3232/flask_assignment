from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from app.routes.employee import employee_bp
    app.register_blueprint(employee_bp)
    
    return app
