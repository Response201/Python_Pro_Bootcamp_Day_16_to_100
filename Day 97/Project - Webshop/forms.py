from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length


class AuthForm(FlaskForm):
    username = StringField(
         render_kw={"placeholder": "Username", "class": "form-control mb-3"},
        validators=[
            DataRequired(message="Username is needed"),
            Length(min=3, max=250)
        ]
    )

    password = PasswordField(
        render_kw={"placeholder": "Password", "class": "form-control mb-3"},
        validators=[
            DataRequired(message="Password needed"),
            Length(min=4, max=12, message="Password must be between 4-12 characters")
        ]
    )

    submit = SubmitField(render_kw={ "class": "btn btn-primary"})

    def __init__(self, *args, submit_text="Let me in", **kwargs):
        super().__init__(*args, **kwargs,  )
        self.submit.label.text = submit_text





class ProductForm(FlaskForm):

    product = StringField(
        "Product name",
        validators=[DataRequired(), Length(min=2, max=100)]
    )

    description = TextAreaField("Description")

    image = StringField("Image URL")

    price = IntegerField(
        "Price",
        validators=[DataRequired()]
    )

    stock_quantity = IntegerField(
        "Stock quantity",
        validators=[DataRequired()]
    )

    submit = SubmitField("Save product")