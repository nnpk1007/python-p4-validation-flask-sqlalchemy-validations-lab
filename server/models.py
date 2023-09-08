from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates("name")
    def validate_name(self, key, name):
        
        if not name:
            raise ValueError("Author must ust have name")
        
        return name


    # All authors have a name.
    @validates("phone_number")
    def validate_phone_number(self, key, phone_number):

        if len(phone_number) != 10:
            raise ValueError("")

        return phone_number


    # Author phone numbers are exactly ten digits.
    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'


class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    
    @validates("title")
    def validate_title(self, key, title):
        # All posts must have a title.
        if not title:
            raise ValueError("Each post must have a title.")
        
        # Words to check for in the title
        words_to_check = ["Won't Believe", "Secret", "Top [number]", "Guess"]
        
        # Check if at least one of the specified words is present in the title
        absent_words = [word for word in words_to_check if word in title]
        
        if not absent_words:
            raise ValueError("The title must contain at least one of the specified words.")

        return title

    # Post content is at least 250 characters long.
    @validates("content")
    def validate_content(self, key, content):

        if len(content) <= 250:
            raise ValueError("Post content is at least 250 characters long.")

        return content

    
    # Post summary is a maximum of 250 characters.
    @validates("summary")
    def validate_summary(self, key, summary):

        if len(summary) >250:
            raise ValueError("Post summary is a maximum of 250 characters.")

        return summary

    
    # Post category is either Fiction or Non-Fiction.
    @validates("category")
    def validate_category(self, key, category):

        categories = ["Fiction", "Non-Fiction"]
        
        if category not in categories: 
            raise ValueError("Post category is either Fiction or Non-Fiction.")

        return category

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'


    # Finally, add a custom validator to the Post model that ensures the title is sufficiently clickbait-y. 
    # The validator should add a validation error if the title does not contain:

"Won't Believe"
"Secret"
"Top [number]"
"Guess"