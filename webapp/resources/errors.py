class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class CrawlAlreadyExistsError(Exception):
    pass

class UpdatingCrawlError(Exception):
    pass

class DeletingCrawlError(Exception):
    pass

class CrawlNotExistsError(Exception):
    pass

class ResultAlreadyExistsError(Exception):
    pass

class UpdatingResultError(Exception):
    pass

class DeletingResultError(Exception):
    pass

class ResultNotExistsError(Exception):
    pass

class EmailAlreadyExistsError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "CrawlAlreadyExistsError": {
         "message": "Crawl with given name already exists",
         "status": 400
     },
     "UpdatingCrawlError": {
         "message": "Updating crawl added by other is forbidden",
         "status": 403
     },
     "DeletingCrawlError": {
         "message": "Deleting crawl added by other is forbidden",
         "status": 403
     },
     "CrawlNotExistsError": {
         "message": "Crawl with given id doesn't exists",
         "status": 400
     },
     "ResultAlreadyExistsError": {
         "message": "Result with given name already exists",
         "status": 400
     },
     "UpdatingResultError": {
         "message": "Updating Result added by other is forbidden",
         "status": 403
     },
     "DeletingResultError": {
         "message": "Deleting Result added by other is forbidden",
         "status": 403
     },
     "ResultNotExistsError": {
         "message": "Result with given id doesn't exists",
         "status": 400
     },
     "EmailAlreadyExistsError": {
         "message": "User with given email address already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     }
}