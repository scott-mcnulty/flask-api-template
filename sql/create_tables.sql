CREATE TABLE "public"."products" (
    "product_id" INTEGER NOT NULL PRIMARY KEY,
    "name" VARCHAR(80) NOT NULL,
    "value" DECIMAL NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL
);