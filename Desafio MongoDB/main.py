import sqlalchemy
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column, create_engine, inspect, select
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey


Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    #atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user",cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name},fullname={self.fullname})"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"),nullable=False)

    user = relationship(
        "User", back_populates="address"
    )

    def __repr__(self):
        return f"Address(id={self.id},email_address={self.email_address})"


# conexão com o banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)


# investia o esquema do banco de dados
inspetor_engine = inspect(engine)

with Session(engine) as session:
    user1 = User(
        name='',
        fullname='',
        address=[Address(email_address='@gmail.com'),
                 Address(email_address='@outlook.com')]
    )
    user2 = User(
        name='',
        fullname=''
    )

    # enviando para BD(persitência de dados)
    session.add_all([user1, user2])

    session.commit()

# retornar os valores
stmt = select(User).where(User.name.in_(["user1",'user2']))
results = session.execute(stmt).scalars().all()
for user in results:
    print(user)
print("--------------")

order_stmt = select(User).order_by(User.fullname.desc())
print("Recuperando inf de maneira ordenada")
for result in session.scalars(order_stmt):
    print(result)