import os,sys

def deploy(message):
    os.system("git add .")
    os.system('git commit -m "' + message+'"')
    os.system('git push heroku master')

if __name__ == "__main__":
    message = sys.argv[1]
    deploy(message)

