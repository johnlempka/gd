DROP TABLE IF EXISTS "book";

CREATE TABLE "book" (
  "id" integer primary key,
  "title" varchar(255),
  "available" boolean default true,
  "timestamp" timestamp with time zone
)
