from . import hello

@hello.route("/")
def root():
    return "Hello World!"
