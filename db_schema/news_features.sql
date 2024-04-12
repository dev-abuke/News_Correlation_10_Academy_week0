CREATE TABLE "articles" (
  "id" integer PRIMARY KEY,
  "title" varchar,
  "author" varchar,
  "url" varchar,
  "content" varchar,
  "source_id" integer,
  "sentiment_id" integer,
  "category_id" integer,
  "author_id" integer,
  "date_published" timestamp,
  "created_at" timestamp default CURRENT_TIMESTAMP
);

CREATE TABLE "source" (
  "id" integer PRIMARY KEY,
  "name" varchar,
  "rank" varchar,
  "location" varchar,
  "created_at" timestamp
);

CREATE TABLE "sentiment" (
  "id" integer PRIMARY KEY,
  "name" varchar,
  "created_at" timestamp
);

CREATE TABLE "article_category" (
  "id" integer PRIMARY KEY,
  "name" varchar,
  "created_at" timestamp
);

CREATE TABLE "author" (
  "id" integer PRIMARY KEY,
  "name" varchar,
  "created_at" timestamp
);

ALTER TABLE "articles" ADD FOREIGN KEY ("source_id") REFERENCES "source" ("id");

ALTER TABLE "articles" ADD FOREIGN KEY ("sentiment_id") REFERENCES "sentiment" ("id");

ALTER TABLE "articles" ADD FOREIGN KEY ("category_id") REFERENCES "article_category" ("id");

ALTER TABLE "articles" ADD FOREIGN KEY ("author_id") REFERENCES "author" ("id");
