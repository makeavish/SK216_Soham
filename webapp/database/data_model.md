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
  "registerDate": Date,
  "crawls":[{"Crawl ID":Object ID}]
}
```

## Past Crawls

**crawls** :

```json
{
  "id": String,
  "query": String,
  "results":[{"Results ID":Object ID}],
  "runDate": Date
}
```

## Results

**results** :

```json
{
  "url": String,
  "title": String,
  "score": String
}
```