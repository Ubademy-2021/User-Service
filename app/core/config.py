import os

POSTGRES_USER = "dnelosexrgszoz"
POSTGRES_PASSWORD = "d0bcea04baf4cb598c261aea150aed55871cc7e65778b78c29b6201f98ddc98a"
POSTGRES_SERVER = "ec2-34-194-123-31.compute-1.amazonaws.com"
POSTGRES_PORT = "5432"
POSTGRES_DB = "dcmlmhd3ipa6a5"

# DATABASE_URL = "postgres://dnelosexrgszoz:d0bcea04baf4cb598c261aea150aed55871cc7e65778b78c29b6201f98ddc98a@ec2-34-194-123-31.compute-1.amazonaws.com:5432/dcmlmhd3ipa6a5"

DATABASE_URL = f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

HEROKU_COURSE_SERVICE_BASE_URL = os.environ.get('HEROKU_COURSE_SERVICE_BASE_URL', "https://course-service-ubademy.herokuapp.com")
