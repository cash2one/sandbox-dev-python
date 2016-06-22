CREATE TABLE blog (
    id INT AUTO_INCREMENT,
    title TEXT,
    content TEXT,
    posted_on DATETIME,
    primary key (id)
);
CREATE TABLE comment (
    id INT AUTO_INCREMENT,
    blog_id INT,
    title TEXT,
    content TEXT,
    posted_on DATETIME,
    primary key (id)
);