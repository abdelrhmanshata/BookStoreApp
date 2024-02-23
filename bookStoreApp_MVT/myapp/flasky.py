## import function ---> entry point to run the application

from myapp import create_app

if __name__ == '__main__':
    app = create_app("prd")
    app.run(port=5005,debug=True)