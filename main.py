#importing the required pakcages
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

#creating a new flaskApp
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video is required", required=True)


videos = {}
#creating our resources, by creating a class inheriting from resource class

def abortIfVideoIdDoesNotExist(video_id):
    if video_id not in videos:
        abort(404, message="Could not find video....")

def abortIfVideoExists(video_id):
    if video_id in videos:
        abort(409, message="Video already exists with that ID...")

class Video(Resource):
    def get(self, video_id):
        abortIfVideoIdDoesNotExist(video_id)
        return videos[video_id]

    def put(self, video_id):
        abortIfVideoExists(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        abortIfVideoIdDoesNotExist(video_id)
        del videos[video_id]
        return '', 204




#registering this as a resource
api.add_resource(Video, "/video/<int:video_id>")

#defining the main program where the action happens
if __name__ == "__main__" :

    #this will start the flask application, and debug=True is given
    #so that the server is rerun whenever the code is changed and saved, 
    #thus avoiding to manually run the code everytime we change the code
    #make sure to never run debug=True in a production environment, this is 
    #only used to run in development environment

    app.run(debug=True)