import os
from dotenv import load_dotenv
from flask_login import UserMixin
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, MetaData, Table, text
from sqlalchemy.orm import registry, relationship, sessionmaker, Mapped
from functions import create_default_posts_database, create_default_users_database

load_dotenv()

# Ansluter till Neon
def get_engine():
    NEON_URL = os.getenv("POSTGRES_URL")
    if not NEON_URL:
        raise ValueError("NEON_DATABASE_URL saknas!")
    engine = create_engine(NEON_URL, future=True, echo=True,  pool_pre_ping=True )
    return engine


mapper_registry = registry()
metadata = MetaData()



users_table = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("email", String(50), nullable=False, unique=True),
    Column("name", String(20), nullable=False),
    Column("password", String(255), nullable=False)
)

posts_table = Table(
    "posts", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(250), unique=True),
    Column("subject", String(1000), nullable=False),
    Column("body", String(1000)),
    Column("image", String(1000), nullable=False),
    Column("date", String(250), nullable=False),
    Column("author_id", Integer, ForeignKey("users.id"))
)

comments_table = Table(
    "comments", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("author_id", Integer, ForeignKey("users.id")),
    Column("post_id", Integer, ForeignKey("posts.id")),
    Column("comment", String(100), nullable=False),
    Column("date", String(250), nullable=False)
)



# Relationer mellan användare, inlägg och kommentarer
@mapper_registry.mapped
class User(UserMixin):
    __table__ = users_table
    posts: Mapped[list["Blog"]] = relationship(
        "Blog",
        back_populates="author",
        uselist=True,
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    comments: Mapped[list["Comment"]] = relationship(
        "Comment",
        back_populates="author",
        uselist=True,
        cascade="all, delete-orphan",
        lazy="selectin"
    )

@mapper_registry.mapped
class Blog:
    __table__ = posts_table
    author: Mapped["User"] = relationship(
        "User",
        back_populates="posts",
        lazy="joined",
        uselist=False
    )
    comments: Mapped[list["Comment"]] = relationship(
        "Comment",
        back_populates="post",
        uselist=True,
        cascade="all, delete-orphan",
        lazy="selectin"
    )

@mapper_registry.mapped
class Comment:
    __table__ = comments_table
    author: Mapped["User"] = relationship(
        "User",
        back_populates="comments",
        uselist=False
    )
    post: Mapped["Blog"] = relationship(
        "Blog",
        back_populates="comments",
        uselist=False
    )


# Skapar tabeller, lägger till standardanvändare och -blogginlägg om databasen är tom
def init_db():
    engine = get_engine()
    metadata.create_all(engine)

    Session = sessionmaker(bind=engine, future=True)
    with Session() as session:


        create_default_users_database(session, User)
        create_default_posts_database(session, Blog)

        # Uppdaterar sequence så autoincrement fortsätter fungera korrekt
        session.execute(text("SELECT setval('users_id_seq', (SELECT MAX(id) FROM users))"))
        session.execute(text("SELECT setval('posts_id_seq', (SELECT MAX(id) FROM posts))"))
        session.commit()

    return engine

# Skapar session för routes
def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine, future=True)
    return Session()