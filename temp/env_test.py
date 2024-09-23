import os

from dotenv import load_dotenv
# Build paths inside the project like this: BASE_DIR / 'subdir'.
load_dotenv()

print(os.getenv("abc"))