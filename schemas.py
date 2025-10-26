from datetime import date
from typing import List
from pydantic import BaseModel, Field, field_validator


# /// Author ///
class AuthorBase(BaseModel):
    name: str


class AuthorCreate(AuthorBase):
    bio: str
    books: List[int]


class AuthorListItem(AuthorBase):
    id: int


class AuthorList(AuthorBase):
    authors: List[AuthorListItem]


class AuthorRetrieve(AuthorBase):
    id: int
    bio: str
    books: List[int]


class AuthorUpdate(AuthorBase):
    bio: str
    books: List[int]


# /// Book ///
class BookBase(BaseModel):
    title: str


class BookCreate(BookBase):
    title: str
    summary: str
    publication_date: date
    author_id: int

    @field_validator("publication_date", mode="before")
    @classmethod
    def publication_date_validation(cls, value: date) -> date:  
        if value.day < date.today():
            raise ValueError("The date must not be earlier than today's date")
        return value


class BookListItem(BookBase):
    id: int


class BookList(BookBase):
    books: List[BookListItem]


class BookRetrieve(BookBase):
    id: int
    summary: str
    publication_date: date
    author_id: int


class BookUpdate(BookBase):
    summary: str
    publication_date: date
    author_id: int