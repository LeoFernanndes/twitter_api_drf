from twitter.celery import app


@app.task
def say_hello_to_new_user():
    print("hey there")
    return 'hello'
