# Database

This document describes the objects present in the database.

## User info

A user

**user** :

```json
{
  "id": String,
  "name": String,
  "password": String,
  "register_date": Date,
  "crawls":[{"Crawl ID":String}]
}
```

## Past Crawls

**crawls** :

```json
{
  "id": String,
  "Query": String,
  "Results":[{"url":string, "Score":number}],
  "Run Date": Date
}
```
